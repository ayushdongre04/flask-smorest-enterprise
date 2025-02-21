# This file contains tests for the user API endpoints.
import pytest
from app.models.user import User
from app.extensions import db



def test_create_user(client):
    response = client.post(
        "/users", json={"username": "test", "email": "test@example.com"}
    )
    assert response.status_code == 201
    assert response.json["username"] == "test"


def test_get_user(client):
    user = User(username="test", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json["username"] == "test"
