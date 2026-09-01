# MVP Functional Specification

## Core flow
Category Context → Upload → Data Readiness → Category Health Check → Findings → Opportunities → Strategy → Roadmap → Challenge / Ask Copilot

## Calculation rules
- Total spend: sum of Spend
- Supplier share: supplier spend / total category spend
- Top-3 concentration: share of three largest suppliers
- HHI: sum of squared supplier shares × 10,000
- Tail suppliers: smallest suppliers whose cumulative spend is within 20% of total category spend
- Price variance: median SKU-level (max unit price - min unit price) / min unit price for SKUs with at least two observations
- Contract coverage: spend associated with rows classified as active/valid/covered
- Weighted payment terms: spend-weighted average

## Interpretation rules
- Top-3 >= 70%: high concentration signal
- Top-3 >= 50%: medium concentration signal
- Median comparable price spread >= 8%: price-harmonization hypothesis
- >=5 tail suppliers: supplier-fragmentation hypothesis
- Contract coverage <80%: contract-exposure hypothesis

## Guardrails
- Opportunity ≠ savings
- Concentration ≠ automatically bad
- External supplier identified ≠ qualified
- Price variance must be normalized before business-case use
- Missing evidence must be stated
