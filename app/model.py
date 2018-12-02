"""Database schema"""

import uuid

from app.extensions import DB, UUID


class User(DB.Model):
    """User data model"""

    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)  # pylint: disable=invalid-name
    steam_id = DB.Column(DB.String(50), nullable=False, unique=True)
    created_at = DB.Column(DB.DateTime())
