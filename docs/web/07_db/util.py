"""Utilities."""

def dict_factory(cursor, row):
    """Convert row to dictionary."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
