"""Test the model layer."""

import sqlite3
from unittest.mock import patch

import models
import util

SCHEMA = """
CREATE TABLE staff (
    staff_id BIGINT, 
    personal TEXT, 
    family TEXT
);
"""

INSERT = """
INSERT INTO staff VALUES(?, ?, ?);
"""

STAFF = [
    (1, "Catalina", "Moyano"),
    (2, "Paloma", "Bellini Ruiz"),
    (4, "Paula", "Martinez"),
]


def make_db():
    connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = util.dict_factory
    connection.executescript(SCHEMA)
    connection.executemany(INSERT, STAFF)
    return connection


def test_can_get_all_staff():
    with patch("models.connect", make_db):
        result = models.all_staff()
        assert len(result) == len(STAFF)
        assert {r["staff_id"] for r in result} == {s[0] for s in STAFF}
