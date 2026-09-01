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

div[data-testid="stButton"] button[kind="primary"],
div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    background-color:{GOLD} !important;
    border-color:{GOLD} !important;
    color:#FFFFFF !important;
}}
div[data-testid="stButton"] button[kind="primary"]:hover,
div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover {{
    background-color:#A96F10 !important;
    border-color:#A96F10 !important;
    color:#FFFFFF !important;
}}


/* Sidebar navigation refinement */
section[data-testid="stSidebar"] div[data-testid="stButton"] button {{
    justify-content:flex-start !important;
    text-align:left !important;
    min-height:2.45rem !important;
    padding:.42rem .65rem !important;
    border-radius:10px !important;
    font-weight:650 !important;
    box-shadow:none !important;
}}

/* Inactive menu item: navy text/icon only, no white button */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] {{
    background:transparent !important;
    border:1px solid transparent !important;
    color:{NAVY} !important;
}}

/* Inactive hover */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"]:hover,
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover {{
    background:rgba(201,138,26,.06) !important;
    border-color:transparent !important;
    color:{GOLD} !important;
}}

/* Active menu item: pale gold rectangle + gold text/icon */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    background:rgba(201,138,26,.13) !important;
    border:1px solid transparent !important;
    color:{GOLD} !important;
}}

section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"]:hover,
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover {{
    background:rgba(201,138,26,.18) !important;
    border-color:transparent !important;
    color:{GOLD} !important;
}}

/* Contact / LinkedIn styled as menu rows */
.nav-link a {{
    display:block;
    padding:.48rem .66rem;
    margin:.10rem 0;
    border-radius:10px;
    text-decoration:none !important;
    color:{NAVY} !important;
    font-weight:650;
    background:transparent !important;
    border:1px solid transparent !important;
}}

.nav-link a:hover {{
    background:rgba(201,138,26,.06) !important;
    color:{GOLD} !important;
}}

/* Main-content primary actions remain Procurement in Motion gold */
section.main div[data-testid="stButton"] button[kind="primary"],
section.main div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    background-color:{GOLD} !important;
    border-color:{GOLD} !important;
    color:#FFFFFF !important;
}}
section.main div[data-testid="stButton"] button[kind="primary"]:hover,
section.main div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover {{
    background-color:#A96F10 !important;
    border-color:#A96F10 !important;
    color:#FFFFFF !important;
}}


/* v6 navigation alignment */
section[data-testid="stSidebar"] div[data-testid="stButton"] button {{
    padding:.48rem .66rem !important;
    margin:.10rem 0 !important;
    font-weight:500 !important;
    min-height:2.38rem !important;
}}

.nav-link a {{
    padding:.48rem .66rem !important;
    margin:.10rem 0 !important;
    font-weight:500 !important;
    min-height:2.38rem !important;
    display:flex !important;
    align-items:center !important;
}}

/* Keep active menu visually highlighted, but not bold */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    font-weight:500 !important;
}}

/* Standardize capability rectangle dimensions */
.pillar {{
    min-height:180px !important;
    height:180px !important;
    display:flex !important;
    flex-direction:column !important;
}}

.pillar h4 {{
    min-height:48px !important;
}}

.pillar p {{
    margin-top:auto !important;
}}


/* v7 navigation card layout */
section[data-testid="stSidebar"] div[data-testid="stButton"] {{
    margin:.65rem 0 !important;
}}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {{
    width:100% !important;
    min-height:4.65rem !important;
    padding:.9rem 1rem !important;
    border-radius:16px !important;
    justify-content:center !important;
    text-align:center !important;
    font-size:1.02rem !important;
    font-weight:500 !important;
}}

/* Inactive navigation cards */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] {{
    background:transparent !important;
    border:1px solid rgba(201,138,26,.65) !important;
    color:{NAVY} !important;
}}

/* Active navigation card */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    background:rgba(201,138,26,.12) !important;
    border:2px solid rgba(201,138,26,.65) !important;
    color:{NAVY} !important;
    box-shadow:0 2px 0 rgba(201,138,26,.20) !important;
}}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {{
    background:rgba(201,138,26,.08) !important;
    border-color:{GOLD} !important;
    color:{NAVY} !important;
}}

/* Contact and LinkedIn use the same navigation-card dimensions */
.nav-link a {{
    width:100% !important;
    min-height:4.65rem !important;
    padding:.9rem 1rem !important;
    margin:.65rem 0 !important;
    border-radius:16px !important;
    border:1px solid rgba(201,138,26,.65) !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    text-align:center !important;
    color:{NAVY} !important;
    font-size:1.02rem !important;
    font-weight:500 !important;
    text-decoration:none !important;
    background:transparent !important;
}}

.nav-link a:hover {{
    background:rgba(201,138,26,.08) !important;
    border-color:{GOLD} !important;
    color:{NAVY} !important;
}}


/* v8 compact, evenly-spaced, typographically consistent navigation */
section[data-testid="stSidebar"] div[data-testid="stButton"] {{
    margin:.38rem 0 !important;
}}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {{
    width:100% !important;
    min-height:3.25rem !important;
    height:3.25rem !important;
    padding:.45rem .8rem !important;
    margin:0 !important;
    border-radius:14px !important;
    justify-content:center !important;
    text-align:center !important;
    font-family:"Segoe UI", Arial, sans-serif !important;
    font-size:.96rem !important;
    font-weight:400 !important;
    line-height:1.2 !important;
}}

section[data-testid="stSidebar"] div[data-testid="stButton"] button p {{
    font-family:"Segoe UI", Arial, sans-serif !important;
    font-size:.96rem !important;
    font-weight:400 !important;
    line-height:1.2 !important;
    margin:0 !important;
}}

.nav-link {{
    margin:.38rem 0 !important;
}}

.nav-link a {{
    box-sizing:border-box !important;
    width:100% !important;
    min-height:3.25rem !important;
    height:3.25rem !important;
    padding:.45rem .8rem !important;
    margin:0 !important;
    border-radius:14px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    text-align:center !important;
    font-family:"Segoe UI", Arial, sans-serif !important;
    font-size:.96rem !important;
    font-weight:400 !important;
    line-height:1.2 !important;
    text-decoration:none !important;
    color:{NAVY} !important;
}}

/* Keep the active item non-bold */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    font-weight:400 !important;
}}


/* v9 — exact menu rhythm + capability card fit */

/* Remove Streamlit wrapper spacing differences */
section[data-testid="stSidebar"] div[data-testid="stButton"],
section[data-testid="stSidebar"] .nav-link {{
    margin:0 !important;
}}

/* Use the same 12px gap after EVERY navigation row */
section[data-testid="stSidebar"] div[data-testid="stButton"] {{
    margin-bottom:12px !important;
}}
section[data-testid="stSidebar"] .nav-link {{
    margin-bottom:12px !important;
}}

/* Identical menu card geometry */
section[data-testid="stSidebar"] div[data-testid="stButton"] button,
section[data-testid="stSidebar"] .nav-link a {{
    width:100% !important;
    height:3.25rem !important;
    min-height:3.25rem !important;
    padding:.45rem .8rem !important;
    margin:0 !important;
    border-radius:14px !important;
    box-sizing:border-box !important;
    font-family:"Segoe UI", Arial, sans-serif !important;
    font-size:.96rem !important;
    font-weight:400 !important;
    line-height:1.2 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    text-align:center !important;
}}

/* Capability cards: equal, taller, and text-safe */
.pillar {{
    height:260px !important;
    min-height:260px !important;
    padding:20px 18px !important;
    display:flex !important;
    flex-direction:column !important;
    overflow:visible !important;
}}

.pillar .num {{
    flex:0 0 auto !important;
}}

.pillar h4 {{
    min-height:62px !important;
    margin:.72rem 0 .55rem !important;
    font-size:1.18rem !important;
    line-height:1.18 !important;
    flex:0 0 auto !important;
}}

.pillar p {{
    margin:0 !important;
    font-size:.84rem !important;
    line-height:1.48 !important;
    overflow-wrap:anywhere !important;
}}


/* v10 — uniform menu gaps and stable thin borders */

/* Normalize Streamlit vertical block gaps inside sidebar */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
    gap:0 !important;
}}

/* Exact same spacing after each navigation row */
section[data-testid="stSidebar"] div[data-testid="stButton"],
section[data-testid="stSidebar"] .nav-link {{
    margin:0 0 14px 0 !important;
    padding:0 !important;
}}

/* Same geometry for all four rectangles */
section[data-testid="stSidebar"] div[data-testid="stButton"] button,
section[data-testid="stSidebar"] .nav-link a {{
    width:100% !important;
    height:3.25rem !important;
    min-height:3.25rem !important;
    margin:0 !important;
    padding:.45rem .8rem !important;
    border-radius:14px !important;
    box-sizing:border-box !important;
    font-family:"Segoe UI", Arial, sans-serif !important;
    font-size:.96rem !important;
    font-weight:400 !important;
    line-height:1.2 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    text-align:center !important;
}}

/* Inactive buttons keep their fine gold border at rest AND hover */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] {{
    background:transparent !important;
    border:1px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"]:hover,
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover {{
    background:rgba(201,138,26,.06) !important;
    border:1px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}

/* Active button keeps the same shape; only fill/border emphasis changes */
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"],
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {{
    background:rgba(201,138,26,.12) !important;
    border:2px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}
section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="primary"]:hover,
section[data-testid="stSidebar"] div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover {{
    background:rgba(201,138,26,.15) !important;
    border:2px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}

/* Contact and LinkedIn keep their thin border when hovering */
section[data-testid="stSidebar"] .nav-link a {{
    background:transparent !important;
    border:1px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}
section[data-testid="stSidebar"] .nav-link a:hover {{
    background:rgba(201,138,26,.06) !important;
    border:1px solid rgba(201,138,26,.70) !important;
    color:{NAVY} !important;
}}


/* v12 — reliable spacing below the Navigation heading */
section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type {{
    margin-top:16px !important;
}}

/* Preserve the exact equal spacing between menu items from v10 */
section[data-testid="stSidebar"] div[data-testid="stButton"],
section[data-testid="stSidebar"] .nav-link {{
    margin-bottom:14px !important;
}}


/* v13 — keep title gap, make every inter-button gap identical */

/* First card: preserve only the extra space below Navigation */
section[data-testid="stSidebar"] div[data-testid="stButton"]:first-of-type {{
    margin-top:16px !important;
}}

/* Every navigation row gets exactly the same 14px gap after it */
section[data-testid="stSidebar"] div[data-testid="stButton"],
section[data-testid="stSidebar"] .nav-link {{
    margin-left:0 !important;
    margin-right:0 !important;
    margin-bottom:14px !important;
    padding-top:0 !important;
    padding-bottom:0 !important;
}}

/* Prevent Streamlit wrappers around consecutive buttons from adding extra space */
section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(div[data-testid="stButton"]) {{
    margin:0 !important;
    padding:0 !important;
}}

section[data-testid="stSidebar"] div[data-testid="stElementContainer"]:has(.nav-link) {{
    margin:0 !important;
    padding:0 !important;
}}


/* v14 — one HTML structure for all navigation cards */
.nav-menu {{
    display:flex;
    flex-direction:column;
    gap:14px;
    margin-top:16px;
}}

.nav-menu .nav-card {{
    width:100%;
    height:3.25rem;
    min-height:3.25rem;
    box-sizing:border-box;
    border:1px solid rgba(201,138,26,.70);
    border-radius:14px;
    background:transparent;
    color:{NAVY} !important;
    text-decoration:none !important;
    display:flex;
    align-items:center;
    justify-content:center;
    gap:.52rem;
    padding:.45rem .8rem;
    font-family:"Segoe UI", Arial, sans-serif;
    font-size:.96rem;
    font-weight:400;
    line-height:1.2;
    margin:0 !important;
}}

.nav-menu .nav-card:hover {{
    background:rgba(201,138,26,.06);
    border:1px solid rgba(201,138,26,.70);
    color:{NAVY} !important;
    text-decoration:none !important;
}}

.nav-menu .nav-card.active {{
    background:rgba(201,138,26,.12);
    border:2px solid rgba(201,138,26,.70);
    box-shadow:0 2px 0 rgba(201,138,26,.18);
}}

.nav-menu .nav-card.active:hover {{
    background:rgba(201,138,26,.15);
    border:2px solid rgba(201,138,26,.70);
}}

.nav-menu .nav-icon {{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:1.1rem;
    font-size:1rem;
    font-weight:400;
}}

.nav-menu .linkedin-icon {{
    font-family:Arial, sans-serif;
    font-size:.92rem;
}}

</style>
""", unsafe_allow_html=True)

logo = Path(__file__).parent / "pim_logo.png"
if logo.exists():
    st.sidebar.image(str(logo), use_container_width=True)

# Navigation is driven by query parameters so every menu row can use the
# exact same HTML structure and spacing.
query_page = st.query_params.get("page", "Expertise")
if isinstance(query_page, list):
    query_page = query_page[0]
if query_page not in ["Expertise", "Portfolio", "Category Strategy Copilot"]:
    query_page = "Expertise"

st.session_state.pim_page = query_page
page = st.session_state.pim_page

def go_to(page):
    st.query_params["page"] = page
    st.session_state.pim_page = page

st.sidebar.markdown("### Navigation")

expertise_class = "nav-card active" if page == "Expertise" else "nav-card"
portfolio_class = "nav-card active" if page == "Portfolio" else "nav-card"

st.sidebar.markdown(
    f"""
    <div class="nav-menu">
      <a class="{expertise_class}" href="?page=Expertise" target="_self">
        <span class="nav-icon">⌂</span><span>Expertise</span>
      </a>
      <a class="{portfolio_class}" href="?page=Portfolio" target="_self">
        <span class="nav-icon">▦</span><span>Portfolio</span>
      </a>
      <a class="nav-card" href="mailto:motalarissa.br@gmail.com">
        <span class="nav-icon">✉</span><span>Contact</span>
      </a>
      <a class="nav-card" href="https://www.linkedin.com/in/motalarissa" target="_blank">
        <span class="nav-icon linkedin-icon">in</span><span>LinkedIn</span>
      </a>
    </div>
    """,
    unsafe_allow_html=True
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

if page == "Expertise":
    hub_hero(
        "Procurement in Motion",
        "Procurement strategy, governance, transformation and AI — translated into practical frameworks and solutions."
    )

    st.markdown("## Expertise")
    st.markdown("""<div class="about-card">
    <p>Procurement and business excellence experience across global, regional and local organizations, combining Strategic Sourcing, Category Management, Procurement Excellence, Source-to-Contract, Source-to-Pay, supplier governance, analytics and digital transformation.</p>
    <p>The common thread is turning complex procurement environments into clearer strategies, scalable processes, stronger governance and practical tools that support better decisions.</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("## Core capabilities")
    p1,p2,p3,p4,p5 = st.columns(5)
    pillars = [
        ("01","Strategy","Translate business priorities into procurement direction."),
        ("02","Category","Connect spend, demand, suppliers, markets and risk."),
        ("03","Process","Design clear and scalable ways of working."),
        ("04","Systems","Enable decisions and controls through digital workflows."),
        ("05","Analytics & AI","Turn data into evidence, insight and action.")
    ]
    for col_, (num,title,desc) in zip([p1,p2,p3,p4,p5], pillars):
        with col_:
            st.markdown(f'<div class="pillar"><div class="num">{num}</div><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown("## Procurement in Motion")
    st.markdown("""<div class="about-card">
    <p>Procurement in Motion is a practical portfolio exploring how Procurement can become more strategic, scalable and decision-oriented through better frameworks, governance, analytics and AI-enabled ways of working.</p>
    <p>The focus is practical: understand the decision, build the evidence, design the process and governance, and then determine where technology and AI can genuinely strengthen the outcome.</p>
    </div>""", unsafe_allow_html=True)

    footer()
    st.stop()

if page == "Portfolio":
    hub_hero(
        "Portfolio",
        "A growing portfolio of practical Procurement frameworks and AI-enabled tools."
    )
    st.markdown('<div class="gold-label">WORK IN PROGRESS (WIP)</div>', unsafe_allow_html=True)
    st.markdown("## Selected projects")

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
            if st.button(
                "Open project  →",
                type="primary",
                key="open_project_portfolio"
            ):
                go_to("Category Strategy Copilot")
                st.rerun()
    footer()
    st.stop()

# ---------------------------
# CATEGORY STRATEGY COPILOT
# ---------------------------
if st.button("‹  Back to Portfolio", key="back_to_portfolio"):
    go_to("Portfolio")
    st.rerun()

hub_hero(
    "Category Strategy Copilot",
    "From procurement data to evidence-based, actionable category strategy."
)

st.markdown("## Category setup")
st.caption("Define the category context and strategic inputs before analyzing the procurement data.")

with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        category = st.text_input("Category", "Corrugated Packaging")
    with c2:
        geography = st.text_input("Geography", "Brazil")
    with c3:
        industry = st.text_input("Business / Industry", "Industrial Equipment")

    st.markdown("#### Strategic inputs")
    s1, s2, s3 = st.columns(3)
    with s1:
        criticality = st.slider("Operational criticality", 1, 5, 4)
        switching = st.slider("Switching cost / complexity", 1, 5, 3)
    with s2:
        qualification = st.slider("Supplier qualification difficulty", 1, 5, 4)
        alternatives = st.slider("Qualified alternatives", 1, 5, 2)
    with s3:
        quality = st.slider("Quality / customer impact", 1, 5, 4)
        st.caption("1 = lower · 5 = higher")

st.markdown("")

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
