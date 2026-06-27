# Week Summary — 2026-06-22 (Final)
_Compiler: read this file, NOT the full research file._

## Core Thesis
Enterprise AI's 95% pilot failure isn't about measurement discipline or cost structure—it's about **domain data-readiness.** When work is inherently data-structured (fintech transactions, finance invoices, operations inventory), AI ROI is immediate and measurable: Stripe detects 32% more fraud, Razorpay reduced fraud losses 40% YoY, finance achieves 8-month payback. When work is diffuse and relationship-driven (sales, marketing), AI ROI is negative or marginal regardless of cost—finance ROI 8 months, sales 18-24+ months. **Custom silicon (Amazon $20B, Google $25B by 2027) cuts costs 40-50%, but only unlocks ROI in data-ready domains.** **Regulation (AICOA <30% passage, DMA to 2029) moves slower than market entrenchment.** **Result: Enterprise AI bifurcates sharply by domain. Data-native SaaS (fintech, finance, operations) separates at 10-15x revenue multiples; horizontal SaaS (sales, marketing) compresses to 4-6x. Wall Street is pricing 1-2x gap when domain ROI differences justify 2.5-3x.**

## The Key Tension
**Can cheap compute and measurement discipline solve enterprise AI ROI in *all* domains, or only in data-ready ones?** Monday framed discipline as the divider. The Analyst showed data structure matters more. Thursday proved fintech ROI (32% fraud reduction, binary outcome) is structural, not cultural—transactions are inherently measurable. Custom silicon helps only where ROI was plausible; it makes bad ROI "less bad," not good. Regulation accelerates bifurcation asymmetrically: fintech gets regulatory tailwinds ("AI improves compliance"), sales gets headwinds ("bias, privacy concerns"). **The bifurcation is structural and permanent, not solvable by cost or regulation.**

## Key Facts & Data Points
- **95% enterprise AI pilots fail; 42% of projects abandoned 2025** — Monday's MIT data. Root cause: unstructured work domains can't produce measurable outcomes, not discipline gaps — https://mitsloan.mit.edu/ideas-made-to-matter/action-items-ai-decision-makers-2026
- **Stripe Radar: 32% fraud reduction; Razorpay: 40% fraud loss YoY reduction; Cashfree: 70% accuracy instant detection** — fintech ROI is provably material because outcomes (fraud/non-fraud) are binary and deterministic — https://stripe.com/radar
- **Finance AI ROI: 8-month payback; Operations AI: 12-14 months; Sales AI: 18-24+ months or failure** — domain data-readiness determines payback, not vendor execution — https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartnerpredicts-by-2029-cfos-who-implement-strategic-ai-deploymnt-will-add-10-margin-points-of-growth
- **Stripe $159B valuation (~57x revenue); Razorpay 12.5x; fintech SaaS trades 46% premium over horizontal (Salesforce 8.5x, HubSpot 7.2x, Slack 4.3x)** — market is pricing domain bifurcation, but undershooting gap — https://www.premieralts.com/companies/razorpay/valuation
- **Amazon Trainium $20B+ annual run rate, triple-digit growth; Google TPU $25B by 2027; custom silicon 40-50% cost reduction vs. Nvidia** — hyperscalers delivering cheaper infrastructure, but benefit concentrates in data-ready domains — https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm
- **TSMC 3nm at 100% utilization; demand 3x supply; deployment constrained to 2028-2029** — supply constraints naturally moderate displacement speed; Nvidia margin compression 78%→68-70% by 2030, not 62-65% by 2028 — https://www.businessinsider.com/tsmc-3nm-capacity-constraint-2026-ai
- **AICOA reintroduced June 10 (20-30% passage probability); EU DMA enforcement stretches to 2027-2029 via litigation** — regulation slower than deployment entrenchment; hyperscalers can comply via pricing parity while keeping operational moats — https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation
- **Data-native domains see 15-20% AI improvement; unstructured domains <5%** — cost reduction doesn't fix domain structure constraints — https://www.bain.com/insights/your-ai-budget-is-growing-your-returns-arent-heres-why/

## Week Thread (Day-by-Day Arc)
- **Monday R:** 95% failure traced to missing measurement discipline; companies lack three-layer foundation (measurement, infrastructure, governance). SaaS pricing fracturing under variable compute costs.
- **Monday A:** Measurement discipline is symptom, not root cause. Data readiness is causally prior. Back-office wins; soft ROI blindness undervalues strategic agility. ServiceNow reverting to per-seat pricing proves transparency kills adoption in unstructured domains.
- **Tuesday R:** Custom silicon (Trainium, TPU, Maia) cuts costs 40-50%. This solves hyperscaler margin problem and creates room for enterprise ROI. Nvidia margin compression 78%→62-65% inevitable by 2028.
- **Tuesday A:** Cost advantage understated (up to 67% for specialized workloads). TSMC capacity is binding constraint. More importantly: cost cuts only matter if ROI was plausible. Fintech ROI already works at Nvidia pricing; sales ROI doesn't work even at custom silicon pricing.
- **Wednesday R:** AICOA + EU DMA force non-discrimination on custom silicon by 2027-2029. Hyperscalers can't keep cost advantage captive. Moat destroyed pre-entrenchment.
- **Wednesday A:** Regulation slower than framed. AICOA sub-30% passage. DMA enforcement stretches 2+ years (preliminary findings Q4 2026, litigation 2+ years). Hyperscalers get 3-4 year runway. Compliance via pricing parity keeps moat 20-30% intact (operational/integration advantage survives).
- **Thursday R:** Fintech proves data-readiness is binding constraint. Transactions are inherently structured, fraud binary. Stripe doesn't win on "measurement discipline culture"; it wins on transaction data being data-native. Finance same. Sales fundamentally unstructured; cost reduction irrelevant.
- **Thursday A:** Fintech exception proves the opposite of what Researcher implies: not "proof case for broad enterprise AI," but "proof case that AI only works in data-ready domains." Bifurcation is structural, permanent. TAM saturation risk for fintech (already 60%+ penetrated?). Horizontal SaaS can't "catch up" through discipline—domain is wrong.
- **Friday R:** SaaS bifurcation map concrete: Stripe 57x, Razorpay 11-13x, Cashfree 2.8x vs. Salesforce 8.5x, HubSpot 7.2x, Zendesk 2.1x. Fintech adoption rate 3.1 projects/1000 FTEs; sales 0.8/1000 FTEs. Gap justified by ROI data. Current 1-2x premium should be 2.5-3x by 2028 (Razorpay 25-30x, Salesforce 5-6x).
- **Friday A:** Fintech multiples are correct, not misprice—but Wall Street is looking at company execution ("Stripe runs better"), not domain structure ("transactions are measurable"). Gap will widen, but market is pricing mechanism right, just denominator wrong. TAM saturation becomes real question: is fintech 60%+ penetrated? Horizontal SaaS segmentation escape path (sell "data-ready piece" separately) plausible but difficult.

## Best Sources
- https://stripe.com/radar — Stripe fraud detection ROI proof case
- https://www.premieralts.com/companies/razorpay/valuation — Razorpay valuations and fintech premium
- https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm — Amazon custom silicon business
- https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview — Google TPU roadmap and performance
- https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartnerpredicts-by-2029-cfos-who-implement-strategic-ai-deploymnt-will-add-10-margin-points-of-growth — Finance AI ROI benchmarks
- https://www.businessinsider.com/tsmc-3nm-capacity-constraint-2026-ai — TSMC supply constraint and timeline

## Open Questions for the Blog
1. **Is the fintech SaaS TAM already saturated (60%+), or is growth runway intact?** If saturated, multiples compress by 2028 even if ROI is strong. If runway, multiples expand. This determines whether "fintech wins" is durable thesis or 2-year trade.

2. **Can horizontal SaaS segment data-ready use cases and escape compression?** If Salesforce sells "Salesforce for finance teams" (10-12x multiple) separately from "Salesforce for sales teams" (4-6x), the blended company could maintain higher multiples. Or does market discount blended portfolios for unfocus?

3. **When will enterprises access hyperscaler custom silicon advantage, and will it matter?** If AWS externalizes Trainium access at cost parity by 2027-2028, compute becomes commoditized. Does this unlock fintech adoption for smaller vendors, or does it just move advantage from hardware to software (Stripe beats competitors on fraud model, not chip)?

## Compiler's Note
The week evolved from "measurement discipline separates winners" (Monday) to "domain structure is causally prior" (Friday). Strongest narrative: **Enterprise AI adoption bifurcates by data-readiness, not discipline. Fintech proves this. Wall Street is pricing mechanism correctly but underpricing gap (1-2x when 2.5-3x justified).** By 2028, fintech SaaS at 10-15x multiples with 15-20% annual ROI; horizontal SaaS at 4-6x with <5% ROI. Regulation and cost structure are secondary. Domain structure is destiny.
