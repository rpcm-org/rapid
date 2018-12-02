"""REST API DB Setup script"""

from setuptools import setup, find_packages

setup(
    name='rapid',
    description='REST API DB',
    version='0.0.1',
    author='celestian',
    license='GPLv3',
    url='https://github.com/rpcm/rapid',

    packages=find_packages(),

    install_requires=[
        'autopep8',
        'docopt',
        'Flask',
        'Flask-SQLAlchemy',
        'flask-rest-jsonapi',
    ],
    setup_requires=['pytest-runner'],
)
