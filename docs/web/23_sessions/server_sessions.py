"""Serve data from data model layer."""

from flask import Flask, abort, make_response, redirect, request, url_for
from flask_cors import CORS
from pathlib import Path

import models
import views
from util import AppException, HTTP_400_BAD_REQUEST, encrypt_password, get_secret, make_secret


COOKIE_NAME = "webonomicon"
HEARTBEAT = {"message": "alive"}
RANDOM_LEN = 8


def create_app():
    """Build application and configure routes."""
    app = Flask("server", static_folder=Path("../static").absolute(), static_url_path="/static")
    CORS(app)
    secret = get_secret()

    @app.get("/")
    def root():
        try:
            return views.all_staff(models.all_staff())
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving all staff: {exc}")

    @app.post("/login")
    def login_handler():
        """Accept password and go back home."""
        username = request.form["username"]
        password = request.form["password"]
        response = make_response(redirect(url_for("root")))
        if (not username) or (not password):
            response.set_cookie(COOKIE_NAME, "", expires=0)
            return response
        password = encrypt_password(secret, password)
        staff_id = models.authenticate(username, password)
        if staff_id is None:
            response.set_cookie(COOKIE_NAME, "", expires=0)
            return response
        cookie = make_secret()
        models.create_session(cookie, staff_id)
        response.set_cookie(COOKIE_NAME, cookie, max_age=None)
        return response

    @app.get("/exp/<staff_id>")
    def exp(staff_id):
        staff_id = int(staff_id)
        cookie_value = request.cookies.get(COOKIE_NAME)
        try:
            session_staff_id = models.get_session(cookie_value)
            if session_staff_id == staff_id:
                return views.experiments(models.experiments(staff_id), staff_id)
            else:
                return "<p>not authorized</p>"
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving experiments for {staff_id}: {exc}")

    @app.get("/logout")
    def logout():
        cookie_value = request.cookies.get(COOKIE_NAME)
        if cookie_value:
            models.delete_session(cookie_value)
        response = make_response(redirect(url_for("root")))
        response.set_cookie(COOKIE_NAME, "", expires=0)
        return response

    @app.get("/heartbeat")
    def heartbeat():
        try:
            return views.heartbeat(HEARTBEAT)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving heartbeat: {exc}")

    return app
