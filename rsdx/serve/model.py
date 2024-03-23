"""Execute SQL queries using Pony ORM."""

from datetime import date
import os
from pathlib import Path

from pony import orm


DB_FILE = str(Path(os.getenv("RSDX_DATA"), "assays.db"))
DB = orm.Database()


class Staff(DB.Entity):
    """Staff members."""

    ident = orm.PrimaryKey(int, auto=True)
    personal = orm.Required(str)
    family = orm.Required(str)
    performed = orm.Set("Performed")
    invalidated = orm.Set("Invalidated")


class Experiment(DB.Entity):
    """Experiments."""

    ident = orm.PrimaryKey(int, auto=True)
    kind = orm.Required(str)
    started = orm.Required(date)
    ended = orm.Optional(date)
    performed = orm.Set("Performed")
    plates = orm.Set("Plate")


class Performed(DB.Entity):
    """Who was involved in which experiments."""

    staff = orm.Required(Staff)
    experiment = orm.Required(Experiment)
    orm.PrimaryKey(staff, experiment)


class Plate(DB.Entity):
    """Plates used in experiments."""

    ident = orm.PrimaryKey(int, auto=True)
    experiment = orm.Required(Experiment)
    upload_date = orm.Required(date)
    filename = orm.Required(str, unique=True)
    invalidated = orm.Set("Invalidated")


class Invalidated(DB.Entity):
    """Invalidated plates."""

    plate = orm.Required(Plate)
    staff = orm.Required(Staff)
    invalidate_date = orm.Required(date)
    orm.PrimaryKey(plate, staff)


DB.bind("sqlite", DB_FILE, create_db=False)
DB.generate_mapping(create_tables=False)


def get_all(kind):
    """Get all entries of particular kind."""
    with orm.db_session:
        if kind == "staff":
            columns = ["ident", "personal", "family"]
            rows = list(orm.select((s.ident, s.personal, s.family) for s in Staff))
        elif kind == "experiments":
            columns = ["ident", "kind", "started", "ended", "num_plates"]
            rows = list(
                orm.select(
                    (e.ident, e.kind, e.started, e.ended, orm.count(e.plates))
                    for e in Experiment
                )
            )
        elif kind == "plates":
            columns = ["ident", "experiment", "uploaded", "invalidated"]
            rows = list(
                orm.select(
                    (
                        p.ident,
                        p.experiment.ident,
                        p.upload_date,
                        orm.exists(p.invalidated),
                    )
                    for p in Plate
                )
            )
        else:
            assert False, f"Unknown kind {kind}"
        return columns, rows


def get_count(kind):
    """How many entries of the given kind?"""
    with orm.db_session:
        if kind == "staff":
            return orm.count(s for s in Staff)
        if kind == "experiments":
            return orm.count(e for e in Experiment)
        if kind == "plates":
            return orm.count(p for p in Plate)
    assert False, f"Unknown kind {kind}"


def get_plate_filename(plate_id):
    """Where is the plate data stored?"""
    with orm.db_session:
        return orm.select(p.filename for p in Plate if p.ident == plate_id).first()
