from exts import db
from datetime import datetime

# 创建存储用户信息ORM模型
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名不可重复
    username = db.Column(db.String(200), nullable=False)
    # 密码至少string200，需要加密，加密后密码会变长
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)


# 创建捕捉邮箱验证码ORM模型
class EmailCodeModel(db.Model):
    # 表名
    __tablename__ = "email_verified"
    # id自动增长，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 邮箱账号
    email = db.Column(db.String(100), nullable=False)
    # 邮箱验证码
    catch = db.Column(db.String(10), nullable=False)
    # 当前捕捉时间
    create_time = db.Column(db.DateTime, default=datetime.now)
