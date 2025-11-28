import json
import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) in {1, 3}, "usage: analyze.py [time_plot] [log_time_plot]"

data = json.load(sys.stdin)
df = pl.from_dicts(data).unpivot(
    on=["dev", "test"], index=["id", "quarter"], variable_name="kind", value_name="time"
).filter(pl.col("time") != 0.0).filter(pl.col("kind") == "dev")

fig = px.histogram(df, x="time", facet_col="quarter", facet_col_wrap=2)
if len(sys.argv) == 1:
    fig.show()
else:
    fig.write_image(sys.argv[1])

fig = px.histogram(df, x="time", log_y=True, facet_col="quarter", facet_col_wrap=2)
if len(sys.argv) == 1:
    fig.show()
else:
    fig.write_image(sys.argv[2])
