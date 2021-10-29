
from flask import Blueprint, request, session
from flask.helpers import make_response
from flask.json import jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

from .create_db import Medico, Paciente, engine


auth = Blueprint('auth', __name__)


@auth.route('/logout')
def logout():
    session.pop("user_email")
    return jsonify({"message": "Logged out sucessfuly"}), 200


@auth.route('/signup', methods=['POST'])
def signup_post():

    # Get request data
    email = request.form.get('email')
    password = request.form.get('password')

    db_session = Session(engine)

    # Check if the email is duplicated in the database
    existing_emails = db_session.query(
        Paciente, Medico).filter_by(email=email)

    if (existing_emails.first() is not None):
        return "Email already exists", 400

    # Hash password with Bcrypt
    password_hash = generate_password_hash(password)

    # Create new Paciente
    new_paciente = Paciente(email=email, contraseña=password_hash)

    # Add and submit the new paciente to the database. And close the session.
    db_session.add(new_paciente)
    db_session.commit()
    db_session.close()

    return "Signup succesful", 200


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    existing_user = engine.execute(text(
        "SELECT * FROM (SELECT email, contraseña FROM pacientes UNION SELECT email, contraseña FROM medicos) WHERE email = :email"), email=email).first()

    if (existing_user is None):
        return "Email doesn't exist", 400

    if (check_password_hash(existing_user["contraseña"], password)):
        session["user_email"] = email

        response = make_response("Logged in")
        response.status_code = 200
        return response

    return "Invalid credentials", 400
