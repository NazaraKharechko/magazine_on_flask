from controllers.magazine_login import magazine_login
from controllers.test_api import test_api
from flask import Flask


def setup_controllers(app: Flask):
    app.register_blueprint(magazine_login, url_prefix="/magazine")
    app.register_blueprint(test_api, url_prefix="/test")

