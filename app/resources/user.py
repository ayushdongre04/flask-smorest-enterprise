# This file defines the API endpoints for CRUD operations on the User resource.
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from app.schemas.user import UserSchema, UserUpdateSchema
from app.services.user_service import UserService

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/users/<int:user_id>")
class UserResource(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        """Get a user by ID."""
        return UserService.get_user(user_id)

    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        """Update a user by ID."""
        return UserService.update_user(user_id, user_data)

    @blp.response(204)
    def delete(self, user_id):
        """Delete a user by ID."""
        UserService.delete_user(user_id)


@blp.route("/users")
class UserListResource(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        """Get all users."""
        return UserService.get_all_users()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        """Create a new user."""
        return UserService.create_user(user_data)
