import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JSON_AS_ASCII = False


DEFAULT_LINK_LENGHT = 6

USER_LINK_LENGHT = 16

REGEX_PATTERN = '^[A-Za-z0-9]*$'
