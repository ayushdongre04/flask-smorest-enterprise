import pytest
from app.models.user import User
from app.services.user_service import UserService
from app.extensions import db

def test_create_user(app):
    """Test creating a user."""
    with app.app_context():
        user_data = {"username": "testuser", "email": "test@example.com"}
        user = UserService.create_user(user_data)
        assert user.username == "testuser"
        assert user.email == "test@example.com"

def test_get_user(app):
    """Test getting a user by ID."""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()

        fetched_user = UserService.get_user(user.id)
        assert fetched_user.username == "testuser"

def test_update_user(app):
    """Test updating a user."""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()

        updated_data = {"username": "updateduser"}
        updated_user = UserService.update_user(user.id, updated_data)
        assert updated_user.username == "updateduser"

def test_delete_user(app):
    """Test deleting a user."""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()

        UserService.delete_user(user.id)
        assert User.query.get(user.id) is None