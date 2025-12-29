# Documentation for Developer Tools

A comprehensive guide to creating documentation that converts. Learnings from Stripe, and how to make docs a growth engine.

---

## Part 1: Docs Philosophy

### Why Docs Matter More Than You Think

Docs are not just support content. They are:
- Middle-of-funnel marketing
- A key differentiator
- Often the first real product experience
- A growth lever

> "If a developer can pick software that is also open source, it's just better." — But even without open source, great docs = transparency.

### The Radiating Circles of Developer Experience

**Product → Docs → Content → Community**

The further you go through product adoption and market maturity, the more "outside" you need to go to deliver value.

Docs are the second circle. Get them right before investing heavily in content and community.

---

## Part 2: Docs Fundamentals (From Ex-Stripe Head of Docs)

### First Impressions Matter

**What developers see first:**
- Whitespace signals approachability
- Diagrams signal thoroughness
- Code signals practical value

Make it inviting. Show you understand developers.

### The Docs MVP

**Before anything else, nail this:**

The first quickstart experience where a developer:
- Understands what the product is
- Accomplishes something
- All in one 15-30 minute sitting

Don't think about other docs until this works.

### Align Docs with Developer Stages

After the quickstart, structure around developer journey:
1. Getting started
2. Design
3. Build
4. Deploy
5. Manage

This helps developers find what they need based on where they are.

---

## Part 3: Making Docs Convert

### The Signup CTA in Docs Header

**Stripe added "Create Account" to their docs header.**

Results: Significant conversion impact.

**Apollo GraphQL:** 20% signup increase from adding signup CTA to docs.

**Lesson:** Docs visitors are often non-users evaluating your product. Give them an easy path to signup.

### Escape Hatches

People land on wrong pages. Example: "Stripe checkout" search can land on dev-focused or no-code page.

**Solution:** Put a link at the top to redirect to the right page.

"Looking for [other thing]? Go here."

### Navigation That Works

**Key principles:**
- Self-hosted deployment in docs dropdown
- Quickstart prominently accessible
- Integration docs findable
- Search that actually works

---

## Part 4: User Research for Docs

### The Most Impactful Research

**Method:** Get a developer to complete a scenario. Ask them to "think out loud" as they normally would.

This uncovers:
- Where they get stuck
- What language they use
- What they expect vs what they find
- Hidden pain points

### The Internal Test

**Quick version:** Ask your company devs to review a doc.

Questions:
- "What are your takeaways?"
- "What would you do next?"
- "What's confusing?"

See if takeaways align with the doc's goal.

### Look at Search Results

**What people search for reveals:**
- Language they use
- Features they want
- Where they're stuck

Many search in Google for "X {BRAND}" or "X {BRAND} docs" — treat these like internal searches.

---

## Part 5: Docs for AI/LLM Era

### Writing for LLMs

As AI assistants reference docs, structure for machine readability:
- Clear headings
- Explicit code examples
- Structured data formats
- llms.txt files

### Solving AI Engines vs Docs

**From Clerk:** As AI assistants become common, ensure your docs are:
- Easily parseable
- Semantically structured
- Updated frequently
- Machine-accessible

---

## Part 6: Measuring Docs

### Key Metrics

**North Star:** Time to first [X]
- Time to first API call
- Time to first dashboard created
- Time to first integration

**Quality indicator:** Customer satisfaction on doc pages
- 60%+ is good
- Track per-page ratings
- Monitor trends

### Search Analytics

What to track:
- Most common searches
- Zero-result searches
- Search → bounce sequences

Use this to:
- Add missing content
- Fix language mismatches
- Improve navigation

---

## Part 7: Docs Content Types

### The Quickstart

**Purpose:** First success in 15-30 minutes

**Structure:**
1. What you'll build
2. Prerequisites
3. Step-by-step instructions
4. Working result
5. What's next

**Tips:**
- Copy-paste ready code
- Minimal prerequisites
- Clear success criteria
- Path to deeper docs

### Integration Guides

**Purpose:** Show how you work with their stack

**Structure:**
1. What this integration enables
2. Prerequisites
3. Setup steps
4. Configuration
5. Testing
6. Troubleshooting

### API Reference

**Purpose:** Complete technical reference

**Best practices:**
- Consistent format
- Clear request/response examples
- Authentication explained first
- Error codes documented

### Conceptual Guides

**Purpose:** Explain the "why" and "how"

**When needed:**
- Complex architectures
- New paradigms
- Design decisions
- Best practices

---

## Part 8: Visual Elements in Docs

### Architecture Diagrams

**Why they work:**
- Increase visibility in Slack and dark social
- Shareable
- Show you understand the ecosystem
- Help architects sell internally

### Code Snippets

**Best practices:**
- Syntax highlighted
- Copy button
- Language selector
- Real, working examples

### Screenshots and GIFs

**When to use:**
- UI instructions
- Visual feedback confirmation
- Complex sequences

**Tips:**
- Keep updated (outdated screenshots hurt trust)
- Annotate when needed
- Consider screen recording for complex flows

---

## Part 9: Doc CTAs

### Blog Post CTAs in Docs

**The V7 approach:**
- CTAs that don't feel "obviously an ad"
- Not too subtle to miss
- Contextually relevant

### Where to Place CTAs

1. **Header:** Signup/trial
2. **End of articles:** Related content, deeper features
3. **Contextual:** When discussing features that require upgrade
4. **Sidebar:** Persistent but non-intrusive

### CTA Copy That Works

**Do:**
- "Start building"
- "Try it free"
- "See it in action"

**Don't:**
- "Buy now"
- "Contact sales"
- "Request demo" (for early docs)

---

## Part 10: Docs Infrastructure

### Search

**Must haves:**
- Fast results
- Good ranking
- Search suggestions
- Zero-result handling

### Navigation

**Patterns that work:**
- Persistent sidebar
- Breadcrumbs
- Version selector
- Language/framework switcher

### Feedback Loops

- Per-page ratings
- "Was this helpful?"
- Edit on GitHub
- Feedback forms

---

## Quick Reference: Docs Checklist

### Foundation
- [ ] Quickstart that works in 15-30 min
- [ ] Signup CTA in header
- [ ] Escape hatches for wrong landings
- [ ] Working search

### Content
- [ ] Getting started guide
- [ ] Integration guides for key platforms
- [ ] API reference complete
- [ ] Conceptual guides where needed

### Visual
- [ ] Architecture diagrams
- [ ] Code snippets with copy buttons
- [ ] Screenshots current and accurate

### Measurement
- [ ] Time to first X tracked
- [ ] Page satisfaction ratings
- [ ] Search analytics monitored

### AI-Ready
- [ ] Clear structure
- [ ] Machine-parseable format
- [ ] llms.txt considered

---

## Templates

### Quickstart Structure

```markdown
# Getting Started with [Product]

## What You'll Build
[One sentence describing the outcome]

## Prerequisites
- [Requirement 1]
- [Requirement 2]

## Step 1: [Action]
[Instructions]
\`\`\`code
example code
\`\`\`

## Step 2: [Action]
[Continue...]

## Verify It Works
[How to confirm success]

## What's Next
- [Link to deeper topic]
- [Link to advanced guide]
```

### Integration Guide Structure

```markdown
# [Product] + [Integration] Guide

## Overview
[What this integration enables]

## Prerequisites
- [Product account]
- [Integration account]
- [Technical requirements]

## Setup
### Step 1: [Configure Product]
### Step 2: [Configure Integration]
### Step 3: [Connect]

## Configuration
[Available options]

## Testing
[How to verify it works]

## Troubleshooting
[Common issues and solutions]
```

---

## Resources & Further Reading

**Masterclass:**
- [Docs Masterclass with Ex-Stripe Head of Docs (Video)](https://www.youtube.com/watch?v=8b4fh_NY5fc) — Dave Nunez
- [Same Episode on Apple Podcasts](https://podcasts.apple.com/us/podcast/just-when-we-started-to-solve-software-docs-ai-blew/id1505372978?i=1000656918860)
- [Same Episode on Spotify](https://open.spotify.com/episode/2c7suSQTnicAstTSmhKcx1?si=6da860371ed34e6f)

**Conversion Optimization:**
- [Adding Signup CTAs to Docs](https://www.linkedin.com/posts/djnunez_if-you-have-a-developer-focused-product-activity-7264690873928413185-cano) — Dave Nunez
- [How "Create Account" CTA in Docs Header Pushed Conversions for Stripe](https://www.markepear.dev/example/sign-up-in-docs-header)

**AI & Documentation:**
- [Clerk's Approach to AI Engines vs Docs](https://www.linkedin.com/posts/mgonto_clerkcom-just-shipped-one-of-my-fav-activation-activity-7333616478371397633-ntF-)
- [Clerk's AI-Friendly Docs Example](https://clerk.com/docs/quickstarts/nextjs)

**Types of Documentation:**
- [The 4 Types of Technical Documentation](https://nick.groenen.me/posts/the-4-types-of-technical-documentation/)

**Tools:**
- [Scalar](https://scalar.com/) — API documentation generation
- [Mintlify](https://mintlify.com/) — Documentation platform

**Newsletters:**
- [Etel Sverdlov's Newsletter](https://etels.substack.com/) — Ex-DigitalOcean Head of Community
