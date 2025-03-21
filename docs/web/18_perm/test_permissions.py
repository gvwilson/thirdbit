import os
from pypika import AliasedQuery, Query, Table
from pypika.functions import Count
import pytest
import sqlite3
import sys

from util import JsonGroupArray, connect


SIMPLE = [
    (1, "add", True),
    (1, "view", True),
    (1, "delete", True),
    (2, "add", False),
    (2, "view", True),
    (2, "delete", False),
    (3, "add", True),
    (3, "view", True),
    (3, "delete", False),
]


@pytest.mark.parametrize("staff_id, action, expected", SIMPLE)
def test_simple(staff_id, action, expected):
    permission = Table("permission")
    role = Table("role")
    performed = Table("performed")
    query = Query.from_(performed)\
                 .inner_join(role)\
                 .on(performed.staff_id == role.staff_id)\
                 .inner_join(permission)\
                 .on(role.role_name == permission.role_name)\
                 .where((role.staff_id == staff_id) & (permission.capability == action))\
                 .select(performed.sample_id)

    connection = connect()
    cursor = connection.execute(str(query))
    actual = len(cursor.fetchall()) != 0
    assert actual == expected


@pytest.mark.parametrize("staff_id, action, expected", SIMPLE)
def test_packed(staff_id, action, expected):
    permission = Table("permission")
    role = Table("role")
    performed = Table("performed")
    allowed = Table("allowed") # subquery

    subquery = Query.from_(role)\
                    .inner_join(permission)\
                    .on(role.role_name == permission.role_name)\
                    .where((role.staff_id == staff_id) & (permission.capability == action))\
                    .select(Count(permission.capability).as_("allowed"))

    query = Query.with_(subquery, "allowed")\
                 .from_(AliasedQuery("allowed"))\
                 .join(performed)\
                 .on(performed.staff_id == performed.staff_id)\
                 .select(
                     performed.staff_id,
                     allowed.allowed,
                     JsonGroupArray(performed.sample_id).as_("samples__json")
                 )\
                 .where(performed.staff_id == staff_id)\
                 .groupby(performed.staff_id)

    connection = connect()
    cursor = connection.execute(str(query))
    actual = cursor.fetchall()
    assert len(actual) == 1
    actual = actual[0]
    assert set(actual.keys()) == {"staff_id", "allowed", "samples"}
    assert actual["staff_id"] == staff_id
    assert bool(actual["allowed"]) == expected
