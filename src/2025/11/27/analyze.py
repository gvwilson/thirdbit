import json
import sys

import polars as pl
import plotly.express as px


assert 1 <= len(sys.argv) <= 2, "usage: analyze-queue.py [queue_plot]"

data = json.load(sys.stdin)

df = pl.from_dicts(data["queue"]).with_columns(
    pl.concat_str(["queue", "priority"], separator="-").alias("which")
).sort("which")
fig = px.line(df, x="time", y="count", color="which")
if len(sys.argv) == 2:
    fig.write_image(sys.argv[1])
else:
    fig.show()
