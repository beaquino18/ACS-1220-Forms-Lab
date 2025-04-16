"""Initialize Config class to access environment variables."""
from dotenv import load_dotenv
import os

load_dotenv()

# Get the absolute path to the project root directory
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config(object):
    """Set environment variables."""

    # Use an absolute path to the database file
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "books_app", "database.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'itsasecret')
