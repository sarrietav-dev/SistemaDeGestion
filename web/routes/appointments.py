from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
appointments_blueprint = Blueprint('appointments', __name__)


@appointments_blueprint.route('/appointments/')
@auth.login_required
def appointments():
    return jsonify(
        {"1000266354229": {
            "medico": "Juan Lopez",
            "paciente": "Camilo Saenz",
        }, "1000874965742": {
            "medico": "Camilo Torres",
            "paciente": "Diana Sanchez",
        }, "1000847517958": {
            "medico": "Fernando Gonzalez",
            "paciente": "Felipe Altamar",
        }, "1000365784952": {
            "medico": "Valentina Correa",
            "paciente": "Nicolas Cervantes",
        }
        }
    )


@appointments_blueprint.route('/appointments/<int:number>/')
def appointment_id(number):
    return jsonify({f"{number}": {
        "medico": "Juan Lopez",
        "paciente": "Camilo Saenz",
        "fecha": "2021-06-24 04:15:00",
        "tipo": "Odontologia",
        "description": "<object: MedicHistory>",
        "comentarios": "Ninguno"
    }})


@appointments_blueprint.route('/appointments/new/', methods=['POST'])
@auth.login_required
def add_appointment_post():
    medico = request.form.get('medico')
    paciente = request.form.get('paciente')
    fecha = request.form.get('fecha')
    # TODO: request the complete data for appointment validation


@appointments_blueprint.route('/appointments/delete/<int:identifier>')
@auth.login_required
def delete_appointment(identifier: int):
    appointment_id = identifier
    # TODO: request the complete data for appointment deletion


@auth.verify_password
def verify_password(username, password):
    return username == "admin" and password == "admin"
