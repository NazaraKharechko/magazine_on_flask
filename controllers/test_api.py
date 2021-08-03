import logging
from http import HTTPStatus
from importlib import reload
from flask import Blueprint, request, Flask
from werkzeug.exceptions import abort
import config


test_api = Blueprint("test_api", __name__)


@test_api.route("/", methods=["GET", "POST"])
def index():
    try:
        reload(config)
        from config import Config
        print(Config.DEBUG)
        if Config.DEBUG == 0:
            return "OK", HTTPStatus.OK
    except Exception as e:
        logging.exception(e)
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
