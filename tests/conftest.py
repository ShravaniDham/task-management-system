import pytest

from app import create_app
from app.database import init_db


@pytest.fixture
def db_path(tmp_path):
    """A fresh, empty SQLite database file for each test."""
    path = str(tmp_path / "test_tasks.db")
    init_db(path)
    return path


@pytest.fixture
def client(tmp_path):
    """Flask test client wired to a temporary database."""
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "app_test.db")})
    return app.test_client()
