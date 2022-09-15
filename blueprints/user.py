from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import wtforms

from .forms import RegistForm,LoginForm
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,session,g
from exts import mail,db
from flask_mail import Message
from models import EmailCodeModel,UserModel
import string
import random
bp = Blueprint("user", __name__, url_prefix='/')


@bp.route("/",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        print("the method is get")
        return render_template("user_login.html")
    else:
        form= LoginForm(request.form)
        if form.validate():
            username=form.username.data
            password=form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if user and check_password_hash(user.password,password):
                print(user)
                session['user_id']=user.id
                return redirect(url_for("list.home"))
            else:
                flash("Invalid username or password")
                print("Invalid username or password")
                return redirect(url_for("user.login"))
        else:
            flash("Invalid format")
            print("Invalid format")
            return redirect(url_for("user.login"))


@bp.route("/registration",methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template("user_regist.html")
    else:
        # 接受前端的form数据
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            #return "sth wroing"
            # flash("Please recheck registration information!")
            #raise wtforms.ValidationError
            print("email:"+form.email.data)
            print("username:"+form.username.data)
            print("password:"+form.password.data)
            print("password_confirm"+form.password_confirm.data)
            print(form.validate())
            return redirect(url_for("list.home"))


@bp.route("/mail", methods=['POST'])
def get_verification():
    # 输入邮箱：get/post
    email = request.form.get("email")
    # 生成随机验证码
    letters = string.ascii_letters + string.digits
    verified_code = "".join(random.sample(letters, 4))
    # 如果邮箱格式正确
    if email:
        # 向指定邮箱发送验证码
        message = Message(
            subject="Verification Code from To do list",
            recipients=[email],
            body=f"You code is: {verified_code}. Please do not tell anyone else."
        )
        mail.send(message)

        # 存储邮箱和验证码
        # 查找该邮箱是否曾经有验证码存储历史
        catch_model = EmailCodeModel.query.filter_by(email=email).first()
        # 如果有，则覆盖为新的
        if catch_model:
            catch_model.catch = verified_code
            catch_model.create_time = datetime.now()
            db.session.commit()
        # 如果没有，则创建新的
        else:
            catch_model = EmailCodeModel(email=email, catch=verified_code)
            db.session.add(catch_model)
            db.session.commit()
        # code: 200则为成功
        return jsonify({"code": 200})
    else:
        # code:400 客户端错误
        return jsonify({"code": 400, "message": "Sending email successfully!"})

