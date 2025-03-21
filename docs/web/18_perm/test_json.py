from pypika import Query, Table
import pytest
import sys

from util import JsonGroupArray, connect


def test_json():
    connection = connect()
    performed = Table("performed")
    query = Query.from_(performed)\
        .select(performed.staff_id, JsonGroupArray(performed.sample_id).as_("samples__json"))\
        .groupby(performed.staff_id)
    cursor = connection.execute(str(query))
    print(cursor.fetchall())
