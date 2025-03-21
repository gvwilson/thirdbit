"""Serve data from data model layer with JWT authentication."""

from flask import Flask, abort, make_response, redirect, request, url_for, jsonify
from flask_cors import CORS
from pathlib import Path
import jwt
from datetime import datetime, timedelta, timezone
import os

import models
import views
from util import AppException, HTTP_400_BAD_REQUEST, encrypt_password, get_secret

COOKIE_NAME = "webonomicon"
HEARTBEAT = {"message": "alive"}
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_DELTA = timedelta(hours=1)

def create_app():
    """Build application and configure routes."""
    app = Flask("server", static_folder=Path("../static").absolute(), static_url_path="/static")
    CORS(app)

    secret = get_secret()

    def create_token(staff_id):
        payload = {
            "exp": datetime.now(timezone.utc) + JWT_EXPIRATION_DELTA,
            "iat": datetime.now(timezone.utc),
            "staffId": staff_id
        }
        return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    def decode_token(token):
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return payload["staffId"]
        except jwt.ExpiredSignatureError:
            return None  # Token has expired
        except jwt.InvalidTokenError:
            return None  # Invalid token

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

        token = create_token(staff_id)
        response.set_cookie(COOKIE_NAME, token, samesite="Lax")
        return response

    @app.get("/exp/<staff_id>")
    def exp(staff_id):
        staff_id = int(staff_id)
        token = request.cookies.get(COOKIE_NAME)
        if not token:
            return jsonify({"error": "Not authenticated"}), 401

        decoded_staff_id = decode_token(token)
        if decoded_staff_id is None:
            return jsonify({"error": "Invalid or expired token"}), 401

        try:
            if int(decoded_staff_id) == staff_id:
                return views.experiments(models.experiments(staff_id), staff_id)
            else:
                return jsonify({"error": "Not authorized"}), 403
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving experiments for {staff_id}: {exc}")

    @app.get("/heartbeat")
    def heartbeat():
        try:
            return views.heartbeat(HEARTBEAT)
        except AppException as exc:
            abort(HTTP_400_BAD_REQUEST, f"Error serving heartbeat: {exc}")

    return app
