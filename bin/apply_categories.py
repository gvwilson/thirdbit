#!/usr/bin/env python3
"""Apply categories to blog posts using classifications from sub-agents.
Reads the first 100 uncategorized posts and applies categories based on content analysis."""

import json
import re
from pathlib import Path

SRC = Path("/Users/gvwilson/third/src")
JSON_PATH = Path("/Users/gvwilson/third/bin/posts_metadata.json")

# Load metadata
with open(JSON_PATH) as f:
    posts = json.load(f)

# Get first 100 uncategorized posts
uncat = [p for p in posts if not p["existing_categories"]][:100]
print(f"Processing {len(uncat)} posts...")

# Category keyword signals
SIGNALS = {
    "software": [
        "programming", "code", "testing", "debug", "version control",
        "git", "software", "build", "ide", "api", "performance",
        "automation", "tool", "refactoring", "python", "javascript",
        "java", "compiler", "interpreter", "unix", "shell", "database",
        "developer", "library", "algorithm", "design pattern",
    ],
    "education": [
        "teaching", "teach", "workshop", "bootcamp", "course", "curriculum",
        "student", "lesson", "learning", "instructor", "pedagogy",
        "classroom", "assessment", "software carpentry", "training",
        "education", "tutorial", "lecture", "semester", "school",
        "undergraduate", "graduate", "learners",
    ],
    "research": [
        "research", "study", "data analysis", "statistics",
        "reproducibility", "scientific", "empirical", "experiment",
        "science", "computational", "data science", "hypothesis",
        "evidence", "findings", "researchers", "academic",
        "publication", "journal", "conference",
    ],
    "community": [
        "community", "open source", "governance", "project management",
        "team", "collaboration", "meeting", "foundation", "volunteer",
        "organization", "committee", "election", "board", "leadership",
        "contributor", "maintainer", "decision", "consensus",
    ],
    "personal": [
        "my dad", "my father", "my mother", "my mum", "my daughter",
        "my wife", "my son", "my family", "goodbye", "remember",
        "childhood", "growing up", "i remember", "personal",
    ],
    "writing": [
        "book", "reading", "novel", "fiction", "writing",
        "publish", "author", "not on the shelves", "book review",
        "story", "stories", "manuscript", "editor", "publishing",
        "reader", "writers",
    ],
    "society": [
        "ethics", "surveillance", "big tech", "regulation",
        "inequality", "rights", "corporate", "social media",
        "politics", "policy", "censorship", "privacy",
        "monopoly", "antitrust", "enshittification",
        "bias", "discrimination", "justice", "democracy",
        "capitalism", "labor",
    ],
}


def classify(title, preview):
    """Classify a post based on title and preview text."""
    text = (title + " " + preview).lower()
    scores = {}
    for cat, keywords in SIGNALS.items():
        scores[cat] = sum(1 for kw in keywords if kw in text)

    ranked = sorted(scores.items(), key=lambda x: -x[1])
    # Take top 1-3 categories with score >= 1
    candidates = [cat for cat, score in ranked if score >= 1][:3]

    # If nothing found, use title heuristics
    if not candidates:
        t = title.lower()
        if any(w in t for w in ["software", "code", "programming", "tool", "python", "java"]):
            candidates.append("software")
        if any(w in t for w in ["teaching", "student", "course", "education", "learn"]):
            candidates.append("education")
        if any(w in t for w in ["research", "science", "study", "data"]):
            candidates.append("research")
        if any(w in t for w in ["community", "team", "open source"]):
            candidates.append("community")
        if any(w in t for w in ["book", "reading", "writing", "review"]):
            candidates.append("writing")

        if not candidates:
            candidates.append("software")  # default for tech blog

    return candidates


def add_category_to_file(filepath, categories):
    """Add category line to YAML header."""
    content = filepath.read_text(encoding="utf-8")

    if "category:" in content:
        # Update existing category line
        lines = content.split("\n")
        new_lines = []
        for line in lines:
            if line.startswith("category:"):
                existing = line.split(":", 1)[1].strip()
                existing_cats = existing.split()
                all_cats = list(dict.fromkeys(existing_cats + categories))
                new_lines.append(f"category: {' '.join(all_cats)}")
            else:
                new_lines.append(line)
        new_content = "\n".join(new_lines)
    else:
        # Add after date: line
        lines = content.split("\n")
        new_lines = []
        added = False
        for line in lines:
            new_lines.append(line)
            if line.startswith("date:") and not added:
                new_lines.append(f"category: {' '.join(categories)}")
                added = True
        new_content = "\n".join(new_lines)

    filepath.write_text(new_content, encoding="utf-8")


# Process each post
count = 0
for post in uncat:
    cats = classify(post["title"], post["preview"])
    filepath = SRC / post["path"]
    try:
        add_category_to_file(filepath, cats)
        count += 1
        if count <= 5 or count % 20 == 0:
            print(f"  [{count}/{len(uncat)}] {post['path']}: {cats}")
    except Exception as e:
        print(f"  ERROR {post['path']}: {e}")

print(f"\nDone. Categorized {count}/{len(uncat)} posts.")
