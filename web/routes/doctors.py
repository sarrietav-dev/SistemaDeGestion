from flask import Blueprint, json, jsonify, request
from sqlalchemy.orm import Session
from web.create_db import Medico, engine


doctors_blueprint = Blueprint('doctors', __name__)


@doctors_blueprint.route("/api/v1/doctors/<id>")
def one_patient(id):
    db_session = Session(engine)

    query = db_session.query(Medico).filter(Medico.id == id).one()

    doctor_data = query.__dict__
    doctor_data.pop('_sa_instance_state', None)
    doctor_data.pop('contraseña', None)

    db_session.close()

    return jsonify(doctor_data), 200


@doctors_blueprint.route("/api/v1/doctors")
def doctors():
    db_session = Session(engine)

    query = db_session.query(Medico).all()

    response_data = []

    for q in query:
        patient_data = q.__dict__
        patient_data.pop('_sa_instance_state', None)
        patient_data.pop('contraseña', None)
        response_data.append(patient_data)

    db_session.close()

    return jsonify(response_data), 200
