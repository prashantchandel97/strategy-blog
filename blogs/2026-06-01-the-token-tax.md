---
title: "The Token Tax: Why AI's Cost Problem Just Got Structural"
date: 2026-06-01
topic: "AI Infrastructure & Economics"
summary: "Microsoft cancelled most internal AI coding licenses after 6 months. Uber blew through its entire 2026 AI budget in 4 months. The problem isn't the per-token price-it's that agents consume 3.2x to 50x more tokens per task, and consumption is growing 10x faster than cost declines."
---

In May 2026, Microsoft quietly cancelled most of its internal Claude Code licenses-the AI coding tools that employees had been using since December 2025. The shutdown came after just six months. One Nvidia executive, speaking to Fortune about the decision, put it bluntly: "the cost of compute was far beyond the cost of the employees" it replaced.

This was Microsoft. The company that owns 49% of OpenAI. The company that spent $14 billion on AI infrastructure in Q1 2026 alone. And even they couldn't make the math work for AI coding assistants at full deployment.

Around the same time, Uber burned through its entire 2026 AI coding tools budget in four months. The company had allocated somewhere between $500 and $2,000 per engineer per month. At 95% adoption, that budget evaporated faster than anyone expected. Not because the tools didn't work-they did. But because the cost of running them at scale was unsustainable.

> **TL;DR** - AI infrastructure economics are bifurcating, not consolidating. Hyperscalers like Google and Amazon will build custom silicon to compress their own infrastructure costs, while enterprise customers stay locked into Nvidia's ecosystem at premium prices. But neither group escapes the real crisis: agentic AI (AI tools that perform multi-step tasks, like writing code or booking travel) consumes 3.2x to 50x more tokens per task than simple chatbots. Token consumption is projected to grow 24x by 2030, far outpacing per-token cost declines. When the token tax exceeds the ROI, no amount of vendor lock-in or clever pricing will save the model.

**In this piece:**
- Memory has become the bottleneck in AI chips-64-68% of the cost of an AI accelerator is now DRAM and HBM (high-bandwidth memory), up from 33% in 2023, which means custom silicon is suddenly economically viable for anyone willing to write their own software.
- Hyperscalers are splitting off into their own infrastructure world, building custom chips to cut costs, while enterprises stay locked into Nvidia's ecosystem because rewriting code and retraining teams costs more than the hardware savings.
- Agentic AI burns tokens at 3.2x to 50x the rate of simple chatbot queries, and Goldman Sachs projects 24x token consumption growth by 2030-if that growth outpaces per-token price declines, the entire enterprise AI market hits an ROI wall.
- SaaS companies are shifting to consumption-based pricing (charging per AI task executed instead of per seat) not to expand margins, but to avoid being crushed by unpredictable token costs they can't control.
- The Microsoft and Uber cancellations are not anomalies-they are leading indicators of what happens when token costs grow faster than the value created, and the only question left is whether this inflection point arrives in 2026-2027 or later.

<div style="margin: 2rem 0;">
<svg viewBox="0 0 800 480" xmlns="http://www.w3.org/2000/svg" style="font-family: Inter, system-ui, sans-serif; width:100%; height:auto; display:block;">
  <!-- Background -->
  <rect x="0" y="0" width="800" height="480" fill="#F8FAFC"/>
  
  <!-- Header band -->
  <rect x="0" y="0" width="800" height="3" fill="#2563EB"/>
  <rect x="0" y="3" width="800" height="52" fill="#0F172A"/>
  <text x="400" y="38" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">Token Consumption vs. Cost Decline: The Widening Gap</text>
  
  <!-- Left card: Per-token cost trajectory -->
  <rect x="42" y="93" width="3" height="340" fill="#0000000D"/>
  <rect x="39" y="90" width="3" height="340" fill="#0000000D"/>
  <rect x="36" y="87" width="350" height="340" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
  <rect x="36" y="87" width="350" height="3" fill="#059669"/>
  
  <text x="211" y="115" text-anchor="middle" font-size="13" font-weight="600" fill="#1E3A5F">Per-Token Cost Declining</text>
  
  <!-- Big metric callout -->
  <text x="211" y="165" text-anchor="middle" font-size="30" font-weight="700" fill="#059669">90%</text>
  <text x="211" y="180" text-anchor="middle" font-size="11" fill="#94A3B8">cost reduction since GPT-4 launch</text>
  
  <!-- Cost trend bars -->
  <text x="50" y="215" font-size="11" fill="#475569">GPT-4 (2023)</text>
  <rect x="155" y="205" width="220" height="18" rx="4" fill="#DC2626" opacity="0.3"/>
  <text x="368" y="218" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">$0.06/1K</text>
  
  <text x="50" y="250" font-size="11" fill="#475569">GPT-4 Turbo (2024)</text>
  <rect x="155" y="240" width="110" height="18" rx="4" fill="#DC2626" opacity="0.3"/>
  <text x="258" y="253" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">$0.01/1K</text>
  
  <text x="50" y="285" font-size="11" fill="#475569">Claude 3 (2025)</text>
  <rect x="155" y="275" width="88" height="18" rx="4" fill="#DC2626" opacity="0.3"/>
  <text x="236" y="288" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">$0.008/1K</text>
  
  <text x="50" y="320" font-size="11" fill="#475569">On-device (2026)</text>
  <rect x="155" y="310" width="22" height="18" rx="4" fill="#059669"/>
  <text x="170" y="323" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">~$0</text>
  
  <!-- Bottom annotation -->
  <text x="50" y="360" font-size="11" font-weight="500" fill="#0F172A">✓ Falling fast</text>
  <text x="50" y="378" font-size="10" fill="#94A3B8">Economies of scale + competition</text>
  <text x="50" y="393" font-size="10" fill="#94A3B8">driving prices down consistently</text>
  
  <!-- Right card: Token consumption growth -->
  <rect x="417" y="93" width="3" height="340" fill="#0000000D"/>
  <rect x="414" y="90" width="3" height="340" fill="#0000000D"/>
  <rect x="411" y="87" width="350" height="340" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="1"/>
  <rect x="411" y="87" width="350" height="3" fill="#DC2626"/>
  
  <text x="586" y="115" text-anchor="middle" font-size="13" font-weight="600" fill="#1E3A5F">Token Consumption Exploding</text>
  
  <!-- Big metric callout -->
  <text x="586" y="165" text-anchor="middle" font-size="30" font-weight="700" fill="#DC2626">24x</text>
  <text x="586" y="180" text-anchor="middle" font-size="11" fill="#94A3B8">projected growth by 2030 (Goldman Sachs)</text>
  
  <!-- Consumption comparison -->
  <text x="425" y="215" font-size="11" fill="#475569">Simple query</text>
  <rect x="530" y="205" width="30" height="18" rx="4" fill="#2563EB" opacity="0.3"/>
  <text x="553" y="218" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">50</text>
  <text x="568" y="218" font-size="10" fill="#94A3B8">tokens</text>
  
  <text x="425" y="250" font-size="11" fill="#475569">AI coding task</text>
  <rect x="530" y="240" width="180" height="18" rx="4" fill="#DC2626" opacity="0.3"/>
  <text x="703" y="253" font-size="12" font-weight="600" fill="#0F172A" text-anchor="end">2K-10K</text>
  <text x="730" y="253" font-size="10" fill="#94A3B8">tokens</text>
  
  <text x="425" y="285" font-size="11" fill="#475569">Autonomous agent</text>
  <rect x="530" y="275" width="210" height="18" rx="4" fill="#DC2626"/>
  <text x="733" y="288" font-size="12" font-weight="600" fill="#FFFFFF" text-anchor="end">5K-25K</text>
  
  <!-- Multiplier callout -->
  <text x="425" y="320" font-size="11" font-weight="500" fill="#DC2626">✗ Consumption multiplier:</text>
  <text x="425" y="338" font-size="11" font-weight="700" fill="#DC2626">3.2x to 50x per task</text>
  
  <!-- Bottom annotation -->
  <text x="425" y="370" font-size="10" fill="#94A3B8">Microsoft cancelled Claude Code after</text>
  <text x="425" y="385" font-size="10" fill="#94A3B8">6 months: "cost of compute was far</text>
  <text x="425" y="400" font-size="10" fill="#94A3B8">beyond the cost of the employees"</text>
  
  <!-- Divider line between cards -->
  <line x1="400" y1="100" x2="400" y2="420" stroke="#E2E8F0" stroke-width="2" stroke-dasharray="4 4"/>
  
  <!-- Source -->
  <text x="790" y="472" text-anchor="end" font-size="10" fill="#94A3B8">prashant-chandel.org/blog</text>
</svg>
</div>

## Memory is the new moat (and the new bottleneck)

For the last three years, the story of AI infrastructure has been about compute. Nvidia's H100 GPUs became the gold standard because they could run massive AI models faster than anything else. The entire industry aligned around a single question: how much compute can you afford?

But that story is changing. The bottleneck has shifted from compute to memory.

Here's what happened: as AI models got bigger and more complex, they needed to store and retrieve vastly more data during each calculation. The chips themselves got faster, but the memory feeding them couldn't keep up. So chipmakers started adding high-bandwidth memory (HBM)-a specialized type of ultra-fast memory that sits right next to the processor on the chip package. HBM is expensive to manufacture and in short supply, and it's now the dominant cost in AI accelerators.

According to Epoch AI data from early 2026, memory now accounts for 64-68% of the total component cost of an AI accelerator chip. In 2023, it was around 33%. DRAM and HBM production absorbed 23% of global memory wafer capacity in 2026, up from 19% in 2024. The memory manufacturers-Samsung, SK Hynix, Micron-are running at full tilt, and they still can't make enough.

This shift changes the economics of custom silicon. When compute was the bottleneck, Nvidia's advantage was overwhelming. Their GPUs were faster, their CUDA software ecosystem (the programming environment that developers use to write code for Nvidia chips) was mature, and switching costs were astronomical. If you wanted to move to a different chip, you had to rewrite all your code and retrain your entire engineering team. For most companies, that cost exceeded the savings.

But when memory becomes the dominant cost, the equation flips. Memory components are commodities-everyone buys from the same three suppliers. If you can design a chip that pairs those memory components with a custom processor optimized for your specific workloads, you can cut costs dramatically. You give up Nvidia's general-purpose flexibility, but you gain efficiency on the tasks you actually run.

This is exactly what the hyperscalers-Google, Amazon, and Meta-are doing. Google has been building TPUs (Tensor Processing Units, their custom AI chips) for nearly a decade. In May 2026, Google and Blackstone announced a joint venture with an initial $5 billion commitment (expandable to $25 billion) to build data centers running TPUs, not Nvidia GPUs. The target: 500 megawatts of TPU capacity by 2027. Sundar Pichai, Google's CEO, explicitly confirmed in the announcement that Google uses TPUs over Nvidia GPUs wherever possible.

Amazon has Trainium and Inferentia. Meta is building its own AI chips. Microsoft has Maia. None of these chips are better than Nvidia's for all tasks-but they don't need to be. They just need to be cheaper for the specific workloads each company runs most often. And because these companies control the full stack-the chip, the cloud infrastructure, and the applications sitting on top-they can optimize the entire system as a unit.

The result: a bifurcation. Hyperscalers will compress their own infrastructure costs by moving to custom silicon. Everyone else stays on Nvidia.

## The CUDA lock and why it holds (for now)

Nvidia still holds 86% of the data center GPU market. That dominance isn't eroding quickly, and the reason is CUDA.

CUDA is Nvidia's software platform-the toolkit that developers use to write code that runs on Nvidia GPUs. It's been around since 2006, and it's extraordinarily mature. Every major AI framework-PyTorch, TensorFlow, JAX-is built to work seamlessly with CUDA. Millions of lines of production code are written in CUDA. Every university computer science program teaches it. If you're training AI researchers or engineers, they're learning CUDA.

This creates a switching cost that goes far beyond hardware. To move off Nvidia chips, you don't just buy different hardware. You rewrite your codebase. You retrain your team. You debug new toolchains. You rebuild deployment pipelines. For a hyperscaler running a million servers, that cost is painful but acceptable-you amortize it across massive scale, and the infrastructure savings eventually pay for the migration.

For a mid-market company deploying 50 or 500 servers, the math doesn't work. The cost of switching exceeds the hardware savings. So you stay on Nvidia, even if you'd prefer not to.

This is why Nvidia's margins haven't collapsed yet. Their data center GPU gross margins are still 73% as of Q1 2026. Custom silicon is gaining share, but Nvidia's pricing power remains intact for the majority of the market.

But there's a trap here, and it's starting to show in the Microsoft and Uber data. CUDA lock-in protects Nvidia's margins, but it doesn't protect their customers from the token tax. And if customers hit an ROI wall, vendor lock-in becomes a liability, not an asset.

## The token tax: when consumption outpaces cost declines

Here's the pattern that matters: per-token costs are falling, but token consumption is rising faster.

Per-token pricing has dropped dramatically over the last two years. GPT-4 Turbo costs about 1/10th what GPT-4 cost at launch. Claude 3 Opus is cheaper than Claude 2. Google's Gemini models undercut OpenAI on price across the board. On-device AI-models that run locally on your phone or laptop-can answer queries for nearly free once you've paid for the chip.

So why are companies cancelling AI pilots?

Because agentic AI-AI tools that perform multi-step tasks instead of single-query responses-consumes vastly more tokens per task. A chatbot answering "What's the weather in New York?" might use 50 tokens. An AI coding assistant writing a function, debugging it, running tests, and refactoring the code might use 2,000 to 10,000 tokens. An autonomous agent booking a flight could burn through 5,000 to 25,000 tokens as it searches options, compares prices, checks your calendar, and confirms the booking.

Goldman Sachs projects that token consumption will grow 24x by 2030. That's not because models are getting worse at efficiency-they're getting better. It's because the use cases are shifting from simple queries to complex, multi-step workflows. The more valuable the task, the more tokens it burns.

And this is where the Microsoft and Uber examples become critical. Both companies were running AI coding assistants at high adoption rates. Both hit budget limits in a matter of months, despite falling per-token costs. The token consumption multiplier-somewhere between 3.2x and 50x depending on task complexity-overwhelmed the per-token price declines.

Microsoft's decision to cancel Claude Code licenses wasn't a rejection of the technology. It was a recognition that at current consumption rates, the cost of running AI assistants for every employee exceeded the labor cost savings. The Nvidia executive's quote-"the cost of compute was far beyond the cost of the employees"-captures the inversion. The tool was supposed to make people more productive. Instead, it became more expensive than the people.

This is the token tax, and it's structural. As long as token consumption grows faster than per-token costs fall, enterprise AI deployments will hit ROI ceilings. It doesn't matter if Nvidia's margins compress or CUDA lock-in holds. The economics break at the application layer.

## SaaS companies are cost-shifting, not margin-expanding

In May 2026, SAP announced a shift to consumption-based pricing for its Autonomous Suite-a set of AI-powered workflow automation tools. Instead of charging per user seat, SAP will charge per workflow execution. The company framed this as a move toward "value-based pricing," where customers pay for outcomes, not inputs.

But look at the incentives. SAP isn't absorbing the AI infrastructure costs. They're passing them through to customers. If a customer runs 10,000 autonomous workflows a month and each workflow consumes 5,000 tokens, SAP is on the hook for 50 million tokens of inference costs. Under a per-seat model, SAP eats that variability and hopes usage averages out across customers. Under consumption pricing, the customer pays per execution, and SAP's margins stay predictable.

This isn't margin expansion-it's cost-shifting. And customers are resisting. The Register reported in May that SAP customers are pushing back on the pricing change, worried that AI agent costs will spiral out of control once they're directly exposed to token consumption variability.

The same dynamic is playing out across enterprise SaaS. Salesforce, ServiceNow, Adobe-every company adding AI features is wrestling with the same problem: how do you price something when the cost structure is unpredictable and rising? The answer, increasingly, is to make the customer absorb the risk.

This works until customers realize they're paying more for AI-enhanced software than they were for the non-AI version, with ROI that's unclear or negative. At that point, the SaaS company faces a choice: cut AI features, compress margins to subsidize usage, or lose customers.

The token tax doesn't just hit infrastructure providers. It cascades up the stack.

## The enterprise ROI wall is already here

The Microsoft and Uber cancellations are not anomalies. They're leading indicators.

Both companies are sophisticated technology buyers. Both ran controlled pilots with clear budgets and measurable outcomes. Both hit cost ceilings in 4-6 months despite falling per-token prices. This tells you something important: the token consumption multiplier is already outpacing cost declines for high-adoption agentic use cases.

The question is whether this is a leading indicator of enterprise-wide ROI rejection, or a Microsoft/Uber-specific issue tied to high agentic task adoption rates that other companies won't hit as quickly.

Here's the evidence for "this is already systemic":
- Goldman Sachs projects 24x token growth by 2030, with most of that growth driven by agentic workflows, not simple queries.
- Microsoft and Uber are early adopters, but they're not outliers. Coding assistants, customer support agents, and autonomous booking tools are all agentic by design. These are the highest-value use cases, and they're the ones burning tokens fastest.
- SaaS companies are shifting to consumption pricing specifically to avoid being crushed by token cost variability. That shift only makes sense if they expect token costs to rise faster than per-seat revenue.

Here's the evidence for "this is a timing blip":
- Per-token costs are still falling fast. GPT-4 Turbo is 1/10th the cost of GPT-4. On-device models are nearly free per query. If cost declines accelerate, token consumption growth might stabilize.
- Microsoft and Uber both had unusually high adoption rates (95% for Uber). Most enterprises are at 10-30% pilot adoption. Lower adoption means lower token burn and more time before hitting ROI walls.
- Agentic AI is still early. As models improve, task completion might require fewer tokens. A task that takes 10,000 tokens today might take 2,000 tokens in 2027 if reasoning efficiency improves.

The unresolved question: do the current data points (Microsoft, Uber, SaaS repricing, Goldman's 24x projection) already prove that token growth outpaces cost declines, or are we watching a leading-indicator blip that stabilizes as models mature?

If the former, the enterprise AI market hits an ROI wall in 2026-2027, and no amount of CUDA lock-in or vendor pricing power will stop the pullback. If the latter, we have 2-3 more years before the inflection point, and the window for infrastructure players to compress costs is still open.

## What this means for the infrastructure layer

If token consumption outpaces cost declines, the entire AI infrastructure stack gets repriced.

Nvidia's CUDA lock-in protects margins in the short term, but it becomes a liability if enterprise customers demand price cuts or threaten to move to cloud providers' custom silicon. Hyperscalers can absorb token cost inflation because they control the full stack and can subsidize infrastructure to win application-layer revenue. Nvidia can't. They sell hardware, not applications. If enterprise customers stop buying, Nvidia's revenue growth flatlines even if margins hold.

Google, Amazon, and Meta benefit from bifurcation. They build custom silicon to cut their own costs, and they sell cloud capacity to enterprises who can't afford to switch off Nvidia. They win on both sides: lower infrastructure costs for their own workloads, and premium pricing for enterprise cloud customers who need Nvidia-compatible infrastructure.

Independent chip startups are caught in the middle. They can't compete with Nvidia on general-purpose performance, and they can't compete with hyperscalers on cost for vertically integrated workloads. The only viable path is to find a niche-specific workloads where custom silicon delivers 5x-10x cost or performance improvements and where customers are willing to rewrite code. That's a small market.

SaaS companies face a margin squeeze. They can shift to consumption pricing to avoid being crushed by token costs, but that only works if customers accept the variability. If customers resist or demand pricing caps, SaaS companies either subsidize token costs (compressing margins) or lose customers.

The big winners: companies that own both the infrastructure and the application layer. Google can afford to run Search on TPUs at cost because Search revenue pays for it. Amazon can subsidize AWS inference costs to win e-commerce AI workloads. Meta can run ads on custom silicon and never show customers an inference bill. Microsoft can bundle AI into Office 365 and spread the cost across 400 million seats.

The big losers: companies that sell AI infrastructure or AI-enhanced software without owning the full stack. If token costs rise faster than customer willingness to pay, they're stuck.

## The path forward (or the path down)

There are three scenarios from here.

**Scenario 1: Token costs compress faster than consumption grows.**
Per-token prices fall by 50-70% over the next 12-18 months due to on-device AI, better model efficiency, and hyperscaler price competition. Token consumption grows, but not fast enough to overwhelm cost declines. Enterprise AI pilots that failed in 2026 get re-piloted in 2027 and succeed. ROI turns positive. The market expands.

**Scenario 2: Token consumption grows faster than costs compress, but only for agentic use cases.**
Simple chatbot queries become nearly free. Agentic workflows (coding assistants, autonomous agents, multi-step automation) remain expensive and hit ROI walls. The market bifurcates: high-volume, low-complexity use cases (customer support FAQs, document search) succeed; high-complexity, high-token use cases (coding, autonomous booking, complex automation) stall or retrench. The total market is smaller than projected, but it's stable.

**Scenario 3: Token consumption outpaces cost declines across the board.**
Agentic AI becomes the dominant use case. Goldman's 24x token growth projection proves accurate. Per-token costs fall, but not fast enough. Enterprise AI budgets get exhausted in 6-12 months, just like Microsoft and Uber. ROI rejection spreads across industries. AI becomes a niche tool for high-margin use cases only. Infrastructure revenue collapses.

The Microsoft and Uber cancellations suggest we're closer to Scenario 2 or 3 than Scenario 1. But the sample size is still small, and both companies are early adopters running high-adoption agentic pilots. We won't know for certain until Q4 2026 or Q1 2027, when enterprise AI budgets either get renewed or slashed.

What's clear: the token tax is real, it's structural, and it's already breaking enterprise AI deployments at the high end. The only question is how fast it spreads.

If you're building in AI infrastructure, your margin depends on per-token cost compression outpacing consumption growth. If you're a SaaS company adding AI features, your survival depends on customers accepting consumption-based pricing and token cost variability. If you're an enterprise buyer, your ROI depends on whether the tasks you automate create enough value to justify token costs that might be 10x-50x higher than you budgeted for.

And if you're Nvidia, your moat is CUDA lock-in-but that only holds as long as your customers can afford to keep buying. The moment the token tax exceeds the ROI, lock-in becomes a reason to leave, not a reason to stay.

The next six months will tell us which scenario we're in. Watch the enterprise AI budget announcements in Q4 2026. If they grow despite 2026's cancellations, the market believes Scenario 1. If they flatten or shrink, the token tax has arrived.


## Sources & Further Reading

- [AI Chip Component Cost Shares](https://epoch.ai/data-insights/ai-chip-component-cost-shares) - Memory now accounts for 64-68% of AI accelerator component costs, up from 33% in 2023
- [The AI Chip Token Bubble Economy](https://fortune.com/2026/05/30/ai-chip-token-bubble-economy-nvidia-microsoft-hyperscalers-2/) - Microsoft's Claude Code cancellation, Uber's 4-month budget burn, and token growth projections
- [Blackstone-Google AI Data Center Joint Venture](https://www.cnbc.com/2026/05/19/blackstone-google-ai-data-center-joint-venture-tpu.html) - $25B TPU infrastructure partnership targeting 500MW by 2027
- [Agentic AI Cost Runaway and Token Budget Management](https://leanopstech.com/blog/agentic-ai-cost-runaway-token-budget-2026/) - Token consumption multiplier data (3.2x-50x per task)
- [Nvidia vs AMD GPUs in 2026](https://www.gpunex.com/blog/nvidia-vs-amd-gpus-2026/) - CUDA lock-in dynamics and 86% market share
- [SAP Customers Warned: AI Agents Could Put Costs on Autopilot](https://www.theregister.com/saas/2026/05/19/sap-customers-warned-ai-agents-could-put-costs-on-autopilot/) - SaaS consumption pricing as cost-shifting strategy
- [Memory Chip Shortage Impacting AI and Consumer Electronics in 2026](https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/) - HBM/DRAM wafer capacity data and Nvidia margin analysis
- [Indian Travel Fintech Scapia Doubles Valuation to Over $500M](https://techcrunch.com/2026/05/20/indian-travel-fintech-scapia-more-than-doubles-valuation-to-over-500m-in-a-year/) - Series C funding and UPI infrastructure arbitrage
- [Will SAP Be a Software Company in the Future?](https://erp.today/will-sap-be-a-software-company-in-the-future-sapphire-2026-keynote-maps-saps-new-erp-stack/) - SAP Autonomous Suite and consumption-based repricing shift
