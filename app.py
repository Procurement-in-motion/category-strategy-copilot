
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

st.set_page_config(page_title="Category Strategy Copilot", page_icon="🧭", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1.3rem; padding-bottom: 3rem;}
div[data-testid="stMetric"] {border: 1px solid #e8e8e8; padding: 14px; border-radius: 14px; background: #fff;}
.small-note {color:#6b7280;font-size:0.88rem;}
.finding {padding:14px 16px;border:1px solid #e5e7eb;border-radius:14px;margin-bottom:10px;background:#fafafa;}
.badge {display:inline-block;padding:4px 9px;border-radius:999px;background:#eef2ff;font-size:0.78rem;font-weight:600;}
</style>
""", unsafe_allow_html=True)

st.title("🧭 Category Strategy Copilot")
st.caption("Evidence-based category intelligence: data → findings → opportunities → strategy → roadmap")

with st.sidebar:
    st.header("Category Context")
    category = st.text_input("Category", "Corrugated Packaging")
    geography = st.text_input("Geography", "Brazil")
    industry = st.text_input("Business / Industry", "Industrial Equipment")
    st.divider()
    st.markdown("**MVP v0.1**")
    st.caption("Internal analytics are calculated from uploaded data. Strategy recommendations are rule-based in this MVP and explicitly separated from factual calculations.")

uploaded = st.file_uploader("Upload procurement data", type=["csv","xlsx","xls"])
st.caption("Minimum recommended fields: Supplier, Spend, Category. Optional: Date, Plant, SKU, Quantity, Unit Price, Contract Status, Payment Terms.")

if uploaded is None:
    st.info("Upload a file to begin. A sample dataset is included in the download package.")
    st.stop()

try:
    if uploaded.name.lower().endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)
except Exception as e:
    st.error(f"Could not read file: {e}")
    st.stop()

# Flexible column matching
def find_col(candidates):
    lower = {str(c).strip().lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower:
            return lower[cand.lower()]
    for c in df.columns:
        lc = str(c).strip().lower()
        if any(cand.lower() in lc for cand in candidates):
            return c
    return None

supplier_col = find_col(["supplier","vendor"])
spend_col = find_col(["spend","amount","value"])
category_col = find_col(["category"])
date_col = find_col(["date","invoice date","po date"])
plant_col = find_col(["plant","site","location"])
sku_col = find_col(["sku","material","item"])
qty_col = find_col(["quantity","qty","volume"])
price_col = find_col(["unit price","price"])
contract_col = find_col(["contract status","contract"])
payment_col = find_col(["payment terms","payment term"])

required_ok = supplier_col is not None and spend_col is not None
if not required_ok:
    st.error("I need at least Supplier/Vendor and Spend/Amount columns.")
    st.write("Detected columns:", list(df.columns))
    st.stop()

df[spend_col] = pd.to_numeric(df[spend_col], errors="coerce").fillna(0)
if qty_col: df[qty_col] = pd.to_numeric(df[qty_col], errors="coerce")
if price_col: df[price_col] = pd.to_numeric(df[price_col], errors="coerce")
if date_col: df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

# Readiness
checks = {
    "Spend analysis": supplier_col is not None and spend_col is not None,
    "Supplier analysis": supplier_col is not None and spend_col is not None,
    "Price analysis": sku_col is not None and price_col is not None,
    "Geographic analysis": plant_col is not None,
    "Demand analysis": qty_col is not None and date_col is not None,
    "Contract analysis": contract_col is not None,
    "Payment terms": payment_col is not None,
}
st.subheader("1. Data Readiness")
cols = st.columns(4)
for i,(name,ok) in enumerate(checks.items()):
    cols[i%4].markdown(f"**{'✓' if ok else '○'} {name}**  \n{'Ready' if ok else 'Not available'}")

# Core analytics
total_spend = float(df[spend_col].sum())
supplier_spend = df.groupby(supplier_col, dropna=False)[spend_col].sum().sort_values(ascending=False)
n_suppliers = int(supplier_spend.shape[0])
top1 = float(supplier_spend.iloc[:1].sum()/total_spend) if total_spend else 0
top3 = float(supplier_spend.iloc[:3].sum()/total_spend) if total_spend else 0
shares = supplier_spend/total_spend if total_spend else supplier_spend*0
hhi = float((shares**2).sum()*10000) if total_spend else 0

# Tail suppliers = suppliers collectively below 20% of spend when sorted ascending
asc = supplier_spend.sort_values()
cum = asc.cumsum()/total_spend if total_spend else asc*0
tail = asc[cum <= 0.20]
tail_count = int(len(tail))
tail_share = float(tail.sum()/total_spend) if total_spend else 0

price_variance = None
if sku_col and price_col:
    temp = df[[sku_col, price_col]].dropna()
    grouped = temp.groupby(sku_col)[price_col].agg(["min","max","count"])
    grouped = grouped[grouped["count"] >= 2]
    if not grouped.empty:
        grouped["spread"] = np.where(grouped["min"]>0,(grouped["max"]-grouped["min"])/grouped["min"],np.nan)
        price_variance = float(grouped["spread"].median())

contract_coverage = None
if contract_col:
    active = df[contract_col].astype(str).str.lower().str.contains("active|valid|yes|covered")
    contract_coverage = float(df.loc[active, spend_col].sum()/total_spend) if total_spend else 0

avg_terms = None
if payment_col:
    terms = pd.to_numeric(df[payment_col], errors="coerce")
    if terms.notna().any():
        avg_terms = float(np.average(terms.fillna(terms.median()), weights=df[spend_col].clip(lower=0)+1e-9))

st.subheader("2. Category Health Check")
m = st.columns(5)
m[0].metric("Total Spend", f"{total_spend:,.0f}")
m[1].metric("Suppliers", n_suppliers)
m[2].metric("Top-3 Concentration", f"{top3:.1%}")
m[3].metric("HHI", f"{hhi:,.0f}")
m[4].metric("Price Variance", "N/A" if price_variance is None else f"{price_variance:.1%}")

# Findings
findings = []
if top3 >= 0.70:
    findings.append(("Supplier concentration","High",f"Top 3 suppliers represent {top3:.1%} of category spend.",
                     "Potential dependency risk, but also potential leverage with strategic suppliers.","High"))
elif top3 >= 0.50:
    findings.append(("Supplier concentration","Medium",f"Top 3 suppliers represent {top3:.1%} of category spend.",
                     "Supplier portfolio should be reviewed for leverage and resilience.","High"))
else:
    findings.append(("Supplier concentration","Low",f"Top 3 suppliers represent {top3:.1%} of category spend.",
                     "Spend is relatively dispersed across suppliers.","High"))

if tail_count >= 5:
    findings.append(("Supplier fragmentation","Medium",f"{tail_count} suppliers together represent {tail_share:.1%} of spend.",
                     "Investigate whether low-value suppliers can be consolidated without harming technical coverage.","High"))

if price_variance is not None and price_variance >= 0.08:
    findings.append(("Comparable price variance","High",f"Median observed SKU price spread is {price_variance:.1%}.",
                     "Validate specification, freight and commercial-condition differences; price harmonization may be feasible.","High"))

if contract_coverage is not None and contract_coverage < 0.80:
    findings.append(("Contract exposure","High",f"Estimated spend under active contract is {contract_coverage:.1%}.",
                     "Review uncovered spend and upcoming sourcing/contracting needs.","Medium"))

st.subheader("3. Key Findings")
for title,level,evidence,implication,confidence in findings:
    st.markdown(
        f"""<div class="finding"><span class="badge">{level}</span>
        <b style="margin-left:8px">{title}</b><br><br>
        <b>Evidence:</b> {evidence}<br>
        <b>Implication:</b> {implication}<br>
        <span class="small-note">Confidence: {confidence}</span></div>""",
        unsafe_allow_html=True
    )

st.subheader("4. Supplier View")
supplier_table = supplier_spend.reset_index()
supplier_table.columns = ["Supplier","Spend"]
supplier_table["Share"] = supplier_table["Spend"]/total_spend if total_spend else 0
supplier_table["Cumulative Share"] = supplier_table["Share"].cumsum()
st.dataframe(supplier_table, use_container_width=True, hide_index=True)

# Opportunities
opps = []
if price_variance is not None and price_variance >= 0.08:
    opps.append(["Price harmonization","High","High","High","Observed comparable-item price spread"])
if top3 >= 0.60:
    opps.append(["Competitive tension / dual-source review","High","Medium","Medium","High supplier concentration"])
if tail_count >= 5:
    opps.append(["Supplier portfolio optimization","Medium","Medium","Medium","Tail-supplier fragmentation"])
if contract_coverage is not None and contract_coverage < 0.80:
    opps.append(["Contract coverage improvement","Medium","High","High","Uncovered / non-active contract spend"])
if avg_terms is not None and avg_terms < 60:
    opps.append(["Payment-term optimization","Medium","Medium","Medium",f"Weighted average terms ≈ {avg_terms:.0f} days"])
if not opps:
    opps.append(["Category deep-dive","Medium","Medium","Low","No major rule-based signals triggered"])

opp_df = pd.DataFrame(opps, columns=["Opportunity","Value Potential","Feasibility","Confidence","Evidence"])
st.subheader("5. Opportunity Hypotheses")
st.dataframe(opp_df, use_container_width=True, hide_index=True)
st.caption("Value Potential is not a savings estimate. Validation is required before business-case commitments.")

# Strategy
pillars = []
if any(opp_df["Opportunity"].str.contains("Price harmonization")):
    pillars.append(("Commercial Consistency","Validate comparable-price differences and harmonize commercial conditions where justified."))
if any(opp_df["Opportunity"].str.contains("Competitive")):
    pillars.append(("Competitive Sourcing & Resilience","Test incumbent competitiveness and assess credible alternatives before changing supplier allocation."))
if any(opp_df["Opportunity"].str.contains("portfolio")):
    pillars.append(("Supplier Portfolio Optimization","Reduce unnecessary fragmentation while preserving technical and continuity requirements."))
if any(opp_df["Opportunity"].str.contains("Contract")):
    pillars.append(("Governance & Coverage","Increase active-contract coverage for material spend and align sourcing waves with expirations."))
if not pillars:
    pillars.append(("Evidence-led Optimization","Deepen internal and market evidence before committing to structural category changes."))

st.subheader("6. Recommended Category Strategy")
st.markdown(f"**Category:** {category}  \n**Geography:** {geography}  \n**Business:** {industry}")
st.markdown("**Strategic direction:** Increase category transparency, validate commercial competitiveness, and improve supplier portfolio decisions using evidence before committing to savings targets.")
for i,(p,desc) in enumerate(pillars,1):
    st.markdown(f"**{i}. {p}** — {desc}")

# Roadmap
roadmap = []
if price_variance is not None and price_variance >= 0.08:
    roadmap.append(["Validate price variance","High","0–30 days","Category Manager","Comparable price baseline"])
if top3 >= 0.60:
    roadmap.append(["Assess alternative suppliers","High","30–60 days","Sourcing","Qualified alternatives"])
    roadmap.append(["Prepare competitive sourcing wave","High","60–90 days","Sourcing","Competitive spend coverage"])
if tail_count >= 5:
    roadmap.append(["Review tail suppliers","Medium","30–90 days","Category Manager","Supplier count / complexity"])
if contract_coverage is not None and contract_coverage < 0.80:
    roadmap.append(["Map contract gaps","High","0–30 days","Procurement + Legal","Contract coverage"])
if not roadmap:
    roadmap.append(["Complete category data gaps","Medium","0–30 days","Category Manager","Data readiness"])

roadmap_df = pd.DataFrame(roadmap, columns=["Initiative","Priority","Timing","Owner","KPI"])
st.subheader("7. Execution Roadmap")
st.dataframe(roadmap_df, use_container_width=True, hide_index=True)

# Challenge-me
st.subheader("8. Challenge My Strategy")
challenges = []
if top3 >= 0.70:
    challenges.append("If you reduce or reallocate incumbent volume, have you quantified switching cost, qualification lead time and business-continuity exposure?")
if price_variance is not None and price_variance >= 0.08:
    challenges.append("Are the compared prices truly like-for-like after specifications, freight, Incoterms, volumes and payment terms are normalized?")
if tail_count >= 5:
    challenges.append("Do tail suppliers cover unique specifications, regions or emergency capacity that would make consolidation risky?")
if contract_coverage is not None and contract_coverage < 0.80:
    challenges.append("Is uncovered spend intentional, or does it reflect contracting-process gaps?")
if not challenges:
    challenges.append("Which external market facts would materially change this strategy if they moved against your current assumptions?")
for c in challenges:
    st.write("•", c)

# Contextual chat - rule based
st.subheader("9. Ask your Category Copilot")
question = st.text_input("Ask about the analysis", placeholder="Why are you recommending competitive sourcing?")
if question:
    q = question.lower()
    if "competitive" in q or "sourcing" in q:
        st.write(f"Competitive sourcing is being suggested as a hypothesis because the top three suppliers represent {top3:.1%} of spend. This does not prove that switching is feasible; alternative-supplier capability and qualification constraints still need validation.")
    elif "price" in q:
        if price_variance is None:
            st.write("Price analysis is not available because SKU/item and unit-price fields were not detected.")
        else:
            st.write(f"The median observed price spread across SKUs with multiple observations is {price_variance:.1%}. Before treating this as an opportunity, normalize specifications, freight, Incoterms, volumes and payment terms.")
    elif "missing" in q or "data" in q:
        missing = [k for k,v in checks.items() if not v]
        st.write("Main analysis gaps: " + (", ".join(missing) if missing else "no major structural gaps detected in the current MVP checks."))
    elif "challenge" in q:
        st.write("Key challenge: the current strategy is based mainly on internal transactional signals. External supplier availability, cost drivers, qualification constraints and market dynamics must be validated before final approval.")
    else:
        st.write("This MVP chat is contextual but rule-based. It can explain concentration, price variance, missing data, competitive sourcing logic and strategy challenges. A full LLM layer is the next implementation step.")

# Export brief
brief = []
brief.append(f"CATEGORY STRATEGY COPILOT\nCategory: {category}\nGeography: {geography}\nBusiness: {industry}\n")
brief.append(f"Total Spend: {total_spend:,.0f}\nSuppliers: {n_suppliers}\nTop-3 Concentration: {top3:.1%}\nHHI: {hhi:,.0f}\n")
brief.append("\nKEY FINDINGS")
for title,level,evidence,implication,confidence in findings:
    brief.append(f"\n- {title} [{level}]\n  Evidence: {evidence}\n  Implication: {implication}\n  Confidence: {confidence}")
brief.append("\n\nOPPORTUNITIES")
for row in opps:
    brief.append(f"\n- {row[0]} | Value: {row[1]} | Feasibility: {row[2]} | Confidence: {row[3]}")
brief.append("\n\nRECOMMENDED STRATEGY")
for i,(p,desc) in enumerate(pillars,1):
    brief.append(f"\n{i}. {p}: {desc}")
brief_text = "".join(brief)
st.download_button("Download Strategy Brief (.txt)", brief_text, file_name="category_strategy_brief.txt")
