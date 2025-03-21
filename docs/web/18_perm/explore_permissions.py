# Imports
from pypika import AliasedQuery, Query, Table
from pypika.functions import Count
import sqlite3

# Create tables and insert values.
# 'permission' shows who can do what: ahmed can view things, other people cannot.
# 'samples' contains the data people want to view.
SETUP = """\
CREATE TABLE permission (
  person TEXT,
  capability TEXT
);
INSERT INTO permission VALUES
  ('ahmed', 'view')
;

CREATE TABLE samples (
  label TEXT
);
INSERT INTO samples VALUES
  ('first'),
  ('second')
;
"""

# Create database.
connection = sqlite3.connect(":memory:")
connection.executescript(SETUP)

# Represent tables.
permission = Table("permission")
samples = Table("samples")

# Build a permission query.
# Result is a single row (name, 0/1), e.g., ('ahmed', 1) or ('zephyr', 0).
def make_permission_query(person, capability):
    return Query.from_(permission)\
                .where((permission.person == person) & (permission.capability == capability))\
                .select(permission.person, Count(permission.capability).as_("allowed"))

# Demonstrate that 'make_permission_query' works as intended.
ahmed_view = make_permission_query("ahmed", "view")
print("ahmed view:", str(ahmed_view))
print(connection.execute(str(ahmed_view)).fetchall())

zephyr_view = make_permission_query("zephyr", "view")
print("zephyr view:", str(zephyr_view))
print(connection.execute(str(zephyr_view)).fetchall())

# And now the problem: get the labels a person is allowed to view.
# Desired result is a list of (allowed, label) pairs, e.g.:
#
# for ahmed: [(1, 'first'), (1, 'second')]
# for zephyr: [(0, 'first'), (0, 'second')]
#
# Note that we do _not_ want an empty list for someone who can't view
# anything, since that would make it impossible to distinguish "no data"
# from "no permission".

perm = Table("perm") # so that subquery fields can be named with dot notation

# 1: add the CTE to the query but don't use it
query = Query.with_(ahmed_view, "perm")\
             .from_(AliasedQuery("perm"))\
             .select(samples.label)
print(f"\n1. query with unused CTE tries to get 'label' from 'perm'\n{str(query)}")

# 2: select from samples and then add CTE
query = Query.from_(samples)\
             .with_(ahmed_view, "perm")\
             .select(samples.label)
print(f"\n2. query starting with samples but not joining\n{str(query)}")

# 3: select from both tables without explicit join
query = Query.from_(samples)\
             .with_(ahmed_view, "perm")\
             .select(samples.label, perm.person, perm.allowed)
print(f"\n3. select from both tables without explicit join tries to get everything from samples\n{str(query)}")

# 4: try joining without .on
try:
    query = Query.with_(ahmed_view, "perm")\
                 .from_(AliasedQuery("perm"))\
                 .join(samples)\
                 .select(samples.label, perm.person, perm.allowed)
except Exception as exc:
    print(f"\n4. attempt to join without .on raises exception {exc}")

# 5: try joining with True
try:
    query = Query.with_(ahmed_view, "perm")\
                 .from_(AliasedQuery("perm"))\
                 .join(samples)\
                 .on(True)\
                 .select(samples.label, perm.person, perm.allowed)
except Exception as exc:
    print(f"\n5. attempt to join with True raises exception {exc}")

# 6: try joining with True
try:
    query = Query.with_(ahmed_view, "perm")\
                 .from_(AliasedQuery("perm"))\
                 .join(samples)\
                 .on(True)\
                 .select(samples.label, perm.person, perm.allowed)
except Exception as exc:
    print(f"\n6. attempt to join with True raises exception {exc}")

# 7: try joining with 'label==label'
query = Query.with_(ahmed_view, "perm")\
             .from_(AliasedQuery("perm"))\
             .join(samples)\
             .on(samples.label == samples.label)\
             .select(samples.label, perm.person, perm.allowed)
print(f"\n7a. joining with 'label == label' for ahmed\n{str(query)}")
print(connection.execute(str(query)).fetchall())

query = Query.with_(zephyr_view, "perm")\
             .from_(AliasedQuery("perm"))\
             .join(samples)\
             .on(samples.label == samples.label)\
             .select(samples.label, perm.person, perm.allowed)
print(f"\n7b. joining with 'label == label' for zephyr\n{str(query)}")
print(connection.execute(str(query)).fetchall())
