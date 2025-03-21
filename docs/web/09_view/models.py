"""Get data from database."""

import os
from pypika import Query, Table
import sqlite3

from util import ModelException, dict_factory


ENV_VAR = "DATA"
STAFF_COLUMNS = ["staff_id", "personal", "family"]


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
    query = Query.from_(staff).select(*STAFF_COLUMNS)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def column(name):
    """Get a single column of staff."""
    if name not in STAFF_COLUMNS:
        raise ModelException(f"Column '{name}' does not exist")

    staff = Table("staff")
    query = Query.from_(staff).select(name)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        return [r[name] for r in cursor.fetchall()]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def row(staff_id):
    """Get a single row of staff."""
    staff = Table("staff")
    query = Query.from_(staff) \
                 .select(*STAFF_COLUMNS) \
                 .where(staff.staff_id == staff_id)
    try:
        connection = connect()
        cursor = connection.execute(str(query))
        result = cursor.fetchall()
        if len(result) == 0:
            raise ModelException(f"no rows match {staff_id}")
        elif len(result) > 1:
            raise ModelException(f"multiple rows match {staff_id}")
        return result[0]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))

