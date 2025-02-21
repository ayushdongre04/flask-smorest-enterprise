# This file defines Marshmallow schemas for request/response validation and serialization.
from marshmallow import Schema, fields


class UserSchema(Schema):
    """Schema for user data."""

    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)


class UserUpdateSchema(Schema):
    """Schema for updating user data."""

    username = fields.Str()
    email = fields.Str()
