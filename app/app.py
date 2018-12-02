"""Application Factory"""

from flask import Flask

from app.settings import ProdConfig
from app.extensions import DB, API

from app.views import register_user_view

# from flask_rest_jsonapi.exceptions import ObjectNotFound
# from sqlalchemy.orm.exc import NoResultFound


def create_app(config_object=ProdConfig):
    """Application factory
    :param config_object: The configuration object to use.
    """

    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_views()

    return app


def register_extensions(app):
    """Register Flask extensions."""

    DB.init_app(app)
    API.init_app(app)


def register_views():
    """Register Flask Views."""

    register_user_view()
