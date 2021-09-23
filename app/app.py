from flask import Flask

from app.extensions import migrate
from app.extensions import database

app = Flask(__name__)


def create_app(config_object):
    _app = Flask(__name__.split(".")[0])
    _app.config.from_object(config_object)
    migrate.init_app(_app, db=database)
    return _app


@app.route('/')
def home():
    return "hola, este es el ciclo numero 3"


if __name__ == '__main__':
    app.run(debug=True)
