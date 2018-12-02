"""User REST API Schemas"""

from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserSchema(Schema):
    """REST API Schema for User"""

    class Meta:
        """API Metadata"""

        type_ = 'user'
        self_view = 'user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'user_list'

    id = fields.Integer(as_string=True, dump_only=True)  # pylint: disable=invalid-name
    steam_id = fields.Str(requried=True)
