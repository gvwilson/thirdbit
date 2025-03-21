"""Serve data from data model layer."""

from flask import Flask, abort
from flask_cors import CORS
from pathlib import Path

import models
import views
from util import AppException, HTTP_400_BAD_REQUEST


HEARTBEAT = {"message": "alive"}


def create_app():
    """Build application and configure routes."""
    app = Flask("server", static_folder=Path("../static").absolute(), static_url_path="/static")
    CORS(app)

    @app.get("/")
    def root():
        try:
            return views.all_staff(models.all_staff())
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving all staff: {exc}")

    @app.get("/exp/<staff_id>")
    def exp(staff_id):
        try:
            return views.experiments(models.experiments(staff_id), staff_id)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving experiments for {staff_id}: {exc}")

    @app.get("/heartbeat")
    def heartbeat():
        try:
            return views.heartbeat(HEARTBEAT)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving heartbeat: {exc}")

    return app
