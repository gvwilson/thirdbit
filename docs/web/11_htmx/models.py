"""Get data from database."""

import os
from pypika import Query, Table
import sqlite3

from util import ModelException, dict_factory


ENV_VAR = "DATA"


def connect():
    """Connect to database."""
    path = os.getenv(ENV_VAR)
    if not path:
        raise ModelException(f"Environment variable {ENV_VAR} not set")
    connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = dict_factory
    return connection


def all_staff():
    """Get all staff."""
    staff = Table("staff")
    query = Query.from_(staff).select("staff_id", "personal", "family")
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def experiments(staff_id):
    """Get all experiments performed by staff member."""
    performed = Table("performed")
    experiment = Table("experiment")
    query = Query.from_(experiment)\
                 .inner_join(performed)\
                 .on(experiment.sample_id == performed.sample_id)\
                 .where(performed.staff_id == staff_id)\
                 .select(experiment.star)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))
