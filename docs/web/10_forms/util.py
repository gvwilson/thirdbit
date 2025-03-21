"""Utilities."""

HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400
HTTP_500_INTERNAL = 500


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


def dict_factory(cursor, row):
    """Convert row to dictionary."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
