#!/usr/bin/env python3

import re
import sys


RENAMES = {
    "cs-education": "education",
    "tools": "programming",
    "software": "programming",
    "community-events": "community",
    "organizational-change": "org-change",
}
PAT = re.compile(r"^category:(.+)$", re.MULTILINE)


def sub(m):
    keys = m.group(1).strip().split(" ")
    keys = {RENAMES.get(k, k) for k in keys}
    return f"category: {' '.join(sorted(list(keys)))}"
    

def main():
    for filename in sys.argv[1:]:
        with open(filename, "r") as reader:
            old = reader.read()
        new = PAT.sub(sub, old)
        print(f"filename: {old != new}", file=sys.stderr)
        with open(filename, "w") as writer:
            writer.write(new)


if __name__ == "__main__":
    main()
