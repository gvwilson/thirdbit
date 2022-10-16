#!/usr/bin/env python                                       # 01
# 02
import hashlib  # 05
import os  # 04
import sys  # 03

# 06
IGNORES = [
    ".git",
    "node_modules",
    ".cache",  # 07
    ".DS_Store",
    ".dropbox",
    "Thumbs.db",
]  # 08
SENSES = {"--unique": True, "--duplicate": False}  # 09
# 10
def main():  # 11
    if sys.argv[1] == "--unique":  # 12
        unique = True  # 13
    elif sys.argv[1] == "--duplicate":  # 14
        unique = False  # 15
    else:  # 16
        print("Unknown sense", sys.argv[1])  # 17
        sys.exit(1)  # 18
        # 19
    roots = sys.argv[2:]  # 20
    if not roots:  # 21
        roots = [os.curdir]  # 22
        # 23
    found = {}  # 24
    count = 0  # 25
    for r in roots:  # 26
        count = find(r, found, count)  # 27
        # 28
    report(unique, found)  # 29
    # 30
    # 31


def find(root, found, count):  # 32
    for (dirpath, dirnames, filenames) in os.walk(root):  # 33
        ignore = False  # 34
        for i in IGNORES:  # 35
            if i in dirpath:  # 36
                ignore = True  # 37
        if ignore:  # 38
            continue  # 39
        count += 1  # 40
        if (count % 10) == 0:  # 41
            print(count, file=sys.stderr)  # 42
        for f in filenames:  # 43
            path = os.path.join(dirpath, f)  # 44
            if not os.path.isfile(path):  # 45
                continue  # 46
            with open(path, "r") as reader:  # 47
                data = reader.read()  # 48
                digest = hashlib.md5(data).digest()  # 49
                if digest not in found:  # 50
                    found[digest] = set()  # 51
                found[digest].add(path)  # 52
    return count  # 53
    # 54
    # 55


def report(unique, found):  # 56
    for digest in found:  # 57
        paths = found[digest]  # 58
        if unique and (len(paths) == 1):  # 59
            print(paths.pop())  # 60
        elif (not unique) and (len(paths) > 1):  # 61
            print(", ".join(sorted(paths)))  # 62
            # 63
            # 64


if __name__ == "__main__":  # 65
    main()  # 66
