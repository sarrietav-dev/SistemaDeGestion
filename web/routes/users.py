from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users/')
@auth.login_required
def users():
    return jsonify(
        {"40057845": {
            "nombre": "Camilo Saenz",
            "tipo": "Paciente",
        }, "400874956": {
            "nombre": "Juan Lopez",
            "tipo": "Medico",
        }, "400145785": {
            "nombre": "Camilo Torres",
            "tipo": "Medico",
        }, "4007845678": {
            "nombre": "Diana Sanchez",
            "tipo": "Paciente",
        }}
    )


@users_blueprint.route('/users/new/', methods=['POST'])
@auth.login_required
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    # TODO: request the complete data for user validation


@users_blueprint.route('/users/delete/<int:identifier>')
@auth.login_required
def delete_user(identifier: int):
    appointment_id = identifier
    # TODO: request the complete data for appointment deletion


@users_blueprint.route('/users/<int:number>/')
def user_id(number):
    return jsonify(
        {f"{number}": {
            "nombreCompleto": "Sean J Person",
            "tipo": "Paciente",
            "fechaNacimiento": "24/05/1983",
            "genero": "hombre",
            "direccion": "1403 Godfrey Street OR",
            "celular": "503-622-2975",
            "email": "seanperson20@hotmail.com",
            "nombreUsuario": "seanjperson",
            "contraseña": "5f4dcc3b5aa765d61d8327deb882cf99",
        }}
    )


@auth.verify_password
def verify_password(username, password):
    return username == "admin" and password == "admin"
