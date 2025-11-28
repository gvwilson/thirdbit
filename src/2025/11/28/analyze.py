import json
import sys

import polars as pl
import plotly.express as px


assert 1 <= len(sys.argv) <= 2, "usage: analyze.py [queue_plot]"

data = json.load(sys.stdin)

df = pl.from_dicts(data["task"]).unpivot(
    on=["dev", "test"], index=["id"], variable_name="kind", value_name="value"
).filter(pl.col("value") != 0.0)
fig = px.histogram(df, x="value", color="kind", barmode="group")
fig.update_xaxes(range=[0, 40])
fig.update_yaxes(range=[0, 250])
if len(sys.argv) == 2:
    fig.write_image(sys.argv[1])
else:
    fig.show()
