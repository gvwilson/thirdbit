"""Serve data from data model layer."""

from flask import Flask, abort, redirect, request
from flask_cors import CORS
from pathlib import Path

import models
import views

from util import AppException, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL


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

    @app.post("/add")
    def add():
        try:
            models.add_staff(request.form["personal"], request.form["family"])
            return redirect("/")
        except AppException as exc:
            abort(HTTP_500_INTERNAL, f"Error adding data: {exc}")

    return app
