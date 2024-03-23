"""Utilities shared by plugins."""

import pandas as pd

# Query to select all samples from database in normalized form.
Q_SAMPLES = """
select
    surveys.site,
    samples.lon,
    samples.lat,
    samples.reading
from surveys join samples
on surveys.label = samples.label
"""


def combine_with_pandas(*tables):
    """Combine tables using Pandas."""
    combined = pd.concat(tables)
    temp = pd.DataFrame(
        {
            "site": combined["site"],
            "weighted_lon": combined["lon"] * combined["reading"],
            "weighted_lat": combined["lat"] * combined["reading"],
            "reading": combined["reading"],
        }
    )
    temp = (
        temp.groupby(["site"])
        .agg({"weighted_lon": "mean", "weighted_lat": "mean", "reading": "mean"})
        .reset_index()
    )
    centers = pd.DataFrame(
        {
            "site": temp["site"],
            "lon": temp["weighted_lon"] / temp["reading"],
            "lat": temp["weighted_lat"] / temp["reading"],
        }
    )
    return {"combined": combined, "centers": centers}
