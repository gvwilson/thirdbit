from pathlib import Path
import re
import sys

XLINK = re.compile(r'<xref\s+linkend="(.+?)"/>')
DEF = re.compile(r'<(\w+)\s+id="(.+?)"\s+label="(.+?)">')


def main():
    html = Path(sys.argv[1]).read_text()
    defs = {m[1]: format_def(m) for m in DEF.findall(html)}
    html = XLINK.sub(lambda m: replace(m, defs), html)
    print(html)


def format_def(m):
    return f"{m[0].title()}&nbsp;{m[2]}"


def replace(m, defs):
    key = m.group(1)
    if key in defs:
        return f'<a href="#{key}">{defs[key]}</a>'
    print(f"missing {key}", file=sys.stderr)
    return m.group(0)


if __name__ == "__main__":
    main()
