import json
import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) in {1, 3}, "usage: analyze.py [time_plot] [count_plot]"

data = json.load(sys.stdin)
df = pl.from_dicts(data).unpivot(
    on=["time_dev", "time_test", "count_dev", "count_test"],
    index=["id", "quarter"],
    variable_name="kind",
    value_name="value"
).filter(pl.col("value") != 0.0)

fig = px.histogram(
    df.filter(pl.col("kind") == "time_dev"),
    x="value",
    facet_col="quarter",
    facet_col_wrap=2,
    labels={"value": "development time"},
)
if len(sys.argv) == 1:
    fig.show()
else:
    fig.write_image(sys.argv[1])

fig = px.histogram(
    df.filter(pl.col("kind") == "count_dev"),
    x="value",
    facet_col="quarter",
    facet_col_wrap=2,
    labels={"value": "number of passes"},
)
if len(sys.argv) == 1:
    fig.show()
else:
    fig.write_image(sys.argv[2])
