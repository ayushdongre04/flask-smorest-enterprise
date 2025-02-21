import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def app():
    """Fixture for creating a test app."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()  # Create the database schema
        yield app
        db.drop_all()  # Drop the database schema after the test

@pytest.fixture
def client(app):
    """Fixture for creating a test client."""
    return app.test_client()