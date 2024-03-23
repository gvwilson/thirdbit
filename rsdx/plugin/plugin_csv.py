"""Load data from CSV files given directory."""

from pathlib import Path

import pandas as pd

import util


def read_data(csvdir):
    """Read CSV files directly into dataframes."""
    raw = [pd.read_csv(filename) for filename in Path(csvdir).glob("*.csv")]
    return util.combine_with_pandas(*raw)
