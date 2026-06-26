# Week Summary — 2026-06-22 (Updated Friday)
_Compiler: read this file, NOT the full research file._

## Core Thesis
Enterprise AI's 95% pilot failure isn't about measurement discipline—it's about **data readiness.** Fintech proves it: Stripe detects 32% more fraud (transaction data = structured), Razorpay reduced fraud losses 40% YoY, Cashfree achieves 70% detection accuracy instantly. Finance, operations, fintech work because their data is inherently measurable; sales and marketing fail because they're diffuse and overdetermined. **Hyperscalers' custom silicon (Amazon Trainium $20B+, Google TPU $25B by 2027) cuts costs 40-50%, but this only unlocks ROI in data-ready domains, not unstructured ones.** Regulation moves slower than deployment (AICOA 20-30% passage; DMA enforcement to 2029), so hyperscalers entrench advantage by 2030. **Real outcome: Enterprise AI bifurcates by domain. Data-native SaaS (fintech, finance, operations) trades at 10-12x revenue multiples with expanding margins; horizontal SaaS (sales, marketing, support) compresses to 4-6x with contracting margins.**

## The Key Tension
**Does cheap compute and regulation change enterprise AI adoption broadly, or only in data-ready domains?** Researcher (Monday): Discipline separates winners. Analyst (Monday): Data structure matters more than discipline. Fintech (Thursday): Data structure is causally prior—fintech ROI is 32%+ fraud reduction because transactions are inherently measurable. Custom silicon cost reduction helps data-ready domains escape the ROI wall; unstructured domains stay stuck. Regulation: AICOA/DMA will eventually force democratization, but fintech gets regulatory exemptions ("AI improves compliance") while sales/marketing don't. **The bifurcation is structural, not regulatory or cost-driven.**

## Key Facts & Data Points
- **95% of enterprise AI pilots fail; 42% of projects abandoned in 2025** — measurement discipline wasn't the root cause — https://mitsloan.mit.edu/ideas-made-to-matter/action-items-ai-decision-makers-2026
- **Stripe Radar: 32% fraud reduction; Razorpay: 40% YoY fraud loss reduction; Cashfree: 70% fraud detection accuracy** — fintech ROI is measurable because transactions are data-native — https://stripe.com/radar
- **Razorpay at 12.5x revenue multiple; Stripe at ~57x (private); fintech premium: 46% above horizontal SaaS** — data-ready domain valuation bifurcation visible now — https://www.premieralts.com/companies/razorpay/valuation
- **Amazon Trainium: $20B+ annual run rate, triple-digit growth; Google TPU: $25B by 2027; Microsoft Maia 200 shipping** — custom silicon cost advantage 40-50% vs. Nvidia, up to 67% for specialized workloads — https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm
- **TSMC 3nm at 100% utilization; demand 3x supply constrains deployment to 2028-2029** — supply constraints naturally moderate displacement — https://www.businessinsider.com/tsmc-3nm-capacity-constraint-2026-ai
- **AICOA reintroduced June 10, 2026; failed three times; 20-30% passage probability; EU DMA enforcement stretches to 2027-2029 via litigation** — regulation moves slower than market entrenchment — https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation
- **Nvidia margin 78% today → realistic 68-70% by 2030 (not 62-65% by 2028); 25-35% custom silicon displacement (not 40-50%)** — supply constraints + regulatory negotiation power moderate impact — https://markets.businessinsider.com/news/stocks/nvidia-faces-margin-compression
- **Data-native domains (finance, operations, compliance) see 15-20% ROI improvement from AI; unstructured domains (sales, marketing) <5% improvement** — cost reduction doesn't unlock ROI where domain fundamentally lacks measurable outcomes — https://www.bain.com/insights/your-ai-budget-is-growing-your-returns-arent-heres-why/

## Week Thread (Day-by-Day Arc)
- **Monday R**: 95% failure from missing measurement discipline; SaaS pricing fractures under variable compute.
- **Monday A**: Data readiness (not discipline) is causally prior; back-office wins; soft ROI undervalued.
- **Tuesday R**: Custom silicon (40-50% cost reduction) solves ROI problem for hyperscalers.
- **Tuesday A**: Cost advantage larger than stated; but TSMC capacity constrains deployment; contradicts measurement thesis if costs weren't the root cause.
- **Wednesday R**: AICOA/DMA force non-discrimination, destroying moat by 2027-2029.
- **Wednesday A**: Regulation moves slower (2029-2030); hyperscalers can comply via pricing parity while keeping operational moats.
- **Thursday R**: Fintech ROI exception proves data readiness is binding constraint; fraud detection works because outcomes are binary and immediate.
- **Thursday A**: Fintech doesn't prove broad AI adoption works—it proves AI only works in structured domains. Bifurcation is structural, not solvable by cost reduction or regulation.

## Best Sources
- https://stripe.com/radar — Stripe's fintech fraud detection proof case
- https://www.premieralts.com/companies/razorpay/valuation — Razorpay valuation and fintech multiples
- https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm — Amazon custom chip business
- https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview — Google TPU roadmap
- https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation — AICOA reintroduction and status
- https://www.businessinsider.com/tsmc-3nm-capacity-constraint-2026-ai — TSMC supply constraints

## Open Questions for the Blog
1. **Which SaaS categories will expand margins (data-native) and which will compress (unstructured)?** Finance and operations are data-native; sales and marketing are unstructured. Is there a middle ground? Build concrete SaaS category map with valuation multiples by domain.

2. **Does fintech's regulatory exemption accelerate its separation from horizontal SaaS?** Fintech AI improves compliance; regulators encourage it. Sales AI has no equivalent exemption. Does this push fintech SaaS to 15-20x multiples while sales stays at 4-6x?

3. **When does custom silicon cost advantage reach enterprise customers, and does it matter?** If hyperscalers externalize Trainium/TPU access at cost parity, compute becomes commoditized. Does cheap compute unlock ROI in unstructured domains, or does it just make bad ROI math less bad?

## Compiler's Note
The week has evolved from "measurement discipline vs. theatrical AI" (Monday) to "data-ready domains win regardless of regulation or cost structure" (Thursday). The strongest blog narrative is **bifurcation by domain, not by discipline or infrastructure.** Fintech is the proof case, but it also reveals the limits: AI doesn't fix unstructured work problems, it only solves structured ones. Stock market is still pricing broad adoption; reality is narrow adoption in data-native verticals.
