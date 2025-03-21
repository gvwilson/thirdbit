"""Explore data insertion."""

from pypika import Query, Table
import pypika.functions as fn
import sys

from models import connect


def main():
    """Main driver."""
    personal = sys.argv[1]
    family = sys.argv[2]
    how = sys.argv[3]

    staff = Table("staff")
    connection = connect()

    if how == "split":
        split(connection, staff, personal, family)
    elif how == "combined":
        combined(connection, staff, personal, family)
    else:
        print(f"unknown {how}")
        sys.exit(1)

    show(connection, staff)


def split(connection, staff, personal, family):
    """Do insertion in two steps."""
    query = Query.from_(staff).select(fn.Max(staff.staff_id).as_("max_staff_id"))
    cursor = connection.execute(str(query))
    largest = cursor.fetchall()[0]["max_staff_id"]
    print(f"largest existing ID {largest}")

    query = Query.into(staff).insert(largest + 1, personal, family)
    cursor = connection.execute(str(query))


def combined(connection, staff, personal, family):
    """Do insertion in a single step."""
    subquery = Query.from_(staff).select(fn.Max(staff.staff_id) + 1)
    query = Query.into(staff).insert(subquery, personal, family)
    print(query)
    connection.execute(str(query))


def show(connection, staff):
    query = Query.from_(staff).select(staff.staff_id, staff.personal, staff.family)
    cursor = connection.execute(str(query))
    print("final table:")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    main()
