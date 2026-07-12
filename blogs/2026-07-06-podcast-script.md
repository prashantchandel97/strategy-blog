---
type: podcast-script
date: 2026-07-06
based_on: 2026-07-06-margin-migration.md
estimated_duration: 23 minutes
word_count: 3,215
---

# Episode: Where Margin Goes When Everything Becomes Commodity

## COLD OPEN

AWS charges $6.88 per hour for an H100 GPU. Spheron charges $2.54 for the exact same chip. [pause] That's a 171% markup. Four dollars and thirty-four cents extra. Every single hour.

And yet, AWS's margins are perfectly safe. [pause]

Meanwhile, GPT-5.2, a general-purpose AI that anyone can access, beat a specialized medical AI at diagnosing diseases. Beat it by 7 percentage points on accuracy. By 18 points on whether doctors would actually trust the diagnosis. [pause]

The specialist lost to the generalist.

Something fundamental shifted in 2026. Capability became free. Hardware became commodity. And margin migrated to a completely different layer. Today, we're going to talk about where it went, and why the companies that haven't figured this out are losing immediately.

---

## INTRODUCTION

I'm Prashant. This is Thinking in Strategies. Every week I take one business or strategy story and try to actually explain what's going on beneath the surface.

This week, we're looking at three things that seemed contradictory at first. GPU prices dropped 63%, but hyperscalers are charging bigger markups than ever. Frontier AI models beat specialized models, killing the specialist moat. And the SaaS sector dropped 40%, but companies like Salesforce are growing at 169%. 

All three stories are about the same thing. Margin didn't disappear. It just moved. And if you're building, investing, or leading anything right now, you need to know where it went.

---

## ACT 1 — CONTEXT

So here's where we are.

For the last two years, the entire tech industry has been in this race to build AI infrastructure. Companies are spending hundreds of billions of dollars on GPUs, on data centers, on compute capacity. Google has a $460 billion cloud backlog. Meta is spending $115 to $135 billion on AI infrastructure just this year.

All of that spending drove massive demand for GPUs. Specifically, Nvidia's H100 chip, which is the flagship GPU for running large AI models. For a while, H100s were impossible to get. Lead times were six months. Prices were sky-high. If you wanted to build an AI product, you basically had to get in line.

But by mid-2026, supply caught up. Nvidia ramped production. Competitors launched alternative chips. And suddenly, H100s became available. Not scarce anymore. Just available.

When supply catches up with demand, prices usually collapse. That's Econ 101. Scarcity creates pricing power. Abundance kills it. And that's exactly what happened with GPUs. A company called Spheron, which is a decentralized cloud provider, started renting H100s for $2.54 per hour. That's 63% cheaper than AWS was charging a year earlier.

You'd think that creates an obvious opportunity, right? Enterprises see the cheaper option, move their AI workloads over to Spheron, and AWS loses billions in revenue. The commodity GPU market kills the hyperscaler margin.

Except that's not what happened. [pause]

AWS kept charging $6.88 per hour for the same chip. And enterprises kept paying it. No mass exodus. No pricing pressure. AWS's cloud margins stayed intact.

At the same time, something strange was happening in the application layer. Companies that had spent years building specialized AI models, trained on proprietary data for specific industries, started seeing their moats evaporate. A study published in Nature Medicine in June tested this. They gave GPT-5.2, which is OpenAI's general-purpose frontier model, and OpenEvidence, which is a specialized medical AI built specifically for clinical diagnosis, the same set of medical exam questions.

GPT-5.2 scored 91.2%. OpenEvidence scored 84.1%. The generalist beat the specialist by 7 points.

Then they asked doctors whether they'd trust each AI's recommendations. GPT-5.2 got 89.3% approval. OpenEvidence got 71.4%. The gap widened to 18 points.

This is the opposite of how markets usually work. Specialists are supposed to win. A cardiologist beats a general practitioner. A tax attorney beats a general lawyer. But in AI, the thing trained on everything is beating the thing trained on one domain.

So if infrastructure is commodity, and capability is commodity, where does margin actually live? That's the question we're answering today.

---

## ACT 2 — THE ARGUMENT

Let's start with that GPU price gap, because it's the clearest example of what's happening.

AWS charges $6.88 per hour. Spheron charges $2.54. The difference is $4.34. But that $4.34 isn't markup on the hardware. AWS isn't pocketing $4.34 in profit per hour. [pause]

That $4.34 is the price of three things Spheron can't offer.

First, compliance. That's worth about $1.50 to $2.00 per hour. If you're a bank, a hospital, or a government contractor, you can't just run your AI workload anywhere. You need SOC 2 Type II certification. That's an audit proving you handle data securely. You need HIPAA compliance if you're dealing with health data. You need FedRAMP authorization if you're working with federal agencies. And often, you need dozens of other regulatory checkboxes.

AWS spent years and hundreds of millions of dollars earning those certifications. Spheron hasn't. And likely won't, because the audit costs are only worth it if you're serving thousands of enterprise customers who need them.

Second, ecosystem integration. That's worth about $0.60 to $1.00 per hour. Your AI model probably doesn't run in isolation. It pulls data from your company's database. It sends results to your CRM. It logs metrics to your monitoring dashboard. It triggers alerts in Slack. It writes outputs to cloud storage.

If all those systems are already on AWS, which for most large companies they are, moving the AI workload to Spheron means connecting an external provider to your internal AWS network. That creates latency, which is the delay when data moves between systems. It creates security risks, because now you have an outside vendor accessing your internal data. And it creates integration headaches, because you need custom code to connect Spheron's APIs to AWS's APIs.

Most companies decide the $4.34 per hour is cheaper than the engineering time required to manage that complexity.

Third, switching costs. That's about $1.50 to $2.50 per hour. Once you've built your AI infrastructure on AWS, your code is written using AWS-specific tools. Your engineers know AWS's interface. Your security team has audited AWS's setup. Your procurement team has a contract with AWS.

Moving to Spheron means rewriting code, retraining engineers, re-auditing security, and renegotiating contracts. For a large company running thousands of AI workloads, that switching cost can easily be tens of millions of dollars. [pause]

Paying an extra $4.34 per hour indefinitely is cheaper than paying $30 million once to switch.

So here's the pattern. Capability became commodity. The GPU itself, the actual hardware, anyone can buy that from Nvidia and resell it. But integration stayed expensive. Compliance, ecosystem, lock-in. Those three things take years to build, and they can't be commoditized by a new entrant just offering lower prices.

AWS isn't in the GPU business anymore. They're in the integration business. [slower] And that's where margin lives now.

---

Now let's move up one layer, to what happened with specialized AI models.

For years, the conventional wisdom was that frontier models would be good at everything but great at nothing. If you wanted an AI to diagnose diseases, you'd train a specialized model on medical textbooks, journal articles, clinical case files. That specialist model would beat the generalist because it was purpose-built. That was the moat.

The Nature Medicine study in June tested that assumption. They gave GPT-5.2 and OpenEvidence, the specialized medical AI, the same diagnosis questions. And the generalist won. By 7 points on accuracy. By 18 points on clinical approval.

This is not supposed to happen. [pause] But it did. And here's why.

GPT-5.2 was trained on vastly more data. Not just medical texts. Everything on the internet. Medical information, yes, but also psychology research, sociology studies, public health data, patient forums. That breadth makes it better at diagnosis than a model trained only on clinical data, because real diagnosis requires understanding human behavior and social context, not just memorizing symptoms.

For companies that built specialized AI models, this is devastating. If you spent three years and $50 million building a legal AI, or a finance AI, or a customer service AI, and then GPT-5.2 beats it out of the box, your moat just evaporated. [pause]

Capability, which you thought was defensible because it required domain expertise and proprietary training data, became commodity the moment frontier models got good enough.

The companies that understood this pivoted. Harvey, which is a legal AI startup, stopped competing on model quality. They started building agent orchestration. That's software that coordinates multiple AI models and connects them to legal databases, document systems, workflow tools. They're not selling capability anymore. They're selling integration.

Sound familiar?

---

Now here's where it gets more complicated, because three things are happening simultaneously in the SaaS sector, and they seem to contradict each other.

First, the SaaS sector dropped 40%. Per-seat pricing, which is how most software companies charge, is collapsing. Per-seat pricing means you pay based on how many employees use the software. But AI agents don't need seats. If you used to pay Salesforce $150 per month for 100 sales reps, but now one AI agent does the work of 20 reps, you only need 5 human seats. Salesforce's revenue from your company just dropped 95%. Investors looked at that math and repriced every SaaS company downward by an average of 40%.

Second, companies executing repricing fast are growing. Salesforce's Agentforce product, which uses AI agents and charges based on outcomes instead of seats, hit $800 million in annual recurring revenue with 169% year-over-year growth. HubSpot, another big SaaS company, shifted to outcome-based pricing and hit its 2027 margin targets a year early. These companies are re-rating upward, even as the sector overall dropped 40%.

Third, specialized AI vendors are surviving longer than expected. The conventional wisdom after the frontier-model-beats-specialist result was that all specialized AI companies would die within 12 months. But that's not happening. Companies with regulatory moats, which are special certifications required to operate in their industry, or data moats, which are proprietary datasets that frontier models can't access, or governance moats, which are systems for auditing and controlling AI decisions that enterprises require, those companies are getting a 3 to 5 year reprieve. They're pivoting from selling capability to selling compliance.

So which is it? Is SaaS dying, thriving, or bifurcating?

The answer is all three, but on different timelines. [pause]

The SaaS sector dropped 40% because the market priced in a slow 12 to 18 month repricing cycle. Most SaaS companies are still on per-seat contracts that won't expire until 2027 or 2028. Investors assume that when those contracts renew, companies will renegotiate to outcome-based pricing or switch to cheaper AI-native alternatives. That assumption caused the 40% sector-wide drop.

Companies executing repricing fast are re-rating upward because they're proving the repricing window is shorter than expected. Salesforce and HubSpot didn't wait for contracts to expire. They launched agent-based products now. They gave existing customers incentives to switch early. They locked in outcome-based pricing before competitors could. The market is rewarding that speed with 10% to 20% valuation increases, even as the sector overall is down 40%. [pause] Execution speed became the new moat.

Specialized AI vendors with governance moats get 3 to 5 years because regulation moves slower than technology. Even if GPT-5.2 is better at medical diagnosis than OpenEvidence, hospitals can't just plug in GPT-5.2 and start using it. They need audit trails. That's records proving every diagnosis decision was made correctly. They need explainability. That's the ability to show a doctor exactly why the AI made a recommendation. And they need liability frameworks. That's legal agreements specifying who is responsible if the AI makes a mistake.

Building those governance layers takes years. Specialized AI vendors that pivoted to building governance infrastructure instead of better models bought themselves a 3 to 5 year window.

[pause]

So the three timelines are: SaaS consolidation takes 12 to 18 months, which is why the sector dropped 40%. Infrastructure moats, like AWS's compliance and ecosystem, last 3 to 5 years, which is why hyperscaler margins are safe. And abstraction layers, like multi-cloud routing tools, last 2 to 3 years before hyperscalers build competing products.

All three are correct. They're just pricing different expiration dates.

---

Let me give you one more example of how this plays out, because it ties everything together.

There's a company called Baseten. They raised $1.5 billion in June 2026. Baseten builds multi-cloud abstraction. That's software that lets you run AI workloads across multiple cloud providers, like AWS, Google Cloud, and Azure, without rewriting code for each one. They grew revenue 1,900% year over year.

Here's why that matters. Baseten exists because enterprises want optionality. If you build your entire AI infrastructure on AWS, you're locked into AWS's pricing, and AWS knows it. If you build on Baseten, you can run the same workload on AWS today, Google Cloud tomorrow, Azure next week, whichever one offers the best price. That optionality saves enterprises millions of dollars and prevents lock-in.

But Baseten's moat has a timer on it. [pause]

In 2 to 3 years, AWS and Azure will build their own multi-cloud routing tools. They'll offer the same abstraction Baseten provides, bundled into their existing cloud services. When that happens, enterprises will use AWS's abstraction tool instead of paying Baseten, because it's easier to use one vendor than two.

Baseten's founders understand this. That's why they're raising $1.5 billion now and spending it to lock in as many enterprise customers as possible before the window closes. The bet is that if they can get 500 large companies using Baseten deeply, integrated into their core infrastructure, with custom configurations and multi-year contracts, those customers won't switch to AWS's tool even when it's available. Because the switching cost will be too high.

Baseten is racing to turn a 2-year moat into a 10-year moat by building switching costs before AWS commoditizes the capability. [pause]

And that's the pattern. Capability, the technical ability to route workloads across clouds, will become commodity in 2 to 3 years. But integration, being deeply embedded in a customer's infrastructure with high switching costs, can last a decade.

---

## ACT 3 — COUNTERARGUMENT

Now, the pushback I'd expect here is this. If integration is the new moat, why can't new entrants just build integration layers from day one? Why does AWS get to charge $4.34 extra per hour forever? Why can't Spheron just get SOC 2 certified, build ecosystem integrations, and undercut AWS on price while matching on integration?

And honestly, it's a fair point. [pause]

Here's why I still think the integration moat holds for 3 to 5 years, but not forever.

Integration takes time to build, but more importantly, it requires customer density. AWS can afford to get SOC 2 certified, HIPAA certified, FedRAMP certified, and dozens of other regulatory approvals because they have thousands of enterprise customers who need those certifications. The audit cost is millions of dollars, but spread across thousands of customers, it's manageable.

Spheron has maybe a few hundred customers. For them, spending $10 million on FedRAMP certification to serve 10 government customers doesn't make economic sense. They'd need to charge each customer $1 million just to break even on the audit.

So the integration moat holds as long as you have customer density and new entrants don't. [pause] But once a new entrant gets to scale, they can start building the same integration layers. That's why I say 3 to 5 years, not forever.

The real question is whether you can build enough switching costs in those 3 to 5 years to keep customers even after competitors catch up on integration. AWS did. They locked in enterprises so deeply that even when Google Cloud matched them on compliance and ecosystem, most companies didn't switch. [pause]

That's the race every company is in right now.

---

## TAKEAWAY

If you take three things from today:

One. [slower] Margin migrated from capability to integration. Vendors selling capability, like specialized AI models or commodity GPUs, are dying. Vendors selling integration, like AWS's compliance frameworks or Harvey's agent orchestration, are surviving. If you're building or investing in anything right now, you need to know which one you're selling.

Two. The moat timelines are different, and that's why three contradictory valuation trends are all correct. SaaS consolidation takes 12 to 18 months, which is why the sector dropped 40%. Infrastructure moats last 3 to 5 years, which is why AWS's margins are safe. Abstraction layers last 2 to 3 years, which is why Baseten raised $1.5 billion but needs to move fast. All three are pricing different expiration dates.

Three. Execution speed became the new moat. Salesforce and HubSpot are re-rating upward because they repriced fast. Baseten is racing to build switching costs before AWS commoditizes multi-cloud routing. Harvey pivoted from capability to integration before frontier models killed their moat. The companies that saw margin migrating and got there first are the ones winning. The companies that waited are getting repriced or acquired.

---

## CLOSE

That's it for this week. If you want to go deeper, the full written piece is at prashant-chandel.org/blog. There's an infographic there that maps out the whole argument visually, showing exactly where the $4.34 AWS markup goes and which moats last versus which expire in 18 months.

If this was useful, share it with one person who'd appreciate it. That's the best way to help the show grow.

See you next Sunday.
