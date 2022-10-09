from flask import Flask, session, g
import config
from app_info.exts import db, mail
# from app_info.blueprints import user_bp, list_bp
from app_info.blueprints import user_bp,list_bp
from flask_migrate import Migrate
from app_info.models import UserModel
from flask_moment import Moment



app = Flask(__name__)
# add configuration file
app.config.from_object(config)
# connect database to app_info
db.init_app(app)
# connect mail to app_info
mail.init_app(app)
# get migrate file through database init
migrate = Migrate(app, db)
# set local moment
moment=Moment(app)

# connect various modules bp to app_info
app.register_blueprint(user_bp)
app.register_blueprint(list_bp)


# setting a user_id to control whole app_info
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # set user for g, which is a user
            g.user = user
        except:
            g.user = None


if __name__ == '__main__':
    app.run()
