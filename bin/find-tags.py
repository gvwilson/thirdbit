"""Find all tags used in blog post YAML front matter and print counts."""

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"

PATTERN = "[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/*.md"


def extract_category(path):
    """Return the category line value from a file's YAML front matter, or None."""
    in_front_matter = False
    with open(path) as f:
        for i, line in enumerate(f):
            if i == 0:
                if line.strip() == "---":
                    in_front_matter = True
                else:
                    return None
            elif in_front_matter:
                if line.strip() == "---":
                    return None
                if line.startswith("category:"):
                    return line[len("category:"):].strip()
    return None


counts = Counter()
for md_file in SRC.glob(PATTERN):
    value = extract_category(md_file)
    if value:
        counts.update(value.split())

for tag in sorted(counts):
    print(f"{tag}: {counts[tag]}")
