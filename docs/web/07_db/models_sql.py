"""Get data from database."""

import os
import sqlite3

import util


ENV_VAR = "DATA"


class ModelException(Exception):
    """Problems with queries."""

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


def connect():
    """Connect to database."""
    path = os.getenv(ENV_VAR)
    if not path:
        raise ModelException(f"Environment variable {ENV_VAR} not set")
    connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = util.dict_factory
    return connection


def all_staff():
    """Get all staff."""
    query = """
    select * from staff
    """
    try:
        connection = connect()
        cursor = connection.execute(query)
        return cursor.fetchall()
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def column(name):
    """Get a single column of staff."""
    query = f"""
    select {name} from staff
    """
    try:
        connection = connect()
        cursor = connection.execute(query)
        return [r[name] for r in cursor.fetchall()]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))


def row(staff_id):
    """Get a single row of staff."""
    query = """
    select * from staff where staff_id=?
    """
    try:
        connection = connect()
        cursor = connection.execute(query, (staff_id,))
        result = cursor.fetchall()
        if len(result) == 0:
            raise ModelException(f"no rows match {staff_id}")
        elif len(result) > 1:
            raise ModelException(f"multiple rows match {staff_id}")
        return result[0]
    except sqlite3.DatabaseError as exc:
        raise ModelException(str(exc))
