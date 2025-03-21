"""Configure multiple routes."""

from flask import Flask, jsonify
from flask_cors import CORS
import polars as pl

import util


# [keep]
def create_app():
    """Build application and configure routes."""
    app = Flask("routes")
    CORS(app)

    @app.get("/")
    def root():
        return util.as_html()

    @app.get("/col/<name>")
    def column(name):
        data = util.as_dataframe()
        return jsonify(list(data[name]))

    @app.get("/row/<staff_id>")
    def row(staff_id):
        staff_id = int(staff_id)
        data = util.as_dataframe()
        row = data.filter(pl.col("staff_id") == staff_id).row(0, named=True)
        return jsonify(row)

    return app
# [/keep]
