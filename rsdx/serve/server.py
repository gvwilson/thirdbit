"""Basic data server."""

import csv

from flask import Flask, render_template
import os
from pathlib import Path
from prettytable import PrettyTable

import model

SITE_TITLE = "Plate Data Server"
PLATES_DIR = str(Path(os.getenv("RSDX_DATA"), "assays"))


app = Flask(__name__)


@app.route("/")
def index():
    """Display data server home page."""
    page_data = {
        "site_title": SITE_TITLE,
        "num_staff": model.get_count("staff"),
        "num_experiments": model.get_count("experiments"),
        "num_plates": model.get_count("plates"),
    }
    return render_template("index.html", **page_data)


@app.route("/staff/")
def staff_index():
    """Display staff details."""
    columns, rows = model.get_all("staff")
    page_data = {
        "site_title": SITE_TITLE,
        "page_title": "Staff",
        "columns": columns,
        "rows": rows,
    }
    return render_template("details.html", **page_data)


@app.route("/experiments/")
def experiment_index():
    """Display experiments."""
    columns, rows = model.get_all("experiments")
    page_data = {
        "site_title": SITE_TITLE,
        "page_title": "Experiments",
        "columns": columns,
        "rows": rows,
    }
    return render_template("details.html", **page_data)


@app.route("/plates/")
def plate_index():
    """Display available plates."""

    def _subpage(ident):
        """Format links to plate pages."""
        return f'<a href="/plate/{ident}">{ident}</a>'

    columns, rows = model.get_all("plates")
    page_data = {
        "site_title": SITE_TITLE,
        "page_title": "Plates",
        "columns": columns,
        "rows": rows,
        "ident": _subpage,
    }
    return render_template("details.html", **page_data)


@app.route("/plate/<plate_id>")
def plate(plate_id):
    """Display single plate."""
    page_data = {
        "site_title": SITE_TITLE,
        "page_title": f"Plate {plate_id}",
        "plate_id": plate_id,
    }

    page_data["filename"] = model.get_plate_filename(plate_id)
    if page_data["filename"]:
        filepath = Path(PLATES_DIR, page_data["filename"])
        page_data["found"] = filepath.exists()
        if page_data["found"]:
            page_data["table"] = _format_plate(filepath)

    return render_template("plate.html", **page_data)


def _format_plate(filepath):
    """Read CSV and format as HTML."""
    with open(filepath, "r") as raw:
        rows = [[val if val else "…" for val in row] for row in csv.reader(raw)]
    tbl = PrettyTable(header=False)
    tbl.add_rows(rows)
    return tbl.get_html_string()
