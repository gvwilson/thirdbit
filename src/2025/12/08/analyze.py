import json
import plotly.express as px
import polars as pl
import sys


def main():
    data = json.load(sys.stdin)
    tasks = data["tasks"]
    df = pl.from_dicts(tasks).filter(pl.col("completed").is_not_null()).with_columns(
        elapsed=pl.col("completed") - pl.col("started"),
    )
    df = df.with_columns(
        ratio=pl.col("elapsed") / pl.col("dev_required"),
        n_interrupt=pl.col("state").list.count_matches("interrupt"),
    )

    fig = px.histogram(df, x="elapsed", log_y=True, facet_col="developer_id")
    fig.show()
    

if __name__ == "__main__":
    main()
