"""Handle errors."""

from flask import Flask, abort, jsonify
from flask_cors import CORS
import polars as pl

import util


# [keep]
def create_app():
    """Build application and configure routes."""
    app = Flask("err")
    CORS(app)

    @app.get("/")
    def root():
        return util.as_html()

    @app.get("/col/<name>")
    def column(name):
        try:
            data = util.as_dataframe()
            return jsonify(list(data[name]))
        except Exception as exc:
            abort(util.HTTP_400_BAD_REQUEST, str(exc))

    @app.get("/row/<staff_id>")
    def row(staff_id):
        try:
            staff_id = int(staff_id)
            data = util.as_dataframe()
            row = data.filter(pl.col("staff_id") == staff_id).row(0, named=True)
            return jsonify(row)
        except Exception as exc:
            abort(util.HTTP_400_BAD_REQUEST, str(exc))

    return app
# [/keep]
