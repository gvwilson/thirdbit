import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) == 3, "usage: analyze-time.py csvfile plotfile"
df = pl.read_csv(sys.argv[1]) \
       .filter((pl.col("kind") == "developer") | (pl.col("kind") == "tester")) \
       .group_by(["kind", "key"]) \
       .agg(pl.mean("value"))
fig = px.bar(df, x="kind", y="value", color="key")
fig.write_image(sys.argv[2])
