# app.py

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from web.auth import auth as auth_blueprint
from web.config import BaseConfig
from web.routes.appointments import appointments_blueprint
from web.routes.users import users_blueprint

app = Flask(__name__)
app.config.from_object(BaseConfig.SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)

app.register_blueprint(appointments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(auth_blueprint)

engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Reto Ciclo 3"


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return 1


if __name__ == '__main__':
    app.run(debug=True)
