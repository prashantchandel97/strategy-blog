# Week Summary — 2026-06-22 (Updated Wednesday)
_Compiler: read this file, NOT the full research file._

## Core Thesis
Enterprise AI's 95% pilot failure is being solved by cheap compute (hyperscaler custom silicon: Amazon Trainium $20B+, Google TPU $25B by 2027) and measurement discipline. **But regulation moves slower than deployment.** AICOA has 20-30% passage probability; EU's DMA enforcement on cloud stretches to 2029 via litigation. Hyperscalers will entrench custom silicon's cost advantage before regulation forces non-discrimination. TSMC 3nm constraints naturally limit displacement to 25-35% of inference (not 40-50%). **Real outcome: Custom silicon moat survives, moderated by regulation; Nvidia margins compress to 68-70% by 2030 (not 62-65% by 2028); SaaS bifurcates on data-readiness, not measurement discipline.**

## The Key Tension
**Does regulation destroy a hardware moat before it scales, or does the market move faster than law?** Researcher: AICOA/DMA force non-discrimination by 2027-2029, collapsing the advantage. Analyst: AICOA has failed three times; DMA litigation stretches to 2029; hyperscalers can comply via pricing parity while keeping operational moats. By then, custom silicon is entrenched. Hyperscalers likely have 3-4 year window (2026-2029) to build defensibility—roughly enough time.

## Key Facts & Data Points
- **95% of enterprise AI pilots deliver zero measurable P&L impact; 42% abandoned in 2025** — MIT Sloan; S&P Global — https://mitsloan.mit.edu/ideas-made-to-matter/action-items-ai-decision-makers-2026
- **Amazon custom chip business: $20B+ annual run rate (Q1 2026), triple-digit growth** — Trainium tracking to exceed Nvidia data center revenue by 2027 — https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm
- **Google TPU: $25B revenue target by 2027; Trillium 1.8x better perf/dollar than prior gen** — https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview
- **Custom silicon 40-50% TCO reduction vs. Nvidia (up to 67% for specialized workloads)** — optimized for Transformers; reduces silicon area — https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia
- **TSMC 3nm at 100% utilization; demand 3x supply** — constrains custom chip scaling through 2027-2028 — https://www.businessinsider.com/tsmc-3nm-capacity-constraint-2026-ai
- **AICOA reintroduced June 10, 2026; failed three times (2020, 2022, 2024); passage probability 20-30%** — tech lobbying $400M+ in 2026 — https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation
- **EU DMA cloud enforcement: preliminary findings mid-2026; final designation Q4 2026–Q1 2027; litigation 2-3 years** — hyperscalers can comply via pricing parity while keeping operational moats — https://www.reuters.com/legal/litigation/eu-rules-reining-big-tech-will-now-target-cloud-services-and-ai-regulators-say-2026-04-28/
- **Nvidia margin: 78% today; consensus 62-65% by 2028 (40-50% displacement assumption); realistic 68-70% by 2030 (25-35% displacement)** — https://markets.businessinsider.com/news/stocks/nvidia-faces-margin-compression-as-hyperscalers-deploy-custom-ai-chips-2026-20240526
- **ServiceNow bundled AI into per-seat pricing; avoided consumption models because transparent costs kill adoption** — https://www.rezolve.ai/blog/servicenow-pricing-guide-custom-quotes-for-tailored-it-service-management/
- **Measured AI winners: 41% return vs. 29% S&P 500** — causality unclear (discipline, data quality, or compute access?) — https://www.morganstanley.com/insights/articles/ai-market-trends-institute-2026
- **Microsoft Maia 200 shipping now; targets 55-60% Azure margin vs. 30% for Nvidia-dependent services** — https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/

## Week Thread (Day-by-Day Arc)
- **Monday R**: 95% failure is organizational (measurement discipline missing), not technological. Winners measure ROI before scaling. SaaS pricing fractures under variable compute costs.
- **Monday A**: Data readiness is causally prior to measurement. Back-office wins because processes are data-native. Soft ROI undervalued. Opacity survives transparency because it kills adoption.
- **Tuesday R**: Custom silicon solves cost problem: Amazon/Google/Microsoft delivering 40-50% TCO reduction. Unit economics flip. TSMC 3nm capacity constraints limit scaling.
- **Tuesday A**: Measurement discipline becomes irrelevant if costs drop 50%. Real dividing line: infrastructure access. TSMC bottleneck extends Nvidia's reprieve to 2029-2030.
- **Wednesday R**: AICOA and DMA force non-discrimination on custom chip pricing, destroying moat by 2027-2029. Regulation mandates interoperability and separate business units.
- **Wednesday A**: Regulation moves slower than market. AICOA 20-30% passage probability; DMA enforcement stretches to 2029 via litigation. Hyperscalers can comply via pricing parity while keeping operational moats. Damage is real but contained.

## Best Sources
- https://www.sec.gov/Archives/edgar/container-0001018724-2026/0001018724-26-000022-index.htm — Amazon Q1 2026: custom chip business
- https://cloud.google.com/blog/products/compute/trillium-sixth-generation-tpu-is-in-preview — Google TPU roadmap
- https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ — Microsoft Maia 200 strategy
- https://introl.com/blog/custom-silicon-inflection-2026-hyperscaler-asics-nvidia — Custom silicon cost & TSMC constraints
- https://www.judiciary.senate.gov/press/rep/releases/grassley-klobuchar-introduce-bipartisan-legislation — AICOA reintroduction
- https://www.reuters.com/legal/litigation/eu-rules-reining-big-tech-will-now-target-cloud-services-and-ai-regulators-say-2026-04-28/ — DMA cloud enforcement timeline

## Open Questions for the Blog
1. **Is AICOA real or symbolic?** Failed three times; ~25% passage probability. If regulation is low-probability, does the market price custom silicon as a real moat (not a regulatory risk)? How does this change Nvidia valuation models?

2. **When does custom silicon cost advantage flow to enterprise customers?** Amazon hinting at externalizing Trainium. If it does, SaaS vendors lose margin layer entirely. If hyperscalers keep it internal, enterprise ROI stays hard. Which path dominates?

3. **Which SaaS categories win from cheap compute?** Finance/operations (data-native, measurable ROI) vs. sales/marketing (unstructured, soft ROI). Does cheap compute move the needle enough to justify adoption friction?

## Strongest Thread for the Blog
**Regulation as a moderating force, not a moat-killer.** Four forces shift the market concurrently (measurement discipline + custom silicon + supply constraints + regulatory pressure), but regulatory pressure is the slowest. AICOA probably fails; DMA litigation stretches to 2029; hyperscalers engineer compliance via pricing parity while keeping operational moats. Result: custom silicon advantage persists but moderates to 20-30% (not 40-50%) by 2030. Nvidia margins compress to 68-70% by 2030 (not 62-65% by 2028). This is the realistic scenario between the bear case ("regulation destroys custom silicon by 2027") and bull case ("custom silicon dominates by 2028").
