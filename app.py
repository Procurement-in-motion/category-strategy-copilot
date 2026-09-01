
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Category Strategy Copilot MVP2", page_icon="🧭", layout="wide")
st.markdown("""
<style>
.block-container {padding-top:1.2rem;padding-bottom:3rem}
div[data-testid="stMetric"] {border:1px solid #e8e8e8;padding:14px;border-radius:14px;background:#fff}
.card {padding:14px 16px;border:1px solid #e5e7eb;border-radius:14px;margin-bottom:10px;background:#fafafa}
.badge {display:inline-block;padding:4px 9px;border-radius:999px;background:#eef2ff;font-size:.78rem;font-weight:600}
.small {color:#6b7280;font-size:.88rem}
</style>
""", unsafe_allow_html=True)

st.title("🧭 Category Strategy Copilot — MVP2")
st.caption("Internal intelligence → Kraljic → SWOT → Strategic implications → Strategy")

with st.sidebar:
    st.header("Category Context")
    category = st.text_input("Category", "Corrugated Packaging")
    geography = st.text_input("Geography", "Brazil")
    industry = st.text_input("Business / Industry", "Industrial Equipment")
    st.divider()
    st.markdown("**Strategic assessment**")
    criticality = st.slider("Operational criticality",1,5,4, help="1 = low operational impact; 5 = severe impact if supply fails")
    qualification = st.slider("Supplier qualification difficulty",1,5,4, help="1 = easy/fast; 5 = difficult/long")
    switching = st.slider("Switching cost / complexity",1,5,3)
    alternatives = st.slider("Availability of qualified alternatives",1,5,2, help="1 = very limited; 5 = many alternatives")
    quality_impact = st.slider("Quality / customer impact",1,5,4)
    st.caption("These are human inputs. MVP3 can enrich them with external market intelligence.")

uploaded = st.file_uploader("Upload procurement data", type=["csv","xlsx","xls"])
if uploaded is None:
    st.info("Upload the MVP1 sample file or your own procurement dataset.")
    st.stop()

try:
    df = pd.read_csv(uploaded) if uploaded.name.lower().endswith(".csv") else pd.read_excel(uploaded)
except Exception as e:
    st.error(f"Could not read file: {e}"); st.stop()

def col(cands):
    for c in df.columns:
        if str(c).strip().lower() in [x.lower() for x in cands]: return c
    for c in df.columns:
        if any(x.lower() in str(c).strip().lower() for x in cands): return c
    return None

supplier=col(["supplier","vendor"]); spend=col(["spend","amount","value"]); sku=col(["sku","material","item"])
price=col(["unit price","price"]); contract=col(["contract status","contract"]); plant=col(["plant","site"])
qty=col(["quantity","qty","volume"]); date=col(["date"]); payment=col(["payment terms","payment term"])

if not supplier or not spend:
    st.error("Supplier/Vendor and Spend/Amount are required."); st.stop()
df[spend]=pd.to_numeric(df[spend],errors="coerce").fillna(0)
total=float(df[spend].sum())
ss=df.groupby(supplier)[spend].sum().sort_values(ascending=False)
n=len(ss); shares=ss/total if total else ss*0
top3=float(ss.head(3).sum()/total) if total else 0
hhi=float((shares**2).sum()*10000) if total else 0
asc=ss.sort_values(); cum=asc.cumsum()/total if total else asc*0
tail=asc[cum<=.20]; tail_n=len(tail); tail_share=float(tail.sum()/total) if total else 0

pv=None
if sku and price:
    df[price]=pd.to_numeric(df[price],errors="coerce")
    g=df[[sku,price]].dropna().groupby(sku)[price].agg(["min","max","count"])
    g=g[g["count"]>=2]
    if len(g):
        g["spread"]=np.where(g["min"]>0,(g["max"]-g["min"])/g["min"],np.nan)
        pv=float(g["spread"].median())

coverage=None
if contract:
    active=df[contract].astype(str).str.lower().str.contains("active|valid|yes|covered")
    coverage=float(df.loc[active,spend].sum()/total) if total else 0

st.subheader("1. Category Health Check")
m=st.columns(5)
m[0].metric("Spend",f"{total:,.0f}"); m[1].metric("Suppliers",n); m[2].metric("Top-3",f"{top3:.1%}")
m[3].metric("HHI",f"{hhi:,.0f}"); m[4].metric("Price variance","N/A" if pv is None else f"{pv:.1%}")

# Kraljic engine: transparent 0-10 scores
# Business impact = criticality 35%, quality 25%, switching 20%, spend-scale proxy 20%
# Spend-scale proxy is relative/internal: concentration/scale signal, not absolute market benchmark
spend_scale = min(5, max(1, 1 + np.log10(max(total,1))/2))
business_raw = criticality*.35 + quality_impact*.25 + switching*.20 + spend_scale*.20
business_score = business_raw*2

# Supply risk = qualification 30%, lack of alternatives 30%, concentration 25%, switching 15%
conc_score = min(5, max(1, 1 + top3*4))
alt_risk = 6-alternatives
supply_raw = qualification*.30 + alt_risk*.30 + conc_score*.25 + switching*.15
supply_score = supply_raw*2

impact_high=business_score>=6
risk_high=supply_score>=6
if impact_high and risk_high: quadrant="STRATEGIC"
elif impact_high and not risk_high: quadrant="LEVERAGE"
elif not impact_high and risk_high: quadrant="BOTTLENECK"
else: quadrant="NON-CRITICAL"

st.subheader("2. Kraljic Matrix")
a,b,c=st.columns([1,1,1])
a.metric("Business Impact",f"{business_score:.1f}/10")
b.metric("Supply Risk",f"{supply_score:.1f}/10")
c.metric("Classification",quadrant)

matrix = pd.DataFrame([
    ["LEVERAGE" if quadrant!="LEVERAGE" else "● LEVERAGE","STRATEGIC" if quadrant!="STRATEGIC" else "● STRATEGIC"],
    ["NON-CRITICAL" if quadrant!="NON-CRITICAL" else "● NON-CRITICAL","BOTTLENECK" if quadrant!="BOTTLENECK" else "● BOTTLENECK"]
], index=["HIGH Business Impact","LOW Business Impact"], columns=["LOW Supply Risk","HIGH Supply Risk"])
st.table(matrix)

with st.expander("Why this Kraljic classification?"):
    st.markdown(f"""
**Business Impact = {business_score:.1f}/10**
- Operational criticality: {criticality}/5 — human input
- Quality/customer impact: {quality_impact}/5 — human input
- Switching complexity: {switching}/5 — human input
- Spend-scale proxy: {spend_scale:.1f}/5 — calculated from uploaded spend

**Supply Risk = {supply_score:.1f}/10**
- Qualification difficulty: {qualification}/5 — human input
- Qualified alternatives: {alternatives}/5 — human input
- Top-3 concentration: {top3:.1%} — internal evidence
- Switching complexity: {switching}/5 — human input

**Method note:** MVP2 uses transparent weighted rules. The classification is a decision-support hypothesis, not an automatic final decision.
""")

# SWOT evidence engine
strengths=[]; weaknesses=[]; opportunities=[]; threats=[]
if total>0: strengths.append(("Purchasing scale visibility",f"Uploaded category spend totals {total:,.0f}.","High"))
if top3>=.65: strengths.append(("Incumbent leverage potential",f"Top 3 suppliers represent {top3:.1%} of spend, creating meaningful commercial scale with key suppliers.","Medium"))
if coverage is not None and coverage>=.75: strengths.append(("Good contract coverage",f"{coverage:.1%} of spend appears under active contract.","Medium"))

if top3>=.65: weaknesses.append(("High supplier concentration",f"Top 3 suppliers represent {top3:.1%} of spend.","High"))
if pv is not None and pv>=.08: weaknesses.append(("Price inconsistency",f"Median observed comparable-SKU price spread is {pv:.1%}.","High"))
if coverage is not None and coverage<.80: weaknesses.append(("Contract exposure",f"Only {coverage:.1%} of spend appears under active contract.","Medium"))
if tail_n>=3: weaknesses.append(("Supplier fragmentation",f"{tail_n} low-spend suppliers together represent {tail_share:.1%} of spend.","High"))

if pv is not None and pv>=.08: opportunities.append(("Price harmonization","Validate like-for-like differences and commercial-condition harmonization.","High"))
if alternatives>=3: opportunities.append(("Competitive sourcing","Human assessment indicates multiple qualified alternatives may be available.","Medium"))
else: opportunities.append(("Alternative supplier development","Qualified alternatives are currently assessed as limited; investigate development/qualification.","Medium"))
if tail_n>=3: opportunities.append(("Supplier portfolio optimization","Assess consolidation of low-value suppliers while protecting technical coverage.","Medium"))
if coverage is not None and coverage<.80: opportunities.append(("Contract coverage improvement","Map uncovered spend and align contracting actions with category priorities.","High"))

if alternatives<=2: threats.append(("Limited qualified alternatives",f"Availability of alternatives rated {alternatives}/5.","Medium"))
if qualification>=4: threats.append(("Long / difficult qualification",f"Qualification difficulty rated {qualification}/5.","Medium"))
if criticality>=4 and top3>=.65: threats.append(("Supply continuity exposure",f"Criticality is {criticality}/5 while supplier concentration is {top3:.1%}.","High"))
if switching>=4: threats.append(("High switching complexity",f"Switching complexity rated {switching}/5.","Medium"))

st.subheader("3. Evidence-Based SWOT")
left,right=st.columns(2)
with left:
    st.markdown("### Strengths")
    for x,e,conf in strengths or [("No strong internal signal yet","More evidence required.","Low")]:
        st.markdown(f"**{x}**  \n{e}  \n*Confidence: {conf}*")
    st.markdown("### Opportunities")
    for x,e,conf in opportunities:
        st.markdown(f"**{x}**  \n{e}  \n*Confidence: {conf}*")
with right:
    st.markdown("### Weaknesses")
    for x,e,conf in weaknesses or [("No major internal weakness triggered","Continue validating category data.","Low")]:
        st.markdown(f"**{x}**  \n{e}  \n*Confidence: {conf}*")
    st.markdown("### Threats")
    for x,e,conf in threats or [("External threats not yet assessed","MVP3 will add market intelligence.","Low")]:
        st.markdown(f"**{x}**  \n{e}  \n*Confidence: {conf}*")

# Strategic implications
imp=[]
if quadrant=="STRATEGIC":
    imp += ["Protect continuity of supply before pursuing aggressive supplier-base changes.",
            "Use partnership and competitive tension selectively; avoid decisions based only on price."]
elif quadrant=="LEVERAGE":
    imp += ["Use purchasing power and competition to improve commercial conditions.",
            "Consider consolidation and sourcing waves where specifications allow."]
elif quadrant=="BOTTLENECK":
    imp += ["Prioritize supply assurance, alternatives and specification flexibility over pure savings.",
            "Reduce dependency and qualification constraints."]
else:
    imp += ["Simplify procurement effort and reduce transactional complexity.",
            "Consider catalogs, consolidation and efficient buying channels."]
if pv is not None and pv>=.08: imp.append("Validate and normalize price variance before setting a savings target.")
if top3>=.65: imp.append("Quantify dependency and resilience before reallocating incumbent volumes.")
if coverage is not None and coverage<.80: imp.append("Close material contract-coverage gaps as part of the category roadmap.")

st.subheader("4. Strategic Implications — So What?")
for i,x in enumerate(imp,1): st.write(f"**{i}.** {x}")

# Strategy
st.subheader("5. Recommended Strategic Direction")
if quadrant=="STRATEGIC":
    direction="Secure supply continuity while using category scale to improve competitiveness, develop alternatives and strengthen supplier relationships."
elif quadrant=="LEVERAGE":
    direction="Exploit purchasing power through competitive sourcing, price harmonization and supplier portfolio optimization."
elif quadrant=="BOTTLENECK":
    direction="Reduce supply vulnerability through alternative qualification, specification flexibility and continuity planning."
else:
    direction="Simplify the supplier base and buying process while minimizing transactional cost."
st.success(direction)

pillars=[]
if top3>=.65: pillars.append(["Supplier Resilience","Assess dependency, capacity, qualification lead time and alternative sources."])
if pv is not None and pv>=.08: pillars.append(["Commercial Excellence","Normalize comparable prices and address unexplained commercial variance."])
if tail_n>=3: pillars.append(["Portfolio Optimization","Review tail suppliers for consolidation without compromising coverage."])
if coverage is not None and coverage<.80: pillars.append(["Governance","Increase active-contract coverage for material spend."])
if not pillars: pillars.append(["Category Intelligence","Close evidence gaps before committing to structural changes."])
st.dataframe(pd.DataFrame(pillars,columns=["Strategic Pillar","Direction"]),use_container_width=True,hide_index=True)

# Roadmap
road=[]
if top3>=.65: road.append(["Dependency & resilience assessment","High","0–30 days","Category Manager","Risk baseline"])
if pv is not None and pv>=.08: road.append(["Normalize price variance","High","0–30 days","Category Manager","Comparable price baseline"])
if alternatives<=2: road.append(["Alternative supplier scan / qualification plan","High","30–90 days","Sourcing + Quality","Qualified alternatives"])
else: road.append(["Competitive sourcing assessment","High","30–60 days","Sourcing","Competitive coverage"])
if tail_n>=3: road.append(["Tail-supplier review","Medium","30–90 days","Procurement","Supplier complexity"])
if coverage is not None and coverage<.80: road.append(["Contract gap closure","High","0–60 days","Procurement + Legal","Contract coverage"])
st.subheader("6. Execution Roadmap")
st.dataframe(pd.DataFrame(road,columns=["Initiative","Priority","Timing","Owner","KPI"]),use_container_width=True,hide_index=True)

st.subheader("7. Challenge My Strategy")
ch=[]
if quadrant=="STRATEGIC": ch.append("Does the proposed commercial strategy preserve continuity if a major incumbent loses capacity?")
if top3>=.65: ch.append("Is concentration caused by a deliberate strategic choice or by historical sourcing behavior?")
if pv is not None and pv>=.08: ch.append("Are price comparisons normalized for specification, volume, freight, Incoterms and payment terms?")
if alternatives<=2: ch.append("Could technical specifications be changed to increase the pool of qualified suppliers?")
for x in ch: st.write("•",x)

st.caption("MVP2 guardrail: internal calculations and human inputs are distinguished. External market facts are intentionally deferred to MVP3.")
