from .constants import Paths
from typing import Dict
from flask import Flask
from flask_cors import CORS
from yaml import safe_load

cors = CORS()


def get_config() -> Dict[str, any]:
    with open(Paths.PATH_TO_CONFIG, "r") as config_file:
        configs = safe_load(config_file)
        return configs


def get_app() -> Flask:
    app = Flask("rsiot-server")
    cors.init_app(app)
    return app
