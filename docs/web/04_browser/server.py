"""Color server."""

from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path
import random


def create_app():
    """Build application and configure routes."""
    app = Flask("server", static_folder=Path("../static").absolute(), static_url_path="/static")
    CORS(app)

    @app.get("/")
    def root():
        return jsonify({
            "red": random.randint(0, 255),
            "green": random.randint(0, 255),
            "blue": random.randint(0, 255),
        })

    return app
