from flask import Flask
from blueprints import user_bp,list_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(list_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
