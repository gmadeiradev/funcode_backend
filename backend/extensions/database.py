from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db=SQLAlchemy()


class Users(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140))
    name = db.Column(db.String(512))
    accont_type = db.Column(db.Integer)


def init_app(app):
    db.init_app(app)
