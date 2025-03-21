"""Define application in function."""

from flask import Flask
from flask_cors import CORS

import util


# [keep]
def create_app():
    """Build application and configure routes."""
    app = Flask("func")
    CORS(app)

    @app.get("/")
    def root():
        """Display home page as HTML."""
        return util.as_html()

    return app
# [/keep]
