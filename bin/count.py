import argparse
import csv
import sys


CHAPTER_START = "##"
SECTION_START = "<section"
SECTION_END = "</section>"


def main():
    """Main driver."""
    args = parse_args()
    base = find_base(args)
    with open(args.filename, "r") as reader:
        text = reader.read()
    if SECTION_START in text:
        chapters(args, text, base)
    else:
        sections(args, text, base)


def chapters(args, text, base):
    """Analyze chapters in long work."""
    lines = text.split("\n")
    in_chapter = False
    title = ""
    count = 0
    total = 0

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
                    print(f"{count:6d}{title}")
                total += count
            count = 0

        elif in_chapter:
            count += len(line.replace("—", " ").replace("…", " ").split())

        else:
            pass

    base = "" if base is None else f" ({total - base})"
    print(f"{total:6d}{base}")


def sections(args, text, base):
    """Analyze sections in short story."""
    total = len([x for x in text.split() if x])
    base = "" if base is None else f" ({total - base})"
    print(f"{total:6d}{base}")


def find_base(args):
    """Find base count if any."""
    if args.base is not None:
        return args.base
    if args.status is None:
        return None

    count = None
    stem = args.filename.split("/")[-2]
    with open(args.status, "r") as reader:
        for line in csv.reader(reader):
            if line[0] == stem:
                count = line[2]
    return int(count)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, default=None, help="book file")
    parser.add_argument("base", type=int, nargs="?", default=None, help="base count")
    parser.add_argument("--status", type=str, default=None, help="status file")
    parser.add_argument("--details", action="store_true", default=False, help="show details")
    return parser.parse_args()


if __name__ == "__main__":
    main()
