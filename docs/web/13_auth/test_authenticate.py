"""Test authentication."""

import sqlite3
from unittest.mock import patch

import models
import util

SCHEMA = """
CREATE TABLE staff (
    staff_id BIGINT, 
    personal TEXT, 
    family TEXT,
    username TEXT NOT NULL DEFAULT "",
    password TEXT NOT NULL DEFAULT ""
);
"""

INSERT = """
INSERT INTO staff VALUES(?, ?, ?, ?, ?);
"""

STAFF = [
    (1, "Catalina", "Moyano", "catalina.m", "123"),
    (2, "Paloma", "Bellini Ruiz", "bellini.r", "456"),
    (4, "Paula", "Martinez", "paula.m", "789"),
]


def make_db():
    connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = util.dict_factory
    connection.executescript(SCHEMA)
    connection.executemany(INSERT, STAFF)
    return connection


def test_can_authenticate_correctly():
    with patch("models.connect", make_db):
        assert models.authenticate("catalina.m", "123") == "catalina.m"


def test_fail_authenticate_with_wrong_password():
    with patch("models.connect", make_db):
        assert models.authenticate("catalina.m", "999") is None
