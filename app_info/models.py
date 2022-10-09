# from exts import db
from .exts import db
from datetime import datetime

# create list model
class ToDoModel(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content= db.Column(db.Text, nullable=False)
    category = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    completion=db.Column(db.Boolean,default=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("UserModel", backref="todos")


# create user information model
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


# create email-verified code model
class EmailCodeModel(db.Model):
    __tablename__ = "email_verified"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    catch = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
