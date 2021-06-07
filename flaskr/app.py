from flask import Flask
from flaskr.extensions import configuration


def minmal_app():
    app=Flask(__name__)
    configuration.init_app(app)


def create_app():
    app = minmal_app()
    configuration.load_extensions(app)
    return app
