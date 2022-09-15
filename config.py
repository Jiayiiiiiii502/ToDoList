# database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "asdsdefe"

# email configuration
# 使用qq邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "350012471@qq.com"
MAIL_PASSWORD = "qosvirlylyywbice"
MAIL_DEFAULT_SENDER = "350012471@qq.com"