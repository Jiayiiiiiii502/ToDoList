from flask import Blueprint,render_template

bp=Blueprint("list",__name__,url_prefix='/list')

@bp.route("/home")
def home():
    return render_template("list_home.html")

@bp.route("/detail")
def detail():
    return render_template("list_detail.html")

@bp.route("/add")
def add():
    return render_template("list_add.html")

@bp.route("/finished")
def finished():
    return render_template("list_finished.html")

@bp.route("/unfinished")
def unfinished():
    return render_template("list_unfinished.html")