from flask import Flask
from flaskr.extensions import configuration


def minmal_app(**config):
    app=Flask(__name__)
    configuration.init_app(app, **config)


def create_app(**config):
    app = minmal_app(**config)
    configuration.load_extensions(app)
    return app
