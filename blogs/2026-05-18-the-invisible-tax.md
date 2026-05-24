---
title: "The Invisible Tax: Why AI's Winners Hide the Bill"
date: 2026-05-18
topic: "AI Infrastructure & Business Strategy"
summary: "OpenAI spends $1.35 for every dollar it earns. Microsoft bundles the same AI costs invisibly into Office 365 and thrives. The difference isn't the technology—it's whether customers can see the price tag."
---

Salesforce changed the price of its AI assistant three times in eighteen months. First, they tried charging per conversation. Then they switched to charging per action the AI took. Then they gave up and created a hybrid model. None of it worked. After all that, only 5–8% of their customers actually turned the thing on.

Meanwhile, Microsoft launched an AI assistant that does roughly the same things—summarizes emails, writes documents, answers questions—and bundled it into Office 365. They didn't change the pricing three times. They didn't need to. The AI costs are there, definitely—Microsoft is spending billions on chips and power—but the cost is invisible to each individual user. It's just part of the Office subscription that 365 million people already pay for. Microsoft's net revenue retention (how much more money existing customers spend year over year) went above 115%. Salesforce's AI adoption stalled at single digits.

The difference is not the technology. It's whether the customer can see the bill.

> **TL;DR** — AI infrastructure costs are now permanent and visible, and markets are splitting based on who can hide them. Companies that bundle AI into existing platforms and spread costs across millions of users (Microsoft, Google, Apple, Meta) will dominate 80%+ of the market. Companies forced to show per-token or per-transaction pricing (OpenAI, Anthropic, SaaS add-ons) are stuck in specialized segments or face adoption collapse. This isn't a pricing problem you can solve with better pricing—it's a structural split that determines who survives.

<div style="margin: 2rem 0;">
<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg" style="font-family: system-ui, sans-serif; width:100%; height:auto; display:block;">
  <!-- Background -->
  <rect width="800" height="450" fill="#ffffff" rx="12" stroke="#e5e7eb" stroke-width="1.5"/>
  
  <!-- Title -->
  <text x="400" y="36" text-anchor="middle" font-size="18" font-weight="bold" fill="#111">The AI Market Split: Bundlers vs. Transparent Pricers</text>
  
  <!-- Left Side: Cost-Hiding Bundlers -->
  <rect x="40" y="70" width="340" height="320" fill="#f0f9ff" rx="8" stroke="#3b82f6" stroke-width="2"/>
  <text x="210" y="100" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">Cost-Hiding Bundlers</text>
  <text x="210" y="125" text-anchor="middle" font-size="13" fill="#3b82f6">80%+ of market</text>
  
  <!-- Bundlers: Companies -->
  <text x="60" y="155" font-size="13" font-weight="600" fill="#111">Microsoft, Google, Apple, Meta</text>
  
  <!-- Bundlers: Key metrics -->
  <text x="60" y="185" font-size="12" fill="#374151">• Office 365: 365M users</text>
  <text x="60" y="205" font-size="12" fill="#374151">• Copilot bundled → invisible cost</text>
  <text x="60" y="225" font-size="12" fill="#374151">• NRR: 115%+</text>
  
  <text x="60" y="255" font-size="12" font-weight="600" fill="#1e40af">Strategy:</text>
  <text x="60" y="275" font-size="11" fill="#374151">Spread AI costs across millions</text>
  <text x="60" y="290" font-size="11" fill="#374151">of existing users. Cost per user:</text>
  <text x="60" y="305" font-size="11" fill="#374151">invisible. Adoption: frictionless.</text>
  
  <text x="60" y="335" font-size="12" font-weight="600" fill="#1e40af">Business model:</text>
  <text x="60" y="355" font-size="11" fill="#374151">Lose money on inference, gain</text>
  <text x="60" y="370" font-size="11" fill="#374151">on retention, upsells, device sales</text>
  
  <!-- Right Side: Cost-Transparent Specialists -->
  <rect x="420" y="70" width="340" height="320" fill="#fef2f2" rx="8" stroke="#ef4444" stroke-width="2"/>
  <text x="590" y="100" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">Cost-Transparent Specialists</text>
  <text x="590" y="125" text-anchor="middle" font-size="13" fill="#ef4444">5–20% of market</text>
  
  <!-- Specialists: Companies -->
  <text x="440" y="155" font-size="13" font-weight="600" fill="#111">OpenAI, Anthropic, SaaS add-ons</text>
  
  <!-- Specialists: Key metrics -->
  <text x="440" y="185" font-size="12" fill="#374151">• OpenAI: $1.35 spent per $1 earned</text>
  <text x="440" y="205" font-size="12" fill="#374151">• Salesforce AI: 5–8% adoption</text>
  <text x="440" y="225" font-size="12" fill="#374151">• Per-token pricing visible to customers</text>
  
  <text x="440" y="255" font-size="12" font-weight="600" fill="#991b1b">Problem:</text>
  <text x="440" y="275" font-size="11" fill="#374151">Customers see exact per-query cost.</text>
  <text x="440" y="290" font-size="11" fill="#374151">Adoption collapses or margins</text>
  <text x="440" y="305" font-size="11" fill="#374151">compress under negotiation pressure.</text>
  
  <text x="440" y="335" font-size="12" font-weight="600" fill="#991b1b">Viable segments:</text>
  <text x="440" y="355" font-size="11" fill="#374151">• Frontier reasoning (high-value niches)</text>
  <text x="440" y="370" font-size="11" fill="#374151">• On-device AI (one-time chip cost)</text>
  
  <!-- Footer -->
  <text x="400" y="440" text-anchor="middle" font-size="11" fill="#9ca3af">prashant-chandel.org/blog</text>
</svg>
</div>


## The Math That Nobody Wants You To See

OpenAI spent $8.4 billion on inference (running AI models to answer queries) in 2025. Inference is the actual work of AI—when you ask ChatGPT a question, that's inference. Training the model happens once; inference happens millions of times per day, every day, forever.

In 2025, OpenAI earned less than they spent. In 2026, they'll spend $14.1 billion on inference. That's a 68% increase year-over-year. Their revenue is growing too, but not fast enough. For every dollar OpenAI earns, they spend $1.35 delivering the service.

This is not a temporary problem that gets better as the technology matures. Inference costs are growing *faster* than revenue because people are using AI more, for harder problems, which require more compute. The cost-per-query is going down thanks to better chips and software, but total queries are exploding faster than efficiency improves.

Here's why that matters: OpenAI's pricing is transparent. You pay per token (basically per word the AI reads or writes). Customers can see exactly what they're spending. Big enterprise customers run the math and realize that at scale, AI is expensive. A company using AI to handle customer service emails might calculate that each AI-handled conversation costs $0.50 in API fees. If they handle a million conversations a month, that's $500,000. Per month. Forever.

When customers can see that number, they do one of two things: they don't adopt AI at all, or they negotiate aggressively and AI becomes a low-margin commodity service.

Microsoft doesn't have this problem. They spend billions on inference too—probably more than OpenAI in absolute terms—but the cost is invisible. If you're an Office 365 customer, you don't get a separate line item that says "AI inference: $47 this month." It's bundled. You're already paying $12.50 per user per month for Office. Microsoft adds Copilot and maybe raises the bundle price by $5 or just absorbs the cost and recoups it by getting you to upgrade to a higher tier. Either way, you never see "$0.50 per conversation" on a spreadsheet.

Bundling isn't just a nice-to-have. It's the entire business model.

## The Power Bill Is Real

Let's talk about what's underneath all of this: electricity.

Training an AI model is expensive, but you do it once. Inference—running that model billions of times—requires 80–90% of all AI-related power consumption. That's the real bottleneck now, not training.

Microsoft signed a deal to restart Three Mile Island (yes, the nuclear plant) and take 835 megawatts of power for 20 years. Meta signed contracts for 6.6 gigawatts of nuclear power. Amazon committed €15.7 billion to data centers in Spain. These aren't small bets. These are the largest infrastructure investments since the original internet build-out in the late 1990s.

And it's not just corporate budgets paying for it. In Maryland, state regulators are forcing ratepayers (ordinary people paying their electric bills) to cover $2 billion in grid upgrades to support out-of-state data centers. Maryland citizens are subsidizing compute infrastructure they don't directly benefit from. This is the cost being socialized—spread across entire populations because the grid is shared.

Hyperscalers (AWS, Google Cloud, Microsoft Azure—basically the giant companies that run most of the internet's infrastructure) are locking in power not because they have some magical ability to generate electricity cheaper than anyone else. It's arbitrage and execution. Spain has cheap renewable energy and favorable regulations, so Amazon goes there. Microsoft goes to nuclear because it's stable and doesn't depend on weather. Meta is hedging across multiple sources.

But here's the thing: power access is not a durable moat (a competitive advantage that's hard for others to copy). It's expensive and hard, yes, but it's not proprietary. If you have the capital and the relationships, you can do the same deals. The real moat is on the other end—whether you can hide the cost from the customer.

> **Aside:** The phrase "inference bottleneck" didn't exist in mainstream tech writing three years ago. Now it's the single most important phrase in AI infrastructure. Training gets the headlines because it involves huge clusters and record-breaking chip orders, but inference is the quiet, relentless cost that runs forever. If training is building a factory, inference is running the assembly line 24/7 for the next decade.

## The Device In Your Pocket Changes The Equation

Not all AI runs in the cloud anymore. Meta shipped something called ExecuTorch, which runs AI models directly on your phone inside WhatsApp and Instagram. Billions of users, no cloud required for many queries. Apple announced on-device AI for Siri at WWDC 2026. Qualcomm is shipping chips with 60 TOPS (trillion operations per second) of AI performance built in.

On-device AI solves one problem: it's nearly free per query. Once the chip is in the phone, running a model costs basically nothing. No data center. No electricity bill. No API call.

This should, in theory, destroy the cloud inference market. If everyone's phone can run AI locally, why would anyone pay for cloud inference?

The answer: because the hard problems still require the big models in the data center. Your phone can handle "set a timer for 10 minutes" or "what's the weather." It cannot handle "read these 50 documents and write a strategy memo" or "analyze this financial model and find errors." Those queries require frontier models (the most advanced, expensive AI models that only a few companies can build and run), and frontier models are too big to run on a phone.

And here's the surprising part: OpenAI's inference costs grew 68% year-over-year *even as on-device AI started shipping at scale*. That suggests that on-device and cloud inference are not competing for the same queries. They're serving different use cases. On-device takes the commodity work (simple, repetitive queries). Cloud takes the frontier work (complex, high-value queries).

If that holds, the bifurcation is even starker. Commodity AI becomes free (on-device). Frontier AI stays expensive (cloud). And the only companies that can afford to run frontier AI at scale are the ones who can hide the cost.

## Two Markets, Not One

This is the key insight: the AI market is splitting into two entirely different structures, and they don't compete.

**Market 1: Cost-hiding bundlers.** Microsoft, Google, Apple, Meta. They have hundreds of millions or billions of existing users already paying for something (Office, Gmail, iCloud, Instagram). They add AI features to those products and spread the infrastructure cost across the entire user base. Each user pays a tiny amount more (or the company absorbs it and recoups through higher retention or upgrades). The cost is invisible. Adoption is high because there's no separate decision to "buy AI"—it's just part of the thing you already use.

These companies will control 80%+ of the AI market by user count and total queries. Not because their AI is better (though it might be), but because they own the distribution and the bundling mechanism.

**Market 2: Cost-transparent specialists.** OpenAI, Anthropic, and any company selling AI as a separate line item or add-on. Their customers see the per-token or per-conversation cost. That transparency kills mass adoption. It works only in specific cases: (1) frontier reasoning that's so valuable the cost doesn't matter (a law firm paying $500/hour for AI legal research is fine because their lawyers bill $800/hour), or (2) on-device AI where the cost is zero per query after the hardware purchase.

This market is 5–20% of total TAM (total addressable market—the total amount of money or users available in a market). It's real. It's profitable for the leaders. But it's capped.

The difference is not product quality. It's structure. Bundlers hide costs and win mass markets. Transparent pricers serve niches.

## What Happens To Traditional SaaS

SaaS companies (software-as-a-service—think Salesforce, Zendesk, Adobe, companies that sell software by subscription) are stuck in the middle.

They used to have gross margins (revenue minus the cost to deliver the service) of 75–82%. Beautiful, capital-efficient businesses. Then AI came along. If they add AI features, their gross margins drop to 60–70% because inference costs are real and per-user. If they *don't* add AI, they lose customers to competitors who do.

Salesforce tried to thread the needle by charging extra for AI. They launched Agentforce (an AI assistant for sales and service teams) and tried three different pricing models. Per-conversation didn't work because customers could see costs scaling with usage. Per-action didn't work for the same reason. Hybrid (a mix of fixed and variable) didn't work because it was too complicated. Adoption stayed at 5–8%.

Microsoft doesn't have this problem because Office 365 is already a bundle. Salesforce sells a point solution (CRM software), so every new feature is a separate buying decision.

The question is whether traditional SaaS companies can *become* bundlers. Can Salesforce turn into a platform where AI is just one invisible piece of a much larger, integrated product? Or are they stuck as a mid-market contractor selling features one by one, with margins compressing forever?

Current evidence suggests bundling is harder than it looks. Microsoft has 365 million Office users and decades of enterprise IT lock-in. Salesforce has strong CRM market share, but CRM is one function. It's not the whole productivity stack. If you can't bundle across the whole workflow, you can't hide the cost effectively.

## Who Survives And Why

The winners in this split are clear:

**Full-stack bundlers** (Microsoft, Google, Apple, Meta) dominate consumer and broad enterprise markets. They own distribution (existing users), infrastructure (data centers and chips), and devices (in some cases). They can subsidize AI costs in one layer and capture profits in another. Microsoft loses money on inference but gains it back through higher Office 365 retention and enterprise upsells.

**Frontier specialists** (OpenAI, Anthropic) survive in high-value niches. They serve customers who need the absolute cutting-edge models and are willing to pay transparent, high per-query costs. Think research labs, hedge funds, law firms, advanced engineering teams. This is a real market, but it's 5–20% of the total, not 80%.

**On-device platforms** (Qualcomm, MediaTek, phone makers) own the commodity tier. Once the chip is in the phone, queries are free. They make money selling the chips, not the inference. This is a different business model entirely—hardware margins, not software margins.

**The losers** are companies stuck in the middle: traditional SaaS vendors who add AI as a paid add-on, and infrastructure companies that sell only compute without owning the application layer. If you expose costs and don't own a must-have application, you get squeezed on price and margin.

## The One Thing That Could Change This

The entire thesis depends on frontier AI staying expensive and valuable. If on-device AI improves faster than expected—if the chips in our phones can run frontier-quality models in two years instead of five—then the hyperscalers' $100 billion power infrastructure investments become oversized. Demand for cloud inference collapses. The bifurcation model breaks.

Right now, that's not happening. OpenAI's costs are growing 68% year-over-year *despite* on-device competition. That suggests frontier and on-device are serving separate markets and both are growing.

But this is the variable to watch. If on-device suddenly leaps forward—if Apple or Qualcomm ships a chip that can run GPT-5-equivalent models locally—the whole game changes. Cloud inference demand craters. Power contracts become liabilities. The winners flip.

For now, though, the pattern is clear: hide the cost, win the market. Show the cost, serve the niche.


## Sources & Further Reading

- [OpenAI Inference Cost Crisis: Economics of AI in 2026](https://aiautomationglobal.com/blog/ai-inference-cost-crisis-openai-economics-2026) — Deep dive into OpenAI's unit economics and cost trajectory
- [Sacra: OpenAI Research](https://sacra.com/research/openai/) — Detailed analysis of OpenAI's inference cost growth
- [The Doomed Evolution of Salesforce's Agentforce Pricing](https://www.getmonetizely.com/blogs/the-doomed-evolution-of-salesforces-agentforce-pricing) — How transparent pricing killed AI adoption at Salesforce
- [The AI Project Gross Margin Reset Every SaaS Company Is About to Face](https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face) — SaaS margin compression mechanics
- [Maryland Citizens Slapped with $2B Grid Upgrade Bill for Out-of-State AI Data Centers](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises) — How AI infrastructure costs are being socialized
- [Meta Signs Multi-Gigawatt Nuclear Deals to Power AI Data Centers](https://www.latimes.com/business/story/2026-01-09/meta-signs-multi-gigawatt-nuclear-deals-to-power-ai-data-centers) — Hyperscaler power infrastructure investments
- [ExecuTorch: On-Device ML at Meta Family of Apps](https://engineering.fb.com/2025/07/28/android/executorch-on-device-ml-meta-family-of-apps/) — Meta's on-device AI at production scale
- [Sierra Raises $950M as the Race to Own Enterprise AI Gets Serious](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/) — Context on enterprise AI adoption patterns
- [On-Device LLMs in 2026: What Changed, What Matters, What Next](https://v-chandra.github.io/on-device-llms/) — Technical deep-dive on on-device inference capabilities
