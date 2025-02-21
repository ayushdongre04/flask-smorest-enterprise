# This file contains the business logic for user-related operations.
from app.models.user import User
from app.extensions import db


class UserService:
    """Service layer for user-related operations."""

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return user

    @staticmethod
    def create_user(user_data):
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, user_data):
        user = User.query.get_or_404(user_id)
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
