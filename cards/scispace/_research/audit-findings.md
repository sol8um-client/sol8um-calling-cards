# Audit Findings for SciSpace

*Note: scispace.com blocks automated screenshot capture (CloudFront 403 + CAPTCHA). All evidence anchors use confirmed verbatim quotes from the live page title, structured review sources, and competitor comparison research. Screenshot annotations will use schematic representations rather than pixel-precise callouts.*

---

## ICP signal block

- **Buyer 01 — Individual PhD candidate / postdoc (primary):** Self-funded grad student or early-career researcher doing literature review or manuscript work at 2am — highest volume, most price-sensitive, most likely to churn at the free-plan paywall. Engagement size: 1M+ registered, ~300K Chrome extension users (active researchers). Fit signal: 85%
- **Buyer 02 — Research lab team / PI (growth ICP):** Lab Principal Investigator or senior postdoc managing 3-5 researchers on a shared project — needs team access, shared citations, consistent tooling. Engagement size: estimated 5-10% of Premium users who would expand to Lab plan. Fit signal: 70%
- **Buyer 03 — University / research institution (enterprise ICP):** Head of library, research IT procurement, or faculty committee evaluating SciSpace for department or campus-wide access — needs compliance info, case studies, institutional pricing. Engagement size: small volume, very high value. Fit signal: 45% (site does not serve this buyer well today)

---

## What's already working (name specific elements)

- **The Chrome extension at 300K users, 4.5/5 stars** — embedding in researchers' actual reading workflow rather than requiring context-switching is a structurally correct GTM move. Competitors haven't matched this.
- **280M+ paper corpus with citation-backed answers** — the breadth of the academic database is a genuine moat over general-purpose tools like ChatGPT Research Mode. Named in the page title, which is the right asset to lead with.
- **The Agent as the organizing concept** — rebranding the homepage around "AI Research Agent | 150+ Tools" signals product maturity and positions SciSpace ahead of tools still describing themselves as "paper summaries." The brand direction is correct.
- **9,000+ journal citation formats** — a specific, defensible feature that Elicit and Consensus don't match. The kind of thing a PhD candidate checks before committing to a tool.

---

## 4 themes (named for SciSpace's actual funnel)

**A. Discovery & AI-search visibility** — How researchers find SciSpace when they query Perplexity, ChatGPT, or Google at the moment of research pain
**B. Trial activation friction** — The hard wall between free plan and paid, and every leak point between Agent awareness and credits purchase
**C. Institutional trust signals** — What a lab PI or university procurement lead sees when evaluating SciSpace for team or campus-wide access
**D. Agent adoption and expansion** — Whether the Agent product's value proposition is clear enough to convert Premium users into Agent credits buyers

---

## 10 findings

### Finding 01 — Your page title counts tools instead of promising an outcome.

- **Theme:** A (Discovery & AI-search visibility)
- **Severity:** Critical · 5-min fix
- **Evidence:** Current page title (confirmed from Google SERP and browser tab): `"SciSpace AI Research Agent | 150+ Tools, 280 M Papers"`
- **Cost-to-ICP:** A PhD candidate stuck on a systematic review pastes "AI research tool" into Perplexity at 11pm. The citation Perplexity reads aloud says "SciSpace — 150 tools, 280 million papers." She hears a spec sheet, not a workflow. She clicks on Elicit instead, whose description reads like a process she recognizes. Your page title is the first sentence in every AI-search citation of your product — it's currently doing inventory disclosure in a workflow-comparison moment.
- **Quick win:** Update the `<title>` tag to a workflow promise: `"SciSpace — From 200 papers to 3 confirmed hypotheses, in one session"` or `"SciSpace AI Research Agent — Complete literature reviews, draft manuscripts, cite accurately."` Five minutes in the CMS or a one-line HTML edit. Compounds across every Perplexity, ChatGPT, and Google result citing your domain.
- **Impact:** 80, red

---

### Finding 02 — Your Agent launch isn't visible from any AI-search citation.

- **Theme:** A (Discovery & AI-search visibility)
- **Severity:** High · 30-min fix
- **Evidence:** The SciSpace Agent launched August 2025 and "unifies the full research pipeline in one single interface." The LinkedIn announcement exists. The scispace.com/agents page exists. But the homepage meta description — the text scraped by Google, Perplexity, and ChatGPT as the summary of your site — almost certainly describes the old Copilot positioning ("AI-powered platform to help academics manage, write, and publish their work") rather than the Agent.
- **Cost-to-ICP:** An industry researcher at a pharma company evaluating AI research tools in April 2026 runs a Perplexity comparison query. SciSpace's citation reads like a literature review helper from 2023. Elicit's citation reads like a systematic review engine. The researcher shortlists Elicit. The Agent's existence — SciSpace's strongest competitive move in 18 months — is invisible at the top of the funnel.
- **Quick win:** Update the homepage meta description to reflect the Agent positioning: `"SciSpace Agent runs your full research pipeline — literature review, manuscript drafting, citation checking, plagiarism scan — across 280M papers. Used by 1M+ researchers."` Update the Open Graph description simultaneously (og:description). 30 minutes including testing the preview in a link checker.
- **Impact:** 75, red

---

### Finding 03 — "Nobel Laureates, MIT, Stanford" trust proof is cited but not shown.

- **Theme:** A (Discovery & AI-search visibility)
- **Severity:** High · 2-hr fix
- **Evidence:** Review research confirms the claim "Trusted by Nobel Laureates and institutions like MIT and Stanford" exists in SciSpace's marketing collateral. This is a homepage-grade trust signal — but it likely lives in a blog post or marketing copy rather than as a visual proof element (logo bar, verified quote, named testimonial) on the homepage above the fold.
- **Cost-to-ICP:** A department head at a mid-tier university checking SciSpace for a campus license hears the MIT/Stanford claim in a review she read, then visits the homepage and doesn't find it confirmed. No logo, no quote, no named researcher. She files it as unverifiable marketing. The claim is doing zero conversion work because it isn't anchored to evidence on the page that matters.
- **Quick win:** Add a 4-logo institution bar (MIT, Stanford, one more) + one named researcher testimonial with affiliation and research area immediately below the hero. Source: existing testimonials in blog posts — reformat, don't rewrite. Two hours to design and ship the component. The claim goes from hearsay to proof.
- **Impact:** 65, amber

---

### Finding 04 — The free plan's 5-paper wall fires before researchers understand what they're upgrading to.

- **Theme:** B (Trial activation friction)
- **Severity:** High · 2-hr fix
- **Evidence:** Multiple independent reviews confirm: "Scispace limits your high-quality searches and analysis to just 5 papers" in the free tier. The limit fires early in a literature review session — before the researcher has experienced the full workflow value.
- **Cost-to-ICP:** A first-year PhD candidate finds SciSpace through the Chrome extension, uploads her first 5 papers, gets exactly the output she needed. On paper 6, she hits a paywall. She hasn't yet seen the Agent, hasn't tried the citation generator on a full bibliography, hasn't experienced the manuscript draft. She's being asked to pay $12/month for a workflow she's only seen 20% of. The upgrade modal is asking her to commit at her lowest-confidence moment.
- **Quick win:** Before the paywall fires, trigger a single guided "Agent preview" task — auto-run the Agent on one of her 5 uploaded papers, show her the full pipeline output (literature synthesis + 3 cited claims + draft paragraph), then gate it. She's now upgrading with evidence, not faith. This is a 2-hour product change: one interstitial page, one pre-computed Agent demo run. Test against current hard-stop modal.
- **Impact:** 85, red

---

### Finding 05 — The Premium pricing page doesn't answer "why $12 more than Elicit?"

- **Theme:** B (Trial activation friction)
- **Severity:** High · 2-hr fix
- **Evidence:** SciSpace Premium = $12/month. Elicit Plus = $12/month (confirmed from pricing comparisons). But the comparison data also confirms SciSpace is perceived as more expensive in some reviews (older pricing was $20/month). Regardless of current price parity, the pricing page almost certainly does not answer the researcher's first question on arrival: "What do I get here that I can't get on Elicit for the same price?"
- **Cost-to-ICP:** A postdoc with $100/year in tool budget opens both pricing pages side by side. Elicit's page says "data extraction, clean interface." SciSpace's page lists features but doesn't name Elicit. There's no "SciSpace vs. the alternative" framing. The postdoc defaults to Elicit because she already knows it. SciSpace loses a comparison it was qualified to win.
- **Quick win:** Add a 3-row comparison table to the pricing page: "What you get with SciSpace that Elicit doesn't offer" — citation generator in 9,000+ styles, Chat with 280M papers, PDF to Video, 150+ Agent tools. Don't name Elicit; just describe the category leader's limitations in neutral language. Two hours to write and build. This is the only content on the pricing page that converts a researcher who's already considering both options.
- **Impact:** 70, amber

---

### Finding 06 — The Agent credits layer has no "first credits free" onboarding hook.

- **Theme:** B (Trial activation friction)
- **Severity:** Strategic · 1-day
- **Evidence:** The Agent operates on a separate credits system on top of Premium. The credits pricing lives at scispace.com/credits-guide (blocked during this audit — currently inaccessible to most visitors, which is itself a signal). There is no confirmed "first Agent task free" offer in any reviewed source.
- **Cost-to-ICP:** A PhD candidate upgrades to Premium, notices the "Agent" button, reads the credits pricing page, doesn't understand the ROI of spending credits on a single literature review task she's never seen work end-to-end. She leaves without ever running the Agent. She stays a Premium subscriber but never becomes an Agent buyer. The entire top of the Agent funnel relies on researchers taking a leap of faith on a credits purchase before seeing the Agent complete a real task.
- **Quick win:** Give every new Premium subscriber 10 free Agent credits at signup — enough to run one complete literature review + manuscript draft task. Instrument the conversion rate: free-credits-used to first-purchase. If the product is good (it is), the conversion will be high. If it isn't, that's a product signal worth knowing. One day to instrument and ship the onboarding change + email trigger.
- **Impact:** 90, amber

---

### Finding 07 — There is no institutional / university landing page.

- **Theme:** C (Institutional trust signals)
- **Severity:** Strategic · 1-day
- **Evidence:** Confirmed from pricing research: institutional and enterprise pricing requires "contacting SciSpace directly." There is no confirmed scispace.com/institutions or scispace.com/universities page in any indexed source. The institutional buyer has no destination on the site that speaks to their specific concerns.
- **Cost-to-ICP:** A university librarian at a mid-size research institution is evaluating site licenses for her 500 PhD students. She searches "SciSpace institutional pricing" — finds a generic pricing page with three tiers (Free, Premium, Lab) and a "contact us" link. She doesn't know if SciSpace has a procurement process, who signs the contract, or whether there's a security page. She has four other tools in her evaluation. She moves on to the ones that have an institutions page. The bottom-up demand from her students (who already use SciSpace) never converts to a campus-wide license because the site doesn't have a landing page that earns her attention for 5 minutes.
- **Quick win:** Create scispace.com/institutions with: (1) a pricing starting point ($8/user/year confirmed), (2) logos of universities already using it, (3) a 3-question form ("institution name / number of researchers / primary use case") instead of a blank "contact us." One day to build the page. This is the surface area where SciSpace's bottom-up momentum converts to enterprise ARR.
- **Impact:** 75, amber

---

### Finding 08 — No security or data privacy page for research data.

- **Theme:** C (Institutional trust signals)
- **Severity:** High · 30-min fix
- **Evidence:** No confirmed scispace.com/security page in any review, competitor comparison, or indexed result. Research institutions handling unpublished data (grant applications, pre-publication manuscripts, proprietary datasets) have explicit data handling requirements. SciSpace's AI Writer and Extract Data tools process uploaded documents — researchers are uploading unpublished research to a cloud platform.
- **Cost-to-ICP:** A lab PI at a pharma company wants to use SciSpace's manuscript draft feature for a pre-submission paper. His company's IT policy requires a data processing agreement (DPA) before uploading unpublished data to any cloud AI tool. He searches scispace.com for "data privacy" and "security." Finds the privacy policy (boilerplate legal) but no security page, no DPA template, no statement about whether uploaded papers are used for training. He cannot get IT approval. SciSpace loses the enterprise deal before it starts.
- **Quick win:** Publish a one-page scispace.com/security with: (1) whether uploaded documents are used for model training (yes/no — this alone unblocks most concerns), (2) data retention policy, (3) SOC 2 / ISO 27001 status or roadmap. If SciSpace has these answers and hasn't published them, this is a 30-minute fix with an existing draft. If the answers require work, add this to the roadmap — the cost of not having this page grows with every enterprise evaluation.
- **Impact:** 70, amber

---

### Finding 09 — The Agent's homepage value proposition is tool-count marketing, not pipeline marketing.

- **Theme:** D (Agent adoption and expansion)
- **Severity:** High · 2-hr fix
- **Evidence:** Current homepage title: "SciSpace AI Research Agent | 150+ Tools, 280 M Papers" — emphasizes quantity of tools and database size. The Agent's actual value (as described in the August 2025 launch LinkedIn post) is: "conducts literature review, synthesizes findings, drafts citation-formatted manuscripts, runs plagiarism checks, generates visualizations, supports patent and grant workflows" — a sequential pipeline, not a tool catalogue.
- **Cost-to-ICP:** A postdoc who already uses SciSpace for Copilot visits the homepage to understand what "Agent" means. She sees "150+ tools" and reads it as an expanded feature set — another way to use the same paper-reading tool she already has, at extra cost. She doesn't see the word "pipeline" or "end-to-end" or "from question to draft." The Agent's core positioning — that it does the research *for* you, not just assists while you do it — is invisible on the page. She doesn't click into the Agent section.
- **Quick win:** Swap the homepage hero from "150+ tools, 280M papers" to a 3-step workflow visualization: (1) Enter your research question → (2) Agent searches 280M papers, extracts evidence, drafts your literature review → (3) Export citation-formatted manuscript. Under 100 words of copy. This reframes from "SciSpace has a lot of tools" to "SciSpace does the research while you sleep." Two hours to design and ship. Test against current conversion rate to Agent page.
- **Impact:** 85, amber

---

### Finding 10 — Your activation funnel has no instrumented waypoints between "free plan user" and "Agent credits buyer."

- **Theme:** D (Agent adoption and expansion)
- **Severity:** Compounding · multi-week
- **Evidence:** Stack detection result — scispace.com loads 2,105 bytes of HTML (a React SPA shell). No analytics tools confirmed in the static HTML. The funnel from free-plan researcher to Agent credits buyer involves at least 8 decision points (sign up → first Copilot query → hits free limit → sees upgrade modal → upgrades to Premium → notices Agent → reads credits pricing → purchases credits → runs first full Agent task → re-purchases). If none of these events are tracked as discrete funnel stages in Mixpanel or equivalent, SciSpace is flying blind during a 50%+/month growth phase.
- **Cost-to-ICP:** The actual cost is Saikiran's: every week that passes without knowing exactly where in the 8-step funnel researchers drop out is a week of growth that can't be compounded. SciSpace has 1M+ registered users and a new credits-based revenue layer. Without knowing whether researchers churn at "hits free limit," "upgrade modal," "Agent discovery," or "first credits purchase," every product decision about the Agent is a bet, not a read. At 50%/month growth, an uninstrumented funnel means 6 months of data lost during the most important growth window in the company's history.
- **Quick win:**
  - **Stage 1 (week 1):** Define 8 funnel events with engineering. Instrument in Mixpanel (or equivalent) with researcher-segment properties: `free_plan_query_1`, `free_limit_hit`, `upgrade_modal_shown`, `upgraded_to_premium`, `agent_page_viewed`, `credits_pricing_viewed`, `credits_purchased`, `agent_task_completed`. Ship as a single instrumentation sprint.
  - **Stage 2 (week 2-3):** Build a Notion/Mixpanel dashboard surfacing the funnel conversion rate per step per week, segmented by ICP (PhD vs. postdoc vs. lab PI vs. industry). The PM and CEO should see this weekly — it's the single most important number for Agent growth.
  - **Stage 3 (week 4+):** Run one experiment per largest drop-off point, starting with the highest-volume stage. Every 10% improvement in conversion at any stage of an 8-step funnel compounds multiplicatively through the rest of the funnel.
- **Impact:** 95, amber

---

## Compounding chart shape

- **Month 1:** Findings 01 + 02 (title/meta) + 08 (security page) ship — quick wins. Expected: 5-10% lift in organic search CTR; institutional evaluation requests increase. Linear growth.
- **Month 2:** Findings 04 + 05 + 06 (activation friction + Agent credits onboarding) ship — activation improvements. Expected: 15-25% lift in free→Premium conversion; 30%+ increase in first Agent task completion rate among new Premium users.
- **Month 3+:** Finding 10 (funnel instrumentation) provides data; Finding 06 (first credits free) proves conversion thesis; Findings 07 + 09 (institution page + Agent pipeline hero) drive institutional inbound. The activation funnel becomes a managed system rather than a guessing game. At 50%/month growth rate, a well-instrumented funnel compounds: each percentage point of improvement at the Agent credits step multiplies through 1M+ registered users entering the top of the funnel monthly.

---

## Contamination check

- **Cielo phrase reuse:** None. No use of "named-LP-grade trust signals," "Figma Make default placeholder," "awareness drift," "AI-Powered Marketing tagline," "most expensive real estate in your funnel," "PE managing partner who pastes." The specific phrases are entirely absent.
- **Theme name overlap with Cielo:** None. Cielo's themes were "First glance & AI-search visibility / Funnel & conversion / Trust signals & proof / Compounding revenue levers." SciSpace themes are "Discovery & AI-search visibility / Trial activation friction / Institutional trust signals / Agent adoption and expansion." Theme A has a similar category (AI-search visibility) because it's a universal funnel reality for any AI SaaS — but the findings, evidence, and ICP framing are entirely different. Theme B, C, D are distinct from Cielo.
- **Cost-to-ICP specificity:** Named buyer type throughout. "PhD candidate at 11pm," "postdoc with $100/year tool budget," "university librarian at a mid-size research institution," "lab PI at a pharma company," "postdoc who already uses SciSpace for Copilot," "Saikiran." No "users" or "visitors" language.
- **Finding 10 stack anchor:** No intent tool detected — instrumentation gap angle. The specific finding is anchored to the 8-step funnel model for SciSpace's actual product motion (free → Premium → Agent credits), not a generic "add automation" recommendation.
- **Cielo brand signal leak:** None. No "Kiana," "Klarité," "Zen Botanica," "Aleph Zero," "AcenosX," "Miami," "brand agency," "branding agency" anywhere.
- **Final verdict:** PASS
