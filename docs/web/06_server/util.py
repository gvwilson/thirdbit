import os
import polars as pl
from prettytable import from_csv


ENV_VAR = "DATA"
HTTP_400_BAD_REQUEST = 400


def as_dataframe():
    """Load dataframe from file specified by DATA environment variable."""
    path = os.getenv(ENV_VAR)
    assert path, f"Environment variable {ENV_VAR} not set"
    return pl.read_csv(path)


def as_html():
    """Load HTML from file specified by DATA environment variable."""
    path = os.getenv(ENV_VAR)
    assert path, f"Environment variable {ENV_VAR} not set"
    with open(path, "r") as reader:
        return from_csv(reader).get_formatted_string("html")
