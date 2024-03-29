import click
from flaskr.extensions.database import db
from flaskr.extensions.auth import create_user
from flaskr.models import Product


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def populate_db():
    data = [
        Product(
            id=1, name="Ciabatta", price="10", description="Italian Bread"
        ),
        Product(id=2, name="Baguete", price="15", description="French Bread"),
        Product(id=3, name="Pretzel", price="20", description="German Bread"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        return create_user(username, password)
