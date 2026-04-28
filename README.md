# Calling Cards

> *Most candidates send a resume. A Calling Card sends a working day-1 plan.*

A standalone system for building custom pre-application deliverables for high-leverage roles where the founder is the buyer. Each card is a single shareable URL combining:

1. **A surgical audit of the company's website**, framed in their ICP's language
2. **Four interactive workflow demos** showing how their day would actually run
3. **A personal narrative** mapping past experience to their portfolio + first-30-days roadmap

Built in 36 hours per company. The CIELO Agency card (`cards/cielo`) is the reference instance shipped on 2026-04-28.

---

## How to use this

You're the user. I'm Claude. You give me four URLs (see `INTAKE.md`). I do everything else.

```
COMPANY URL:        https://...
JD URL:             https://...
FOUNDER LINKEDIN:   https://...
CALL DATE:          YYYY-MM-DD
```

I research, write the 10 audit findings, customize the 4 workflow demos with their context, generate mock data, build the screenshots with annotations, and ship to `cards.sol8um.tech/[company]`. You review and send the URL.

---

## Project structure

```
calling-cards/
├── README.md              ← this file (system overview)
├── INTAKE.md              ← what you give me to start
├── DEPLOY.md              ← git + Vercel + custom domain
├── styles.css             ← shared brand system — DO NOT FORK PER CARD
├── _automation/           ← scripts I run during research
│   ├── capture_site.py    ← Microlink screenshots
│   ├── sample_layout.py   ← pixel-sample screenshots for annotation positions
│   └── detect_stack.py    ← curl the company HTML for analytics/CRM tools
├── _template/             ← clean copy of the card structure (no company yet)
└── cards/
    └── cielo/             ← reference card · CIELO Agency / Kiana Blücher
        ├── index.html
        ├── audit.html
        ├── morning-brief.html
        ├── email-triage.html
        ├── pre-meeting.html
        ├── reflection.html
        └── shots/
```

`styles.css` lives at the root and every card pulls from `../../styles.css`. One brand system, n cards.

---

## Visual system

White background, pure black ink, hairline borders. Premium minimalist that signals brand-design-savvy without being precious about it.

| | Value |
|---|---|
| Background | `#FFFFFF` |
| Primary ink | `#0A0A0A` |
| Soft ink | `#525252` |
| Muted | `#8A8A8A` |
| Hairline | `#E5E5E5` |
| Soft surface | `#FAFAFA` |
| Accent green | `#16A34A` |
| Accent red | `#DC2626` |
| Accent amber | `#D97706` |
| Accent blue | `#2563EB` |
| WhatsApp green | `#25D366` |

| | Font |
|---|---|
| Headings + body | Rethink Sans (400 / 500 / 600 / 700) |
| Italic accents | Instrument Serif Italic |
| Mono labels | Geist Mono |

**Component vocabulary** — these stay fixed across every card. New components only with intent:

- Pulse-dot eyebrow · Page title with serif italic accent · KPI grid · Marquee proof bar · Day arc SVG · Workflow cards (4-up) · VA-vs-me block · Founder note with N avatar · Roadmap timeline · Industry overlap grid · On-the-call agenda · How-this-was-built ribbon · Audit findings (severity tag, screenshot frame, annotated callouts, impact bar) · Compounding chart · Calm pill · Toast notification · Maker's mark (serif italic N)

---

## What stays the same vs. what changes per card

### Fixed (system DNA)
- Visual theme + typography
- Page structure: Overview / Audit / 4 Workflows
- The 4 workflow concepts: Morning Brief, Email Triage, Pre-Meeting Brief, Reflection Layer
- "VA-vs-me" framing
- Vipassana / awareness thesis
- "PM who builds" positioning
- Marquee with track-record metrics
- Maker's mark (serif italic "N")
- Closing graceful line ("the audit is yours either way")

### Customized (per company)
- Hero copy + page subhead (mentions ICP/industry)
- 10 audit findings (freshly researched against their actual site)
- Workflow demo mock data (their named clients, their meeting types, their inbox patterns)
- Industry overlap grid (mapping past roles to their client verticals)
- Pre-meeting sample uses their actual prospect type
- Audit screenshots come from their live site, with annotations pixel-aligned to the actual UI
- 30-day roadmap reflects their JD scope

---

## Why a separate project (vs. nested under JOB Hunty or Sol8um)

This is reused across applications. Keeping it in JOB Hunty would conflate per-application work with system-level work. Keeping it in Sol8um.tech would conflate Nihal's company with his job-search tool. Standalone is correct.

It does *pull* from both:
- **JOB Hunty** — resume, candidate profile, application playbook, role/metric history
- **Sol8um.tech** — automation patterns, brand voice, the deploy domain (`cards.sol8um.tech`)

---

## Reserved card slugs

```
cielo  · Kiana Blücher / CIELO Agency  · DELIVERED 2026-04-28
```

When a new card is built, append below.

---

## Quality bar before shipping any card

- [ ] Every audit annotation overlays the actual UI element (verified at 1280px+)
- [ ] All four workflows fully interactive — every button does something visible
- [ ] No console errors on any page
- [ ] Email + LinkedIn + WhatsApp + phone clickable in the footer
- [ ] No em dashes (—) anywhere
- [ ] No AI-stiff phrases (synergy, leverage, robust, etc.)
- [ ] Page weight under 5 MB total
- [ ] Loads under 2 seconds on a cold connection
- [ ] Mobile preview at 375px still legible

If any fail, do not send.

---

*Built by Nihal Choudhary · sol8um.tech · misclifebusiness@gmail.com*
