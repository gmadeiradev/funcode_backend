from flask import Flask
from backend.extensions import configuration


def create_app():
    app=Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
