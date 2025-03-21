"""Serve data from data model layer."""

from flask import Flask, jsonify
from flask_cors import CORS

import models_sql as models


def create_app():
    """Build application and configure routes."""
    app = Flask("routes")
    CORS(app)

    @app.get("/")
    def root():
        return jsonify(models.all_staff())

    @app.get("/col/<name>")
    def column(name):
        try:
            return jsonify(models.column(name))
        except models.ModelException as exc:
            return {"message": f"Error serving column {name}: {exc}"}, 404

    @app.get("/row/<staff_id>")
    def row(staff_id):
        try:
            return jsonify(models.row(staff_id))
        except models.ModelException as exc:
            return {"message": f"Error serving row {staff_id}: {exc}"}, 404

    return app
