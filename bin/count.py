import argparse
import sys


CHAPTER_START = "##"
SECTION_START = "<section"
SECTION_END = "</section>"


def main():
    """Main driver."""
    args = parse_args()
    with open(args.filename, "r") as reader:
        text = reader.read()
    if SECTION_START in text:
        chapters(args, text)
    else:
        sections(args, text)


def chapters(args, text):
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
                if args.details:
                    print(f"{number:02d}){count:5d}{title}")
                total += count
            count = 0
            number += 1

        elif in_chapter:
            count += len(line.replace("—", " ").replace("…", " ").split())

        else:
            pass

    print(f"{total:6d}")


def sections(args, text, base):
    """Analyze sections in short story."""
    total = len([x for x in text.split() if x])
    base = "" if base is None else f" ({total - base})"
    print(f"{total:6d}{base}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("details", action="store_true", help="show details")
    parser.add_argument("filename", type=str, default=None, help="book file")
    return parser.parse_args()


if __name__ == "__main__":
    main()
