from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='blog',
    version=__version__,
    package=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'python-dotenv',
        'psycopg2',
        'sqlalchemy_utils'
    ],
    entry_points={
        'console_scripts': [
            'blog = blog.manage:cli'
        ]
    }
)
