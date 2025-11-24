import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) == 3, "usage: analyze-queue.py csvfile plotfile"
df = pl.read_csv(sys.argv[1]) \
       .filter((pl.col("kind") == "dev_queue") | (pl.col("kind") == "test_queue"))
fig = px.line(df, x="time", y="count", color="kind")
fig.write_image(sys.argv[2])
