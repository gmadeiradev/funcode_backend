from flask_simplelogin import SimpleLogin
from werkzeug.security import generate_password_hash, check_password_hash
from backend.extensions.database import db, Users


def verify_login(user):
    username = user.get("username")
    password = user.get("password")
    if not username or password:
        return False
    existing_user = Users.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(username, password):
    if Users.query.filter_by(username=username).first():
        raise RuntimeError( f'{ username } já registrado!')
    user = Users(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
