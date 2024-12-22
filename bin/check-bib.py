import bibtexparser as bp
from pathlib import Path
import re
import sys

KEY_PAT = re.compile(r'^(.+)(\d\d\d\d)(.*)$')
FILENAME_PAT = re.compile(r'([^-]+).+(\d\d\d\d)\.pdf')


def main():
    bib_dir = Path(sys.argv[1])
    if not bib_dir.exists():
        print(f"no such directory {bib_dir}")
        sys.exit(1)

    library = bp.parse_string(sys.stdin.read())
    unused_files(bib_dir, library)

    report(
        bib_dir,
        library,
        "no local file",
        lambda _, key, value: "local" not in value,
        lambda key, value: f"- {key}"
    )

    report(
        bib_dir,
        library,
        "file not found",
        file_exists,
        lambda key, value: f"- {key}: {value['local']}"
    )

    report(
        bib_dir,
        library,
        "person name and filename disagree",
        person_name_match,
        lambda key, value: f"- {key}: {value['local']}"
    )

    report(
        bib_dir,
        library,
        "years disagree",
        years_match,
        lambda key, value: f"- {key}: {value['local']}"
    )


def file_exists(bib_dir, key, value):
    if "local" not in value:
        return False
    return not Path(bib_dir, value["local"][0].lower(), value["local"]).is_file()


def person_name_match(bib_dir, key, value):
    if "local" not in value:
        return False
    m = KEY_PAT.match(key)
    if not m:
        return True
    expected = m.group(1)
    m = FILENAME_PAT.match(value["local"])
    if not m:
        return False
    return expected != m.group(1)


def report(bib_dir, library, title, test, fmt):
    keys = {key for key, value in library.entries_dict.items() if test(bib_dir, key, value)}
    if not keys:
        return
    print("\n#", title, f"({len(keys)})")
    for k in sorted(keys):
        print(fmt(k, library.entries_dict[k]))


def unused_files(bib_dir, library):
    actual = {str(x.name) for x in list(bib_dir.glob("*/*.pdf")) if "misc/" not in str(x)}
    expected = {value["local"] for value in library.entries_dict.values() if "local" in value}
    extra = actual - expected
    if extra:
        print("\n#", "unused files", f"({len(extra)})")
        for x in sorted(extra):
            print(f"- {x}")


def years_match(bib_dir, key, value):
    if "local" not in value:
        return False
    m = KEY_PAT.match(key)
    if not m:
        return True
    name, year = m.group(1), m.group(2)
    m = FILENAME_PAT.match(value["local"])
    if not m:
        return False
    return (name == m.group(1)) and (year != m.group(2))


if __name__ == "__main__":
    main()
