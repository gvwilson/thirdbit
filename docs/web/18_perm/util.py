"""Utilities."""

import json
import os
from pypika import CustomFunction
import sqlite3


ENV_VAR = "DB"


class AppException(Exception):
    """Root of exception hierarchy."""

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class ModelException(AppException):
    pass


class ViewException(AppException):
    pass


def connect():
    """Connect to database."""
    path = os.getenv(ENV_VAR)
    assert path is not None, (f"Environment variable {ENV_VAR} not set")
    connection = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = dict_factory
    return connection


JsonGroupArray = CustomFunction("json_group_array", ["values"])


def dict_factory(cursor, row):
    """Convert row to dictionary."""
    fields = [column[0] for column in cursor.description]
    return dict(_unpack_json(key, value) for key, value in zip(fields, row))


def _unpack_json(key, value):
    if key.endswith("__json"):
        return key[:-6], json.loads(value)
    return key, value
