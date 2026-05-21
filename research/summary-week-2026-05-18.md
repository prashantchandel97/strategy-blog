# Week Summary — 2026-05-18 (Updated Wednesday)
_Compiler: read this file, NOT the full research file._

## Core Thesis
The AI infrastructure boom is forcing unprecedented **cost transparency** across enterprise software, cloud compute, and consumer devices. For the first time, technology companies cannot abstract away operational costs. SaaS vendors must transparently charge for LLM token consumption (pushing margins from 75–82% to 60–70%). Hyperscalers must own or lock in power supply because inference costs now dominate their economics. Device makers must bifurcate: on-device inference for commodity queries (Apple, Meta, Qualcomm), cloud frontier APIs for complex reasoning (OpenAI, Anthropic, Google). Winners will build defensible cost models; losers will try to hide infrastructure costs under abstraction layers that no longer work.

## The Key Tension
**Can hyperscalers actually sustain "power = moat" when on-device AI is shifting 30–50% of inference demand to phones and edge hardware?** Researcher says yes, cloud infrastructure becomes stranded. Analyst says no—cloud demand stays strong (OpenAI's inference costs up 68% YoY), but *composition* shifts: commodity queries (chatbots, summaries, basic tasks) move to on-device; frontier reasoning (legal analysis, research, complex problem-solving) stays cloud. The market bifurcates, it doesn't collapse. Microsoft's Three Mile Island is correctly sized for the higher-margin remainder.

## Key Facts & Data Points
- **OpenAI inference costs: $8.4B (2025) → $14.1B (2026), 68% YoY growth**, suggesting demand is *increasing* despite on-device alternatives — https://sacra.com/research/openai/
- **Sierra raised $950M at $15.8B valuation** as agentic AI platform, yet Salesforce (120%+ NRR) and ServiceNow (125% NRR) retain customers while compressing margins — https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/
- **Cloudflare cut 1,100 employees (20%) at record Q1 2026 revenue** with 600% internal AI usage growth, proving headcount no longer scales with SaaS growth — https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/
- **SaaS gross margin compression: 75–82% → 60–70%** from LLM token costs, inference infrastructure, eval engineering labor — https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face
- **Inference consumes 80–90% of AI power** (not training); single ChatGPT query = 2.9 Wh; centralized inference now drives grid demands — https://ttms.com/growing-energy-demand-of-ai-data-centers-2024-2026/
- **Maryland FERC complaint (May 9, 2026): ratepayers pay $2B of $22B grid upgrade plan (9%)** for out-of-state data centers they don't use — https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises
- **Meta's ExecuTorch runs production inference** on billions of WhatsApp, Instagram, Facebook users (1B–3B parameter models at 50+ tokens/sec on iPhone 15) — https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/
- **Qualcomm Snapdragon 8 Elite: 60 TOPS NPU**, running quantized LLMs; Apple WWDC 2026 (June) to unveil on-device Siri — https://v-chandra.github.io/on-device-llms/
- **Hyperscaler power strategy: Microsoft (Three Mile Island, 835 MW by 2028), Meta (6.6 GW nuclear), Google (Kairos/NextEra), Amazon (Spain €15.7B, Texas renewables)** — https://www.latimes.com/business/story/2026-01-09/meta-signs-multi-gigawatt-nuclear-deals-to-power-ai-data-centers

## Week Thread (Day-by-Day Arc)
- **Monday R**: Sierra's $15.8B raise + Cloudflare's 20% layoffs at record revenue signal per-seat SaaS is broken; agentic AI will replace it.
- **Monday A**: SaaS isn't dying, it's hybridizing. Incumbents (Salesforce 120%+ NRR, ServiceNow 125%) retain customers; margins compress 10–15 points from token costs, not defection.
- **Tuesday R**: Inference (80–90% of power consumption) is true bottleneck. Maryland ratepayers pay $2B for out-of-state data centers. Hyperscalers integrate vertically into power (nuclear, Spain) as moat.
- **Tuesday A**: Vertical integration is capital-intensive arbitrage, not sustainable moat. Power scarcity is regional (Northern Virginia, Northern California), not global. Spain, Texas, and renewable PPAs beat nuclear ownership for ROI.
- **Wednesday R**: On-device AI (Meta ExecuTorch, Qualcomm 60-TOPS, Apple WWDC on-device Siri) is production-scale. If 30–50% of inference migrates to edge, hyperscalers' $100B+ power capex becomes stranded.
- **Wednesday A**: On-device bifurcates, doesn't destroy. OpenAI's inference costs up 68% YoY suggest cloud demand growing. Cloud frontier reasoning stays concentrated and high-margin; commodity queries move to devices. Market splits, not collapses.

## Best Sources
- https://sacra.com/research/openai/ — OpenAI inference economics (growth despite alternatives)
- https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/ — Sierra, agentic AI thesis
- https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises — Power cost externality, grid arbitrage
- https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face — SaaS margin mechanics
- https://ttms.com/growing-energy-demand-of-ai-data-centers-2024-2026/ — Inference power dominance
- https://v-chandra.github.io/on-device-llms/ — On-device AI architecture and viability

## Open Questions for the Blog
1. **Market bifurcation or consolidation?** If SaaS margins settle at 60–70% and cloud inference splits into frontier-only high-margin + on-device commodity low-margin, do winners emerge, or does the entire stack become commoditized? Who captures value in a bifurcated architecture?
2. **Who bears infrastructure cost externalities?** Maryland ratepayers pay for data center grid upgrades. Will FERC intervention change site selection economics, or do hyperscalers just shift to willing-to-subsidize regions (Texas, Spain, Appalachia)?
3. **Timing of on-device inflection point?** Apple's June WWDC will signal whether on-device Siri meaningfully reduces cloud demand. If WWDC shows material shift, hyperscaler power ROI assumptions change in real time. When does edge AI reach 30%+ of inference volume?
