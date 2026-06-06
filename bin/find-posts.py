"""Find posts by category tag(s).

Usage:
  find-posts.py TAG               posts that have TAG (among possibly others)
  find-posts.py --all TAG ...     posts that have ALL listed tags
  find-posts.py --any TAG ...     posts that have ANY of the listed tags
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"

PATTERN = "[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]/*.md"


def get_categories(path):
    """Return the set of categories from a file's YAML front matter."""
    in_front_matter = False
    with open(path) as f:
        for i, line in enumerate(f):
            if i == 0:
                if line.strip() == "---":
                    in_front_matter = True
                else:
                    return set()
            elif in_front_matter:
                if line.strip() == "---":
                    return set()
                if line.startswith("category:"):
                    return set(line[len("category:"):].split())
    return set()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--all", dest="mode", action="store_const", const="all")
    mode.add_argument("--any", dest="mode", action="store_const", const="any")
    parser.add_argument("tags", nargs="+")
    args = parser.parse_args()

    if args.mode is None and len(args.tags) != 1:
        parser.error("exactly one tag required without --all or --any")

    wanted = set(args.tags)

    for md_file in sorted(SRC.glob(PATTERN)):
        cats = get_categories(md_file)
        if not cats:
            continue
        if args.mode == "all":
            match = wanted <= cats
        elif args.mode == "any":
            match = bool(wanted & cats)
        else:
            match = wanted <= cats
        if match:
            print(md_file)


if __name__ == "__main__":
    main()
