#!/usr/bin/env python
"""Convert ark talk decks (remark.js) to pandoc reveal.js slides.

For each src/talks/*/index.qmd:
- drop `---` slide separators (an H2 already starts a slide);
- turn `--` fragment separators into `. . .` (reveal.js pause).

The slides themselves are built with pandoc (see the mccole.mk slides rule),
not with Quarto. Idempotent; only touches the talk decks, not the top-level
talks pages.
"""

import re
import sys
from pathlib import Path


def convert_file(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return False
    fm, body = m.group(1), m.group(2)

    lines = []
    for line in body.splitlines():
        s = line.strip()
        if s == "---":
            continue
        if s == "--":
            lines.append(". . .")
        else:
            lines.append(line)

    path.write_text(f"---\n{fm}\n---\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return True


def main():
    decks = sorted(Path("src/talks").glob("*/index.qmd"))
    converted = sum(1 for d in decks if convert_file(d))
    print(f"converted {converted} talk decks", file=sys.stderr)


if __name__ == "__main__":
    main()
