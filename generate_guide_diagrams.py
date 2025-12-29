#!/usr/bin/env python3
"""
Generate diagrams for developer marketing guides and insert them into articles.

This script:
1. Generates images using Gemini (with OpenAI fallback)
2. Saves them to guides/images/
3. Inserts image references into the correct positions in each guide

Usage:
    python generate_guide_diagrams.py              # Generate all diagrams
    python generate_guide_diagrams.py --guide 01   # Generate for specific guide
    python generate_guide_diagrams.py --dry-run    # Show what would be generated
    python generate_guide_diagrams.py --insert-only # Only insert refs (skip generation)
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Universal style requirements appended to all prompts
STYLE_REQUIREMENTS = (
    "Style: Clean vector/flat design, tech illustration aesthetic. "
    "NO photorealistic imagery, NO people's faces, NO cinematic scenes. "
    "White or light background, professional blue/gray/teal colors, clean sans-serif typography. "
    "NO watermarks, NO attribution text, NO signatures, NO 'infographic by' text, NO credits, NO title text in the image."
)

# Base paths
SCRIPT_DIR = Path(__file__).parent
GUIDES_DIR = SCRIPT_DIR / "guides"
IMAGES_DIR = GUIDES_DIR / "images"

# All diagram definitions: (guide_number, diagram_id, prompt, insert_after_heading)
# Headings must match EXACTLY what's in each guide file
DIAGRAMS = [
    # 01 - Website & Landing Pages (uses "Level" headings)
    (
        "01",
        "homepage-architecture",
        """Developer tool homepage architecture diagram showing:
- Navigation bar at top with: Logo, Product dropdown, Docs link, Pricing link, Login/Signup CTAs
- Hero section with: Headline, subheadline, primary CTA button, code snippet preview
- Proof section below with: company logos bar, "Trusted by X developers" text
- Below that: 3-column feature grid with icons
- Use case tabs section
- Testimonial cards
- Footer with resource links
Layout as vertical wireframe with labeled sections and arrows showing user flow""",
        "## Level 2: Header & Value Proposition",
    ),
    (
        "01",
        "developer-trust-ladder",
        """Trust ladder diagram showing 5 ascending steps of developer trust:
Step 1 (bottom): "Anonymous Visit" - icon: eye
Step 2: "Docs/Tutorial Read" - icon: book
Step 3: "Free Trial/Signup" - icon: user-plus
Step 4: "Active Usage" - icon: code
Step 5 (top): "Paid/Advocate" - icon: star

Left side arrow pointing up labeled "Trust Increases"
Right side shows what unlocks each level:
- "Clear value prop" → Step 2
- "Easy quickstart" → Step 3
- "Aha moment" → Step 4
- "Team features" → Step 5""",
        "## Level 4: CTAs & Conversion",
    ),
    # 02 - Hacker News & Product Hunt
    (
        "02",
        "hn-post-anatomy",
        """Anatomy of a successful Hacker News post, showing a sample post with labeled callouts:

Main post box:
- Title area with callout: "No marketing speak, technical benefit"
- Points counter: "100+ points = front page"
- Submitter name: "Personal account > company"
- Time: "9-10am EST optimal"

Below, comment section with callouts:
- Founder comment: "Be present, answer everything"
- Technical question: "Opportunity to show depth"
- Criticism: "Acknowledge, don't defend"

Side panel showing "HN Etiquette":
- "Don't ask for upvotes"
- "Don't use company accounts"
- "Be genuinely helpful"
- "Share story, not pitch" """,
        "## Part 1: Hacker News Fundamentals",
    ),
    (
        "02",
        "launch-timeline",
        """Product Hunt launch timeline showing a horizontal timeline:

BEFORE (left section):
-4 weeks: "Build hunter relationships, prepare assets"
-2 weeks: "Teaser on social, inform supporters"
-1 week: "Final asset review, schedule posts"
-1 day: "Notify community, prepare team"

LAUNCH DAY (center, highlighted):
12:01 AM PT: "Go live"
Morning: "First comments, team engagement"
Afternoon: "Respond to all, share updates"
Evening: "Final push, thank supporters"

AFTER (right section):
+1 day: "Share results, thank community"
+1 week: "Follow up with contacts"
+1 month: "Case study from launch"

Icons at each stage showing relevant activity""",
        "## Part 6: Product Hunt Launch",
    ),
    # 03 - Paid Advertising
    (
        "03",
        "channel-selection-matrix",
        """2x2 matrix for paid channel selection:

X-axis: "Intent Level" (Low → High)
Y-axis: "Targeting Precision" (Low → High)

Quadrants with channels:
- Top-Right (High Intent + High Precision): Google Search Ads, direct keyword targeting
- Top-Left (Low Intent + High Precision): LinkedIn Ads (job titles, skills)
- Bottom-Right (High Intent + Low Precision): Reddit Ads (subreddit targeting)
- Bottom-Left (Low Intent + Low Precision): Display/Banner ads

Annotations:
- Arrow pointing to top-right: "Start here for dev tools"
- Note on LinkedIn: "Good for enterprise, expensive"
- Note on Reddit: "Authentic only, no marketing speak" """,
        "## Part 2: Channel Selection Framework",
    ),
    (
        "03",
        "retargeting-funnel",
        """Retargeting funnel diagram showing visitor journey:

Top of funnel (widest):
"All Website Visitors" - pool icon

First filter:
"Docs Visitors" - subset, book icon
→ Retarget with: "Tutorial content, quickstart"

Second filter:
"Pricing Page Visitors" - subset, dollar icon
→ Retarget with: "Case studies, ROI content"

Third filter:
"Signup Abandoned" - subset, form icon
→ Retarget with: "Free trial reminder, limited offer"

Bottom (narrowest):
"Trial Users" - active users icon
→ Retarget with: "Feature highlights, upgrade prompts"

Side note: "Each stage = different ad creative and message" """,
        "## Part 8: Retargeting",
    ),
    # 04 - Pricing & Positioning
    (
        "04",
        "positioning-stack",
        """Positioning hierarchy pyramid with 4 layers:

Top layer (smallest): "TAGLINE"
- Example: "Ship 10x faster"
- Note: "Memorable, aspirational"

Second layer: "VALUE PROPOSITION"
- Example: "The API platform that grows with you"
- Note: "Benefit-focused"

Third layer: "POSITIONING STATEMENT"
- Example: "For teams who need X without Y"
- Note: "Who, what, why different"

Bottom layer (largest): "MESSAGING PILLARS"
- 3 boxes: "Speed", "Reliability", "Developer Experience"
- Note: "Proof points and features"

Arrow on left showing "Specificity increases" going down""",
        "## Part 1: Positioning Fundamentals",
    ),
    (
        "04",
        "gtm-framework",
        """1-2-3 GTM Framework visualization:

Three horizontal lanes labeled:

MOTION 1 - FREE (top lane, lighter shade):
- Icon: Single developer
- Focus: "Individual productivity"
- Metric: "Adoption, DAU"
- Trigger: "Signup, first API call"

MOTION 2 - SELF-SERVE (middle lane):
- Icon: Small team (3 people)
- Focus: "Team collaboration"
- Metric: "MRR, team size"
- Trigger: "Invite teammate, hit limits"

MOTION 3 - ENTERPRISE (bottom lane, darker):
- Icon: Building/organization
- Focus: "Compliance, scale, control"
- Metric: "ACV, expansion"
- Trigger: "SSO request, security review"

Arrows showing progression between lanes
Right side: "Value prop changes at each level" """,
        "## Part 5: Pricing Models for Dev Tools",
    ),
    # 05 - Documentation
    (
        "05",
        "docs-radiating-circles",
        """Radiating circles showing documentation priorities:

Center circle (smallest, darkest): "QUICKSTART"
- Note: "Copy-paste to Hello World"

Second ring: "API REFERENCE"
- Note: "Complete, searchable"

Third ring: "TUTORIALS"
- Note: "Common use cases"

Fourth ring: "GUIDES"
- Note: "Conceptual understanding"

Outer ring (largest, lightest): "ADVANCED"
- Note: "Edge cases, architecture"

Arrows radiating outward labeled "Developer Journey"
Side annotation: "Start from center, expand as needed" """,
        "## Part 2: Docs Fundamentals (From Ex-Stripe Head of Docs)",
    ),
    (
        "05",
        "docs-content-types",
        """Four-quadrant diagram of documentation types (Divio system):

X-axis: "Practical" ←→ "Theoretical"
Y-axis: "Learning" ↑ ↓ "Working"

Top-Left: TUTORIALS
- "Learning + Practical"
- Icon: graduation cap
- "Step-by-step lessons"

Top-Right: EXPLANATION
- "Learning + Theoretical"
- Icon: lightbulb
- "Understanding concepts"

Bottom-Left: HOW-TO GUIDES
- "Working + Practical"
- Icon: wrench
- "Solve specific problems"

Bottom-Right: REFERENCE
- "Working + Theoretical"
- Icon: book
- "Technical descriptions"

Center note: "Each type serves different need" """,
        "## Part 7: Docs Content Types",
    ),
    # 06 - Content Marketing
    (
        "06",
        "content-maturity-pyramid",
        """Content maturity pyramid showing progression:

Level 1 (base, widest):
"DOCS + CHANGELOG"
- Checklist: API ref, quickstart, release notes
- Stage: "Foundation"

Level 2:
"TUTORIALS + USE CASES"
- Checklist: How-tos, integration guides, examples
- Stage: "Enabling"

Level 3:
"THOUGHT LEADERSHIP"
- Checklist: Technical blogs, architecture posts
- Stage: "Authority"

Level 4:
"COMMUNITY CONTENT"
- Checklist: Guest posts, podcasts, conference talks
- Stage: "Amplification"

Level 5 (top, smallest):
"RESEARCH + REPORTS"
- Checklist: Benchmarks, state-of-X reports
- Stage: "Industry Voice"

Arrow on side: "Build each level before next" """,
        "## Part 2: Content Types That Work",
    ),
    (
        "06",
        "content-repurposing-flow",
        """Content repurposing flowchart:

Start: "PILLAR CONTENT" (large box)
- Example: "Technical deep-dive blog post"

Branches into 6 derivative formats:

→ "Twitter Thread"
  - "Key points as thread"

→ "LinkedIn Post"
  - "Summary + insight"

→ "YouTube Video"
  - "Visual walkthrough"

→ "Newsletter Section"
  - "Curated highlight"

→ "Podcast Topic"
  - "Discussion starter"

→ "Slide Deck"
  - "Conference talk"

Each branch shows arrow back:
"All link back to pillar content"

Footer note: "1 piece → 6+ distribution channels" """,
        "## Part 4: Content Distribution",
    ),
    # 07 - Events & Conferences
    (
        "07",
        "conference-timeline",
        """Conference marketing timeline:

Horizontal timeline with three main phases:

BEFORE (left, 4-6 weeks):
Week -6: "Reserve booth, book travel"
Week -4: "Create collateral, prep demos"
Week -2: "Announce attendance, schedule meetings"
Week -1: "Ship swag, final prep"

DURING (center, highlighted):
Day 1: "Setup, opening sessions"
Day 2-3: "Peak networking, demos"
- Callout: "Collect leads + context"
Last Day: "Wrap meetings, follow-up list"

AFTER (right):
+24h: "Thank you emails"
+1 week: "Detailed follow-ups"
+2 weeks: "Move to CRM pipeline"
+1 month: "ROI assessment"

Bottom bar: "Time investment = heavy before, critical after" """,
        "## Part 2: Conference Booth Strategy",
    ),
    (
        "07",
        "event-budget-segments",
        """Event budget allocation by company segment:

Two pie charts side by side:

SMB / PLG Company:
- 70% Digital (Google, content, webinars)
- 30% Events (selective attendance)
Note: "Focus on scalable reach"

Enterprise Company:
- 30% Digital (targeted campaigns)
- 70% Events (dinners, conferences, field)
Note: "Focus on relationship building"

Below, bar chart showing:
"Marketing % of Total Budget"
- Typical SaaS: 7-9%
- PLG-Heavy: ~20%

Footer: "Mix shifts as you move upmarket" """,
        "## Part 9: Measuring Event ROI",
    ),
    # 08 - Community Building
    (
        "08",
        "community-flywheel",
        """Community growth flywheel:

Circular diagram with 5 connected stages:

1. "NEW MEMBERS JOIN" (top)
   → Arrow with: "1:1 conversations"

2. "MEMBERS GET VALUE" (right)
   → Arrow with: "Questions answered, connections made"

3. "MEMBERS CONTRIBUTE" (bottom-right)
   → Arrow with: "Share expertise, help others"

4. "COMMUNITY GROWS" (bottom-left)
   → Arrow with: "Word of mouth, reputation"

5. "MORE PEOPLE ATTRACTED" (left)
   → Arrow with: "Quality draws quality"
   → Loops back to step 1

Center: "COMMUNITY MANAGER"
- Role: "Catalyze each transition"

Outer note: "Flywheel accelerates over time" """,
        "## Part 3: Growing Engagement",
    ),
    (
        "08",
        "community-scaling-stages",
        """Community scaling stages:

Horizontal progression with 4 stages:

STAGE 1: "Founder-Led" (0-100 members)
- Icon: Single person
- Activities: "Personal outreach, 1:1 chats, seeding content"
- Key metric: "Response rate"

STAGE 2: "First Hire" (100-500 members)
- Icon: Two people
- Activities: "Community manager, structured programs"
- Key metric: "Engagement rate"

STAGE 3: "Power Users" (500-2000 members)
- Icon: Star users highlighted
- Activities: "Champion program, delegated moderation"
- Key metric: "User-to-user help ratio"

STAGE 4: "Community Team" (2000+ members)
- Icon: Team of people
- Activities: "Events, content, tooling, analytics"
- Key metric: "Business impact"

Arrow at bottom: "Automation increases, personal touch preserved" """,
        "## Part 5: Scaling Community",
    ),
    # 09 - Sales & GTM
    (
        "09",
        "gtm-approaches",
        """Three GTM approaches comparison:

Three vertical columns:

BOTTOM-UP (left):
- Arrow pointing up
- Flow: "Dev adopts → Team uses → Enterprise buys"
- Pros: "Sticky, organic, lower CAC"
- Cons: "Slow, unpredictable revenue"
- Examples: "Stripe, Twilio, Datadog"

MIDDLE-OUT (center):
- Arrows pointing both up and down from center
- Flow: "Target Eng Manager → Excite devs + Enable directors"
- Pros: "Faster than bottom-up, authentic"
- Cons: "Need both product + sales motion"
- Examples: "MongoDB, Snowflake"

TOP-DOWN (right):
- Arrow pointing down
- Flow: "CTO/VP buys → Mandates usage"
- Pros: "Fast revenue, predictable"
- Cons: "Expensive, may not stick"
- Examples: "Traditional enterprise"

Footer: "Most dev tools combine approaches" """,
        "## Part 1: Developer GTM Fundamentals",
    ),
    (
        "09",
        "sales-signals-dashboard",
        """Sales signals dashboard mockup:

Header: "Product-Qualified Account: Acme Corp"

Four signal sections:

PRODUCT SIGNALS (green indicators):
- "Active 3+ weeks" ✓
- "5 team members" ✓
- "Core feature adopted" ✓
- "Above usage threshold" ✓

WEBSITE SIGNALS (blue indicators):
- "Pricing page: 3 visits"
- "Security docs: viewed"
- "Contact page: clicked"

COMMUNITY SIGNALS (purple indicators):
- "Slack: asking enterprise questions"
- "GitHub: opened integration issue"

EXTERNAL SIGNALS (orange indicators):
- "Series B announced"
- "Hiring DevOps lead"

Bottom action bar:
"Score: 85/100 | Recommended: AE Outreach"
"Buyer contact: VP Engineering (LinkedIn)" """,
        "## Part 4: Sales Signals",
    ),
    # 10 - Open Source & GitHub
    (
        "10",
        "github-growth-loop",
        """GitHub PR growth loop (Snyk example):

Circular flow diagram:

1. "User signs up for tool" (top)
   → Arrow to next

2. "Connects GitHub account"
   → Arrow to next

3. "Tool scans repos, finds issues"
   → Arrow to next

4. "Bot creates branded PR to fix" (highlighted)
   → Callout: "Visible to entire team"
   → Arrow to next

5. "Team members see PR, investigate"
   → Arrow to next

6. "Some follow links to tool"
   → Arrow to next

7. "New signups" (loops back to 1)

Center stats:
- "PR visible to avg 5 devs"
- "10% click through"
- "Viral coefficient > 1"

Note: "Built into natural workflow" """,
        "## Part 3: The GitHub PR Growth Loop",
    ),
    (
        "10",
        "first-1000-stars-roadmap",
        """Roadmap to first 1000 GitHub stars:

Horizontal timeline with star milestones:

0-100 STARS: "Artificial Growth"
- Tactics: "Friends, family, office, conferences"
- Icon: Seeds being planted
- Note: "Personal asks"

100-300 STARS: "Content Push"
- Tactics: "Blog posts, tutorials, listicles"
- Icon: Megaphone
- Note: "Syndicate everywhere"

300-500 STARS: "List Submissions"
- Tactics: "awesome-*, curated lists, directories"
- Icon: Checklist
- Note: "PR to every relevant list"

500-750 STARS: "Community Engagement"
- Tactics: "Reddit, Discord, Slack groups"
- Icon: People talking
- Note: "Be helpful, not promotional"

750-1000 STARS: "Influencer + Paid"
- Tactics: "Reach out to influencers, Ethical Ads"
- Icon: Rocket
- Note: "Accelerate momentum"

Footer: "Each stage builds on previous" """,
        "## Part 2: Getting Your First 1000 Stars",
    ),
    # 11 - Social Media
    (
        "11",
        "platform-selection-guide",
        """Social platform selection guide for dev tools:

Matrix showing platforms vs use cases:

Columns (Platforms):
Twitter/X | LinkedIn | YouTube | Reddit | Discord

Rows (Use Cases):
"Dev conversations" → Twitter ✓✓✓, Reddit ✓✓
"B2B/Enterprise" → LinkedIn ✓✓✓
"Tutorials" → YouTube ✓✓✓
"Community Q&A" → Discord ✓✓✓, Reddit ✓✓
"Announcements" → Twitter ✓✓, LinkedIn ✓✓
"Thought leadership" → LinkedIn ✓✓✓, Twitter ✓✓

Side panel - Audience characteristics:
- Twitter: "Tech conversations, real-time"
- LinkedIn: "Decision makers, B2B"
- YouTube: "Learning, long-form"
- Reddit: "Authentic only, hates marketing"
- Discord: "Community, async support"

Footer: "Start with 1-2, do them well" """,
        "## Part 1: Social Media Philosophy",
    ),
    (
        "11",
        "tweet-anatomy",
        """Anatomy of high-performing dev tool tweet:

Sample tweet mockup with labeled callouts:

HOOK (first line, bold):
"We just made Postgres 10x faster"
- Callout: "Specific claim, developer speak"

VALIDATION (middle):
"Here's how:
• Technique 1
• Technique 2
• Technique 3"
- Callout: "Shows there's real value"

PUSH (end):
"Full benchmark: [link]"
- Callout: "CTA to learn more"

Engagement bar below tweet:
- Callout pointing to comments: "Respond to everyone"

Side panel - Formula:
"Hook + Validation + Push"

Anti-patterns to avoid:
✗ "We're excited to announce..."
✗ Marketing buzzwords
✗ No code/technical content""",
        "## Part 2: Twitter/X Strategy",
    ),
    # 12 - Metrics & Attribution
    (
        "12",
        "developer-journey-metrics",
        """Developer journey with stage-specific metrics:

Horizontal funnel with 5 stages:

DISCOVER (widest):
- Metrics: "Traffic, impressions, reach"
- Signals: "First visit, content views"
- Owner: "Marketing"

START:
- Metrics: "Signups, time to first action"
- Signals: "Account created, docs visited"
- Owner: "Marketing/Growth"

ACTIVATE:
- Metrics: "Activation rate, time to first X"
- Signals: "First API call, feature used"
- Owner: "Product/Growth"
- Note: "Aha moment here"

CONVERT:
- Metrics: "Trial-to-paid, upgrade rate"
- Signals: "Payment, team invite"
- Owner: "Growth/Sales"

SCALE (narrowest):
- Metrics: "Expansion, seat growth"
- Signals: "Enterprise features, SSO"
- Owner: "Sales/CS"

Bottom highlight:
"Time to First Hello World" = Key activation metric""",
        "## Part 4: Developer Journey Metrics",
    ),
    (
        "12",
        "attribution-mix",
        """Attribution mix diagram:

Two overlapping circles (Venn diagram style):

Left circle: "SOFTWARE ATTRIBUTION"
Contents:
- "UTM tracking"
- "Cookie-based"
- "CRM touchpoints"
- "Analytics platforms"
Note: "What you can track"
Limitation: "Misses dark social"

Right circle: "SELF-REPORTED"
Contents:
- "Signup survey"
- "Sales conversations"
- "Customer interviews"
Note: "What they remember"
Limitation: "Recall bias"

Overlap section:
"COMBINED TRUTH"
- "More complete picture"
- "Validate each other"

Below diagram, examples of what self-reported catches:
- Podcast mentions
- Slack recommendations
- Conference encounters
- Word of mouth
- Twitter threads

Footer: "Neither alone is sufficient" """,
        "## Part 2: Attribution Fundamentals",
    ),
]


def generate_with_gemini(prompt: str, output_path: str) -> bool:
    """Generate an image using Gemini API."""
    from google import genai
    from google.genai import types

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set")

    client = genai.Client(api_key=api_key)
    full_prompt = f"{prompt}. {STYLE_REQUIREMENTS}"

    response = client.models.generate_content(
        model="gemini-2.0-flash-exp-image-generation",
        contents=full_prompt,
        config=types.GenerateContentConfig(
            response_modalities=["Text", "Image"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(part.inline_data.data)
            return True

    raise ValueError("No image in Gemini response")


def generate_with_openai(prompt: str, output_path: str) -> bool:
    """Generate an image using OpenAI gpt-image-1."""
    import base64
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    full_prompt = f"{prompt}. {STYLE_REQUIREMENTS}"

    response = client.images.generate(
        model="gpt-image-1",
        prompt=full_prompt,
        n=1,
        size="1536x1024",
        response_format="b64_json",
    )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    image_data = response.data[0].b64_json
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_data))
    return True


def generate_image(prompt: str, output_path: str, force_openai: bool = False) -> bool:
    """Generate an image. Tries Gemini first, falls back to OpenAI on quota errors."""
    print(f"Generating image...")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")

    if not force_openai:
        try:
            if generate_with_gemini(prompt, output_path):
                print(f"✓ Saved: {output_path} (via Gemini)")
                return True
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "quota" in error_str.lower():
                print(f"Gemini quota exceeded, falling back to OpenAI...")
            else:
                print(f"Gemini error: {e}, falling back to OpenAI...")
    else:
        print("Using OpenAI (--force-openai)")

    try:
        if generate_with_openai(prompt, output_path):
            print(f"✓ Saved: {output_path} (via OpenAI)")
            return True
    except Exception as e:
        print(f"OpenAI error: {e}")

    print("✗ Failed to generate image")
    return False


def get_guide_file(guide_num: str) -> Path:
    """Find the guide file for a given guide number."""
    pattern = f"{guide_num}-*.md"
    matches = list(GUIDES_DIR.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No guide found matching {pattern}")
    return matches[0]


def insert_image_into_guide(guide_path: Path, image_name: str, heading: str) -> bool:
    """Insert image reference after a specific heading in the guide."""
    content = guide_path.read_text()

    # Image markdown to insert
    image_md = f"\n![{image_name.replace('-', ' ').title()}](images/{image_name}.png)\n"

    # Check if image already inserted
    if f"images/{image_name}.png" in content:
        print(f"  Image already in guide, skipping insertion")
        return True

    # Find the heading and insert after it
    heading_pattern = re.escape(heading)
    match = re.search(f"({heading_pattern})\n", content)

    if not match:
        print(f"  ✗ Heading not found: {heading}")
        return False

    # Insert image after the heading line
    insert_pos = match.end()
    new_content = content[:insert_pos] + image_md + content[insert_pos:]

    guide_path.write_text(new_content)
    print(f"  ✓ Inserted image reference after: {heading}")
    return True


def process_diagrams(
    guide_filter: str = None,
    dry_run: bool = False,
    insert_only: bool = False,
    force_openai: bool = False,
):
    """Process all diagrams - generate and insert into guides."""

    # Create images directory
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Filter diagrams if specific guide requested
    diagrams = DIAGRAMS
    if guide_filter:
        diagrams = [d for d in DIAGRAMS if d[0] == guide_filter]
        if not diagrams:
            print(f"No diagrams found for guide {guide_filter}")
            return

    print(f"\nProcessing {len(diagrams)} diagrams...")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for guide_num, diagram_id, prompt, heading in diagrams:
        image_name = f"{guide_num}-{diagram_id}"
        image_path = IMAGES_DIR / f"{image_name}.png"

        print(f"\n[{image_name}]")

        if dry_run:
            print(f"  Would generate: {image_path}")
            print(f"  Prompt: {prompt[:80]}...")
            print(f"  Insert after: {heading}")
            continue

        # Generate image (unless insert-only mode)
        if not insert_only:
            if image_path.exists():
                print(f"  Image exists, skipping generation")
            else:
                if not generate_image(prompt, str(image_path), force_openai):
                    fail_count += 1
                    continue

        # Insert into guide
        try:
            guide_path = get_guide_file(guide_num)
            if insert_image_into_guide(guide_path, image_name, heading):
                success_count += 1
            else:
                fail_count += 1
        except FileNotFoundError as e:
            print(f"  ✗ {e}")
            fail_count += 1

    print("\n" + "=" * 60)
    print(f"Complete: {success_count} successful, {fail_count} failed")


def main():
    parser = argparse.ArgumentParser(
        description="Generate diagrams for developer marketing guides"
    )
    parser.add_argument(
        "--guide",
        help="Only process specific guide (e.g., '01', '02')",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without doing it",
    )
    parser.add_argument(
        "--insert-only",
        action="store_true",
        help="Only insert image references, skip generation",
    )
    parser.add_argument(
        "--force-openai",
        action="store_true",
        help="Skip Gemini and use OpenAI directly",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all diagrams that would be generated",
    )

    args = parser.parse_args()

    if args.list:
        print("\nDiagrams to generate:")
        print("=" * 60)
        for guide_num, diagram_id, prompt, heading in DIAGRAMS:
            print(f"\n[{guide_num}-{diagram_id}]")
            print(f"  Insert after: {heading}")
            print(f"  Prompt: {prompt[:100]}...")
        print(f"\nTotal: {len(DIAGRAMS)} diagrams")
        return

    process_diagrams(
        guide_filter=args.guide,
        dry_run=args.dry_run,
        insert_only=args.insert_only,
        force_openai=args.force_openai,
    )


if __name__ == "__main__":
    main()
