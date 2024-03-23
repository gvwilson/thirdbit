"""Load data from database using Pandas."""

import sqlite3

import pandas as pd

import util


def read_data(dbfile):
    """Read database tables into Pandas dataframes and manipulate."""
    con = sqlite3.connect(dbfile)
    raw = pd.read_sql(util.Q_SAMPLES, con)
    return util.combine_with_pandas(raw)
