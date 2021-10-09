# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import BaseConfig

from .routes.appointments import appointments_blueprint
from .routes.users import users_blueprint

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

app.register_blueprint(appointments_blueprint)
app.register_blueprint(users_blueprint)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Reto Ciclo 3"


if __name__ == '__main__':
    app.run(debug=True)
