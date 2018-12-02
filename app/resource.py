"""Application Resources"""

from flask_rest_jsonapi import ResourceDetail, ResourceList

from app.extensions import DB

from app.model import User
from app.schema import UserSchema


class UserList(ResourceList):
    """User List Resource"""

    schema = UserSchema
    data_layer = {'session': DB.session,
                  'model': User}


class UserDetail(ResourceDetail):
    """User Detail Resource"""

    schema = UserSchema
    data_layer = {'session': DB.session,
                  'model': User}
