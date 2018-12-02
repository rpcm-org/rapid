# -*- coding: utf-8 -*-
"""rapid_utils
Usage:
  rapid_utils.py db_init <db_file>
  rapid_utils.py (-h | --help)
Options:
  -h --help         Show this screen.
  db_file           Absolute path to the DB file
"""

import os
import sys
from docopt import docopt
from flask.helpers import get_debug_flag

from app.app import create_app
from app.settings import DevConfig, ProdConfig, TestConfig
from app.extensions import DB

from app.model import User  # pylint: disable=unused-import


def db_init(config):
    """Creation of database"""

    if os.path.isfile(config.DB_FILE):
        print('[WARNING] File [{}] already exists.'.format(config.DB_FILE))
        sys.exit(0)

    if not os.path.exists(os.path.dirname(config.DB_FILE)):
        os.makedirs(os.path.dirname(config.DB_FILE))

    app = create_app(config_object=config)

    with app.app_context():
        DB.init_app(app)
        DB.create_all()
        DB.session.commit()

    print('[SUCCESS] File [{}] created.'.format(config.DB_FILE))
    sys.exit(0)


def main():  # pylint: disable=too-many-statements
    """Entry point"""

    args = docopt(__doc__)

    testing = os.environ.get('VLS_TESTING', 0)
    if testing:
        config = TestConfig
    else:
        config = DevConfig if get_debug_flag() else ProdConfig

    config.DB_FILE = args['<db_file>']
    config.SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(config.DB_FILE)

    if args['db_init']:
        db_init(config)


if __name__ == '__main__':
    main()
