#!/usr/bin/env python3
"""Extract title, body preview, and existing categories from all blog posts."""

import json
import re
import sys
from pathlib import Path

SRC_DIR = Path("/Users/gvwilson/third/src")

def extract_post(filepath):
    """Extract YAML header fields and first 3 paragraphs from a blog post."""
    text = filepath.read_text(encoding="utf-8")
    
    # Parse YAML header (between --- markers)
    header = {}
    body = ""
    in_header = False
    header_done = False
    lines = text.split("\n")
    
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_header = True
            continue
        if in_header and line.strip() == "---":
            in_header = False
            header_done = True
            continue
        if in_header:
            if ":" in line:
                key, _, val = line.partition(":")
                header[key.strip()] = val.strip().strip('"')
        if header_done and not in_header:
            body = "\n".join(lines[i:])
            break
    
    if not header_done:
        body = text
    
    # Extract first 3 paragraphs (text between <p> tags)
    paragraphs = re.findall(r'<(?:p|blockquote)[^>]*>(.*?)</(?:p|blockquote)>', body, re.DOTALL)
    preview_paras = []
    for p in paragraphs[:3]:
        # Strip HTML tags
        clean = re.sub(r'<[^>]+>', '', p).strip()
        clean = re.sub(r'\s+', ' ', clean)
        if clean:
            preview_paras.append(clean)
    
    # Fallback: if no <p> tags found, strip all HTML and take first 800 chars
    if not preview_paras:
        clean_body = re.sub(r'<[^>]+>', ' ', body)
        clean_body = re.sub(r'\s+', ' ', clean_body).strip()
        if clean_body:
            preview_paras.append(clean_body)
    
    existing_cats = header.get("category", "").split() if "category" in header else []
    
    return {
        "path": str(filepath.relative_to(SRC_DIR)),
        "title": header.get("title", ""),
        "date": header.get("date", ""),
        "existing_categories": existing_cats,
        "preview": " ".join(preview_paras)[:800]
    }


def main():
    posts = []
    pattern = SRC_DIR / "20*" / "*" / "*" / "*.md"
    
    for filepath in sorted(SRC_DIR.glob("20*/*/*/*.md")):
        post = extract_post(filepath)
        posts.append(post)
    
    output_path = Path("/Users/gvwilson/third/bin/posts_metadata.json")
    output_path.write_text(json.dumps(posts, indent=2, ensure_ascii=False))
    
    print(f"Extracted {len(posts)} posts to {output_path}")
    
    # Stats
    has_cats = sum(1 for p in posts if p["existing_categories"])
    print(f"Posts with existing categories: {has_cats}")
    print(f"Posts without categories: {len(posts) - has_cats}")


if __name__ == "__main__":
    main()
