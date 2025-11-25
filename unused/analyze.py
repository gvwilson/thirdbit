import json
import sys

import polars as pl
import plotly.express as px


assert len(sys.argv) == 3, "usage: analyze-queue.py queue_plot time_plot"

data = json.load(sys.stdin)

# Queue lengths
dev = pl.from_dicts(data["dev_queue"]) \
        .with_columns(pl.lit("dev").alias("kind"))
test = pl.from_dicts(data["test_queue"]) \
         .with_columns(pl.lit("test").alias("kind"))
df = pl.concat([dev, test])
fig = px.line(df, x="time", y="count", color="kind")
fig.write_image(sys.argv[1])

# Times
dev = pl.from_dicts(data["developer"])
test = pl.from_dicts(data["tester"])
df = pl.concat([dev, test]) \
       .unpivot(
           on=["working", "waiting"],
           index=["name", "id"],
           variable_name="kind",
           value_name="value"
       ) \
       .group_by(["name", "kind"]) \
       .agg(pl.mean("value"))
print(df)
fig = px.bar(df, x="name", y="value", color="kind")
fig.write_image(sys.argv[2])
