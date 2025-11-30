import json
import plotly.express as px
import polars as pl
import sys


def main():
    data = json.load(sys.stdin)
    params = data["params"]

    # Task states over time.
    df = (
        pl.from_dicts(data["snapshot"]["tasks"])
        .group_by(["time", "state"])
        .agg(pl.len())
        .sort("time")
    )
    fig = px.line(df, x="time", y="len", color="state")
    manage(fig, "tasks")

    # Queue lengths.
    df = pl.from_dicts(data["snapshot"]["queues"])
    fig = px.line(df, x="time", y="length", color="name")
    manage(fig, "queues")

    # Worker states.
    df = (
        pl.from_dicts(data["snapshot"]["workers"])
        .with_columns(
            pl.concat_str([pl.col("kind"), pl.col("state")], separator="_").alias(
                "kind_state"
            )
        )
        .group_by(["time", "kind_state"])
        .agg(pl.len())
        .sort("time")
        .pivot(index="time", on="kind_state", values="len")
        .fill_null(0)
        .unpivot(index="time", variable_name="kind_state", value_name="count")
    )
    fig = px.line(df, x="time", y="count", color="kind_state")
    manage(fig, "workers")


def manage(fig, name):
    if len(sys.argv) == 1:
        fig.show()
    elif len(sys.argv) == 2:
        fig.write_image(f"{sys.argv[1]}_{name}.svg")


if __name__ == "__main__":
    main()
