"""Parse messy data files."""

import argparse
import csv
from enum import Enum
import sys
import pandas as pd


class State(Enum):
    """Enumerate possible parser states."""

    HEADER = "header"
    SEARCHING = "searching"
    BODY = "body"
    DONE = "done"


def main():
    """Main driver."""
    args = parse_args()

    if args.infile:
        with open(args.infile, "r") as reader:
            df = load(reader)
    else:
        df = load(sys.stdin)

    if args.outfile:
        with open(args.outfile, "w") as writer:
            df.to_csv(writer, index=False)
    else:
        df.to_csv(sys.stdout, index=False)


def is_empty(row):
    """Is this row effectively empty?"""
    return not any(row)


def is_start_of_body(row):
    """Is this row the start of the body section?"""
    return (len(row) > 0 and row[0].lower() == "site") or (
        len(row) > 1 and row[1].lower() == "site"
    )


def load(reader):
    """Load messy data."""
    lines = [row for row in csv.reader(reader)]
    header, body = split(lines)
    titles, data = normalize(body)
    assert titles[0] == "site"
    return pd.DataFrame(data, columns=titles)


def normalize(rows):
    """Remove leading spaces from rows if necessary."""
    if rows[0][0] == "":
        rows = [r[1:] for r in rows]
    return [r.lower() for r in rows[0]], rows[1:]


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", type=str, default=None, help="input file")
    parser.add_argument("--outfile", type=str, default=None, help="output file")
    return parser.parse_args()


def split(rows):
    """Split header from body."""
    header = []
    body = []
    state = State.HEADER
    for row in rows:
        if state == State.HEADER:
            if is_empty(row):
                state = State.SEARCHING
            elif is_start_of_body(row):
                state = State.BODY
                body.append(row)
            else:
                header.append(row)

        elif state == State.SEARCHING:
            if is_start_of_body(row):
                state = State.BODY
                body.append(row)

        elif state == State.BODY:
            if is_empty(row):
                state = State.DONE
            else:
                body.append(row)

        else:
            assert state == State.DONE

    return header, body


if __name__ == "__main__":
    main()
