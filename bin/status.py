import argparse
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from prettytable import MARKDOWN, PrettyTable
import sys

WEEK = 7


def main():
    options = parse_args()

    # Load data.
    info = pd.read_csv(options.info)
    status = pd.read_csv(options.status)\
               .groupby("story")\
               .filter(lambda x: len(x) > 1)\
               .sort_values("date")

    # Find word counts of active stories and show current totals.
    df = status.set_index("story")\
               .join(info.set_index("story"))\
               .sort_values(["title", "date"])\
               .reset_index()\
               [["title", "date", "words", "category"]]
    df["date"] = pd.to_datetime(df["date"]).dt.date
    start = df.drop_duplicates(["title"], keep="first")\
              .rename(columns={"date": "start", "words": "initial"})\
              [["title", "initial", "start"]]
    current = df.drop_duplicates(["title"], keep="last")
    summary = start.set_index("title").join(current.set_index("title")).reset_index()
    summary["diff"] = summary["words"] - summary["initial"]
    print(summary[["title", "date", "words", "diff"]].to_markdown(index=False))

    # Find change over time.
    df["change"] = df[["title", "date", "words"]]\
                     .groupby("title")\
                     .diff()["words"]
    change = df.dropna()[["date", "change"]]\
               .groupby(["date"])\
               .sum("change")\
               .reset_index()
    change = change[change["change"] != 0]
    change = change.rename(columns={"change": "words"})
    change["title"] = "change"

    # Fill in missing dates.
    known = set(change["date"])
    min_date = min(change["date"])
    max_date = max(datetime.today().date(), max(change["date"]))
    num_days = (max_date - min_date).days + 1
    full = {min_date + timedelta(days=d) for d in range(0, num_days)}
    missing = pd.DataFrame({"title": "change", "words": 0, "date": list(sorted(full - known))})
    change = pd.concat([change, missing]).sort_values("date").reset_index()
    print(f'\n{change[["date", "words"]].tail(n=WEEK).to_markdown(index=False)}')

    # Show overall rate.
    print(f'\nrate: {int(sum(summary["diff"]) / num_days)} words/day')

    # Combine stories and changes for plotting.
    change["category"] = "delta"
    df = pd.concat([df[["title", "date", "words", "category"]], change])

    # Plot.
    fig = px.line(df, x="date", y="words", color="title", line_shape="hv", facet_row="category")
    date_offset = timedelta(days=1)
    fig.update_xaxes(range=[min_date - date_offset, max_date + date_offset])
    fig.update_yaxes(matches=None)
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    if options.show:
        fig.show()
    fig.write_image(options.chart, width=800, height=800)


def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", required=True, help="Chart filename")
    parser.add_argument("--info", required=True, help="Information about stories")
    parser.add_argument("--show", action="store_true", help="Show plot")
    parser.add_argument("--status", required=True, help="Status information")
    return parser.parse_args()


if __name__ == "__main__":
    main()
