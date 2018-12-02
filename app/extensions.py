"""Extensions module. Each extension is initialized in the app factory located in app.py."""

import uuid

from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID as postgreUUID

from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api


class UUID(TypeDecorator):  # pylint: disable=abstract-method
    """Platform-independent UUID type.

    Uses PostgreSQL's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            dialect_type = dialect.type_descriptor(postgreUUID())
        else:
            dialect_type = dialect.type_descriptor(CHAR(32))

        return dialect_type

    def process_bind_param(self, value, dialect):
        if value is None:
            result = value
        elif dialect.name == 'postgresql':
            result = str(value)
        else:
            if not isinstance(value, uuid.UUID):
                result = "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                result = "%.32x" % value.int

        return result

    def process_result_value(self, value, dialect):
        if value is None:
            result = value
        else:
            if not isinstance(value, uuid.UUID):
                result = uuid.UUID(value)

        return result


DB = SQLAlchemy()
API = Api()
