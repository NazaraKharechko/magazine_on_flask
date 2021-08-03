import os


class Config:
    # The solution should be defined here
    # We can change the value in debug
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
    os.environ["WERKZEUG_DEBUG_PIN"] = 'off'
    URL_PREFIX = os.environ.get("URL_PREFIX", "webservice")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
