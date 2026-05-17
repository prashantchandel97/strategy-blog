---
title: "The Real AI Infrastructure Moat Isn't Custom Silicon—It's Owning The Whole Stack"
date: 2026-05-11
topic: "AI Infrastructure & Business Models"
summary: "Hyperscalers are winning not because their chips are better than Nvidia's—they're winning because they own silicon, cloud, and services, letting them subsidize infrastructure to capture application-layer profits. This kills independent chip startups and reshapes where value flows in AI."
---

In December 2025, Nvidia paid $20 billion to acquire Groq, a six-year-old AI chip startup. On paper, that sounds like a win—a classic Silicon Valley exit story. But look closer at the structure, and the truth is darker: Nvidia bought Groq for its intellectual property and engineering team, not because Groq had a sustainable business. Groq's chip, the Language Processing Unit (LPU), was genuinely impressive. It delivered 25-40% better performance than Nvidia's GPUs for specific inference workloads—the kind of tasks that power ChatGPT responses and Claude conversations. And yet Groq couldn't survive on its own. Why not? Because having a better chip is no longer enough.

Three months later, in February 2026, another AI chip startup called SambaNova—once valued at $5.1 billion—took a down-round that slashed its valuation to $2.2 billion, a 57% collapse. Intel tried to buy the company outright for $1.6 billion, but talks fell apart. SambaNova is still alive, but barely, propped up by a minority investment from Intel and dependent on Intel's manufacturing muscle. Then in May 2026, Cerebras—the last major independent AI chip company—went public. But its IPO was only possible because OpenAI committed to spending $20 billion buying Cerebras chips over the next few years. Cerebras isn't really independent; it's effectively a captive supplier to a single customer.

These aren't isolated failures. They're signals of a structural shift in how AI infrastructure works. And the shift has almost nothing to do with whose chip is technically superior.

> **TL;DR** — Amazon, Google, and Microsoft are building their own custom AI chips (Trainium, TPU, Maia), and their cloud businesses are showing real margin expansion—AWS just hit 37.7% operating margins, up from around 33% a year ago. But the advantage isn't that these chips are better than Nvidia's. It's that hyperscalers own the entire stack: the silicon, the cloud platform, and the services customers actually buy. That lets them subsidize infrastructure costs to win market share in higher-margin businesses like SaaS and AI agents. Nvidia survives but narrower. Independent chip startups are dead. And the real battle is shifting upstream to AI applications—the only layer where startups can still compete.

<div style="overflow-x:auto; margin: 2rem 0;">
<svg width="800" height="450" xmlns="http://www.w3.org/2000/svg" style="font-family: system-ui, sans-serif; max-width:100%;">
  <rect width="800" height="450" fill="#f9fafb" rx="12"/>
  
  <!-- Title -->
  <text x="400" y="36" text-anchor="middle" font-size="18" font-weight="bold" fill="#111">The AI Infrastructure Power Shift: 2025-2026</text>
  
  <!-- Left side: Hyperscalers Rising -->
  <rect x="40" y="70" width="340" height="300" fill="#fff" stroke="#e5e7eb" stroke-width="2" rx="8"/>
  <text x="210" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#059669">Hyperscalers: Margin Expansion</text>
  
  <!-- AWS bar -->
  <text x="60" y="125" font-size="12" fill="#374151">AWS Operating Margin</text>
  <rect x="60" y="135" width="240" height="24" fill="#dbeafe" rx="4"/>
  <rect x="60" y="135" width="160" height="24" fill="#3b82f6" rx="4"/>
  <text x="230" y="152" font-size="11" fill="#1e40af" font-weight="bold">37.7% (Q1 2026)</text>
  <text x="60" y="175" font-size="10" fill="#6b7280">↑ from ~33% in 2025</text>
  
  <!-- Google Cloud bar -->
  <text x="60" y="200" font-size="12" fill="#374151">Google Cloud Margin</text>
  <rect x="60" y="210" width="240" height="24" fill="#fef3c7" rx="4"/>
  <rect x="60" y="210" width="198" height="24" fill="#f59e0b" rx="4"/>
  <text x="268" y="227" font-size="11" fill="#92400e" font-weight="bold">32.9%</text>
  <text x="60" y="250" font-size="10" fill="#6b7280">↑ from 17.8% in 2025</text>
  
  <!-- Custom silicon metric -->
  <text x="60" y="280" font-size="12" fill="#374151">AWS Trainium Revenue</text>
  <text x="60" y="300" font-size="20" fill="#059669" font-weight="bold">$20B</text>
  <text x="60" y="318" font-size="10" fill="#6b7280">annual run rate, sold out</text>
  
  <!-- Right side: Chip Startups Collapsing -->
  <rect x="420" y="70" width="340" height="300" fill="#fff" stroke="#e5e7eb" stroke-width="2" rx="8"/>
  <text x="590" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#dc2626">Independent Chips: Casualties</text>
  
  <!-- Groq -->
  <circle cx="470" cy="135" r="8" fill="#dc2626"/>
  <text x="490" y="140" font-size="12" fill="#374151" font-weight="bold">Groq</text>
  <text x="490" y="156" font-size="10" fill="#6b7280">Acquired by Nvidia, $20B</text>
  <text x="490" y="170" font-size="9" fill="#9ca3af">Dec 2025 — tech lead, no distribution</text>
  
  <!-- SambaNova -->
  <circle cx="470" cy="205" r="8" fill="#dc2626"/>
  <text x="490" y="210" font-size="12" fill="#374151" font-weight="bold">SambaNova</text>
  <text x="490" y="226" font-size="10" fill="#6b7280">Down-round: $5.1B → $2.2B (-57%)</text>
  <text x="490" y="240" font-size="9" fill="#9ca3af">Feb 2026 — Intel stake, struggling</text>
  
  <!-- Cerebras -->
  <circle cx="470" cy="275" r="8" fill="#f59e0b"/>
  <text x="490" y="280" font-size="12" fill="#374151" font-weight="bold">Cerebras</text>
  <text x="490" y="296" font-size="10" fill="#6b7280">IPO, but locked to OpenAI deal</text>
  <text x="490" y="310" font-size="9" fill="#9ca3af">May 2026 — $20B customer commitment</text>
  
  <!-- Bottom insight -->
  <rect x="60" y="385" width="680" height="42" fill="#eff6ff" stroke="#3b82f6" stroke-width="1" rx="6"/>
  <text x="400" y="405" text-anchor="middle" font-size="11" fill="#1e40af" font-weight="600">The Pattern: Hyperscalers capture margin through vertical integration (chip + cloud + services).</text>
  <text x="400" y="420" text-anchor="middle" font-size="10" fill="#1e40af">Startups with best-in-class chips still die without owning the customer relationship.</text>
  
  <!-- Footer -->
  <text x="400" y="440" text-anchor="middle" font-size="11" fill="#9ca3af">prashant-chandel.org/blog</text>
</svg>
</div>

## The Margin Expansion That Actually Happened

For the past two years, the conventional wisdom about AI infrastructure has been simple: Nvidia wins. Their GPUs dominate, their software ecosystem (CUDA) creates lock-in, and their margins are absurd—around 77% gross margin in fiscal 2025. Every other player is scrambling to compete. But something changed in the first quarter of 2026 that upends this narrative.

Amazon Web Services reported operating income of $14.2 billion on $37.6 billion in revenue. Do the math, and that's a 37.7% operating margin—up from roughly 33-34% a year earlier. That's a meaningful jump, not a rounding error. Google Cloud's margins are even more dramatic: from 17.8% to 32.9% in a single year, a 1500 basis point expansion. These are real, reported numbers, not projections or promises.

Here's why this matters. For years, hyperscalers have been spending astronomical amounts on AI infrastructure—over $700 billion combined in 2026 across Amazon, Google, and Microsoft. But AI services (the stuff they sell to customers, like inference APIs and model hosting) have terrible margins compared to traditional cloud. Traditional cloud services run at 70-80% gross margins. AI inference services? More like 50-60%, because every API call burns compute and costs real money. That margin squeeze was supposed to be the price hyperscalers paid to stay competitive in AI. But instead, margins are expanding. How?

Custom silicon is the catalyst. Amazon's Trainium chips (designed for training AI models) and Inferentia chips (designed for running those models in production) just crossed a $20 billion annual revenue run rate. Andy Jassy, Amazon's CEO, said publicly that Trainium delivers "several hundred basis points of operating margin advantage" over using Nvidia GPUs. Google's TPU (Tensor Processing Unit) chips reportedly deliver 40%+ cost advantages for specific workloads. Microsoft's Maia chips are rolling into Azure datacenters. This isn't R&D theater—this is production infrastructure at scale.

But here's the crucial detail most analysis misses: custom silicon doesn't create margin expansion because these chips are inherently cheaper to manufacture than Nvidia's. They create margin expansion because hyperscalers can optimize the entire stack—the chip design, the datacenter power efficiency, the software orchestration layer—in ways that a company selling chips to third parties simply cannot. When you own the full pipeline from silicon to service, you can squeeze out inefficiencies at every layer.

> **Aside:** The comparison to Nvidia is instructive here. Nvidia's gross margins on datacenter accelerators were 77% in fiscal 2025. By 2026, multiple analysts and CFO commentary suggest that's falling toward 65-70%. That's still extraordinarily healthy for a hardware business, but the trend is unmistakable. Hyperscaler custom silicon is eating into Nvidia's pricing power, not because the chips are superior in every dimension, but because hyperscalers don't need to sell to third parties at high margins—they can price at cost internally and capture the value elsewhere.

Now, here's where the story gets interesting. These margin gains aren't happening because supply is abundant. In fact, it's the opposite. Jassy confirmed in Q1 2026 earnings that "Trainium2 is largely sold out, Trainium3 is nearly fully subscribed, and much of Trainium4 has already been reserved." The chips are scarce, which means AWS can keep prices high internally and externally. When supply constraints ease—probably 2027 or 2028—hyperscalers will face a choice: hold margins high and risk losing market share to competitors, or cut prices and compete on volume.

The historical pattern in infrastructure technology is clear: price compression always wins. During the cloud price wars of 2014-2018, AWS, Google, and Microsoft undercut each other repeatedly, and margins compressed. But here's the asymmetry that makes custom silicon different: even if hyperscalers cut prices by 30-40% to match competitors, they're cutting from a lower cost base. AWS can afford to sell Trainium capacity cheaper than anyone buying Nvidia GPUs at market rates, because AWS manufactures Trainium at cost. That's a structural advantage, not a temporary one.

## The Moat Is Integration, Not Innovation

Let's return to Groq for a moment, because the story clarifies what actually matters. Groq's chip was legitimately innovative. It used SRAM (static random-access memory, the fastest type of memory you can build into a processor) instead of the HBM (high-bandwidth memory) that Nvidia GPUs rely on. For specific types of AI inference—particularly long-context models that need to process thousands or tens of thousands of words at once—Groq's architecture was measurably faster. Independent benchmarks showed 25-40% better latency and throughput compared to Nvidia's A100 and H100 GPUs for those workloads.

But Groq had no path to monetize that advantage. Here's why. When an enterprise customer wants to run AI models, they don't call a chip company. They call their cloud provider—AWS, Azure, or Google Cloud. The cloud provider offers a menu: you can use our GPUs (which are Nvidia H100s), or you can use our custom chips (Trainium, Maia, TPU). For most customers, the decision comes down to two things: price and integration. Is the custom chip cheaper? And more importantly, does it integrate seamlessly with the rest of the services I'm already using?

For Groq to compete, they'd need to either (a) convince cloud providers to offer Groq chips as an option alongside Nvidia and custom silicon, which puts Groq in a weak negotiating position, or (b) build their own cloud platform, which requires billions in capital and years of customer acquisition that Groq didn't have. Neither path was viable. So Groq had a superior chip with no distribution channel.

Now contrast that with AWS. When AWS builds Trainium, it doesn't need to convince anyone to adopt it. AWS already has millions of customers using EC2 (its compute service), SageMaker (its machine learning platform), and Bedrock (its generative AI service). AWS can say to those customers: "If you use Trainium instead of GPUs, we'll give you 30% better price-performance." That's not a sales pitch to a new buyer—it's an upsell to an existing customer who already trusts you. And because AWS owns the full stack, it can bundle Trainium with credits, volume discounts, and preferential support. Groq couldn't do any of that.

This is what vertical integration actually means in practice. It's not about owning every step of the supply chain for ideological reasons. It's about controlling enough of the value chain that you can subsidize one part (infrastructure) to win in another part (services). AWS can sell Trainium capacity at low or even zero margin if it needs to, because AWS makes money on SageMaker subscriptions, Bedrock API calls, consulting services, and data egress fees. Nvidia can't subsidize anything—it only makes money on chip sales.

The same logic explains why Anthropic, one of the leading AI research labs, signed a $100 billion commitment to AWS in April 2026. The deal gives Anthropic preferential access to Trainium3 and Trainium4 chips—capacity that Anthropic simply couldn't get from Nvidia at any price, because Nvidia's production is constrained and allocated to the highest bidders. But AWS can guarantee that capacity to Anthropic because AWS manufactures it. In exchange, AWS gets deep insight into how cutting-edge AI models are trained and deployed, which feeds back into improving Trainium's design for the next generation. That's a closed loop that benefits both sides. Nvidia, selling to everyone, can't create that kind of partnership because it doesn't control the full stack.

## The SaaS Margin Compression That Didn't Stick

There's a second-order effect of custom silicon that initially looked like a crisis but turned out to be a temporary adjustment: the impact on software companies building AI features. When Salesforce, Workday, HubSpot, and others started adding AI agents and copilots to their products, they ran into a brutal economic reality. AI features are expensive.

Traditional SaaS (software as a service, the subscription model where companies pay monthly or annually for software) operates at 70-85% gross margins. You build software once, and every additional customer costs almost nothing to serve—just some server capacity and support overhead. But AI changes the unit economics. Every time a customer interacts with an AI agent, the software company has to call an inference API (from OpenAI, Anthropic, or AWS Bedrock), and that call costs real money. ICONIQ Capital, a prominent venture firm, found that AI-first SaaS companies are spending roughly 23% of their total revenue on inference costs alone. That compresses gross margins from 75-85% down to 50-65%.

On the surface, this looks like a disaster. Hyperscalers own the infrastructure (the chips and the APIs), so they can squeeze SaaS companies by raising inference prices whenever they want. SaaS companies are stuck—they need AI features to stay competitive, but those features destroy their margins. That was the doom scenario.

But it didn't play out that way. Salesforce, the largest independent SaaS company, launched Agentforce in 2025—a suite of AI agents that handle customer service, sales workflows, and data analysis. By Q4 fiscal 2026 (which ended January 31, 2026), Agentforce had hit $800 million in annual recurring revenue. That's a massive scale-up in less than a year. And crucially, Salesforce's gross margin didn't collapse. It actually expanded slightly, to 77.73%, while Agentforce was scaling. How?

The answer is pricing innovation and cost optimization. Salesforce structured Agentforce as hybrid pricing: customers pay a base subscription plus a usage fee (roughly $2 per conversation). That consumption-based pricing aligns the cost of running the AI (which scales with usage) with the revenue Salesforce collects (which also scales with usage). So when Salesforce's inference costs go up, customer bills go up proportionally. The company isn't absorbing the volatility—it's passing it through.

At the same time, Salesforce negotiated better terms with AWS for Bedrock (the service that hosts models like Claude and GPT-4). Large companies like Salesforce can get volume discounts that smaller SaaS startups can't. And Salesforce optimized which models to use for which tasks—using expensive, high-quality models (like Claude 3.5 Sonnet) only when necessary, and cheaper models (like Claude Haiku or open-source Llama) for simpler tasks. Those optimizations bring the effective cost per interaction way down.

The pattern that's emerging is clear: large SaaS companies with scale can negotiate, optimize, and stay profitable. Mid-market SaaS companies that can't get volume discounts or afford the R&D to optimize usage are getting squeezed. But instead of dying, they're getting acquired by larger platforms. Salesforce, Workday, and ServiceNow are all actively buying smaller SaaS companies to consolidate customer bases and spread infrastructure costs over larger revenue pools. That's not hyperscalers crushing SaaS—it's SaaS consolidating upward, which is a normal part of market maturation.

The takeaway: SaaS margins compressed temporarily as companies figured out how to price and optimize AI features. But margins are stabilizing around 65-70%, which is healthy. The real losers aren't SaaS companies broadly—they're the small, sub-scale SaaS startups that can't negotiate or optimize fast enough.

## The Independent Chip Startup Graveyard

Now let's return to the graveyard where Groq, SambaNova, and dozens of other AI chip startups ended up. The mechanics of why these companies failed are worth understanding in detail, because they reveal something fundamental about how infrastructure businesses work.

Building an AI chip from scratch costs $500 million to $2 billion per generation. That includes chip design (paying a team of world-class engineers for 2-3 years), manufacturing (booking capacity at a foundry like TSMC), testing and validation (making sure the chip works at scale), and software integration (building compilers, libraries, and tooling so developers can actually use the chip). Groq raised over $1.5 billion across multiple funding rounds. SambaNova raised a similar amount. Cerebras raised even more. These are enormous capital commitments.

But here's the problem: the addressable market for custom AI chips is tiny. Only a few dozen customers—hyperscalers, major AI labs (like OpenAI and Anthropic), large enterprises, and governments—buy enough compute to justify custom silicon. Everyone else rents capacity from cloud providers. So if you're an AI chip startup, you need to win a few anchor customers willing to commit billions in purchases, or you need to get acquired.

Groq never secured that anchor customer. SambaNova tried and failed. Cerebras succeeded, but only by giving OpenAI massive equity stakes and a $1 billion loan, which effectively makes Cerebras a supplier with terms dictated by its largest customer. That's not independence—that's dependence dressed up as partnership.

The second dynamic that kills chip startups is supply chain leverage. When TSMC's most advanced manufacturing capacity (3nm, 5nm nodes) is constrained—which it has been for most of 2024-2026—the foundry allocates capacity to its biggest, most reliable customers first. That means Apple, Nvidia, and AMD get priority access. Startups like Groq and SambaNova are pushed to older process nodes or longer wait times, which means their chips are less competitive when they finally ship. By the time SambaNova's chip is ready, Nvidia has already moved two generations ahead. This is a capital and relationship problem, not a technology problem.

The third mechanism is the hyperscaler advantage we've been discussing. When AWS offers Trainium and Google offers TPU, both companies can subsidize those offerings internally to win customers. Trainium doesn't need to be profitable on a standalone basis—it just needs to be good enough to keep AWS customers from switching to Azure or Google Cloud. AWS can price Trainium at cost or below, because AWS makes money on the services layer. Groq had no services layer. It only made money on chip sales. So when Groq tried to undercut Nvidia on price, it was cutting into its own margins with no offsetting revenue stream.

By late 2025, the venture capital market had figured this out. Funding for AI hardware startups dropped 64% between Q4 2025 and Q1 2026. Investors stopped funding standalone chip companies unless they had a clear path to hyperscaler backing or a locked-in customer. The message to entrepreneurs was clear: if you want to build in infrastructure, you need a corporate parent or an exclusive deal. Otherwise, you're building a product that will be acqui-hired or shut down.

The most telling signal: Recursive Superintelligence, a new AI company founded by DeepMind veterans, raised a $1.1 billion seed round in April 2026—one of the largest seed rounds in history. What's the company building? Not chips. It's building AI models and agents. That's where the value has migrated. Startups are fleeing infrastructure and moving upstream to applications, because that's the only layer where a small team can still outmaneuver hyperscalers through speed and specialization.

## What This Means for the Next Layer

The consolidation we're seeing in AI infrastructure isn't a failure of innovation or entrepreneurship. It's the natural evolution of any technology wave. In the 1990s, there were dozens of CPU startups. By the 2000s, there were two—Intel and AMD—because making CPUs became capital-intensive and manufacturing-constrained. In the 2010s, there were dozens of GPU startups and research projects. By the 2020s, Nvidia dominates, because it had superior execution and built an ecosystem (CUDA) that locked in developers. Now the same thing is happening to AI chips. The layer is consolidating around capital-rich players who can integrate vertically.

But here's what that means for the broader AI market: value is migrating. As infrastructure commoditizes (custom chips become table stakes for hyperscalers), the competitive battlefield shifts to the layers above—AI models, agents, and applications. That's where startups still have an advantage. A three-person team building an AI agent for legal document review can move faster than Amazon or Google, because they don't have to navigate corporate bureaucracy or worry about cannibalizing existing product lines. They can experiment, iterate, and find product-market fit in months, not years.

The hyperscalers know this, which is why they're not just building chips—they're also building services on top of those chips. AWS offers Bedrock (a marketplace for AI models). Google offers Vertex AI (a platform for training and deploying models). Microsoft offers Azure OpenAI (a managed service for GPT-4 and other models). These are attempts to capture the application layer too, by making it easier for customers to build on hyperscaler infrastructure without switching providers.

But there's a limit to how far hyperscalers can climb the stack. The more specific and vertical the application, the harder it is for a generalist hyperscaler to compete. AWS can build a generic AI customer service agent, but it probably can't build the best agent for handling insurance claims, because that requires deep domain knowledge of insurance workflows, regulations, and customer behavior. That's where startups win—by going narrow and deep.

So the prediction for the next 2-3 years: Infrastructure consolidates to three hyperscalers (AWS, Google Cloud, Azure) with Nvidia surviving as the "anywhere" option for enterprises that want flexibility. Chip startups either get acquired, back down to narrow niches (edge computing, specialized inference), or shut down. SaaS companies consolidate upward into larger platforms. And the real action moves to the application layer—AI agents, vertical SaaS with AI, and services built on top of foundation models. That's where the next generation of billion-dollar companies will come from.

The takeaway isn't that hyperscalers have won everything. It's that they've won infrastructure, which was always going to consolidate. The question now is whether they can win applications too, or whether that layer stays fragmented and competitive. My bet: applications stay fragmented, because building great software for specific use cases requires speed and specialization that large companies struggle with. But the infrastructure game is over. Hyperscalers own it, and the moat is vertical integration—owning silicon, cloud, and services—not any single chip's technical superiority.

If you're an entrepreneur looking at this landscape, the lesson is clear: don't build infrastructure unless you have billions in capital or a hyperscaler parent. Build applications. Build on top of Bedrock, Azure OpenAI, or Vertex AI. Build agents that solve real problems for specific industries. That's where the opportunity still exists. The infrastructure layer is closed. The application layer is wide open.


## Sources & Further Reading

**Custom Silicon & Margin Data:**
- [Amazon Q1 2026: AWS Surges 28% as Custom AI Chips Top $20B Run Rate](https://convergedigest.com/amazon-q1-2026-aws-surges-28-as-custom-ai-chips-top-20b-run-rate/)
- [Amazon Q1 2026 Earnings Beat on Every Line](https://www.tikr.com/blog/amazon-beat-q1-2026-earnings-on-every-line-the-bigger-story-is-the-chip-business-inside-aws)
- [Amazon's $20 Billion Strategy for Custom AI Silicon](https://science-technology.news-articles.net/content/2026/05/10/amazon-s-20-billion-strategy-for-custom-ai-silicon.html)
- [Amazon Q1 2026: AWS at 15-Quarter High Growth Drives Record Operating Margin](https://news.alphastreet.com/amazon-amzn-q1-2026-aws-at-15-quarter-high-growth-drives-record-operating-margin/)
- [Google's Latest TPU Advances Make the AI Hardware Race Feel Less One-Sided](https://247wallst.com/investing/2026/04/27/googles-latest-tpu-advances-make-the-ai-hardware-race-feel-less-one-sided/)
- [Alphabet (GOOGL) Q1 2026 Earnings Call Transcript](https://www.fool.com/earnings/call-transcripts/2026/04/29/alphabet-googl-q1-2026-earnings-call-transcript/)
- [Microsoft Maia 200: The AI Accelerator Built for Inference](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/)

**SaaS Margin Compression & Pricing:**
- [Why AI Gross Margins Are So Much Lower Than SaaS](https://www.softwareseni.com/why-ai-gross-margins-are-so-much-lower-than-saas-and-what-that-means-for-your-business/)
- [The Economics of AI-First B2B SaaS in 2026](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026/)
- [Your AI Feature Is Quietly Destroying Your Gross Margin](https://www.thesaascfo.com/your-ai-feature-is-quietly-destroying-your-gross-margin/)
- [The AI Project Gross Margin Reset Every SaaS Company Is About to Face](https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face/)
- [Salesforce Q4 FY 2026 Earnings Show Agentic AI Scaling](https://futurumgroup.com/insights/salesforce-q4-fy-2026-earnings-show-agentic-ai-scaling-guidance-steadies/)
- [Salesforce Agentforce Hits $800 Million ARR](https://completeaitraining.com/news/salesforce-agentforce-hits-800-million-arr-as-enterprise/)
- [Salesforce Q4 2026 Earnings Beat Expectations (Transcript)](https://www.investing.com/news/transcripts/earnings-call-transcript-salesforce-q4-2026-earnings-beat-expectations-93CH-4526261)

**Regulatory & Market Structure:**
- [Amazon and Microsoft Finally Face EU Anti-Competitive Cloud Probe](https://euobserver.com/215316/amazon-and-microsoft-finally-face-eu-anti-competitive-cloud-probe/)
- [The Register: Amazon, Microsoft Cloud DMA Investigation](https://www.theregister.com/2025/11/18/amazon_microsoft_cloud_dma)
- [EU Regulators Launch Cloud Market Probes](https://www.ciodive.com/news/eu-regulators-launch-cloud-market-probes/805841/)
- [Anthropic Amazon Compute Partnership](https://www.anthropic.com/news/anthropic-amazon-compute)
- [Amazon Invests Additional $5 Billion in Anthropic AI](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai)

**AI Chip Startup Outcomes:**
- [Nvidia-Groq Deal: AI Chip Startups in Play](https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/)
- [Nvidia Buying AI Chip Startup Groq for About $20 Billion](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html)
- [Cerebras IPO Mints Two Billionaires, Sets Stage for Potential AI Wave](https://www.cnbc.com/2026/05/14/cerebras-ipo-mints-two-billionaires-sets-stage-for-potential-ai-wave.html)
- [Cerebras Prices IPO Above Expected Range](https://www.cnbc.com/2026/05/13/cerebras-prices-ipo-above-expected-range-wall-street-expects-ai-flood.html)
- [OpenAI to Spend More Than $20 Billion on Cerebras Chips](https://www.reuters.com/technology/openai-spend-more-than-20-billion-cerebras-chips-receive-equity-stake-2026-04-17/)
- [Intel Partners with SambaNova After Buyout Talks Reportedly Failed](https://www.cnbc.com/2026/02/24/intel-partners-with-sambanova-after-buyout-talks-reportedly-failed.html)
- [SambaNova Raises $350 Million Series E at $2.2 Billion Valuation](https://businesswire.com/news/home/20260128/SambaNova-Raises-$350-Million-Series-E-at-$2.2-Billion-Valuation-Down-From-$5.1B-Peak)
- [DeepMind's David Silver Just Raised $1.1B to Build an AI That Learns Without Human Data](https://www.cnbc.com/2026/05/04/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/)

**Market Analysis & Frameworks:**
- [The AI Profit Map: Why the Biggest Winners Aren't Who You Think](https://longyield.substack.com/p/the-ai-profit-map-why-the-biggest)
- [Major Hyperscalers Just Reported Earnings: Nvidia Was the Winner](https://247wallst.com/investing/2026/05/02/major-hyperscalers-just-reported-earnings-nvidia-was-the-winner/)
- [GPU vs TPU: Which AI Hardware Should You Choose in 2026?](https://aihardware.ai/gpu-vs-tpu-which-ai-hardware-should-you-choose-in-2026/)
- [Q1 2026 AI Funding Blows Past 2025 Total](https://pitchbook.com/news/articles/q1-2026-ai-funding-blows-past-2025-total-with-three-deals-accounting-for-67-of-capital)
- [NVIDIA Q1 2026 Earnings Call Transcript](https://www.rev.com/transcripts/nvidia-q1-2026-earnings-call)
