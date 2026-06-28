---
type: podcast-script
date: 2026-06-22
based_on: 2026-06-22-domain-structure-beats-discipline.md
estimated_duration: 23 minutes
word_count: 3,280
---

# Episode: Why Only Some SaaS Companies Will Win From AI (And It's Not About Discipline)

## COLD OPEN

Stripe trades at 57 times revenue. [pause] Salesforce trades at 8 and a half. [pause]

Same technology stack. Same AI hype. Both enterprise software. But one is worth seven times more per dollar of revenue than the other.

Wall Street will tell you it's about execution. Stripe's management is just better. [pause]

The data tells a completely different story. And if you're investing in SaaS companies right now, or building one, this gap is about to get a lot wider.

---

## INTRODUCTION

I'm Prashant. This is Thinking in Strategies.

Every week I take one business or strategy story and try to actually explain what's going on beneath the surface.

Today we're talking about why most enterprise AI is failing to deliver ROI, why fintech is the massive exception, and why the valuation gap between those two categories is about to triple. This matters if you're investing in software companies, if you're building one, or if you're a CFO trying to figure out where AI actually works.

Let's get into it.

---

## ACT 1 — CONTEXT

So here's where we are. In 2025, 42% of companies abandoned most of their AI projects. [pause] MIT looked at enterprise AI pilots and found that 95% delivered zero measurable impact on the profit and loss statement. Morgan Stanley studied the entire S&P 500 and found only 21% of companies could cite any measurable AI benefit at all.

This is happening while hyperscalers are pouring $675 billion into AI infrastructure this year. While CEOs are announcing AI transformations in earnings calls. While 72% of enterprises say they're deploying AI.

The gap between enthusiasm and proof is enormous. And debt markets noticed first. Citi identified a 30 basis point credit spread penalty for AI spenders who can't show returns. That means companies burning cash on AI without proving ROI are paying more to borrow money because lenders think they're riskier bets.

The consensus explanation goes like this: most companies lack measurement discipline. They run pilots without defining what success looks like. They deploy AI without proving it moves the needle. They scale before validating ROI.

And yes, that's part of it. But framing this as a discipline problem misses something more fundamental. [pause]

The real constraint is that most enterprise work doesn't have the data structure AI needs to produce measurable outcomes. Let me explain what I mean by that.

A transaction in a payment network carries hundreds of signals. Device fingerprint, location, spending patterns, velocity, merchant category, time of day, customer history. All of it already structured. All of it standardized. The outcome is binary and immediate. Either this transaction is fraud or it's not. There's no ambiguity.

Compare that to a sales rep's day. Calls, emails, relationship building, conversations that resist standardization. Success is measured in closed deals, but any given deal is influenced by a dozen factors. The rep's skill, product fit, market timing, decision maker politics, competitor moves, economic conditions. You can measure whether the deal closed, but you can't cleanly attribute how much of that was the AI tool versus everything else.

This is not a cultural difference. It's an information structure difference. And it explains why fintech AI works while sales AI mostly doesn't.

---

## ACT 2 — THE ARGUMENT

Let me show you what data-native work looks like in practice.

Stripe's Radar system processes hundreds of billions of dollars in transactions annually. It analyzes hundreds of signals per transaction and reaches a decision in under 100 milliseconds. The result: Stripe reports a 32% average fraud reduction for customers using Radar. [pause] For SEPA payments, which are common in Europe, the reduction hits 42%. For ACH transfers, 20%.

The ROI math is completely transparent. If your average transaction is $50 and your fraud rate is half a percent, that's typical for e-commerce, preventing 32% of that fraud saves you 0.16% of revenue per transaction. Process a million dollars annually, you save $1,600. Process $100 million, you save $160,000. And Stripe's cost to deliver this is negligible as a percentage of gross margin because Radar runs at hyperscale across all customers.

Razorpay, India's payment processor, told investors at a fintech summit in 2026 that per-transaction fraud losses dropped 40% year over year as their AI detection improved. [pause] Razorpay now processes over $50 billion in transactions annually. A 40% fraud reduction means somewhere between $500 million and $1 billion in prevented fraud losses across their customer base.

That's not hype. That's measurable cash that didn't get stolen.

Cashfree Payments reports 70% fraud detection accuracy with 10-minute go-lives for new merchant integrations. In the traditional model, where India's central bank requires manual verification, merchants waited weeks for KYC clearance and fraud checks. AI reduces that friction by 95%. Faster onboarding means more merchants live faster, which means more transaction volume, which means more revenue.

Now here's what all of these have in common. [slower] The work product is inherently data-structured. A transaction is a data object with standardized fields. Fraud is a binary outcome. It either happened or it didn't. The measurement happens automatically as part of the payment rails. There's no need to build a measurement culture because the measurement is baked into the infrastructure.

This is why fintech didn't need the 18-month discipline ramp that everyone talks about. They had 15 years of transaction data. They knew what the outcome variable was. Deployment was a data engineering problem, not a cultural one.

So that's what's happening in fintech. Here's why it matters for everyone else.

According to Gartner, finance functions deploying AI for invoice automation, forecasting, and expense auditing achieve 8-month average payback periods. [pause] Some implementations hit full ROI in 6 months. Operations and supply chain AI hits 12 to 14-month payback. Demand forecasting, inventory optimization, logistics routing.

Sales and marketing? 18 to 24-plus month payback periods. And customer service ROI is ambiguous. Chatbots handle more volume, but the labor savings are diffuse and hard to measure.

This is a 2-to-3 times difference in payback speed. And it's structural. It's not because finance teams are smarter. It's because finance work is already data-native. Invoices are structured documents. Expense codes are standardized. Forecasts are numerical outputs that map directly to the P&L. A CFO deploying AI for invoice processing can immediately measure the impact. Invoices processed per hour, error rates, time to close.

A sales leader deploying AI for lead scoring measures something much murkier. Did this help close the deal? Which is overdetermined by a dozen other factors.

Now here's the part that I think most people miss. [pause]

Wall Street is treating this as a temporary learning curve problem. The story they're telling is that fintech companies are just better run. Stripe's management is exceptional. Razorpay executed flawlessly in a tough market. These are company-specific wins.

But if this were a management problem, you'd expect some horizontal SaaS companies to crack it. You'd expect Salesforce or HubSpot or ServiceNow to figure out how to deliver measurable AI ROI. They have the best talent, the most resources, the longest customer relationships. [pause] And they're not cracking it.

The reason is that you can't measure what you can't structure into data. And you can't structure relationship-driven work into clean, deterministic outcomes no matter how disciplined you are.

And this is where it gets genuinely interesting because there's a second layer to this. The cost reduction happening right now in AI infrastructure only helps if you already have ROI.

Amazon's custom chip business crossed $20 billion in annual revenue in Q1 2026, growing at triple-digit rates year over year. That's Trainium for training and Graviton for general compute. Google's TPU infrastructure is projected to hit $25 billion in revenue by 2027. Microsoft's Maia 200 chip started shipping in volume this year, optimized specifically for inference, which is running trained models at scale. That's where 80% of AI infrastructure cost lives.

These chips are specialized. Nvidia GPUs are general-purpose accelerators. They run training, inference, scientific computing. That generality is why they command 70 to 80% gross margins. But hyperscalers don't need generality. Google's TPUs are optimized for Transformer models, which represent 95% of large language model workloads. Trainium is optimized for training transformers. Maia 200 is optimized for inference.

Because they're specialized, they execute the same workloads as an Nvidia H100 with 40 to 50% less silicon area, which means 40 to 50% lower cost.

That cost advantage is not theoretical. Google's Trillium TPU delivers 1.8 times better performance per dollar versus the prior generation. Morgan Stanley analysts estimate that a customer migrating from Nvidia GPUs to Google TPUs saves 35 to 40% on total AI compute costs. For a company running $100 million in annual AI infrastructure, that's $35 to 40 million per year in permanent cost reduction.

But here's what matters. [pause] Stripe, Razorpay, and Cashfree didn't wait for custom silicon to achieve real ROI. They deployed fraud detection at traditional GPU pricing because the fraud prevention value was so large that even Nvidia's margins didn't kill the economics.

This tells you the fintech ROI advantage isn't driven by cheap compute. It's driven by data structure.

Once compute costs drop another 40 to 50%, fintech AI features move from strategically important to mandatory for competition. But for sales and marketing AI, where the fundamental problem is that you can't cleanly measure whether the tool helped close the deal, cost reduction is irrelevant. You're just making a marginal ROI proposition slightly less marginal.

The implication: custom silicon accelerates bifurcation rather than solving it. Data-ready domains get cheaper compute and expand margins. Unstructured domains get cheaper compute and still have broken ROI.

And this is where regulation comes in, which sounds like it should slow everything down, but actually it accelerates the split.

On June 10, 2026, Senators Chuck Grassley and Amy Klobuchar reintroduced the American Innovation and Choice Online Act. The bill prohibits large tech platforms from self-preferencing. That means giving their own services advantages over competitors. If it passes, Amazon would have to offer Trainium chips to Azure and Google Cloud at the same price AWS pays internally. Google would have to sell TPU access to competitors. Microsoft would need to make Maia 200 available to third parties.

The bill has failed three times before. It has bipartisan sponsors, but tech lobbying spend in 2026 is at historic highs. Over $400 million aimed specifically at killing this type of legislation. The baseline probability of passage is below 30%.

Meanwhile, the EU's Digital Markets Act is already in force. The European Commission issued preliminary findings in late June 2026 suggesting AWS and Azure qualify as cloud gatekeepers under the DMA. That triggers an 8 to 12-week response window, followed by a final determination in Q4 2026 or early 2027. Then comes the legal challenge window. Based on precedent from Apple and Meta DMA appeals, both still ongoing, expect 2 to 3 years of litigation before enforcement really bites.

Here's what this means. Hyperscalers have a 3 to 4-year runway to entrench their custom silicon advantages before regulation forces them to share. That's enough time for custom chips to capture 25 to 35% of inference workloads and 15 to 20% of training workloads.

But regulation has an asymmetric effect that accelerates bifurcation. Fintech companies deploying AI for fraud detection can argue: our AI improves our regulatory compliance posture. We need custom silicon optimization to maintain detection accuracy and meet central bank and PCI requirements. Regulators buy this argument. Finance and operations teams make the same case.

Sales AI, marketing AI, customer success AI have no equivalent regulatory exemption. If anything, they face headwinds. Bias scrutiny in hiring and promotion decisions, privacy concerns around tracking and targeting, disclosure requirements about whether a customer is talking to a bot or a human.

The result: data-ready domains keep custom silicon advantages longer because regulators justify them. Unstructured domains lose advantages faster because regulators question them.

Regulation doesn't stop the bifurcation. It accelerates it.

---

## ACT 3 — COUNTERARGUMENT

Now, the pushback I'd expect here is: you're cherry-picking fintech. What about all the other data-native domains? Operations, supply chain, logistics. If data structure is the differentiator, why aren't those companies trading at the same premium as fintech?

And honestly, it's a fair point. [pause]

The answer is that they are starting to. It's just less visible because those companies are smaller and mostly private. Gartner's data shows that supply chain AI achieves 18% inventory overstocking reduction, which is measurable and repeatable. Operations teams deploying AI for demand forecasting and logistics routing are seeing 12 to 14-month payback periods. That's not as fast as fintech's 8 months, but it's twice as fast as sales and marketing.

The difference between fintech and other data-native domains is that fintech's outcome is money. Fraud detection literally saves cash. Operations AI saves cost, which flows to the bottom line, but it's not as visceral. It doesn't compound the same way preventing fraud does.

So the valuation premium for fintech should be the highest, but other data-native domains should see premiums too. Just not as extreme. And that's exactly what we're starting to see in private markets. Finance operations SaaS is trading at 6 to 9 times revenue. Supply chain and operations SaaS at 6 to 8 times. That's still above horizontal SaaS at 4 to 6 times.

The question is whether that gap widens further. And I think it does, because the ROI difference is structural.

---

## TAKEAWAY

If you take three things from today:

One. [slower] AI ROI isn't about discipline. It's about data structure. If your work product isn't already structured into deterministic outcomes, no amount of measurement culture will make AI deliver clean ROI. Fintech works because transactions are data objects with binary outcomes. Sales doesn't work because deals are overdetermined by factors you can't isolate.

Two. Custom silicon and regulation both accelerate bifurcation rather than solving it. Cheaper compute makes fintech margins better, but it doesn't fix sales AI's broken attribution problem. And regulation gives data-ready domains exemptions that unstructured domains don't get.

Three. The valuation gap is underpriced. Fintech SaaS trades at about 1.5 times the multiple of horizontal SaaS today. But the ROI difference is 2 to 3 times. That means fintech should be trading at 20 to 25 times revenue while horizontal SaaS compresses to 5 to 7 times. The repricing is coming. If you're investing in SaaS companies, bet on depth in data-native domains, not breadth across all enterprise software.

---

## CLOSE

That's it for this week.

If you want to go deeper, the full written piece is at prashant-chandel.org/blog. There's an infographic there that maps out the whole argument visually, and all the sources are linked if you want to verify the numbers.

If this was useful, share it with one person who'd appreciate it. That's the best way to help the show grow.

See you next Sunday.
