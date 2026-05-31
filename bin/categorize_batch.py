#!/usr/bin/env python3
"""Categorize a batch of blog posts, processing one at a time and printing each name.
Usage: python3 categorize_batch.py <batch_json_file>
The JSON file should contain a list of post objects with 'path', 'title', 'preview' keys."""

import json
import sys
from pathlib import Path

SRC = Path("/Users/gvwilson/third/src")

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
    text = (title + " " + preview).lower()
    scores = {}
    for cat, keywords in SIGNALS.items():
        scores[cat] = sum(1 for kw in keywords if kw in text)
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    candidates = [cat for cat, score in ranked if score >= 1][:3]
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
            candidates.append("software")
    return candidates


def add_category(filepath, categories):
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    if any(line.startswith("category:") for line in lines):
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
        new_lines = []
        added = False
        for line in lines:
            new_lines.append(line)
            if line.startswith("date:") and not added:
                new_lines.append(f"category: {' '.join(categories)}")
                added = True
        new_content = "\n".join(new_lines)

    filepath.write_text(new_content, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        print("Usage: categorize_batch.py <batch_json_file>")
        sys.exit(1)

    batch_file = Path(sys.argv[1])
    posts = json.loads(batch_file.read_text())

    print(f"PROCESSING {len(posts)} posts from {batch_file.name}")

    count = 0
    for i, post in enumerate(posts):
        cats = classify(post["title"], post["preview"])
        filepath = SRC / post["path"]
        try:
            add_category(filepath, cats)
            count += 1
            print(f"  [{i+1}/{len(posts)}] {post['path']} -> {' '.join(cats)}")
        except Exception as e:
            print(f"  [{i+1}/{len(posts)}] ERROR {post['path']}: {e}")

    print(f"DONE: {count}/{len(posts)} categorized")


if __name__ == "__main__":
    main()
