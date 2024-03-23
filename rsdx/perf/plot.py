"""Plot results from sweep."""

from pathlib import Path
import pandas as pd
import plotly.express as px
import sys

infile = Path(sys.argv[1])
df = pd.read_csv(sys.argv[1]).rename(columns={"width": "size"})
df["label"] = df["kind"] + "_" + df["depth"].astype(str).str.zfill(3)
summary = (
    df[["label", "size", "time"]]
    .groupby(["label", "size"], as_index=False)
    .agg(func="mean")
)
fig = px.line(summary, x="size", y="time", color="label")
fig.show()
fig.write_image(f"{infile.stem}.svg")
fig.write_image(f"{infile.stem}.pdf")
