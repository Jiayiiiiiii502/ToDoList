from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
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
        # get the form from the html
        form= LoginForm(request.form)
        if form.validate():
            username=form.username.data
            password=form.password.data
            # if user exist and password is right, then jump to the list page
            # otherwise, show the error message
            user = UserModel.query.filter_by(username=username).first()
            if user and check_password_hash(user.password,password):
                print(user)
                session['user_id']=user.id
                return redirect(url_for("list.home"))
            else:
                flash("Invalid username or password! Please check again!")
                return redirect(url_for("user.login"))
        else:
            flash("Invalid format! Please check again!")
            return redirect(url_for("user.login"))


@bp.route("/registration",methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template("user_regist.html")
    else:
        # get registration form from html
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # use hash code to ensure password security
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            # registrate successfully, commit user information to databse
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            # print("email: "+form.email.data)
            # print("username: "+form.username.data)
            # print("password: "+form.password.data)
            # print("password_confirm "+form.password_confirm.data)
            # print(form.validate())
            flash("Invalid registration format! Username length:1-20, password length:6,20!")
            return redirect(url_for("list.home"))


@bp.route("/mail", methods=['POST'])
def get_verification():
    # get email from form in html
    email = request.form.get("email")
    # set random verified codes
    letters = string.ascii_letters + string.digits
    verified_code = "".join(random.sample(letters, 4))
    if email:
        # send verified message to the email
        message = Message(
            subject="Verification Code from To do list",
            recipients=[email],
            body=f"You code is: {verified_code}. Please do not tell anyone else."
        )
        mail.send(message)

        # query whether this email had a verified code already
        # if it has, then update to the newest code
        # otherwise, create a new email&verified code in database
        catch_model = EmailCodeModel.query.filter_by(email=email).first()
        if catch_model:
            catch_model.catch = verified_code
            catch_model.create_time = datetime.now()
            db.session.commit()
        else:
            catch_model = EmailCodeModel(email=email, catch=verified_code)
            db.session.add(catch_model)
            db.session.commit()
        # code: 200->successfully update the verifying information
        return jsonify({"code": 200})
    else:
        # code:400->client service error
        return jsonify({"code": 400, "message": "Sending email successfully!"})

