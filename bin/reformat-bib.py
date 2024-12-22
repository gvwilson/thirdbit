from bs4 import BeautifulSoup
import sys

HEADER = """\
---
title: "References"
template: page
---
<dl class="bibliography">
"""

FOOTER = """</dl>"""

doc = BeautifulSoup(sys.stdin.read(), "html.parser")
print(HEADER)
for node in doc.select("div.csl-entry"):
    node.name = "dd"
    ident = node["id"].replace("ref-", "", 1)
    del node["class"]
    del node["role"]
    del node["id"]
    print(f'<dt id="{ident}">{ident}</dt>')
    print(node)
print(FOOTER)
