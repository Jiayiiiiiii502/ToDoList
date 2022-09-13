from flask import Blueprint,render_template

bp = Blueprint("user", __name__, url_prefix='/')


@bp.route("/")
def login():
    return render_template("user_login.html")


@bp.route("/registration")
def regist():
    return render_template("user_regist.html")
