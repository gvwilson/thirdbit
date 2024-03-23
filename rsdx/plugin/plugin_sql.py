"""Load data from SQLite database using Pandas."""

import pandas as pd
import sqlite3

import util


Q_CENTERS = """
select
    surveys.site,
    sum(samples.lon * samples.reading) / sum(samples.reading) as lon,
    sum(samples.lat * samples.reading) / sum(samples.reading) as lat
from surveys join samples
on surveys.label = samples.label
group by surveys.site
"""


def read_data(dbfile):
    """Read tables and do calculations directly in SQL."""
    con = sqlite3.connect(dbfile)
    return {
        "combined": pd.read_sql(util.Q_SAMPLES, con),
        "centers": pd.read_sql(Q_CENTERS, con),
    }
