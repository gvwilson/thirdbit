from pathlib import Path
from unittest.mock import patch

import pytest

from click.testing import CliRunner
from lims import cli
from tinydb import TinyDB

ADMIN = "n.bhakta"
INTERN = "a.apte"
SCIENTIST = "d.handa"
INITIAL_DB = "test_initial.json"
DB = "test.json"
STEMS = [
    "fcb9f0d6",
    "fd63dab1",
    "fff9b2d6",
]
ASSAY_FILES = [f"../../data/assays/{s}.csv" for s in STEMS]
ASSAY_ONE = ASSAY_FILES[0]
DESIGN_FILES = [f"../../data/designs/{s}.csv" for s in STEMS]
DESIGN_ONE = DESIGN_FILES[0]
PARAMS = "assays.json"


@pytest.fixture
def db():
    """Create test database."""
    Path(DB).write_bytes(Path(INITIAL_DB).read_bytes())


class Timestamp:
    def __init__(self):
        self.next = 0

    def __call__(self):
        self.next += 1
        return str(self.next)


def _is_bad(result):
    """Check test result."""
    return (result.exit_code == 1) and (result.exception is not None)


def _perform_valid_upload():
    """Perform a valid upload."""
    ts = Timestamp()
    with patch("lims.get_timestamp", ts):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "upload",
                "--db", DB,
                "--assay", ASSAY_ONE,
                "--design", DESIGN_ONE,
                "--params", PARAMS,
                "--user", SCIENTIST,
            ],
        )
        assert result.exit_code == 0
        assert int(result.output.strip()) == 1

        result = runner.invoke(
            cli, ["status", "--db", DB, "--user", ADMIN, "--upload", 1]
        )
        assert result.exit_code == 0
        assert result.output.strip() == "created"

        return runner, ts


def test_bad_upload_nonexistent_assay_file(db):
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "upload",
            "--db", DB,
            "--assay", "nonexistent",
            "--design", DESIGN_ONE,
            "--params", PARAMS,
            "--user", ADMIN,
        ],
    )
    assert _is_bad(result)


def test_bad_upload_nonexistent_design_file(db):
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "upload",
            "--db", DB,
            "--assay", ASSAY_ONE,
            "--design", "nonexistent",
            "--params", PARAMS,
            "--user", ADMIN,
        ],
    )
    assert _is_bad(result)


def test_bad_upload_valid_files_nonexistent_user(db):
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "upload",
            "--db", DB,
            "--assay", ASSAY_ONE,
            "--design", DESIGN_ONE,
            "--params", PARAMS,
            "--user", "nonexistent",
        ],
    )
    assert _is_bad(result)


def test_bad_upload_single_valid_user_not_allowed(db):
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "upload",
            "--db", DB,
            "--assay", ASSAY_ONE,
            "--design", DESIGN_ONE,
            "--params", PARAMS,
            "--user", INTERN,
        ],
    )
    assert _is_bad(result)


def test_bad_listing_nonexistent_user(db):
    runner = CliRunner()
    result = runner.invoke(cli, ["listing", "--db", DB, "--user", "nonexistent"])
    assert _is_bad(result)


def test_bad_listing_valid_user_disallowed_subject(db):
    runner = CliRunner()
    result = runner.invoke(
        cli, ["listing", "--db", DB, "--user", INTERN, "--subject", SCIENTIST]
    )
    assert _is_bad(result)


def test_upload_by_allowed_user(db):
    runner, _ = _perform_valid_upload()
    with TinyDB(DB) as db:
        upload = db.table("uploads").all()
        assert len(upload) == 1
        assert upload[0]["timestamp"] == "1"
        status = db.table("status").all()
        assert len(status) == 1
        assert status[0]["upload"] == 1


def test_invalidate_by_allowed_user(db):
    runner, ts = _perform_valid_upload()
    result = runner.invoke(
        cli, ["status", "--db", DB, "--user", ADMIN, "--upload", 1]
    )
    assert result.exit_code == 0
    assert result.output.strip() == "created"

    with patch("lims.get_timestamp", ts):
        result = runner.invoke(
            cli, ["invalidate", "--db", DB, "--user", ADMIN, "--upload", 1]
        )
        assert result.exit_code == 0
        result = runner.invoke(
            cli, ["status", "--db", DB, "--user", ADMIN, "--upload", 1]
        )
        assert result.exit_code == 0
        assert result.output.strip() == "invalid"


def test_listing_valid_user_no_uploads(db):
    runner = CliRunner()
    result = runner.invoke(cli, ["listing", "--db", DB, "--user", ADMIN])
    assert result.exit_code == 0


def test_listing_valid_user_allowed_subject_no_uploads(db):
    runner = CliRunner()
    result = runner.invoke(
        cli, ["listing", "--db", DB, "--user", ADMIN, "--subject", SCIENTIST]
    )
    assert result.exit_code == 0


def test_listing_with_uploads(db):
    runner, _ = _perform_valid_upload()
    result = runner.invoke(cli, ["listing", "--db", DB, "--user", SCIENTIST])
    assert result.exit_code == 0
    assert result.output.strip() == "{'timestamp': '1', 'uid': 'd.handa', 'design': '../../data/designs/fcb9f0d6.csv', 'assay': '../../data/assays/fcb9f0d6.csv'}"
