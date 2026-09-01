import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Procurement in Motion | Larissa Mota",
    page_icon="◈",
    layout="wide"
)

NAVY="#0B2A59"
GOLD="#C98A1A"
BG="#FBFAF7"
TEXT="#172033"
BEIGE="#F3EEE5"
WHITE="#FFFFFF"
MUTED="#667085"

st.markdown(f"""
<style>
html, body, [class*="css"] {{
    font-family: "Segoe UI", Arial, sans-serif;
}}
.stApp {{
    background:{BG};
    color:{TEXT};
}}
.block-container {{
    padding-top:1.15rem;
    padding-bottom:2.4rem;
    max-width:1450px;
}}
header[data-testid="stHeader"] {{
    background:{BG};
    border-bottom:1px solid #ECE8E1;
}}
section[data-testid="stSidebar"] {{
    background:{BEIGE};
    border-right:1px solid #DED6CA;
}}
section[data-testid="stSidebar"] > div {{
    padding-top:1.1rem;
}}
section[data-testid="stSidebar"] * {{
    color:{NAVY};
}}
section[data-testid="stSidebar"] input {{
    color:{TEXT} !important;
    background:white !important;
    border-radius:12px !important;
}}
section[data-testid="stSidebar"] [data-baseweb="slider"] * {{
    color:{NAVY};
}}
h1,h2,h3,h4 {{
    color:{NAVY};
}}
div[data-testid="stMetric"] {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:16px;
    padding:14px;
    box-shadow:0 2px 10px rgba(11,42,89,.04);
}}
div[data-testid="stMetricValue"] > div {{
    font-size:2.05rem !important;
    line-height:1.05 !important;
}}
[data-testid="stFileUploader"] {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:18px;
    padding:10px;
}}
div[data-testid="stTabs"] button p {{
    font-weight:700;
    color:{NAVY};
}}
div[data-testid="stTabs"] button[aria-selected="true"] {{
    border-bottom-color:{GOLD} !important;
}}
.stAlert {{
    border-radius:14px;
}}
hr {{
    border-color:#DED6CA;
}}
.pim-hero {{
    background:{NAVY};
    border-left:6px solid {GOLD};
    padding:34px 36px;
    border-radius:20px;
    color:white;
    margin-bottom:26px;
    box-shadow:0 4px 18px rgba(11,42,89,.10);
}}
.pim-hero h1 {{
    color:white;
    margin:0;
    font-size:2.75rem;
    line-height:1.08;
}}
.pim-hero p {{
    color:#E8EEF8;
    margin:.85rem 0 0;
    font-size:1.08rem;
    max-width:900px;
}}
.eyebrow {{
    color:white;
    font-size:.73rem;
    letter-spacing:.14em;
    font-weight:800;
    margin-bottom:.55rem;
}}
.eyebrow .dot {{
    color:{GOLD};
}}
.gold-label {{
    color:{GOLD};
    font-size:.76rem;
    letter-spacing:.12em;
    font-weight:800;
    text-transform:uppercase;
}}
.intro {{
    font-size:1.08rem;
    color:{MUTED};
    max-width:900px;
}}
.project-card {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:18px;
    padding:22px;
    height:100%;
    box-shadow:0 2px 12px rgba(11,42,89,.035);
}}
.project-card.active {{
    border-top:4px solid {GOLD};
}}
.project-card h3 {{
    margin:.35rem 0 .55rem;
}}
.project-card p {{
    color:{MUTED};
    font-size:.92rem;
    min-height:78px;
}}
.status {{
    color:{GOLD};
    font-size:.74rem;
    font-weight:800;
}}
.pillar {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:16px;
    padding:18px;
    min-height:150px;
}}
.pillar .num {{
    color:{GOLD};
    font-size:.72rem;
    font-weight:800;
}}
.pillar h4 {{
    margin:.65rem 0 .4rem;
}}
.pillar p {{
    color:{MUTED};
    font-size:.88rem;
}}
.about-card {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:18px;
    padding:24px;
    margin:10px 0;
}}
.card {{
    background:white;
    border:1px solid #E6E0D7;
    border-radius:16px;
    padding:16px;
    margin:8px 0;
    box-shadow:0 2px 10px rgba(11,42,89,.03);
}}
.footer {{
    margin-top:36px;
    padding-top:18px;
    border-top:1px solid #DED6CA;
    color:#7A8290;
    font-size:.76rem;
    letter-spacing:.08em;
}}
</style>
""", unsafe_allow_html=True)

logo = Path(__file__).parent / "pim_logo.png"
if logo.exists():
    st.sidebar.image(str(logo), use_container_width=True)

if "pim_page" not in st.session_state:
    st.session_state.pim_page = "Home"

def go_to(page):
    st.session_state.pim_page = page

st.sidebar.markdown("### Navigation")
page = st.sidebar.radio(
    "Procurement in Motion",
    ["Home", "Projects", "About", "Approach", "Category Strategy Copilot"],
    key="pim_page",
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Portfolio status**")
st.sidebar.caption("Category Strategy Copilot · WIP")
st.sidebar.caption("3 projects · To be initiated")

def hub_hero(title, subtitle):
    st.markdown(
        f"""<div class="pim-hero">
        <div class="eyebrow">PROCUREMENT STRATEGY <span class="dot">·</span> GOVERNANCE <span class="dot">·</span> TRANSFORMATION <span class="dot">·</span> AI</div>
        <h1>{title}</h1><p>{subtitle}</p></div>""",
        unsafe_allow_html=True
    )

def footer():
    st.markdown(
        '<div class="footer">PROCUREMENT IN MOTION &nbsp; | &nbsp; BY LARISSA MOTA</div>',
        unsafe_allow_html=True
    )

if page == "Home":
    hub_hero(
        "Procurement in Motion",
        "Practical frameworks and AI-enabled solutions for modern Procurement."
    )
    st.markdown(
        '<p class="intro">A portfolio connecting strategy, category management, sourcing, governance, processes, analytics and AI — designed to turn procurement information into clearer decisions and executable action.</p>',
        unsafe_allow_html=True
    )

    st.markdown("## Explore the portfolio")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="project-card active">
        <span class="status">WIP · FUNCTIONAL MVP</span>
        <h3>Category Strategy Copilot</h3>
        <p>Turn spend, business requirements, supplier dynamics, market intelligence and risk into an evidence-based, actionable category strategy.</p>
        </div>""", unsafe_allow_html=True)
        st.button(
            "Open Category Strategy Copilot →",
            type="primary",
            use_container_width=True,
            on_click=go_to,
            args=("Category Strategy Copilot",)
        )
    with c2:
        st.markdown("""<div class="project-card">
        <span class="status">TO BE INITIATED</span>
        <h3>Strategic Sourcing Event</h3>
        <p>Guide the sourcing journey from scope and requirements through market engagement, RFI/RFP/RFQ, bid analysis, negotiation, supplier selection and award.</p>
        </div>""", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("""<div class="project-card">
        <span class="status">TO BE INITIATED</span>
        <h3>Negotiation Framework</h3>
        <p>A disciplined and evidence-based approach to negotiation preparation, scenarios, BATNA, targets, concessions, total value and documented outcomes.</p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="project-card">
        <span class="status">TO BE INITIATED</span>
        <h3>Procurement Governance Architecture</h3>
        <p>Connect policy, process, risk, controls, approvals, evidence, exceptions and performance across the Procurement lifecycle.</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("## Procurement in Motion")
    p1,p2,p3,p4,p5 = st.columns(5)
    pillars = [
        ("01","Strategy","Translate business priorities into procurement direction."),
        ("02","Category","Connect spend, demand, suppliers, markets and risk."),
        ("03","Process","Design clear and scalable ways of working."),
        ("04","Systems","Enable decisions and controls through digital workflows."),
        ("05","Analytics","Turn data into evidence, insight and action.")
    ]
    for col_, (num,title,desc) in zip([p1,p2,p3,p4,p5], pillars):
        with col_:
            st.markdown(f'<div class="pillar"><div class="num">{num}</div><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

    footer()
    st.stop()

if page == "Projects":
    hub_hero(
        "Projects",
        "A growing portfolio of Procurement frameworks and AI-enabled tools."
    )
    st.markdown('<div class="gold-label">WORK IN PROGRESS (WIP)</div>', unsafe_allow_html=True)
    st.markdown("## Selected Portfolio")

    projects = [
        ("01","Category Strategy Copilot","WIP",
         "An AI-enabled approach that turns spend, business requirements, supply-market intelligence, supplier dynamics and risk into an evidence-based, actionable category strategy."),
        ("02","Strategic Sourcing Event","To be initiated",
         "An end-to-end sourcing approach from scope and business requirements through market engagement, RFI/RFP/RFQ, bid analysis, supplier evaluation, negotiation, decision governance and award."),
        ("03","Negotiation Framework","To be initiated",
         "A disciplined, ethical and evidence-based method to prepare, conduct and document supplier negotiations — connecting fact base, BATNA, targets, scenarios, concessions and total value."),
        ("04","Procurement Governance Architecture","To be initiated",
         "A governance architecture connecting policy, standards, processes, controls, approvals, evidence, exceptions, KPIs and continuous improvement.")
    ]
    for num,title,status,desc in projects:
        st.markdown(
            f"""<div class="about-card">
            <span class="gold-label">{num} · {status}</span>
            <h3>{title}</h3>
            <p>{desc}</p>
            </div>""",
            unsafe_allow_html=True
        )
        if title == "Category Strategy Copilot":
            st.button(
                "Open project →",
                type="primary",
                key="open_project_projects",
                on_click=go_to,
                args=("Category Strategy Copilot",)
            )
    footer()
    st.stop()

if page == "About":
    hub_hero(
        "About",
        "Procurement experience translated into practical frameworks, governance and digital solutions."
    )
    st.markdown("## About Larissa Mota")
    st.markdown("""<div class="about-card">
    <p>Procurement and business excellence professional with experience across global, regional and local organizations, combining Strategic Sourcing, Category Management, Procurement Excellence, Source-to-Contract, Source-to-Pay, supplier governance, analytics and digital transformation.</p>
    <p>The common thread is turning complex procurement environments into clearer strategies, scalable processes, stronger governance and practical tools that support better decisions.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("## Core capabilities")
    a,b,c = st.columns(3)
    with a:
        st.markdown("""<div class="pillar"><div class="num">STRATEGY</div><h4>Strategic Sourcing & Category</h4><p>Category strategy, sourcing, negotiation, supplier portfolio and value creation.</p></div>""", unsafe_allow_html=True)
    with b:
        st.markdown("""<div class="pillar"><div class="num">EXCELLENCE</div><h4>Governance & Transformation</h4><p>Processes, policies, controls, operating models, CLM and procurement transformation.</p></div>""", unsafe_allow_html=True)
    with c:
        st.markdown("""<div class="pillar"><div class="num">DIGITAL</div><h4>Analytics, Automation & AI</h4><p>KPIs, dashboards, workflows, automation and AI-enabled procurement use cases.</p></div>""", unsafe_allow_html=True)

    st.markdown("## Procurement in Motion")
    st.write(
        "Procurement in Motion is a practical portfolio for exploring how Procurement can become more strategic, scalable and decision-oriented through better frameworks, governance, analytics and AI-enabled ways of working."
    )
    footer()
    st.stop()

if page == "Approach":
    hub_hero(
        "Approach",
        "Start with the decision. Build the evidence. Define the process and governance. Then determine where technology and AI can strengthen the outcome."
    )
    st.markdown("## How the approach works")
    steps = [
        ("01","Decision","Define the business or Procurement decision that needs to be improved."),
        ("02","Evidence","Identify the internal data, external intelligence and human inputs required."),
        ("03","Process","Create a clear workflow from input through analysis, decision and execution."),
        ("04","Governance","Define policies, controls, approvals, exceptions and evidence requirements."),
        ("05","Technology & AI","Use automation and AI where they improve speed, consistency, insight or user experience."),
        ("06","Human validation","Keep accountable judgment and approval with the appropriate people.")
    ]
    for num,title,desc in steps:
        st.markdown(f'<div class="about-card"><span class="gold-label">{num}</span><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("## Design principles")
    st.markdown(
        "**Evidence before recommendation · Assumptions made explicit · Confidence visible · "
        "Opportunity is not automatically savings · External intelligence requires sources · "
        "AI supports decisions; it does not replace accountable judgment.**"
    )
    footer()
    st.stop()

# ---------------------------
# CATEGORY STRATEGY COPILOT
# ---------------------------
hub_hero(
    "Category Strategy Copilot",
    "From procurement data to evidence-based, actionable category strategy."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Category Context")
category=st.sidebar.text_input("Category","Corrugated Packaging")
geography=st.sidebar.text_input("Geography","Brazil")
industry=st.sidebar.text_input("Business / Industry","Industrial Equipment")
st.sidebar.markdown("---")
st.sidebar.markdown("### Strategic Inputs")
criticality=st.sidebar.slider("Operational criticality",1,5,4)
qualification=st.sidebar.slider("Supplier qualification difficulty",1,5,4)
switching=st.sidebar.slider("Switching cost / complexity",1,5,3)
alternatives=st.sidebar.slider("Qualified alternatives",1,5,2)
quality=st.sidebar.slider("Quality / customer impact",1,5,4)

uploaded=st.file_uploader("Upload procurement data",type=["csv","xlsx","xls"])

with st.expander("What data should I upload?", expanded=False):
    st.markdown("""
Upload **one CSV or Excel file** containing category-level procurement data.  
Only **Supplier** and **Spend** are required to start; additional fields unlock richer analysis.
""")
    requirements = pd.DataFrame([
        ["Supplier","Required","Supplier analysis, concentration and dependency"],
        ["Spend","Required","Spend baseline and supplier concentration/share"],
        ["Category","Recommended","Category scope and context validation"],
        ["Date","Recommended","Spend and demand trends over time"],
        ["Plant / Location","Optional","Site and geographic analysis"],
        ["SKU / Material","Recommended","Comparable item and price analysis"],
        ["Quantity","Recommended","Demand and volume analysis"],
        ["Unit Price","Recommended","Comparable price variance"],
        ["Contract Status","Recommended","Contract coverage and exposure"],
        ["Payment Terms","Optional","Commercial terms analysis"],
    ], columns=["Field","Status","Used for"])
    st.dataframe(requirements, use_container_width=True, hide_index=True)
    st.markdown("""**Minimum to start:** Supplier + Spend  
**For richer insights:** add SKU, Unit Price, Quantity, Contract Status and Date.""")

sample_path = Path(__file__).parent/"sample_corrugated_packaging.xlsx"
sample_col, guide_col = st.columns([1,2])
with sample_col:
    if sample_path.exists():
        st.download_button(
            "Download sample dataset",
            data=sample_path.read_bytes(),
            file_name="sample_corrugated_packaging.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
with guide_col:
    st.caption("Use the sample as a template for column structure. Your own file can contain additional fields.")

if uploaded is None:
    st.info("Not sure what to upload? Review the required fields above or download the sample dataset.")
    st.stop()

df=pd.read_csv(uploaded) if uploaded.name.lower().endswith(".csv") else pd.read_excel(uploaded)

def col(names):
    for c in df.columns:
        if str(c).strip().lower() in [n.lower() for n in names]: return c
    for c in df.columns:
        if any(n.lower() in str(c).lower() for n in names): return c
    return None

supplier=col(["supplier","vendor"])
spend=col(["spend","amount","value"])
category_col=col(["category"])
date_col=col(["date","invoice date","po date"])
plant=col(["plant","site","location"])
sku=col(["sku","material","item"])
qty=col(["quantity","qty","volume"])
price=col(["unit price","price"])
contract=col(["contract status","contract"])
payment=col(["payment terms","payment term"])

if not supplier or not spend:
    st.error("The file cannot be analyzed yet. Required fields missing: Supplier and/or Spend.")
    st.stop()

analysis_readiness = [
    ("Spend baseline", bool(spend), "Spend"),
    ("Supplier concentration", bool(supplier and spend), "Supplier + Spend"),
    ("Price variance", bool(sku and price), "SKU / Material + Unit Price"),
    ("Demand / volume analysis", bool(qty), "Quantity"),
    ("Trend analysis", bool(date_col), "Date"),
    ("Plant / location analysis", bool(plant), "Plant / Location"),
    ("Contract coverage", bool(contract), "Contract Status"),
    ("Payment terms analysis", bool(payment), "Payment Terms"),
]
available_count = sum(1 for _, ready, _ in analysis_readiness if ready)
total_analyses = len(analysis_readiness)

st.markdown("### Data Readiness")
r1, r2 = st.columns([1,3])
with r1:
    st.metric("Analyses available", f"{available_count}/{total_analyses}")
with r2:
    if available_count >= 7:
        st.success("Strong dataset — most internal analyses are available.")
    elif available_count >= 4:
        st.info("Good starting point — some analyses will be limited by missing fields.")
    else:
        st.warning("Basic analysis only — add recommended fields to unlock richer insights.")

ready_df = pd.DataFrame([
    ["Ready" if ready else "Not available", analysis, fields]
    for analysis, ready, fields in analysis_readiness
], columns=["Status","Analysis","Required data"])
st.dataframe(ready_df, use_container_width=True, hide_index=True)
st.caption("Missing data is shown explicitly. The Copilot does not infer unavailable evidence.")

df[spend]=pd.to_numeric(df[spend],errors="coerce").fillna(0)
total=float(df[spend].sum()); ss=df.groupby(supplier)[spend].sum().sort_values(ascending=False)
n=len(ss); shares=ss/total if total else ss*0
top3=float(ss.head(3).sum()/total) if total else 0
hhi=float((shares**2).sum()*10000) if total else 0

def compact_number(value):
    value = float(value)
    abs_value = abs(value)
    if abs_value >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"
    if abs_value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"
    if abs_value >= 1_000:
        return f"{value/1_000:.1f}K"
    return f"{value:,.0f}"
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

spend_scale=min(5,max(1,1+np.log10(max(total,1))/2))
business=(criticality*.35+quality*.25+switching*.20+spend_scale*.20)*2
conc=min(5,max(1,1+top3*4))
risk=(qualification*.30+(6-alternatives)*.30+conc*.25+switching*.15)*2
q="STRATEGIC" if business>=6 and risk>=6 else "LEVERAGE" if business>=6 else "BOTTLENECK" if risk>=6 else "NON-CRITICAL"

tabs=st.tabs(["Overview","Internal Intelligence","Market Intelligence","Kraljic","SWOT","Opportunities","Strategy","Roadmap","Evidence"])

with tabs[0]:
    st.subheader(f"{category} · {geography}")
    m=st.columns(5)
    m[0].metric("Spend", compact_number(total))
    m[1].metric("Suppliers", n)
    m[2].metric("Top-3", f"{top3:.1%}")
    m[3].metric("Price variance", "N/A" if pv is None else f"{pv:.1%}")
    m[4].metric("Kraljic", q.title())
    st.markdown('<div class="card"><b>Category North Star</b><br>Evidence before recommendation: facts, human inputs and external intelligence are separated before action.</div>',unsafe_allow_html=True)

with tabs[1]:
    st.subheader("Internal Intelligence")
    st.dataframe(ss.rename("Spend").reset_index(),use_container_width=True,hide_index=True)
    rows=[]
    if top3>=.65: rows.append(["Supplier concentration",f"Top 3 = {top3:.1%}","Dependency risk + leverage potential","High"])
    if pv is not None and pv>=.08: rows.append(["Price variance",f"Median SKU spread = {pv:.1%}","Validate harmonization","High"])
    if tail_n>=3: rows.append(["Tail fragmentation",f"{tail_n} suppliers = {tail_share:.1%}","Portfolio optimization","High"])
    if coverage is not None and coverage<.8: rows.append(["Contract exposure",f"Coverage = {coverage:.1%}","Governance opportunity","Medium"])
    st.dataframe(pd.DataFrame(rows,columns=["Finding","Evidence","Implication","Confidence"]),use_container_width=True,hide_index=True)

with tabs[2]:
    st.subheader("Supply Market Intelligence")
    st.warning("MVP3A workspace — external facts are not fabricated. Live cited research will be connected in MVP3B.")
    for title,desc in [
        ("Market Structure","Size · growth · concentration · capacity · regional/global structure · entry barriers"),
        ("Supplier Landscape","Current and alternative suppliers · capabilities · geography · scale"),
        ("Cost Drivers","Raw materials · energy · labor · conversion · freight · FX — no invented weights"),
        ("Trends & Risks","Technology · regulation · sustainability · capacity · M&A · geopolitics")]:
        st.markdown(f'<div class="card"><b>{title}</b><br>{desc}</div>',unsafe_allow_html=True)

with tabs[3]:
    st.subheader("Kraljic Matrix")
    a,b,c=st.columns(3); a.metric("Business Impact",f"{business:.1f}/10"); b.metric("Supply Risk",f"{risk:.1f}/10"); c.metric("Classification",q)
    mat=pd.DataFrame([["● LEVERAGE" if q=="LEVERAGE" else "LEVERAGE","● STRATEGIC" if q=="STRATEGIC" else "STRATEGIC"],
                      ["● NON-CRITICAL" if q=="NON-CRITICAL" else "NON-CRITICAL","● BOTTLENECK" if q=="BOTTLENECK" else "BOTTLENECK"]],
                     index=["HIGH Business Impact","LOW Business Impact"],columns=["LOW Supply Risk","HIGH Supply Risk"])
    st.table(mat)
    with st.expander("Why this classification?"):
        st.write(f"Business impact {business:.1f}/10 — criticality {criticality}/5, quality/customer impact {quality}/5, switching {switching}/5.")
        st.write(f"Supply risk {risk:.1f}/10 — qualification {qualification}/5, alternatives {alternatives}/5, Top-3 concentration {top3:.1%}.")
        st.caption("Transparent decision-support hypothesis; Category Manager validation required.")

strength=[["Purchasing scale visibility",f"Spend = {total:,.0f}","High"]]; weak=[]; opp=[]; threat=[]
if top3>=.65:
    strength.append(["Incumbent leverage potential",f"Top 3 = {top3:.1%}","Medium"])
    weak.append(["High supplier concentration",f"Top 3 = {top3:.1%}","High"])
if pv is not None and pv>=.08:
    weak.append(["Price inconsistency",f"Median SKU spread = {pv:.1%}","High"])
    opp.append(["Price harmonization","Normalize like-for-like prices","High"])
if tail_n>=3:
    weak.append(["Supplier fragmentation",f"{tail_n} tail suppliers = {tail_share:.1%}","High"])
    opp.append(["Portfolio optimization","Assess tail consolidation","Medium"])
if coverage is not None and coverage<.8:
    weak.append(["Contract exposure",f"Coverage = {coverage:.1%}","Medium"])
    opp.append(["Contract coverage","Close material gaps","High"])
if alternatives<=2:
    threat.append(["Limited qualified alternatives",f"Human assessment = {alternatives}/5","Medium"])
    opp.append(["Alternative supplier development","Investigate qualification","Medium"])
if qualification>=4: threat.append(["Qualification constraint",f"Difficulty = {qualification}/5","Medium"])

with tabs[4]:
    st.subheader("Evidence-Based SWOT")
    l,r=st.columns(2)
    with l:
        st.markdown("### Strengths")
        for x,e,c in strength: st.write(f"**{x}** — {e} · Confidence: {c}")
        st.markdown("### Opportunities")
        for x,e,c in opp: st.write(f"**{x}** — {e} · Confidence: {c}")
    with r:
        st.markdown("### Weaknesses")
        for x,e,c in weak: st.write(f"**{x}** — {e} · Confidence: {c}")
        st.markdown("### Threats")
        for x,e,c in threat: st.write(f"**{x}** — {e} · Confidence: {c}")
        st.caption("External threats excluded until cited research is connected.")

with tabs[5]:
    st.subheader("Opportunity Portfolio")
    rows=[]
    if pv is not None and pv>=.08: rows.append(["Price harmonization","Commercial","High","High"])
    if top3>=.65: rows.append(["Supplier resilience","Risk","High","High"])
    if alternatives<=2: rows.append(["Alternative supplier development","Supplier","Medium","Medium"])
    if tail_n>=3: rows.append(["Tail supplier optimization","Process","Medium","Medium"])
    if coverage is not None and coverage<.8: rows.append(["Contract coverage","Governance","High","High"])
    st.dataframe(pd.DataFrame(rows,columns=["Opportunity","Type","Potential","Confidence"]),use_container_width=True,hide_index=True)
    st.caption("Opportunity ≠ savings. Financial value requires a validated business case.")

with tabs[6]:
    st.subheader("Recommended Category Strategy")
    direction={"STRATEGIC":"Secure continuity while using category scale to improve competitiveness, develop qualified alternatives and strengthen strategic supplier management.",
               "LEVERAGE":"Use purchasing power through competitive sourcing, commercial harmonization and supplier portfolio optimization.",
               "BOTTLENECK":"Reduce vulnerability through alternatives, specification flexibility and continuity planning.",
               "NON-CRITICAL":"Simplify the supplier base and buying process while minimizing transactional cost."}[q]
    st.success(direction)
    st.markdown("### Challenge My Strategy")
    st.write("• Is concentration deliberate or historical?")
    st.write("• Are price comparisons normalized for specification, volume, freight, Incoterms and payment terms?")
    st.write("• Does the strategy protect continuity if a major incumbent loses capacity?")
    st.write("• Which recommendation would change if external evidence contradicts our assumptions?")

with tabs[7]:
    st.subheader("Execution Roadmap & Governance")
    road=[]
    if top3>=.65: road.append(["Dependency & resilience assessment","High","0–30 days","Category Manager"])
    if pv is not None and pv>=.08: road.append(["Normalize price variance","High","0–30 days","Category Manager"])
    road.append(["Supply market intelligence","High","0–45 days","Category Manager"])
    if alternatives<=2: road.append(["Alternative supplier qualification plan","High","30–90 days","Sourcing + Quality"])
    if coverage is not None and coverage<.8: road.append(["Contract gap closure","High","0–60 days","Procurement + Legal"])
    st.dataframe(pd.DataFrame(road,columns=["Initiative","Priority","Timing","Owner"]),use_container_width=True,hide_index=True)
    st.info("Governance: recommendation → human validation → business case → approval → execution → KPI review.")

with tabs[8]:
    st.subheader("Evidence Center")
    evidence=[
        ["FACT","Total spend",f"{total:,.0f}","Uploaded data","High"],
        ["FACT","Top-3 concentration",f"{top3:.1%}","Uploaded data","High"],
        ["HUMAN INPUT","Operational criticality",f"{criticality}/5","Category assessment","Medium"],
        ["HUMAN INPUT","Qualified alternatives",f"{alternatives}/5","Category assessment","Medium"],
        ["INFERENCE","Kraljic classification",q,"Transparent weighted rule","Medium"],
        ["EXTERNAL INTELLIGENCE","Supply market evidence","Not connected yet","MVP3B","Not available"]]
    st.dataframe(pd.DataFrame(evidence,columns=["Type","Evidence","Value","Source","Confidence"]),use_container_width=True,hide_index=True)
    st.info("No external market claim is shown without a source. Missing evidence is explicit.")


footer()
