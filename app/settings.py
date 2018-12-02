"""Application configuration."""
import os


class Config():
    """Base configuration."""

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_FILE = os.environ.get('RAPID_DB_FILE', '')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_FILE)


class ProdConfig(Config):
    """Production configuration."""

    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = False


class TestConfig(Config):
    """Development configuration."""

    DEBUG = True
    TESTING = True
