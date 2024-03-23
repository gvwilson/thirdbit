"""Implement simple LIMS."""

from datetime import datetime

import click
from click import ClickException
from tinydb import TinyDB, Query

import assay_params
import lint


@click.group()
def cli():
    """Interact with laboratory data."""


@cli.command()
@click.option("--db", type=str, required=True, help="Database")
@click.option("--upload", type=int, required=True, help="upload ID")
@click.option("--user", type=str, required=True, help="User ID")
def invalidate(db, user, upload):
    """Invalidate existing upload."""
    with TinyDB(db) as db:
        _require_exists(db, "user", user)
        upload_doc = _require_exists(db, "upload", upload)
        cap = _get_capability(db, user, "validate")
        _require_cap(
            (cap == "all") or ((cap == "own") and (upload_doc["uid"] == user)),
            f"{user} cannot invalidate {upload}",
        )
        timestamp = get_timestamp()
        db.table("status").insert(
            {"upload": upload, "uid": user, "status": "invalid", "timestamp": timestamp}
        )


@cli.command()
@click.option("--db", type=str, required=True, help="Database")
@click.option("--user", type=str, required=True, help="User ID")
@click.option("--subject", type=str, default=None, help="Whose uploads to view")
def listing(db, user, subject):
    """Show uploads by subject."""
    if subject is None:
        subject = user
    with TinyDB(db) as db:
        _require_exists(db, "user", user)
        _require_exists(db, "user", subject)
        cap = _get_capability(db, user, "view")
        _require_cap(
            (cap == "all") or ((cap == "own") and (subject == user)),
            f"{user} cannot view uploads for {subject}",
        )
        uploads = db.table("uploads").search(Query().uid == subject)
        uploads.sort(key=lambda x: x["timestamp"])
        for up in uploads:
            click.echo(up)


@cli.command()
@click.option("--db", type=str, required=True, help="Database")
@click.option("--upload", type=int, required=True, help="Upload ID")
@click.option("--user", type=str, required=True, help="User ID")
def status(db, user, upload):
    """Get current status of existing upload."""
    with TinyDB(db) as db:
        _require_exists(db, "user", user)
        upload_doc = _require_exists(db, "upload", upload)
        cap = _get_capability(db, user, "view")
        _require_cap(
            (cap == "all") or ((cap == "own") and (upload_doc["uid"] == user)),
            f"{user} cannot view status for {upload}",
        )
        statuses = db.table("status").search(Query().upload == upload)
        statuses.sort(key=lambda x: x["timestamp"])
        click.echo(statuses[-1]["status"])


@cli.command()
@click.option("--db", type=str, required=True, help="Database")
@click.option("--assay", type=str, required=True, help="Assay filename")
@click.option("--design", type=str, required=True, help="Design filename")
@click.option("--params", type=str, required=True, help="Parameters filename")
@click.option("--user", type=str, required=True, help="User ID")
def upload(db, user, params, design, assay):
    """Upload design and assay files."""
    params = assay_params.load_params(params)
    design_data = lint.load_file(design)
    assay_data = lint.load_file(assay)
    errors = [
        *lint.lint_design(params, design, design_data),
        *lint.lint_assay(params, assay, assay_data),
    ]
    _require_no_errors(errors)

    with TinyDB(db) as db:
        _require_exists(db, "user", user)
        cap = _get_capability(db, user, "upload")
        _require_cap(cap == "own", f"{user} cannot upload")
        assay_id = _upload_data(db, user, design, assay)
        click.echo(assay_id)


def get_timestamp():
    """Get timestamp for action."""
    return str(datetime.utcnow())


def _get_capability(db, user, kind):
    """Find capability."""
    results = db.table("users").search(Query().uid == user)
    if len(results) != 1:
        raise ClickException(f"unknown user {user}")

    roles = db.table("roles").search(Query().uid == user)
    if len(results) != 1:
        raise ClickException(f"user {user} has no role")
    role = roles[0]["role"]

    q = Query()
    capabilities = db.table("capabilities").search(
        (q.role == role) & (q.capability == kind)
    )
    if not capabilities:
        return None
    if len(capabilities) > 1:
        caps = ", ".join(str(c) for c in capabilities)
        raise ClickException(
            f"duplicate capabilities for user {user} and kind {kind}: {caps}"
        )
    return capabilities[0]["scope"]


def _require_cap(condition, message):
    """Check condition and raise exception."""
    if not condition:
        raise ClickException(f"permission error: {message}")


def _require_exists(db, kind, value):
    """Check existence of something in database."""
    q = Query()
    match kind:
        case "upload":
            found = db.table("uploads").get(doc_id=value)
            if found is not None:
                return found

        case "user":
            found = db.table("users").search(q.uid == value)
            if len(found) > 1:
                raise ClickException(f"data integrity error: multiple {kind}: {value}")
            if len(found) == 1:
                return found[0]

        case other:
            raise ClickException(f"internal error: unknown kind {kind}")

    raise ClickException(f"No such {kind}: '{value}'")


def _require_no_errors(errors):
    """Fail if any error messages."""
    if not errors:
        return
    msg = "\n".join(errors)
    import sys

    print("ERROR", msg, file=sys.stderr)
    raise ClickException(f"Data validation errors\n{msg}")


def _upload_data(db, user, design_file, assay_file):
    """Upload validated data."""
    timestamp = get_timestamp()
    doc_id = db.table("uploads").insert(
        {"timestamp": timestamp, "uid": user, "design": design_file, "assay": assay_file}
    )
    db.table("status").insert(
        {"upload": doc_id, "uid": user, "status": "created", "timestamp": timestamp}
    )
    return doc_id


if __name__ == "__main__":
    cli()
