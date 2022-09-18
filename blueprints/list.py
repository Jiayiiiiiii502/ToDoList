from flask import Blueprint,g,render_template,request,redirect,flash,url_for
from .forms import TodoForm
from models import ToDoModel
from exts import db

bp=Blueprint("list",__name__,url_prefix='/list')

@bp.route("/home")
def home():
    # 将登陆的用户名称获取并显示在导航栏中
    context = {
        "user": g.user.username
    }
    return render_template("list_home.html",**context)

@bp.route("/detail")
def detail():
    context = {
        "user": g.user.username
    }
    return render_template("list_detail.html",**context)

@bp.route("/add",methods=['GET','POST'])
def add():
    if request.method == 'GET':
        context = {
            "user": g.user.username
        }
        return render_template("list_add.html", **context)
    else:
        context = {
            "user": g.user.username
        }
        form = TodoForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            category = form.category.data
            todo = ToDoModel(title=title,content=content,category=category,user=g.user)
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('list.home'))
        else:
            print("something wrong")
            print(form.errors)
            flash("Invalid format!")
            return redirect(url_for('list.add'))


@bp.route("/finished")
def finished():
    context = {
        "user": g.user.username
    }
    return render_template("list_finished.html",**context)

@bp.route("/unfinished")
def unfinished():
    context = {
        "user": g.user.username
    }
    return render_template("list_unfinished.html",**context)