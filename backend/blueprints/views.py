from flask import abort, render_template
from backend.extensions.database import Users


def init_app(app):
    @app.route("/")
    def index():
        users = Users.query.all()
        return render_template("index.html", users=users) 


    @app.route("/user/<user_id>")
    def user(user_id):
        user = Users.query.filter_by(id=user_id).first() or abort(404, "Usuário não encontrado.")
        return render_template("user.html", user=user)
