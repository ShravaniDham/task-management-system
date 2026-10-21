"""Task Management System - Flask application factory."""

import os

from flask import Flask

from . import database

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def create_app(test_config=None):
    """Create and configure the Flask app (used by run.py and by the tests)."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
        DATABASE=os.environ.get(
            "DATABASE_PATH", os.path.join(BASE_DIR, "instance", "tasks.db")
        ),
    )
    if test_config:
        app.config.update(test_config)

    os.makedirs(os.path.dirname(app.config["DATABASE"]), exist_ok=True)
    database.init_db(app.config["DATABASE"])

    from .routes import bp

    app.register_blueprint(bp)
    return app
