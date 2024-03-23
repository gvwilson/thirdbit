"""Create empty LIMS database."""

import argparse
import sqlite3

from tinydb import TinyDB


CAPABILITIES = [
    {"role": "admin", "capability": "view", "scope": "all"},
    {"role": "admin", "capability": "upload", "scope": "own"},
    {"role": "admin", "capability": "validate", "scope": "all"},
    {"role": "scientist", "capability": "view", "scope": "all"},
    {"role": "scientist", "capability": "upload", "scope": "own"},
    {"role": "intern", "capability": "view", "scope": "own"},
]


def main():
    """Main driver."""
    args = parse_args()
    con = sqlite3.connect(args.sqlite)
    con.row_factory = sqlite3.Row
    rows = con.execute("select personal, family from staff").fetchall()
    rows = [
        {
            "uid": f"{r['personal'][0].lower()}.{r['family'].lower()}",
            "personal": r["personal"],
            "family": r["family"],
        }
        for r in rows
    ]

    with TinyDB(args.tinydb) as db:
        db.truncate()

        capabilities = db.table("capabilities")
        capabilities.truncate()
        for cap in CAPABILITIES:
            capabilities.insert(cap)

        users = db.table("users")
        users.truncate()
        for r in rows:
            users.insert(r)

        roles = db.table("roles")
        roles.truncate()
        admin, intern, scientists = rows[0], rows[1], rows[2:]
        roles.insert({"uid": admin["uid"], "role": "admin"})
        roles.insert({"uid": intern["uid"], "role": "intern"})
        for r in scientists:
            roles.insert({"uid": r["uid"], "role": "scientist"})


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sqlite", type=str, required=True, help="SQLite database file (input)"
    )
    parser.add_argument(
        "--tinydb", type=str, required=True, help="TinyDB database file (output)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
