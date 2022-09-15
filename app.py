from flask import Flask,session,g
import config
from exts import db,mail
from blueprints import user_bp,list_bp
from flask_migrate import Migrate
from models import UserModel


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate=Migrate(app,db)

app.register_blueprint(user_bp)
app.register_blueprint(list_bp)


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user=UserModel.query.get(user_id)
            # 给g绑定一个user变量，值为user
            # setattr(g,"user",user)
            g.user = user
        except:
            g.user = None


if __name__ == '__main__':
    app.run()
