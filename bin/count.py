#!/usr/bin/env python
import sys


CHAPTER_START = "##"
SECTION_START = "<section"
SECTION_END = "</section>"


def main():
    """Main driver."""
    filename, previous = parse_args()
    with open(filename, "r") as reader:
        text = reader.read()
    if SECTION_START in text:
        chapters(filename, text, previous)
    else:
        sections(filename, text, previous)


def chapters(filename, text, previous):
    """Analyze chapters in long work."""
    lines = text.split("\n")
    in_chapter = False
    title = ""
    count = 0
    total = 0
    number = 1

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith(SECTION_START):
            in_chapter = True

        elif line.startswith(CHAPTER_START):
            title = line.strip().split(maxsplit=1)[1]

        elif line.startswith(SECTION_END):
            in_chapter = False
            if count > 0:
                if title:
                    title = f": {title}"
                if previous is None:
                    print(f"{number:02d}){count:5d}{title}")
                total += count
            count = 0
            number += 1

        elif in_chapter:
            count += len(line.replace("—", " ").replace("…", " ").split())

        else:
            pass

    if previous is None:
        print(f"{total:6d}")
    else:
        increase = total - previous
        print(f"{total:6d} ({increase})")


def sections(filename, text, base):
    """Analyze sections in short story."""
    total = len([x for x in text.split() if x])
    base = "" if base is None else f" ({total - base})"
    print(f"{total:6d}{base}")


def parse_args():
    """Parse command-line arguments."""
    if not (2 <= len(sys.argv) <= 3):
        print("Usage: count.py filename [previous]", file=sys.stderr)
        sys.exit(1)
    filename = sys.argv[1]
    previous = int(sys.argv[2]) if len(sys.argv) > 2 else None
    return filename, previous


if __name__ == "__main__":
    main()
