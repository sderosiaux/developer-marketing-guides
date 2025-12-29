---
number: 134
title: "Two AI tips/prompts for audience research, and a LinkedIn Outreach Playbook"
slug: "134-two-ai-tips-prompts-for-audience-research-and-a-linkedin-outreach-playbook"
url: "https://newslepear.beehiiv.com/p/134-two-ai-tips-prompts-for-audience-research-and-a-linkedin-outreach-playbook"
date: "November 09, 2025"
---



# Developer marketing insights
### 1. Two AI tips/prompts for audience research 
Saw this post and it inspired me to share two thoughts around using AI for dev marketing work. 
[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d94d2cc5-67d7-496e-a37e-84831be99096/image.png)](https://www.linkedin.com/posts/shlomogenchin_i-really-think-perplexity-labs-is-the-most-activity-7389590097504940032-08M0/?utm_source=share&utm_medium=member_ios&rcm=ACoAAA6PPusBHGh3FZIjVWx49BUzJv6Bq6AODbE)
btw Shlomo has some awesome examples of ads/campaigns on his site [https://thecreativemarketer.net/](https://thecreativemarketer.net/)
Anyhow the first tip is exactly what Shlomo shared: **extract testimonials/insights with AI search engines.**
Use Perplexity / ChatGPT to get exact user quotes from Reddit and review platforms. Sometimes you have additional case studies, testimonials, user inputs to signup forms etc. Perplexity is really good for all those research use cases. 
You group it, analyze it, extract the actual wording people use. This informs your positioning/messaging, campaigns, landing pages, ads etc. 
Btw while [interviewing Aditya about marketing to devs on Reddit](https://www.youtube.com/watch?v=vAiccJ8zoiU&utm_source=newslepear.beehiiv.com&utm_medium=referral&utm_campaign=134-two-ai-tips-prompts-for-audience-research-and-a-linkedin-outreach-playbook) I learned about Reddit Answers (feature in beta) that you can use for that too. 
**Another tip/tool that I use a ton is role playing.**
For example, when I create a positioning/messaging doc or a HN launch post with founders I upload the asset (often together with a screenshot of it) and run it through this prompt to get a first line of feedback. 
You can go as deep or as shallow with context you want. Also sometimes I just record context and then tell chat to convert to the prompt like this. 
```
SYSTEM
You are conducting a fast, realistic user test. Role-play as the specified persona. Stay in character: use their knowledge level, tone, and constraints. Be candid, specific, and pragmatic.

USER INPUTS
[PERSONA]
- Role/title: {{e.g., Senior Rust backend engineer}}
- Context/industry/company size: {{e.g., fintech scaleup, ~30 engineers, heavy Postgres/Kafka}}
- Goals & pains: {{e.g., hates YAML/infra toil; needs portability & self-host; latency sensitive}}
- Tools & stack familiarity: {{e.g., Rust (Tokio/Axum), Postgres, SQS, Kubernetes basics}}
- Decision criteria: {{e.g., low lock-in, self-hostable, clear perf, simple DX}}
- Skeptic triggers: {{e.g., vague claims, hidden pricing, runtime magic/macros}}

[CHANNEL / ENTRY POINT]
- Where they discovered it: {{e.g., Hacker News post}}
- What they expect from this surface: {{e.g., quick proof it’s real, code sample, deployment story}}

[TARGET ASSET]
- URL or description: {{e.g., product homepage / landing wireframe}}
- Primary CTA(s): {{e.g., Launch playground, See quickstart}}
- Reading task: {{e.g., scan top-to-bottom once; then decide if I’d try it today}}

[EXTRA MATERIALS]
- Comparable transcript/quotes: {{paste any interview notes or forum thread}}
- Product notes or constraints: {{e.g., not open source yet; AWS-first self-host guide}}
- Example copy or wireframes: {{paste or link}}

[REVIEW GOALS]
- What we need from this review: {{e.g., likes/dislikes, confusions, unanswered Qs, what I’d tell a teammate, go/no-go}}

OUTPUT FORMAT
1) First-impressions (≤6 bullets)
2) Running commentary while scrolling (short notes per section)
3) What I liked (specific)
4) Friction / confusions (specific)
5) Unanswered questions (prioritized)
6) What I remember 10 minutes later (top 3 takeaways)
7) How I’d describe it to a colleague (1–2 sentences, persona voice)
8) Would I try it? Why/why not (score /10)
9) Highest-impact fixes (ranked; crisp copy or UX changes)
10) Risks I’d still worry about (and what would de-risk them)
```

Catches a lot of obvious problems right away. 
If the first run comes out overly optimistic, I like to go a bit more rough on my asset I ask for an Eastern European senior dev who is not in a good mood and saw smth on Hacker News. So far it finds the cracks every time. 
### 2. LinkedIn Outreach Playbook (for dev tools)
I shared a lot of tips and resources about selling to devs [here](https://www.markepear.dev/blog/linkedin-ceo-founder-playbook) and [here](https://www.markepear.dev/blog/selling-to-developers). 
But this guide/webinar from [reo.dev](http://reo.dev) on LinkedIn outreach for dev audiences added a ton of color, examples, and tips I haven’t shared. 
[ Winning DevTool Deals: The Ultimate LinkedIn Outreach Playbook How to book meetings with engineering leaders & CTOs using intent signals www.reo.dev/resources/linkedin-outreach-playbook ![](https://cdn.prod.website-files.com/67f245093fcfae53e5bcbd31/68af0dbdc533155655feefca_Winning%20DevTool%20Deals%20-%20The%20Ultimate%20LinkedIn%20Outreach%20Playbook%20OG%20Image.jpg) ](https://www.reo.dev/resources/linkedin-outreach-playbook)
I suggest that you both watch the video and read the guide as the resources while overlapping are complementary. If 
Takeaways:
  Optimize headline for invite request view (no one reads ‘SDR @ X’).** Use problem/benefit first, not your job title. Bar is low; <2% do a reasonably good job here. 
  Keep two ICP lists:** your main ICP list and a live, in-market subset filtered by real intent (docs consumption depth, “build/deploy” signals, competitor repos, hiring signals etc.). Prioritize in-market list and try to react “as asap as possible” ;)
  Research cohorts (not accounts).** Segment by **industry** , **use case** , **company size**. Write one tight message per cohort. You want relevance. They go deep into this in the guide. 
  Multi-thread on purpose. **Top-down:** target 3–5 buyers (VP/Dir/CTO) on LinkedIn. 
    Bottom-up:** nurture active devs with useful content and make them internal champions. Use the most active dev’s network to map buyers. Don’t outreach to devs / ICs though. Just the buyers / decision makers (sometimes senior devs). 
  Blank connection requests:** 300 characters isn’t enough to be useful. They saw higher accepts with no note (same experience for me). Withdraw stale requests after ~30 days to protect your ratio. 
  Don’t be creepy with signals.** Use activity to **time** outreach, not to creep ppl out with the “just saw you on our pricing” kind of thing. 
  Metrics that matter.** Daily/weekly: request volume, accept rate, positive responses per accept, meetings per positive. Improve the biggest leak first (usually positive responses).
  Follow-ups are key.** Reo shipped a 5-minute personalized one-pager/microsite (built with Lovable): their logo, their likely use case, quick demo, relevant proof. Share case studies by **category** and “how it works” explainers. [An example of this here. ](https://langchain-reodev-one-pager.lovable.app/)
  1st mesage that worked for Reo .** Heavy on the value prop, specific, clear.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/36140624-94b7-4311-bce5-eafa4e306e3f/image.png)
  Automate after you see it work manually.** This is something that ppl get very wrong all across marketing/growth/sales. Most of the time, you want to start manual, find something that works, scale it up with automations and process. You scale something that doesn’t work it will just not work at scale. But when you do automate there are lots of tools (and they list out what they use/see people use). 

Strong [recommendation to read/watch](https://www.reo.dev/resources/linkedin-outreach-playbook). There are just tons of examples, links to case studies and deeper deep-dives in there. Just a really good piece of content.
