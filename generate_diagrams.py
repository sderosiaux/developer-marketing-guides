#!/usr/bin/env python3
"""
Generate conceptual diagrams for developer marketing guides using Gemini.

Usage:
    python generate_diagrams.py [--dry-run] [--guide N]
"""

import argparse
import os
import sys
import time
from pathlib import Path

# Style requirements for clean conceptual diagrams
STYLE = (
    "Style: Clean minimalist diagram, flat design. "
    "White background, professional blue/teal/gray color palette. "
    "Clear sans-serif labels, clean lines and shapes. "
    "NO photorealistic elements, NO people, NO decorations. "
    "NO watermarks, NO attribution text, NO title text in image. "
    "Simple, clear, educational diagram only."
)

# Diagram definitions: (guide_num, filename, prompt, insert_after_heading)
DIAGRAMS = [
    # Guide 01: Website & Landing Pages
    (1, "01-developer-trust-ladder.png",
     "Create a vertical ladder/pyramid diagram showing developer trust progression. "
     "5 levels from bottom to top: 'Visitor' -> 'Explorer' -> 'Evaluator' -> 'User' -> 'Advocate'. "
     "Each level slightly narrower than the one below. Arrow pointing upward on the side. "
     "Label on side: 'Trust & Commitment'. Simple boxes with text labels.",
     "## Level 1: Foundations"),

    # Guide 02: HN & Product Hunt
    (2, "02-launch-timeline.png",
     "Create a horizontal timeline diagram for product launches. "
     "3 main phases: 'PRE-LAUNCH (2-4 weeks)' -> 'LAUNCH DAY' -> 'POST-LAUNCH (1 week)'. "
     "Under Pre-launch: bullets 'Prep content', 'Build network', 'Test experience'. "
     "Under Launch Day: bullets 'Post early', 'Engage comments', 'Social amplify'. "
     "Under Post-launch: bullets 'Follow up', 'Share results', 'Nurture leads'. "
     "Simple horizontal flow with boxes and bullet points.",
     "## Part 2: The HN Launch Formula"),

    # Guide 03: Paid Advertising
    (3, "03-channel-selection-matrix.png",
     "Create a 2x2 matrix diagram for advertising channel selection. "
     "X-axis: 'Lower Cost' to 'Higher Cost'. Y-axis: 'Niche Audience' to 'Broad Audience'. "
     "Quadrants contain: Top-left 'Reddit, Newsletters', Top-right 'LinkedIn, YouTube'. "
     "Bottom-left 'Ethical Ads, Carbon', Bottom-right 'Google Ads'. "
     "Simple 2x2 grid with labeled axes and channel names in each quadrant.",
     "## Part 2: Channel Selection Framework"),

    # Guide 04: Pricing & Positioning
    (4, "04-positioning-stack.png",
     "Create a vertical stack diagram showing positioning layers. "
     "4 horizontal layers stacked vertically, bottom to top: "
     "'PRODUCT (Core logic)' -> 'POSITIONING (API)' -> 'MESSAGING (Components)' -> 'COPY (UI)'. "
     "Arrow on side pointing up labeled 'Abstraction Level'. "
     "Each layer a simple rectangle with label inside.",
     "## Part 1: Positioning Fundamentals"),

    # Guide 05: Documentation
    (5, "05-docs-radiating-circles.png",
     "Create a concentric circles diagram showing developer experience layers. "
     "4 rings from center outward: 'PRODUCT' (center) -> 'DOCS' -> 'CONTENT' -> 'COMMUNITY' (outer). "
     "Arrow pointing outward labeled 'Market Maturity'. "
     "Simple concentric circles with text labels in each ring.",
     "## Part 1: Docs Philosophy"),

    # Guide 06: Content Marketing
    (6, "06-content-repurposing-flow.png",
     "Create a flowchart showing content repurposing. "
     "Start with one box 'Blog Post' on left. "
     "Arrows branching to 4 boxes on right: 'Twitter Thread', 'LinkedIn Post', 'Newsletter', 'Video Script'. "
     "Simple one-to-many flow diagram with labeled boxes and arrows.",
     "## Part 4: Content Distribution"),

    # Guide 07: Events & Conferences
    (7, "07-conference-timeline.png",
     "Create a horizontal timeline for conference preparation. "
     "3 phases: '4 WEEKS BEFORE' -> 'EVENT DAY' -> '1 WEEK AFTER'. "
     "Under 4 weeks: 'Order assets, Brief team, Schedule meetings'. "
     "Under Event: 'Staff booth, Capture leads, Daily sync'. "
     "Under After: 'Follow up, Qualify leads, Document learnings'. "
     "Simple timeline with phases and bullet points below each.",
     "## Part 2: Conference Booth Strategy"),

    # Guide 08: Community Building
    (8, "08-community-flywheel.png",
     "Create a circular flywheel diagram for community growth. "
     "4 segments in a circle with arrows connecting them clockwise: "
     "'Members Join' -> 'Value Delivered' -> 'Engagement Grows' -> 'Word Spreads' -> back to 'Members Join'. "
     "Circular flow with arrows between each segment. Label in center: 'Community Flywheel'.",
     "## Part 1: Community Fundamentals"),

    # Guide 09: Sales & GTM
    (9, "09-gtm-approaches.png",
     "Create a 3-column comparison diagram for GTM approaches. "
     "3 columns: 'BOTTOM-UP', 'TOP-DOWN', 'MIDDLE-OUT'. "
     "Under Bottom-up: 'Dev adopts -> Team expands -> Enterprise'. "
     "Under Top-down: 'CTO buys -> Mandate usage -> Adoption'. "
     "Under Middle-out: 'Eng Manager -> Excite both devs & directors'. "
     "Simple 3-column layout with flow arrows in each column.",
     "## Part 1: Developer GTM Fundamentals"),

    # Guide 10: Open Source & GitHub
    (10, "10-first-1000-stars-roadmap.png",
     "Create a horizontal roadmap diagram for GitHub star growth. "
     "4 stages left to right: '0-100 STARS' -> '100-300' -> '300-700' -> '700-1000'. "
     "Under 0-100: 'Friends, network, first posts'. "
     "Under 100-300: 'Content, awesome-lists'. "
     "Under 300-700: 'Communities, Reddit, paid'. "
     "Under 700-1000: 'Influencers, PR, momentum'. "
     "Simple horizontal progression with labels and bullets.",
     "## Part 2: Getting Your First 1000 Stars"),

    # Guide 11: Social Media
    (11, "11-platform-selection-guide.png",
     "Create a simple matrix/table showing social platform selection. "
     "Columns: 'Twitter', 'LinkedIn', 'YouTube', 'Reddit'. "
     "Rows: 'Best For', 'Audience', 'Content Type'. "
     "Twitter: 'Dev conversations', 'Developers', 'Short/memes'. "
     "LinkedIn: 'B2B/Enterprise', 'Managers/CTOs', 'Thought leadership'. "
     "YouTube: 'Tutorials', 'Learners', 'Long-form video'. "
     "Reddit: 'Discussions', 'Community', 'Authentic only'. "
     "Clean table/grid format.",
     "## Part 1: Social Media Philosophy"),

    # Guide 12: Metrics & Attribution
    (12, "12-attribution-mix.png",
     "Create a Venn diagram for attribution approaches. "
     "Two overlapping circles. "
     "Left circle: 'SOFTWARE ATTRIBUTION' with bullets 'UTM tracking', 'Analytics', 'Cookie-based'. "
     "Right circle: 'SELF-REPORTED' with bullets 'Survey responses', 'How did you hear about us'. "
     "Overlap area: 'COMBINED TRUTH' with 'Best understanding'. "
     "Simple two-circle Venn diagram with labels.",
     "## Part 2: Attribution Fundamentals"),
]


def generate_with_gemini(prompt: str, output_path: str) -> bool:
    """Generate an image using Gemini API only."""
    from google import genai
    from google.genai import types

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set")

    client = genai.Client(api_key=api_key)
    full_prompt = f"{prompt} {STYLE}"

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


def insert_image_into_guide(guide_num: int, image_filename: str, heading: str) -> bool:
    """Insert image reference into guide markdown file."""
    guide_path = Path(f"guides/{guide_num:02d}-*.md")
    matches = list(Path(".").glob(str(guide_path)))

    if not matches:
        print(f"  Warning: No guide file found for guide {guide_num}")
        return False

    guide_file = matches[0]
    content = guide_file.read_text()

    # Create image markdown
    image_name = image_filename.replace(".png", "").replace("-", " ").title()
    image_md = f"\n![{image_name}](images/{image_filename})\n"

    # Find the heading and insert after it
    if heading not in content:
        print(f"  Warning: Heading '{heading}' not found in {guide_file}")
        return False

    # Check if image already inserted
    if image_filename in content:
        print(f"  Image already in {guide_file.name}")
        return True

    # Insert after heading line
    lines = content.split('\n')
    new_lines = []
    inserted = False

    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip() == heading and not inserted:
            new_lines.append(image_md)
            inserted = True

    if inserted:
        guide_file.write_text('\n'.join(new_lines))
        print(f"  Inserted image reference into {guide_file.name}")
        return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Generate diagrams for guides using Gemini")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--guide", type=int, help="Generate only for specific guide number")
    parser.add_argument("--insert-only", action="store_true", help="Only insert references, don't generate")
    args = parser.parse_args()

    print("=" * 60)
    print("Developer Marketing Guide Diagram Generator")
    print("Using: Gemini (gemini-2.0-flash-exp-image-generation)")
    print("=" * 60)

    images_dir = Path("guides/images")

    if not args.dry_run and not args.insert_only:
        images_dir.mkdir(parents=True, exist_ok=True)

    diagrams_to_process = DIAGRAMS
    if args.guide:
        diagrams_to_process = [d for d in DIAGRAMS if d[0] == args.guide]
        if not diagrams_to_process:
            print(f"No diagrams found for guide {args.guide}")
            sys.exit(1)

    success_count = 0
    fail_count = 0

    for guide_num, filename, prompt, heading in diagrams_to_process:
        output_path = images_dir / filename
        print(f"\n[Guide {guide_num:02d}] {filename}")

        if args.dry_run:
            print(f"  Prompt: {prompt[:80]}...")
            print(f"  Insert after: {heading}")
            continue

        # Generate image if not insert-only
        if not args.insert_only:
            if output_path.exists():
                print(f"  Image already exists: {output_path}")
            else:
                try:
                    print(f"  Generating...")
                    if generate_with_gemini(prompt, str(output_path)):
                        print(f"  Created: {output_path}")
                        success_count += 1
                        time.sleep(2)  # Rate limiting
                except Exception as e:
                    print(f"  Error: {e}")
                    fail_count += 1
                    continue

        # Insert image reference
        insert_image_into_guide(guide_num, filename, heading)

    print("\n" + "=" * 60)
    if not args.dry_run:
        print(f"Generated: {success_count} | Failed: {fail_count}")
    else:
        print(f"Dry run complete. {len(diagrams_to_process)} diagrams would be generated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
