# Week Summary — 2026-05-18 (Updated Tuesday)
_Compiler: read this file, NOT the full research file._

## Core Thesis
AI is reshaping two foundational enterprise cost structures simultaneously: SaaS unit economics AND physical infrastructure. Both are driving toward vertical integration, but not in the way tech simplistically frames it. SaaS vendors compress margins 10–15 points (to 60–70%) and hybridize pricing as customers deploy fewer seats and vendors absorb LLM token costs; meanwhile, hyperscalers are securing power through nuclear deals and regional arbitrage because inference demand is outrunning grid capacity. The real competitive moat won't be technology—it will be whoever solves *infrastructure coordination* (power + compute + software together) at lowest total cost.

## The Key Tension
**SaaS thread:** Researcher says per-seat is dead (customers replacing with agentic AI); Analyst says it's hybridizing with margin compression (60–70% vs. 75–82%) but customer retention stays strong (Salesforce/ServiceNow 120%+ NRR). **Infrastructure thread:** Researcher says power ownership creates moat (Microsoft-Three Mile Island controls AI destiny); Analyst says scarcity is regional, not global, renewable procurement beats nuclear ownership, and on-device AI disrupts the "centralized data center" assumption. **The synthesis:** Both threads point to the same winner—companies that can coordinate power, compute, and software across regions without overspending on captive infrastructure.

## Key Facts & Data Points
- **Sierra raised $950M at $15.8B valuation** on thesis of replacing human work with AI agents — https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/
- **Cloudflare cut 1,100 employees (20% workforce) while hitting record Q1 2026 revenue**, citing 600% internal AI growth and structural need to "reimagine every team" for agentic era — https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/
- **Salesforce NRR 120%+**, Agentforce at 12% of 150k customers with only 6% on paid plans (early); ServiceNow NRR 125% with metered agent assists — https://www.salesforceben.com/are-salesforce-customers-actually-adopting-agentforce/ / https://finance.yahoo.com/news/three-reasons-investors-love-servicenow-141879070.html
- **SaaS gross margin compression 10–15 points** (75–82% → 60–70%) from LLM token costs, inference infrastructure, eval engineering overhead — https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face
- **Maryland filed FERC complaint May 9, 2026: ratepayers absorbing $2B of PJM's $22B grid upgrade plan** (9% of bill) for out-of-state (VA, PA, OH) data centers despite not using the power — https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises
- **Inference is 80–90% of AI power consumption**, not training (IEA, TTMS research). Single ChatGPT query = 2.9 Wh; at 100M daily queries = 106 TWh/year for one vendor — https://ttms.com/growing-energy-demand-of-ai-data-centers-2024-2026/ / https://www.spheron.network/blog/ai-inference-power-electricity-cost-2026/
- **Power approval timelines: 24–36 months in Northern Virginia, Silicon Valley** (grid capacity constraint, not GPU shortage) — https://hardware.slashdot.org/story/26/05/09/2155207/will-marylands-utility-bills-increase-1-6b-to-support-other-states-datacenters
- **Hyperscaler power vertical integration:** Microsoft (Constellation Three Mile Island ~835 MW by 2028), Meta (6.6 GW nuclear by 2035), Google (Kairos/NextEra deals), Amazon (Spain €15.7B investment, Texas renewables) — https://www.latimes.com/business/story/2026-01-09/meta-signs-multi-gigawatt-nuclear-deals-to-power-ai-data-centers / https://techcrunch.com/2026/02/28/billion-dollar-infrastructure-deals-ai-boom-data-centers-openai-oracle-nvidia-microsoft-google-meta/
- **Spain has 45+ GW wind capacity, excess generation; AWS €15.7B + Microsoft multi-billion committed there** (arbitrage: cheap existing power, not integration) — https://www.bloomberg.com/news/features/2026-04-16/spain-s-90-billion-ai-data-center-plan-draws-amazon-web-services-microsoft
- **On-device AI growing:** Qualcomm, Apple, Meta shipping inference-optimized chips 2–3x more power-efficient for single-user tasks; reduces centralized data center demand — https://v-chandra.github.io/on-device-llms/

## Week Thread (Day-by-Day Arc)
- **Monday R**: Sierra's $15.8B raise + Cloudflare's 20% layoffs at record revenue signal per-seat SaaS model is broken; customers will shift to agentic platforms.
- **Monday A**: Per-seat isn't dying—it's hybridizing. Salesforce/ServiceNow 120%+ NRR proves retention; real pressure is margin compression (10–15 points) from token costs, not defection to Sierra.
- **Tuesday R**: Inference (80–90% of AI power) is the true bottleneck. Maryland ratepayers pay $2B for out-of-state data centers. Hyperscalers integrating vertically into power (nuclear, renewables) because grid capacity is scarce; vertical integration = competitive moat.
- **Tuesday A**: Vertical integration is riskier than it looks. Power scarcity is regional, not global. Renewable PPAs beat nuclear ownership for cost. On-device AI reduces centralized data center demand. Microsoft/Amazon are doing smart procurement arbitrage, not strategic integration.

## Best Sources
- https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/ — Sierra funding, agentic AI thesis
- https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises — Maryland FERC complaint, power cost externality
- https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face — SaaS margin compression mechanics
- https://ttms.com/growing-energy-demand-of-ai-data-centers-2024-2026/ — Inference power consumption dominance
- https://finance.yahoo.com/news/three-reasons-investors-love-servicenow-141879070.html — Incumbent vendor strength (NRR, native agents)
- https://www.bloomberg.com/news/features/2026-04-16/spain-s-90-billion-ai-data-center-plan-draws-amazon-web-services-microsoft — Spain as power arbitrage, not integration

## Open Questions for the Blog
1. **Does margin compression (10–15 points) create a permanently lower-margin SaaS market, or is it temporary friction before new equilibrium?** And if margins stabilize at 60–70%, how does that reshape M&A, IPO valuations, and startup fundraising in software?
2. **Which costs are hyperscalers actually internalizing vs. externalizing?** Maryland ratepayers pay for grid upgrades data centers cause—if FERC rules hyperscalers must pay, does that kill the Spain/Texas arbitrage, or just shift the site selection to regions with willing subsidies?
3. **Will on-device AI materially reduce centralized inference demand by 2028–2030**, or will edge AI grow *alongside* cloud inference (no displacement)? This determines if power scarcity is structural or temporary.

