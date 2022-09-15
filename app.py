from flask import Flask, session, g
import config
from exts import db, mail
from blueprints import user_bp, list_bp
from flask_migrate import Migrate
from models import UserModel

app = Flask(__name__)
# add configuration file
app.config.from_object(config)
# connect database to app
db.init_app(app)
# connect mail to app
mail.init_app(app)
# get migrate file through database init
migrate = Migrate(app, db)

# connect various modules bp to app
app.register_blueprint(user_bp)
app.register_blueprint(list_bp)


# setting a user_id to control whole app
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
