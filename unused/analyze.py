import json
import plotly.express as px
import polars as pl
import sys


def main():
    data = json.load(sys.stdin)
    params = data["params"]
    log = (
        pl.from_dicts(data["log"])
        .unpivot(index=["time"], variable_name="key", value_name="value")
        .sort(["time"])
    )
    tasks = pl.from_dicts(data["tasks"]).sort(["id"])
    developers = pl.from_dicts(data["developers"]).sort(["id"])
    testers = pl.from_dicts(data["testers"]).sort(["id"])

    fig = px.line(
        log.filter(pl.col("key").str.starts_with("task_")).with_columns(pl.col("value").alias("length")),
        x="time",
        y="length",
        color="key",
    )
    manage(fig, "queues")

    temp = tasks.filter(pl.col("state") == "task_complete").with_columns(
        pl.col("n_dev").alias("num_iterations"),
        (pl.col("t_dev") + pl.col("t_test")).alias("total_time"),
    )
    fig = px.scatter(temp, x="num_iterations", y="total_time")
    fig.update_traces(marker={"size": 12})
    manage(fig, "time")

    temp = pl.concat(
        [
            developers.with_columns(pl.lit("developer").alias("kind")),
            testers.with_columns(pl.lit("tester").alias("kind")),
        ]
    ).with_columns((100 * pl.col("busy") / params["sim_time"]).alias("busy"))
    fig = px.scatter(temp, x="n_task", y="busy", color="kind")
    fig.update_yaxes(range=[0, 100]).update_traces(marker={"size": 12})
    manage(fig, "workers")


def manage(fig, name):
    if len(sys.argv) == 1:
        fig.show()
    elif len(sys.argv) == 2:
        fig.write_image(f"{sys.argv[1]}_{name}.svg")


if __name__ == "__main__":
    main()
