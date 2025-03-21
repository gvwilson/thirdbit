"""Database migration."""

import argparse
from pathlib import Path
import re
import sqlite3
import sys


PATTERNS = {
    "bwd": re.compile(r"^(\d+)_bwd_(.+)"),
    "check": re.compile(r"^(\d+)_check_(.+)"),
    "fwd": re.compile(r"^(\d+)_fwd_(.+)"),
}


def handle_check_file(connection, migration_file, direction, opt):
    """Handle the check file for a given migration."""
    check_filename = migration_file.with_name(
        migration_file.name.replace(f"_{direction}_", "_check_", 1)
    )
    if check_filename.exists():
        check_migration(connection, check_filename, opt.verbose)
    elif not opt.skip_missing_checks:
        print(f"Warning: Check file {check_filename} not found. Aborting.")
        sys.exit(1)
    else:
        print(f"Warning: Check file {check_filename} not found. Skipping.")


def main():
    """Main driver."""
    opt = parse_args()
    connection = sqlite3.connect(opt.db)
    if opt.forward:
        direction = "fwd"
    elif opt.backward:
        direction = "bwd"
    else:
        assert False, "Unknown direction"
    migrations = get_migrations(opt.migrations, direction, opt.limit)
    
    # Validate all check files before starting migrations
    if not validate_check_files(migrations, direction, opt):
        print("Aborting due to missing check files.")
        sys.exit(1)
    
    for filename in migrations if opt.forward else reversed(migrations):
        if opt.backward:
            handle_check_file(connection, filename, direction, opt)
        
        migrate(connection, filename, opt.verbose)
        
        if opt.forward:
            handle_check_file(connection, filename, direction, opt)


def get_migrations(dirpath, direction, limit):
    """Find migration files."""
    pat = PATTERNS[direction]
    result = []
    for filepath in sorted(Path(dirpath).glob("*.sql")):
        m = pat.match(str(filepath.name))
        if not m:
            continue
        if limit and (m.group(1) > limit):
            continue
        result.append(filepath)
    return result


def migrate(connection, filename, verbose):
    """Apply migration."""
    if verbose:
        print(f"migrating {filename}")
    connection.executescript(filename.read_text())


def check_migration(connection, filename, verbose):
    """Perform check migration."""
    if verbose:
        print(f"checking {filename}")
    try:
        connection.executescript(filename.read_text())
    except sqlite3.Error as e:
        print(f"Check failed for {filename}: {e}")
        sys.exit(1)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--backward", action="store_true", help="migrate backward")
    parser.add_argument("--db", required=True, help="database file")
    parser.add_argument("--forward", action="store_true", help="migrate forward")
    parser.add_argument("--migrations", type=str, required=True, help="migrations directory")
    parser.add_argument("--limit", type=str, help="how far to go or where to start regression")
    parser.add_argument("--verbose", action="store_true", help="report progress")
    parser.add_argument("--skip-missing-checks", action="store_true", help="skip missing check files instead of aborting")
    opt = parser.parse_args()

    if (opt.backward + opt.forward) != 1:
        print("Must specify exactly one of --forward or --backward")
        sys.exit(1)


    return opt


def validate_check_files(migrations, direction, opt):
    """Validate that all required check files exist before starting migrations."""
    all_checks_exist = True
    for migration_file in migrations:
        check_filename = migration_file.with_name(
            migration_file.name.replace(f"_{direction}_", "_check_", 1)
        )
        if not check_filename.exists():
            if opt.skip_missing_checks:
                print(f"Warning: Check file {check_filename} not found. Will be skipped during migration.")
            else:
                print(f"Error: Check file {check_filename} not found.")
                all_checks_exist = False
    return all_checks_exist or opt.skip_missing_checks

if __name__ == "__main__":
    main()