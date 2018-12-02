"""Application Views"""

from app.extensions import API

from app.resource import UserList, UserDetail


def register_user_view():
    """Register User View"""

    API.route(UserList, 'user_list', '/users')
    API.route(UserDetail, 'user_detail', '/users/<int:id>')
