"""Utilities."""

from hashlib import blake2b
import json
import os
from pathlib import Path
import secrets


DIGEST_SIZE = 16

HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400
HTTP_403_NOT_AUTHORIZED = 403
HTTP_500_INTERNAL = 500

NUM_RANDOM_BITS = 30
SECRET_VAR = "SECRET"

TRANSLATIONS_VAR = "TXLATE"
TranslationsTable = None


class AppException(Exception):
    """Root of exception hierarchy."""

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class ModelException(AppException):
    pass


class SecurityException(AppException):
    pass


class ViewException(AppException):
    pass


class Translation:
    def __init__(self, lookup, key_lang="en"):
        if isinstance(lookup, (str, Path)):
            with open(lookup, "r") as reader:
                lookup = json.loads(reader.read())

        self._lookup = lookup
        self._key_lang = key_lang

    def translator(self, lang):
        def func(key):
            if key not in self._lookup:
                return f"{key}??"
            if lang == self._key_lang:
                return key
            if lang not in self._lookup[key]:
                return f"{key}/{lang}??"
            return self._lookup[key][lang]
        return func


def dict_factory(cursor, row):
    """Convert row to dictionary."""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def encrypt_password(secret, plain):
    """Encrypt a password."""
    combined = f"{secret}:{plain}"
    h = blake2b(bytes(combined, "utf-8"), digest_size=DIGEST_SIZE)
    return h.hexdigest()


def get_secret():
    """Get the secret value from an environment variable."""
    secret = os.getenv(SECRET_VAR, None)
    if secret is None:
        raise SecurityException(f"secret not set: use {SECRET_VAR} environment variable")
    return secret


def get_translations(key_lang="en"):
    """Load the translation table."""
    global TranslationsTable
    if TranslationsTable is None:
        path = os.getenv(TRANSLATIONS_VAR, None)
        if path is None:
            raise ViewException(f"no translation table path defined (use {TRANSLATIONS_VAR})")
        TranslationsTable = Translation(path, key_lang)
    return TranslationsTable


def make_secret():
    """Make a secret value."""
    return str(secrets.randbits(NUM_RANDOM_BITS))
