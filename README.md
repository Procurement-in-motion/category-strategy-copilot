# Category Strategy Copilot — MVP v0.1

A working Streamlit prototype for procurement category strategy.

## What it does
- Upload CSV/XLSX procurement data
- Flexible column detection
- Data readiness check
- Spend and supplier analysis
- Top-1 / Top-3 concentration
- HHI concentration index
- Tail supplier analysis
- Comparable SKU price-variance analysis
- Contract coverage
- Payment-term signal
- Evidence-based findings
- Opportunity hypotheses
- Recommended category strategy
- Execution roadmap
- "Challenge my strategy"
- Contextual rule-based copilot Q&A
- Downloadable strategy brief

## Important design principle
Calculations come from the analytics layer. The interpretation layer does not invent the underlying metrics.

## Run locally

1. Install Python 3.10+
2. Open a terminal in this folder
3. Install dependencies:

   pip install -r requirements.txt

4. Start:

   streamlit run app.py

5. Open the local URL shown by Streamlit.
6. Upload `sample_corrugated_packaging.csv`.

## Expected next version
- External Market Intelligence with cited sources
- LLM-based contextual reasoning
- Evidence/source panel
- Strategic scenario comparison
- Export to PPTX / DOCX
- User-configurable category methodology

## Expected input columns

Minimum:
- Supplier or Vendor
- Spend / Amount / Value

Recommended:
- Category
- Subcategory
- Date
- Plant / Site
- SKU / Material / Item
- Quantity
- Unit Price
- Contract Status
- Payment Terms
