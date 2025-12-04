import json
import plotly.express as px
import polars as pl
import sys


def main():
    data = read_raw()
    df_tasks = build_df(data, "tasks")
    df_workers = build_df(data, "workers")
    print(df_tasks)
    print(df_workers)
    plot(df_workers, "n_dev")
    plot(df_workers, "n_rework")


def build_df(data, key):
    df = None
    for ((needed, chosen), raw) in data.items():
        temp = pl.from_dicts(raw[key]).with_columns(
            pl.lit(needed).alias("needed"),
            pl.lit(chosen).alias("chosen"),
        )
        if df is None:
            df = temp
        else:
            df = pl.concat([df, temp])
    return df


def read_raw():
    data = {}
    for filename in sys.argv[1:]:
        with open(filename, "r") as reader:
            raw = json.load(reader)
            needed = raw["params"]["p_rework_needed"]
            chosen = raw["params"]["p_rework_chosen"]
            data[(needed, chosen)] = raw["summary"]
    return data


def plot(df, key):
    df = df.filter(pl.col("kind") == "dev").group_by(["needed", "chosen"]).agg(pl.col(key).sum())
    fig = px.scatter(df, x="needed", y="chosen", size=key, title=key)
    fig.write_image(f"{key}.svg")


if __name__ == "__main__":
    main()
