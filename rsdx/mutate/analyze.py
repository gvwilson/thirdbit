"""Look for correlation between SNPs and snail size."""

import argparse
import pandas as pd
import plotly.express as px


def main():
    """Main driver."""
    args = parse_args()
    raw = pd.read_csv(args.infile)[["sequence", "reading"]]
    assert (
        len({len(s) for s in raw["sequence"]}) == 1
    ), "Sequences have different lengths"

    pivoted = pivot_dataframe(raw)
    plot(args, pivoted, "all data")

    candidate_locs = select_candidate_locs(raw)
    slimmed = pivoted[pivoted.apply(lambda row: row["loc"] in candidate_locs, axis=1)]
    plot(args, slimmed, "slimmed data")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", type=str, default=None, help="input file")
    parser.add_argument("--plot", action="store_true", default=False, help="show plots")
    return parser.parse_args()


def pivot_dataframe(raw):
    """Turn (sequence, reading) into (loc, base, reading)."""
    pivoted = []
    for _, row in raw.iterrows():
        for i, ch in enumerate(row["sequence"]):
            pivoted.append((i, ch, row["reading"]))
    return pd.DataFrame(pivoted, columns=["loc", "base", "reading"])


def select_candidate_locs(raw):
    """Select locations with more than one base."""
    sequences = list(raw["sequence"])
    keep = set()
    for i in range(len(sequences[0])):
        if len({s[i] for s in sequences}) > 1:
            keep.add(i)
    return keep


def plot(args, df, title):
    """Show standard plots of (subset of) data."""
    if not args.plot:
        return
    summarized = df.groupby(["loc", "base"], as_index=False).agg(func="mean")
    fig = px.scatter(
        summarized,
        x="base",
        y="loc",
        size="reading",
        title=f"{title}: mean by loc and base",
    )
    fig.show()

    sorted = summarized.sort_values("reading", ascending=False)
    sorted["rank"] = sorted.reset_index().index
    fig = px.line(
        sorted,
        x="rank",
        y="reading",
        title=f"{title}: mean by loc and base sorted by rank",
    )
    fig.show()


if __name__ == "__main__":
    main()
