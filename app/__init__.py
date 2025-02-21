#  This file initializes the Flask application and sets up the app factory pattern.
from flask import Flask
from flask_smorest import Api

from app.config import Config
from app.extensions import db, migrate
from app.resources.user import blp as UserBluePrint

def create_app():
    """Factory function to create and configure the Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    # Register Blueprints
    api.register_blueprint(UserBluePrint)

    return app