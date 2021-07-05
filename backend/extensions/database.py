from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin


db=SQLAlchemy()


class Users(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140), nullable=False)
    name = db.Column(db.String(140), nullable=False)
    accont_type = db.Column(db.Integer, nullable=False)


class Classes(db.Model, SerializerMixin):
    id_classes = db.Column(db.Integer, primary_key=True)
    name_classes = db.Column(db.String(140), nullable=False)
    description_classes = db.Column(db.String(140), nullable=False)


def init_app(app):
    app.db = db.init_app(app)
    Migrate(app, db)
