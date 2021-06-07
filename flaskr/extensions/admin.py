from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required

from flaskr.extensions.database import db
from flaskr.models import Product, User


# Protect the admin with login by Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(AdminIndexView._handle_view)
admin = Admin()


class UserAdmin(sqla.ModelView):
    column_list = ['username']
    can_edit = False


def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Product, db.session))
    admin.add_view(UserAdmin(User, db.session))
