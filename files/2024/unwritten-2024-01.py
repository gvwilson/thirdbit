from collections import Counter
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

reader = csv.reader(sys.stdin)
to_read = Counter()
to_write = Counter()
for i, line in enumerate(reader):
    if i == 0:
        continue
    for src, coll in (("read", to_read), ("write", to_write)):
        for name in [x.strip() for x in line[keys[src]].split(",")]:
            if name:
                coll[name] += 1

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
fig.show()
fig.write_image("unwritten-2024-01.png")
fig.write_image("unwritten-2024-01.svg")
