---
title: "In AI, the Margin Is the Moat"
date: 2026-04-04
topic: "AI industry strategy"
summary: "The CEO of a company targeting a $500 billion IPO just told investors he could go bankrupt if he's off by a year. That sentence contains the entire structure of the 2026 AI market — and most people are still reading it wrong."
---

[[Dario Amodei]] said the quiet part out loud in February.

In an interview with [[Dwarkesh Patel]], the [[CEO]] of [[Anthropic]] — a company in active discussions about an [[IPO]] that could value it between $400 and $500 billion — said this: "If I'm just off by a year in that rate of growth, or if the growth rate is 5x a year instead of 10x a year, then you go bankrupt." He then went further. "If my revenue is not $1 trillion, if it's even $800 billion, there's no force on Earth, there's no hedge on Earth that could stop me from going bankrupt if I buy that much compute."

Pause on that. The CEO of one of the two most celebrated AI companies in the world, preparing for what could be one of the largest IPOs in technology history, is telling investors — on the record, in public — that his margin for error is measured in quarters, not years. One bad year and the company is insolvent. Not struggling. Not restructuring. Bankrupt.

Now look at Nvidia's most recent earnings: $215.9 billion in annual revenue, 75% GAAP gross margin in Q4. The company is printing money at a rate that has no parallel in the history of semiconductor companies. It just acquired the leading inference chip startup for $20 billion — not because it needed to, but because it could, and because the acquisition deepened a competitive moat that already had no meaningful challengers.

These two data points are the same story told from opposite ends of the AI value stack. And once you see it, you cannot unsee it: **the most important strategic variable in AI right now is not model quality, market share, or growth rate. It is margin. And the margin gap between the infrastructure layer and the model layer is widening, not narrowing.**

---

## The Stack Nobody Drew Correctly

Every diagram of the AI ecosystem shows the same thing: hardware at the bottom, cloud infrastructure in the middle, models on top, applications at the apex. It's a clean hierarchy. The problem is that clean hierarchies obscure the actual strategic question, which is not "who is at what layer" but "who captures the economic value at each layer."

In cloud computing, the answer was brutally simple: Amazon Web Services, running at what felt like impossibly thin margins in the early years, eventually became the most profitable division in tech. The lesson most people took from that story is that infrastructure wins long-term. Build the picks and shovels. Sell to all sides. Collect rent.

The AI industry took that lesson seriously. And it produced a generation of analysis that says Nvidia is the arms dealer, the hyperscalers are the railroads, and the model labs — Anthropic, OpenAI — are somewhere between the most important companies in the world and the most gloriously subsidized experiments in history.

All of that is approximately correct and almost entirely unhelpful for understanding what actually happens next.

Here is the version that is actually predictive: **the AI stack has sorted itself into two tiers, and the boundary between them is structural, not temporary.** Tier 1 is what you might call the Margin Sovereigns — Nvidia, Google, Microsoft. Tier 2 is the Margin Constrained — Anthropic and OpenAI. The Tier 1 players have margin cushions that let them absorb losses, fund acquisitions, and iterate across multiple architectural bets simultaneously. The Tier 2 players are running extraordinary growth businesses with existentially thin margin profiles, where the hardware-bound cost floor of AI inference means the traditional software scaling playbook does not apply.

The margin scoreboard, using Q4 2025 actuals, tells the story without editorial:

| Player | Margin | Revenue | Burn Rate | Trend |
|---|---|---|---|---|
| Nvidia | 71–75% GAAP gross | $215.9B annual | Net positive | Stable |
| Microsoft (Azure) | 44–47% operating | $81.3B/quarter | Net positive | Slight compression |
| Google Cloud | 30%+ operating | $17.7B/quarter | Net positive | Improving |
| Anthropic | ~40% gross | $19B ARR | ~$19B/year | Improving from -94% |
| OpenAI | ~33% gross | $24B ARR | $25B+ projected 2026 | **Declining** |

That last column is the one that matters. Nvidia and Microsoft are stable. Google is improving. Anthropic is improving dramatically, but from a starting point of negative 94% gross margins eighteen months ago. And OpenAI — the most famous, most funded AI company in history — is watching its gross margin go *down* as it scales. From 40% in 2024 to 33% in 2025, as inference costs quadrupled to $8.4 billion. The company tripled revenue and burned $9 billion doing it.

That is not the trajectory of a company on the AWS path to infrastructure dominance. That is the trajectory of a company running faster to stay in the same place.

---

## Why the AWS Analogy Breaks Down

Let's address the bull case directly, because it's the argument you will hear most often and it has real intellectual weight.

AWS operated at sub-30% margins for years. People said Amazon Web Services was a money-losing distraction, a side project that Jeff Bezos was funding with retail cash flows. Then it became the most profitable cloud business in history and generated the majority of Amazon's operating income. The lesson: margin thin today, margin dominant tomorrow. Don't be fooled by the early numbers.

If you believe this analogy applies to AI model labs, then Anthropic's move from -94% to 40% gross margins in 18 months is the steepest margin improvement in enterprise software history, 77% by 2028 is achievable, and the entire "infrastructure always wins" thesis needs revisiting.

Here is why it doesn't hold. AWS's margin expansion came from near-zero marginal cost at scale. Software and data centers that could serve 10x the customers for 2x the cost. The marginal cost curve approached zero asymptotically. That is the fundamental economic property that makes software businesses magical — once you build the product, the incremental cost of the next unit is almost nothing.

AI inference is hardware-bound. Every query requires GPU cycles. Every GPU cycle costs money. There is no world in which Anthropic runs a billion Claude conversations for the same cost as running a million Claude conversations. The hardware requirements scale. You can improve efficiency — and Google has, dramatically, running 78% cost reductions in Gemini serving costs over 2025. But Google achieved that through proprietary TPU silicon that took a decade and tens of billions to build. Anthropic does not have that, and cannot build it without multi-year fab partnerships that don't yet exist.

This is the kill shot on the early-AWS analogy: it requires AI inference to behave like software. It does not.

---

## The Hidden Strongest Player

Everyone is talking about Nvidia and OpenAI. Here is the company that should be at the center of the conversation: Google.

Google Cloud posted a 30%+ operating margin in Q4 2025 on $17.7 billion in quarterly revenue — a 48% year-over-year increase. For context, that margin figure is higher than Anthropic's blended *gross* margin. Google's cloud business is now more profitable, on an operating basis, than the AI lab that investors are considering valuing at half a trillion dollars.

But the operating margin is not even the most important Google number. The most important number is the 78% reduction in Gemini serving costs over the course of 2025. That cost reduction came from Ironwood — Google's seventh-generation TPU, designed explicitly for the inference era — delivering 4x better performance-per-dollar than Nvidia H100s for LLM inference workloads.

What this means in practice: when Anthropic runs an enterprise Claude conversation, it is paying Nvidia's price for the hardware. When Google runs a Gemini conversation, it is paying Google's price, on Google's hardware, with Google's power contracts, optimized by Google's DeepMind research team. The effective cost per query is not 4x different. It is the structural difference between renting someone else's tools and owning the factory.

Google is the only company in the world that is simultaneously: a hyperscaler with profitable cloud infrastructure, a frontier model developer with a top-tier model running on captive silicon, the owner of DeepMind producing research that directly lowers its own inference costs, and a distribution giant with Search, Android, and YouTube as built-in deployment surfaces. Alphabet's consolidated operating margin for full-year 2025 was 31.6% on $350 billion in revenue.

This is the margin profile of a company that can subsidize the AI race indefinitely. And unlike Microsoft — whose AI model strategy depends critically on a partnership with OpenAI that is showing cracks — Google does not need a partner to execute on the model layer.

> **Aside: The Smartphone Profit Pool, Revisited**
>
> In 2022-2023, Apple held roughly 20-27% of global smartphone unit share and captured 85% of the industry's operating profit. Samsung, with two to three times the unit share, captured most of the remaining profit. Every other Android OEM operated at razor-thin or negative margins. The market "grew" for everyone in absolute terms, but only Apple and Samsung generated returns above their cost of capital.
>
> This is the dynamic forming in AI. Nvidia's market share is declining from 87% to a projected 75% by end of 2026 — but at 71-75% gross margins on $216 billion in revenue, every point of retained share generates disproportionate cash flow. The model labs are the Android OEMs of this analogy: growing volume spectacularly while the margin structure remains structurally impaired by hardware-bound inference costs. Declining share, disproportionate profit capture. It's not a bug in Nvidia's position. It's the feature.

---

## Nvidia's Real Move

Nvidia's decision to stop investing in OpenAI and Anthropic — pulling back from a $30 billion OpenAI position and a $10 billion Anthropic position — looks, on the surface, like a simple pre-IPO cleanup. Jensen Huang said as much publicly: the companies are going public, Nvidia doesn't need equity when it already captures the infrastructure spend.

Dig one layer deeper and it is something more elegant: a platform player deciding it does not need vertical integration into the application layer, because it has just vertically integrated into the infrastructure layer.

In December 2025, Nvidia acquired Groq — the most technically credible inference-specialized challenger to GPU dominance — for $20 billion. At GTC 2026 in March, Nvidia unveiled the Groq 3 LPU, the first chip from the acquisition. The specs are extraordinary: 512 MB of on-chip SRAM per die, delivering 150 TB/s of memory bandwidth — nearly 7x the bandwidth from HBM4 on each Rubin GPU. A full LPX rack delivers 35x higher throughput per megawatt than Blackwell alone for trillion-parameter models, at a target of $45 per million tokens. Samsung is manufacturing on its 4nm process with shipments expected Q3 2026.

The analytical frame for this move is "Embrace, Extend, Absorb." Embrace: Nvidia spent 20 years building CUDA into the default AI development environment. Every framework, every researcher, every production pipeline runs on CUDA. Extend: when inference workloads threatened to migrate to specialized silicon — Groq LPUs, Google TPUs, Amazon Trainium — Nvidia paid a 2.9x premium to acquire the best inference architecture on the market and is building a dual-stack architecture within the CUDA umbrella. Absorb: by pulling back from application-layer equity, Nvidia simplifies its competitive position. It doesn't need to own its customers. It needs its customers to have no alternative infrastructure stack.

The historical parallel is not Intel losing to ARM — which is the critique most often leveled at Nvidia. Intel's mistake was refusing to adapt its architecture to a new workload profile and dismissing mobile as a niche. Nvidia did the opposite: it saw the inference workload shift coming and acquired the best inference architecture on the market. A better parallel is Microsoft acquiring GitHub — buying the tools developers were already using, making the platform stickier, not competing with the application layer.

The strongest counter-argument: the Groq acquisition might be a defensive panic buy, not confident platform extension. Nvidia paid 2.9x valuation. If LPU technology proves difficult to integrate, or if hyperscaler custom silicon outpaces Nvidia's dual-stack roadmap, the $20 billion becomes a write-down. The Intel parallel would be apt after all — a dominant incumbent spending billions to chase a paradigm shift it cannot structurally adapt to.

Here is why I ultimately reject that counter-argument: Nvidia's gross margins at 71-75% are structurally different from Intel's historical 58%. Nvidia has the cash flow to acquire, the R&D budget to iterate, and the pricing flexibility to compete on inference cost. Intel never had any of that financial headroom. A company with 75% gross margins buying optionality is not the same as a company with 58% gross margins trying to survive.

---

## Microsoft: The Landlord With a Nervous Tenant

Microsoft's position is the most structurally interesting — and the most misread — of any major player in AI.

The restructured Microsoft-OpenAI deal from October 2025 is extraordinary in scope: 27% of the new OpenAI Public Benefit Corporation (worth roughly $230 billion at OpenAI's current $852 billion valuation), a $250 billion Azure commitment from OpenAI, exclusive rights to sell OpenAI models via API through 2030, and IP licensing through 2032. Microsoft's $625 billion demand backlog doubled year-over-year. Satya Nadella is calling Azure a "planet-scale token factory."

But here is what the optimistic read glosses over: six days after the restructured deal closed, OpenAI signed a $38 billion seven-year infrastructure deal with AWS. There are also reports of a $300 billion Oracle commitment. Microsoft reportedly considered suing OpenAI over the Amazon deal. That is not the behavior of a company feeling quietly victorious. It is the behavior of a company watching its most important customer diversify away.

The correct frame: Microsoft is a landlord whose tenant just signed a second lease across the street. The $250 billion Azure commitment guarantees revenue, and Microsoft wins in every scenario — OpenAI IPO success lifts the equity stake, compute commitment pays as cloud revenue, OpenAI competition with Copilot still runs on Azure. But the API exclusivity runs only through 2030, and OpenAI is already shifting workloads elsewhere. Mustafa Suleyman's internal frontier model effort, and Microsoft's quiet evaluation of Meta, xAI, and DeepSeek models as Copilot alternatives, tells you everything about Microsoft's own uncertainty about whether the OpenAI relationship holds.

This is structurally brilliant, tactically fragile. The 44-47% operating margin gives Microsoft the runway to wait it out. The nervousness is real.

---

## The IPO Race Nobody Is Framing Correctly

Both Anthropic and OpenAI are targeting Q4 2026 public offerings. The market is framing this as a first-mover advantage race — whoever lists first absorbs the retail AI demand wave, whoever lists second faces IPO fatigue.

That framing is wrong in an important way.

OpenAI already raised $3 billion from retail investors in its March $122 billion private round, partially defusing the "retail demand absorption" thesis. But more importantly, the real game is not about who absorbs retail dollars — it is about who sets the comparable multiple. If Anthropic lists at 25x revenue and trades down, OpenAI's IPO gets harder. If it trades up, OpenAI benefits from the rising tide. This is a signaling game, not a zero-sum competition for a fixed pool of capital.

The deeper constraint on both IPOs is the one nobody in the market commentary is comfortable saying directly: there is no historical comparable for what either company is attempting. No software company has ever gone public at a $400-500 billion valuation with sub-50% gross margins. Snowflake IPO'd at roughly $70 billion with 62% gross margins. Palantir at roughly $22 billion with 68% margins. The most aggressive SaaS IPOs of the 2021 bubble demanded 70%+ gross margins for premium multiples.

Anthropic's margin trajectory — negative 94% in 2025, targeting 40% in 2026, projecting 77% by 2028 — is unprecedented. The 40% number is the binary signal. If Q3 2026 financials show 40%+ with intact trajectory, bankers will pitch "early-stage AWS economics" and institutional investors will construct a story about a decade-long margin expansion ahead. If it comes in below 40%, the valuation compresses violently toward $250 billion.

There is no middle ground. The Anthropic S-1's segment-level margins will be the most important financial disclosure in tech IPO history. The question to watch: are enterprise contracts (150%+ dollar-based net retention rate) already margin-positive while API developer usage is deeply negative? If yes, the margin expansion story is about mix shift, not cost reduction — bullish. If even the enterprise contracts are margin-negative, Anthropic is subsidizing growth with venture capital, and 77% becomes aspirational rather than architectural.

---

## Three Paths for the Model Labs

The AI infrastructure layer — Nvidia, Google, Microsoft — has effectively won the structural margin war. The question is no longer whether the infrastructure players win. It is what happens to the model labs when they finish running out of easy money.

There are exactly three paths:

**Path A: Vertical Integration.** Anthropic and OpenAI successfully build or secure proprietary inference silicon by 2027-2028, reaching 77% gross margin targets through reduced compute dependency. On this path, the early-AWS analogy becomes valid, the IPOs price at premium multiples, and the model layer earns the right to call itself infrastructure. This path requires either breakthrough model efficiency advances (reducing compute requirements per query) or fab partnerships that deliver custom silicon at competitive economics. Anthropic's disclosed 2+ gigawatts of committed compute through blended architecture is a step in this direction. It is not yet proof of arrival.

**Path B: Acquisition.** The margin gap proves unbridgeable at the model layer alone, and a Tier 1 player acquires the capability it needs. Google buys Anthropic. Microsoft deepens its OpenAI stake to controlling interest. The model labs become the R&D divisions of the infrastructure companies that were always going to win. On this path, the IPO plans are abandoned or restructured, founders get rich, and the AI value stack consolidates exactly as industry structure theory predicts.

**Path C: Race the Clock.** Both companies IPO in 2026, raise the public capital to fund the compute war for another 24-36 months, and run as fast as possible toward the margin expansion that justifies their valuations. The IPO is not a liquidity event — it is a financing round for the compute war. This is what both companies are currently planning. The risk is Amodei's own words: if the growth rate is 5x a year instead of 10x a year, there is no hedge on Earth.

Most market participants are pricing the model labs as if Path A is probable. The evidence — the hardware-bound cost structure, the hyperscaler custom silicon advances, the infrastructure players' margin advantages — suggests Path C is most likely in the near term, with Path B as the eventual resolution if Path A does not materialize by 2028.

---

## The So-What

**For investors:** The risk-adjusted position is Tier 1 infrastructure. Google is the most underappreciated, holding a unique dual position as both cloud provider and frontier model developer with captive silicon. Nvidia is the margin-sovereign silicon arms dealer. Microsoft is the structural winner in every OpenAI scenario, despite tactical fragility. The model lab IPOs will be fascinating events, but the valuation math requires believing in a margin trajectory with no confirmed historical precedent in hardware-bound businesses. Watch the Anthropic S-1's segment-level margins — specifically whether enterprise contracts are margin-positive — before making any conviction bet.

**For builders:** Your supplier is in a margin war with the infrastructure layer below it. That means API pricing is structurally unpredictable — it will be subsidized aggressively until it is not. Build portability into your stack now. The inference startup consolidation (SambaNova into Intel, Groq into Nvidia, Cerebras into Amazon's orbit) tells you that standalone model access is becoming a platform feature, not a standalone product. Design your architecture accordingly.

**For strategists:** Watch for Anthropic and OpenAI's custom silicon announcements in 2026. That is the signal that they understand what business they actually need to be in. When a model lab starts talking like a semiconductor company — discussing fab partnerships, die yields, on-chip SRAM specifications — the structural thesis has arrived at its conclusion. The consolidation prediction is not "infrastructure acquires models." It is "models race to become infrastructure." The ones that make it will be unrecognizable from what they are today.

---

## The Thesis, Stated Plainly

The defining strategic reality of the 2026 AI market is that the infrastructure layer has already won the margin war, and the model layer has not yet admitted it.

Nvidia, Google, and Microsoft sit atop a margin stack that lets them subsidize competition, acquire threats, and iterate across multiple architectural bets simultaneously. They can afford to lose market share because the market share they keep is disproportionately profitable — the Apple smartphone profit pool model applied to silicon and cloud.

Anthropic and OpenAI are running extraordinary growth businesses with existentially thin margin cushions, where a one-year miss on growth projections leads — the CEO of one has said this explicitly — directly to bankruptcy. The market is pricing both companies as if they will successfully vertically integrate into margin-positive businesses by 2028. That is possible. But it is not probable without either a profound improvement in inference efficiency or a fundamental shift in their relationship with the Tier 1 players who are simultaneously their largest customers, their compute suppliers, and their most formidable long-term competitors.

In AI, the margin is the moat. The moat is widening, not narrowing. And the companies with the widest moats are the ones spending the least time on stage at AI conferences.

---

## Sources & Further Reading

**Nvidia / Groq Acquisition**
- [CNBC — Nvidia buying AI chip startup Groq's assets for about $20 billion](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html)
- [Motley Fool — Nvidia's $20 Billion Groq Acquisition Just Paid Off](https://www.fool.com/investing/2026/03/24/nvidias-20-billion-groq-acquisition-just-paid-off/)
- [NVIDIA Technical Blog — Inside Groq 3 LPX: Low-Latency Inference Accelerator](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/)
- [NVIDIA Q4 FY2026 Earnings — Record $68.1B Revenue](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- [SemiAnalysis — Nvidia: The Inference Kingdom Expands (GTC 2026)](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands)
- [Silicon Analysts — NVIDIA GPU Market Share 2024-2026](https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026)

**Anthropic**
- [Fortune — Dario Amodei warns 'then you go bankrupt' if growth forecasts miss by a year](https://fortune.com/2026/02/14/anthropic-ceo-dario-amodei-spending-capex-risk-ai-revenue-forecasts-bankruptcy/)
- [The Information — Anthropic Lowers Gross Margin Projection as Revenue Skyrockets](https://www.theinformation.com/articles/anthropic-lowers-profit-margin-projection-revenue-skyrockets)
- [Anthropic Eyes $60 Billion IPO as Soon as Q4 2026 — WinBuzzer](https://winbuzzer.com/2026/03/30/anthropic-ipo-q4-2026-60-billion-target-xcxwbn/)
- [Shanaka Perera — The Growth Miracle and the Six Fractures: Anthropic at $380 Billion](https://shanakaanslemperera.substack.com/p/the-growth-miracle-and-the-six-fractures)
- [Seeking Alpha — Anthropic IPO: What You Need to Know](https://seekingalpha.com/article/4887778-anthropic-ipo-what-you-need-to-know)
- [Axios — Anthropic Turns the Tables on OpenAI in Critical Revenue Category](https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai)

**OpenAI**
- [Bloomberg — OpenAI Valued at $852 Billion After Completing $122 Billion Round](https://www.bloomberg.com/news/articles/2026-03-31/openai-valued-at-852-billion-after-completing-122-billion-round)
- [TechCrunch — OpenAI Raises $3B from Retail Investors in $122B Round](https://techcrunch.com/2026/03/31/openai-not-yet-public-raises-3b-from-retail-investors-in-monster-122b-fund-raise/)
- [The Decoder — OpenAI adds $111 billion to its cash burn forecast](https://the-decoder.com/openai-adds-111-billion-to-its-cash-burn-forecast-as-ai-costs-spiral-beyond-projections/)
- [Aakash Gupta — OpenAI tripled revenue to $13.1B in 2025, burned $9B, gross margins fell to 33%](https://x.com/aakashgupta/status/2025268716469108895)

**Microsoft**
- [DCD — OpenAI Completes For-Profit Move; Microsoft Gets 27% Stake and $250B Azure Contract](https://www.datacenterdynamics.com/en/news/openai-completes-for-profit-move-microsoft-given-27-stake-and-250bn-azure-contract-but-no-longer-has-cloud-right-of-first-refusal/)
- [WinBuzzer — Microsoft Weighs Suing OpenAI Over Amazon Cloud Deal](https://winbuzzer.com/2026/03/19/microsoft-weighs-suing-openai-amazon-cloud-deal-xcxwbn/)
- [Seeking Alpha — Microsoft: OpenAI Is Simply a Strategic Hedge](https://seekingalpha.com/article/4857402-microsoft-openai-is-simply-a-strategic-hedge)
- [Fortune — Microsoft Q2 FY2026: demand backlog doubles to $625B](https://fortune.com/2026/01/28/microsoft-stock-drops-azure-growth-slows-capex-spending-q2/)

**Google / TPU Economics**
- [Alphabet Q4 FY2025 Earnings — Google Cloud $17.7B Revenue, 30%+ Operating Margin](https://futurumgroup.com/insights/alphabet-q4-fy-2025-highlights-cloud-acceleration-and-enterprise-ai-momentum/)
- [Ironwood: Google's First TPU for the Age of Inference](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/)
- [AI Inference Costs 2025: Why Google TPUs Beat Nvidia GPUs by 4x](https://www.ainewshub.org/post/ai-inference-costs-tpu-vs-gpu-2025)
- [SemiAnalysis — Google TPUv7: The 900lb Gorilla in the Room](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)

**Market Structure**
- [Morningstar — Which of the 3 Giant AI IPOs Should You Buy?](https://www.morningstar.com/markets/which-3-giant-ai-ipos-should-you-buy)
- [SaaStr — Have AI Gross Margins Really Turned the Corner?](https://www.saastr.com/have-ai-gross-margins-really-turned-the-corner-the-real-math-behind-openais-70-compute-margin-and-why-b2b-startups-are-still-running-on-a-treadmill/)
- [Technology M&A: AI Enters Its Industrial Phase — McKinsey](https://www.mckinsey.com/capabilities/m-and-a/our-insights/technology-m-and-a-ai-enters-its-industrial-phase)
- [Tom Tunguz — SpaceX, OpenAI & Anthropic IPOs: A $3 Trillion Stress Test](https://tomtunguz.com/spacex-openai-anthropic-ipo-2026/)
- [Bloomberg — Apple captured 85% of smartphone operating profit (2023)](https://www.bloomberg.com/news/articles/2023-02-03/iphone-grabs-record-smartphone-profit-share-of-85-for-apple)
