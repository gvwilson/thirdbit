from pypika import Query, Table
import sqlite3
import sys

import util

connection = sqlite3.connect(sys.argv[1], detect_types=sqlite3.PARSE_DECLTYPES)
connection.row_factory = util.dict_factory

staff = Table("staff")
q = Query.from_(staff).select("staff_id", "personal", "family")
print(str(q))
cursor = connection.execute(str(q))
for row in cursor.fetchall():
    print(row)
