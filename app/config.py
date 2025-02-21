# This file contains configuration settings for the Flask app.

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base Configration"""

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Flask Enterprise API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
