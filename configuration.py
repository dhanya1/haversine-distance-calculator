import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOWNLOAD_DIR = os.path.dirname(os.path.abspath(__file__))
    RANGE = 100


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "test"


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECURITY_KEY")


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("SECURITY_KEY")

