# Week Summary — 2026-05-18 (Updated Saturday | Final)
_Compiler: read this file, NOT the full research file. This is the final, synthesized summary for Sunday compilation._

## Core Thesis
**AI infrastructure costs are no longer abstract—they're now permanent and visible, forcing markets to bifurcate based on who can hide them and who cannot.** Companies that bundle AI into existing platforms and socialize costs across millions of users (Microsoft, Google, Apple, Meta) will dominate 80%+ of the market. Companies forced to expose costs per-token or per-transaction (OpenAI, Anthropic, SaaS add-on vendors) are confined to specialized frontier segments (5–20% TAM) or face adoption collapse. This is not a pricing problem; it's a structural realignment. **Cost-hiding bundlers win permanently. Cost-transparent exposers survive only in micro-segments.**

## The Key Tension
**Will frontier reasoning stay expensive enough to justify hyperscalers' $100B+ power infrastructure investment, or will on-device alternatives and efficiency improvements collapse frontier demand faster than expected?** Current data (OpenAI's inference costs growing 68% YoY despite on-device growth) suggests frontier demand is robust and separately-growing from commodity inference. But this is the single variable that determines if the bifurcation thesis holds through 2028–2030. If on-device adoption accelerates faster than projected, power infrastructure becomes oversized and the entire bifurcation model shifts.

## Key Facts & Data Points
- **OpenAI spends $1.35 for every $1 earned** on inference; $8.4B in 2025 → $14.1B in 2026 (unprofitable) — https://sacra.com/research/openai/
- **Salesforce changed Agentforce pricing 3 times in 18 months** because transparent pricing killed adoption (5–8% penetration) — https://www.getmonetizely.com/blogs/the-doomed-evolution-of-salesforces-agentforce-pricing
- **Microsoft Copilot (bundled in 365)** drives 115%+ NRR; Salesforce's add-on model stalled at 5–8% — https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/
- **SaaS margins compressed from 75–82% to 60–70%** due to token costs, not seat loss — https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face
- **Inference (80–90% of AI power) bottleneck, not training.** Maryland ratepayers: $2B bill for out-of-state data center upgrades — https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises
- **Hyperscalers locking power:** Microsoft 835 MW Three Mile Island, Meta 6.6 GW nuclear, Amazon Spain €15.7B — https://www.latimes.com/business/story/2026-01-09/meta-signs-multi-gigawatt-nuclear-deals-to-power-ai-data-centers
- **On-device AI at production scale:** Meta ExecuTorch (WhatsApp/Instagram billions of users), Apple on-device Siri (WWDC 2026), Qualcomm 60-TOPS — https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/
- **OpenAI inference costs +68% YoY** despite on-device growth, proving frontier demand separate from commodity — https://aiautomationglobal.com/blog/ai-inference-cost-crisis-openai-economics-2026

## Week Thread (Day-by-Day Arc)
- **Monday R+A**: SaaS per-seat model hybridizing, not dying. Salesforce's three pricing models in 18 months (conversation → action → hybrid) reveal core problem: when customers see per-token costs, adoption collapses (5–8% penetration). Microsoft's bundled Copilot thrives (NRR 115%+) because costs are invisible per-user.
- **Tuesday R+A**: Inference (80–90% of AI power) is now bottleneck, not training. Hyperscalers locking in power ($100B+ investments: Microsoft Three Mile Island 835MW, Meta 6.6GW, Amazon Spain €15.7B). But power is regional arbitrage (Spain's cheap renewables beat owning nuclear) + execution risk, not durable moat. Maryland ratepayers subsidizing out-of-state data centers via $2B grid bill.
- **Wednesday R+A**: On-device AI shipped at production scale (Meta ExecuTorch, Apple Siri, Qualcomm 60-TOPS). Bifurcates demand, doesn't destroy cloud: OpenAI's inference costs growing 68% YoY despite on-device competition suggests frontier reasoning demand is separate and growing. Edge takes commodity queries; cloud stays expensive for frontier.
- **Thursday R+A**: Cost transparency is competitive liability. OpenAI's per-token pricing ($1.35 spent per $1 earned) bleeds. Salesforce's add-on costs kill adoption (5–8%). Microsoft's hidden-cost bundling (Copilot in 365) succeeds. Pattern: when costs are visible, adoption or margins collapse. When bundled, adoption and margins stay healthy.
- **Friday R+A (Synthesis)**: Market permanently bifurcated: (1) **Cost-hiding bundlers** (Microsoft, Google, Apple, Meta) dominate 80%+ by spreading costs invisibly across 365M–2B users. (2) **Cost-transparent specialists** (OpenAI, Anthropic, Sierra, on-device makers) confined to 5–20% TAM (frontier reasoning, edge, specialized segments). This is structural, not cyclical. Winners own multiple layers (software + infrastructure + devices) or operate in frontier-only segments. Losers expose costs as add-ons.

## Best Sources
- https://aiautomationglobal.com/blog/ai-inference-cost-crisis-openai-economics-2026 — OpenAI unit economics and cost trajectory
- https://sacra.com/research/openai/ — Inference cost growth
- https://www.getmonetizely.com/blogs/the-doomed-evolution-of-salesforces-agentforce-pricing — Salesforce pricing chaos and adoption failure
- https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face — SaaS margin mechanics
- https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises — Power cost externalities
- https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/ — On-device AI at scale

## Open Questions for the Blog
1. **Can OpenAI survive as a cost-transparent supplier, or must it become Microsoft's frontier-AI engine?** OpenAI's path to profitability requires moving upmarket (enterprise fixed pricing) and accepting a 5–20% TAM constraint. But Microsoft already owns 365 distribution. The question: how much of the frontier market is actually available to an independent OpenAI vs. services locked inside Microsoft?
2. **At what speed does on-device adoption reduce hyperscaler power demand?** Current trajectory: OpenAI costs up 68% YoY despite on-device competition, suggesting frontier cloud demand is separating from commodity demand and growing. But if on-device improves faster than expected, power infrastructure becomes oversized. The inflection point for this is 2028–2030.
3. **Will traditional SaaS vendors (Salesforce, Zendesk, Adobe) successfully bundle AI or remain permanently margin-compressed?** Current evidence: Salesforce's three pricing pivots suggest bundling is harder than bundlers (Microsoft) make it look. The answer determines whether SaaS survives as a category or becomes a mid-market contractor to larger platforms.
