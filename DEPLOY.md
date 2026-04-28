# Calling Cards · Deploy

Live at `cards.sol8um.tech` (or Vercel default URL until DNS is wired).

---

## Hosting model

**Subdomain + path-based cards** on Vercel.

```
cards.sol8um.tech/cielo/        ← CIELO card
cards.sol8um.tech/[next]/       ← future card
cards.sol8um.tech/              ← (optional) landing page listing all cards
```

Why subdomain: keeps the calling-cards repo separate from the marketing sol8um.tech repo. Zero risk to the main site, simpler mental model, faster iteration.

---

## One-time setup (already done if reading this)

### 1. GitHub repo

```bash
cd "E:/calling-cards"
git init -b main
git config user.name "Nihal Choudhary"
git config user.email "misclifebusiness@gmail.com"
git add .
git commit -m "Initial: Calling Cards system + cielo card"

# Create empty GitHub repo via gh CLI
gh repo create sol8um-calling-cards --public --source=. --remote=origin --push
```

### 2. Vercel project

```bash
# From the project root
cd "E:/calling-cards"
vercel --prod
# Pick: scope (sol8um-7719), name (sol8um-calling-cards), framework (Other),
#       root directory (./), build command (empty), output directory (./)
```

After first deploy, link a custom domain in the Vercel dashboard:
- **Settings → Domains → Add** → `cards.sol8um.tech`
- Vercel gives you a CNAME record. Add it in the DNS provider for `sol8um.tech`.
- DNS propagates in ~5 min. Card is live.

---

## Shipping a new card

Every time, after building the card files in `cards/[company]/`:

```bash
cd "E:/calling-cards"
git add cards/[company] cards/[company]/shots
git commit -m "Add [Company] calling card"
git push
```

Vercel auto-deploys within 30 seconds. URL is `cards.sol8um.tech/[company]/`.

---

## Local preview while building

```bash
cd "E:/calling-cards"
python -m http.server 8091
# open http://localhost:8091/cards/[company]/
```

Or via `vercel dev` (closer to production behavior):

```bash
vercel dev
```

---

## Sharing the URL with the founder

Once live, the URL goes in:

1. **Email reply** confirming the call: *"Built a Calling Card for you ahead of our chat — `cards.sol8um.tech/[company]`. Walk through it before we talk if you have a few minutes."*
2. **LinkedIn DM** (same line)
3. **Calendar invite** description (same line)
4. **On the call** — screenshare, walk through the audit and workflows live

The link does the talking. Don't over-explain.

---

## Rollback

If something embarrassing ships:

```bash
# Pull the offending card off the live site fast
cd "E:/calling-cards"
git rm -r cards/[company]
git commit -m "Temporarily remove [Company] card"
git push
```

Vercel reflects in ~30 seconds. When fixed, restore from `git revert` or rebuild and push.

---

## Pre-flight before every push

- [ ] Audit annotations all pixel-aligned with the elements they call out
- [ ] No stale CIELO references in another company's card
- [ ] All 4 workflow demos respond to clicks
- [ ] Email / LinkedIn / WhatsApp / phone all clickable
- [ ] Phone is `+91 9468688354` everywhere
- [ ] No console errors
- [ ] No `localhost:` URLs
- [ ] Page weight under 5 MB total
- [ ] Mobile preview at 375px legible

---

*Domain: `cards.sol8um.tech` · GitHub: `sol8um-client/sol8um-calling-cards` · Vercel: `sol8um-7719/sol8um-calling-cards`*
