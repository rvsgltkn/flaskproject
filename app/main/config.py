import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_project_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_BASE_URL="https://sandbox-reporting.rpdpymnt.com/api/v3/"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_project_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_BASE_URL = "https://sandbox-reporting.rpdpymnt.com/api/v3/"


class ProductionConfig(Config):
    DEBUG = False

    #replace with live url
    CLIENT_BASE_URL = "https://sandbox-reporting.rpdpymnt.com/api/v3/"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY