"""Read data using Pony ORM."""

from datetime import date

import pandas as pd
from pony import orm

DB = orm.Database()


class Sites(DB.Entity):
    """Survey sites."""

    site = orm.PrimaryKey(str)
    lon = orm.Required(float)
    lat = orm.Required(float)
    surveys = orm.Set("Surveys")


class Surveys(DB.Entity):
    """Surveys done."""

    label = orm.PrimaryKey(int)
    site = orm.Required(Sites)
    date = orm.Required(date)
    samples = orm.Set("Samples")


class Samples(DB.Entity):
    """Individual samples."""

    rowid = orm.PrimaryKey(int, auto=True)
    label = orm.Required(Surveys)
    lon = orm.Required(float)
    lat = orm.Required(float)
    reading = orm.Required(float)


def read_data(dbfile):
    """Read database and do calculations with Pony ORM."""
    DB.bind("sqlite", dbfile, create_db=False)
    DB.generate_mapping(create_tables=False)
    with orm.db_session:
        combined = orm.select((s.label.label, s.lon, s.lat, s.reading) for s in Samples)
        combined = pd.DataFrame(combined, columns=["label", "lon", "lat", "reading"])
        centers = orm.select(
            (
                site.site,
                orm.sum(
                    sample.lon * sample.reading
                    for sample in Samples
                    if sample.label.site == site
                )
                / orm.sum(
                    sample.reading for sample in Samples if sample.label.site == site
                ),
                orm.sum(
                    sample.lat * sample.reading
                    for sample in Samples
                    if sample.label.site == site
                )
                / orm.sum(
                    sample.reading for sample in Samples if sample.label.site == site
                ),
            )
            for site in Sites
        )
        centers = pd.DataFrame(centers, columns=["site", "lon", "lat"])
        return {
            "combined": combined,
            "centers": centers,
        }
