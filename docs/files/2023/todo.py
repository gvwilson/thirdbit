import sys
from collections import Counter
from datetime import datetime
import plotly.express as px

raw = {}
for line in sys.stdin:
    end, start = [datetime.fromisoformat(x) for x in line.split(" ")[1:3]]
    if start not in raw:
        raw[start] = Counter()
    duration = (end - start).days
    raw[start][duration] += 1

data = {
    "start": [],
    "duration": [],
    "count": []
}
for start in sorted(raw.keys()):
    for duration in sorted(raw[start].keys()):
        data["start"].append(start)
        data["duration"].append(duration)
        data["count"].append(raw[start][duration])

fig = px.scatter(data, x="start", y="duration", size="count", log_y=True)
fig.show()
fig.write_image("todo.svg")
