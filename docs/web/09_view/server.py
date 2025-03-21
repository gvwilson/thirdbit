"""Serve data from data model layer."""

from flask import Flask, abort
from flask_cors import CORS

import models
import views

from util import AppException, HTTP_400_BAD_REQUEST


HEARTBEAT = {"message": "alive"}


def create_app():
    """Build application and configure routes."""
    app = Flask("server")
    CORS(app)

    @app.get("/")
    def root():
        try:
            return views.all_staff(models.all_staff())
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving all staff: {exc}")

    @app.get("/heartbeat")
    def heartbeat():
        try:
            return views.heartbeat(HEARTBEAT)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving heartbeat: {exc}")

    @app.get("/col/<name>")
    def column(name):
        try:
            return views.column(models.column(name))
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving column {name}: {exc}")

    @app.get("/row/<staff_id>")
    def row(staff_id):
        try:
            return views.row(models.row(staff_id))
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving row {staff_id}: {exc}")

    return app
