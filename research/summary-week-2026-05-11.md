# Week Summary — 2026-05-11 (Final | Sunday)
_Compiler: read this file, NOT the full research file._

## Core Thesis
Hyperscalers (AWS, Google, Microsoft) are winning AI infrastructure not because custom silicon is technically superior—it's because vertical integration (owning silicon + cloud + services) lets them subsidize infrastructure to capture application-layer profits. This business model asymmetry is structural: it kills independent chip startups and forces Nvidia into a narrower market. By 2028, hyperscaler margins stabilize at 33-35% (down from current 37-38%), but remain healthy—and that's still better than the 15-20% they'd achieve without custom silicon.

## The Key Tension
If hyperscaler margins compress once supply constraints ease and competition commoditizes (2027-2028), does that undermine the "vertical integration moat" argument? The tension: margin expansion is happening *now*, but whether it's permanent depends on pricing power persisting as custom chips become commodity products. Regulatory risk (EU DMA gatekeeper designation, May 2027 compliance) could accelerate compression if forced interoperability mandates emerge—but enforcement is slower than the tech roadmap, so Trainium4 will be incumbent before compliance lands.

## Key Facts & Data Points
- **AWS divisional margin: 37.7%** (Q1 2026, up from ~33% in 2025) — https://news.alphastreet.com/amazon-amzn-q1-2026-aws-at-15-quarter-high-growth-drives-record-operating-margin/
- **Google Cloud margin: 32.9%** (Q1 2026, up from 17.8% in 2025) — https://www.fool.com/earnings/call-transcripts/2026/04/29/alphabet-googl-q1-2026-earnings-call-transcript/
- **AWS Trainium $20B run rate, sold out through Trainium4** — https://www.theaiconsultingnetwork.com/blog/amazon-q1-2026-aws-44b-capex-and-cre-data-center-impact
- **Trainium inference cost: 54% cheaper than A100 clusters on identical workloads** (internal AWS benchmarks) — https://www.cloudzero.com/blog/cloud-gpu-pricing-comparison/
- **Groq acquired by Nvidia for $20B** (December 2025, structured as talent/IP acquisition, not standalone business valuation) — https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/
- **SambaNova valuation collapsed 57%**: $5.1B (2021 peak) → $2.2B (February 2026) — https://www.cnbc.com/2026/02/24/intel-partners-with-sambanova-after-buyout-talks-reportedly-failed.html
- **Anthropic committed $100B to AWS** for 10-year infrastructure deal (April 2026), preferential Trainium access — https://www.anthropic.com/news/anthropic-amazon-compute
- **Salesforce Agentforce $800M ARR with 77.73% gross margin** (Q4 FY2026, margin *expanded* despite AI inference consuming 23% of revenue) — https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/
- **Cerebras IPO May 13, 2026** ($22-27B valuation) dependent on $20B OpenAI customer commitment — https://www.cnbc.com/2026/05/13/cerebras-prices-ipo-above-expected-range-wall-street-expects-ai-flood.html
- **AI-first SaaS companies show 52% gross margins** vs. 75-85% for traditional SaaS, but compression is temporary—Salesforce Q4 proves this — https://www.thesaascfo.com/your-ai-feature-is-quietly-destroying-your-gross-margin/
- **Recursive Superintelligence $1.1B seed** (April 2026) for models/agents, *not* chips—canary in coal mine for VC exit from hardware — https://www.cnbc.com/2026/04/27/deepmind-ineffable-intelligence-record-seed-funding-nvidia-google.html
- **EU DMA investigation into AWS/Azure concludes November 2026**, compliance due May 2027 — https://euobserver.com/215316/amazon-and-microsoft-finally-face-eu-anti-competitive-cloud-probe/

## Week Thread (Day-by-Day Arc)
- **Monday R**: AWS Trainium hit $20B run rate driving margin expansion; vertical integration (silicon + cloud + services) is the real advantage, not chip superiority.
- **Monday A**: Analyst challenges: custom silicon solves CapEx problem, not margin problem; hyperscalers racing to bottom, not capturing permanent margin.
- **Tuesday R**: EU DMA investigation concludes November 2026 with potential gatekeeper designation; regulatory risk could force interoperability by May 2027.
- **Tuesday A**: Regulatory risk is real but glacial; Anthropic's $100B AWS commitment *after* public investigation signals market prices risk as manageable; CISPE sovereignty threat is larger than pure competition law.
- **Wednesday R**: AWS operating margin is actually flat at 37.7% despite Trainium; margin gains may just be CapEx savings being reinvested into volume.
- **Wednesday A**: Correction: AWS margins ARE actually expanding 3-5 bps in single quarter; Google Cloud jump from 17.8% to 32.9% proves custom silicon delivers visible profit improvement.
- **Thursday R**: SaaS gross margins compress from 75-85% to 50-65% due to inference costs; hyperscalers can undercut pricing, creating "pricing trap" for independent SaaS.
- **Thursday A**: Counter: SaaS margin compression is temporary optimization phase, not permanent extraction; Salesforce Q4 shows margin *expansion* while Agentforce scaled to $800M ARR.
- **Friday R**: Startup AI chip apocalypse is complete—Groq acquired, SambaNova down-round, Cerebras IPO-dependent on single customer; VC capital fleeing hardware to applications.
- **Friday A**: Apocalypse is normal consolidation, not market failure; infrastructure layers always consolidate to 2-3 winners; startups survive by moving upstream to applications/models.
- **Saturday R**: Core insight held up through five days of stress-testing: vertical integration (not silicon) creates durable competitive advantage; regulatory risk is manageable; SaaS consolidates upward.
- **Saturday A**: Business model topology is the prize, not technology; value migrates from commoditizing infrastructure layer to services/applications; entrepreneurs should build where capital is not the primary constraint.

## Best Sources
- https://news.alphastreet.com/amazon-amzn-q1-2026-aws-at-15-quarter-high-growth-drives-record-operating-margin/ — AWS margin expansion, confirms 37.7% divisional margin
- https://www.cnbc.com/2026/02/24/intel-partners-with-sambanova-after-buyout-talks-reportedly-failed.html — SambaNova down-round, Intel deal structure, industry consolidation
- https://www.fool.com/earnings/call-transcripts/2026/04/29/alphabet-googl-q1-2026-earnings-call-transcript/ — Google Cloud 17.8% → 32.9% margin jump, CapEx guidance
- https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/ — Groq $20B acquisition structure, talent/IP grab
- https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/ — Agentforce $800M ARR, gross margin *expansion*, disproves SaaS doom narrative
- https://euobserver.com/215316/amazon-and-microsoft-finally-face-eu-anti-competitive-cloud-probe/ — DMA gatekeeper investigation timeline, regulatory risk

## Open Questions for the Blog
1. **When exactly do hyperscaler margins peak and compress?** The data shows expansion through Q1 2026, but is this sustainable through 2027-2028 when supply constraints ease and competitors' custom chips mature? Is the peak now (37-38%), or do margins expand another 2-3 points before commoditization kicks in?

2. **What's the actual profitability of custom silicon production itself?** AWS's $20B Trainium run rate is impressive, but at what gross margin? If it's 50-60% (matching AI service margins), it's not a high-margin business; if it's 75%+, it's transformative. This data doesn't exist publicly but determines whether custom silicon is a temporary CapEx optimization or permanent margin driver.

3. **Will European industrial policy (CISPE sovereignty) reshape the competitive landscape faster than DMA enforcement?** Regulatory designation happens in November 2026, but enforcement is slow. Meanwhile, if EU mandates European cloud alternatives, that fragments the market and hurts hyperscaler scale economies—potentially the more material risk than pure competition law.
