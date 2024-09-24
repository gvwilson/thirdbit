from collections import Counter, defaultdict
import csv
import pandas as pd
import plotly.express as px
import sys

columns = [
    "timestamp",
    "read",
    "write",
    "background",
    "email",
]
keys = {c: i for i, c in enumerate(columns)}

reader = csv.reader(open("unwritten-2024-01.csv", "r"))
to_read = Counter()
to_write = Counter()
authors = defaultdict(set)
for i, line in enumerate(reader):
    if i == 0:
        continue
    for src, coll in (("read", to_read), ("write", to_write)):
        titles = [x.strip() for x in line[keys[src]].split(",")]
        titles = [x for x in titles if x]
        for t in titles:
            coll[t] += 1
            if src == "write" and line[keys["email"]]:
                authors[t].add(line[keys["email"]])

for title in sorted(authors.keys(), key=lambda x: len(authors[x]), reverse=True):
    print(f"({len(authors[title]):2d}) {title}: {', '.join(sorted(authors[title]))}")

result = {
    "title": [],
    "kind": [],
    "count": []
}
for title in sorted(set(to_read.keys()) | set(to_write.keys()), key=lambda x: to_read.get(x, 0)):
    for (kind, source) in (("read", to_read), ("write", to_write)):
        result["title"].append(title)
        result["kind"].append(kind)
        result["count"].append(source.get(title, 0))

df = pd.DataFrame(data=result)
fig = px.bar(df, y="title", x="count", color="kind", barmode="group", width=1000, height=600)
fig.write_image("unwritten-2024-01.png")
fig.write_image("unwritten-2024-01.svg")
