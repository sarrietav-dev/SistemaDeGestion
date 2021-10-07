# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Reto Ciclo 3"


if __name__ == '__main__':
    app.run(debug=True)
