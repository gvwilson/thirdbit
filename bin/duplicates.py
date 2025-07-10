#!/usr/bin/env python

"""Find duplicate files."""

from hashlib import sha256
from pathlib import Path
import sys

def find_groups(roots):
    groups = {}
    for r in roots:
        for f in Path(r).glob("**/*"):
            if not f.is_file():
                continue
            data = open(f, "rb").read()
            hash_code = sha256(data).hexdigest()
            if hash_code not in groups:
                groups[hash_code] = set()
            groups[hash_code].add(str(f))
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for h, c in groups.items():
        if len(c) > 1:
            print(", ".join(sorted(c)))
