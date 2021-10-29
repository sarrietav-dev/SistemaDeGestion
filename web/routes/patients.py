from flask import Blueprint, json, jsonify, request
from sqlalchemy.orm import Session
from web.create_db import Paciente, engine


patients_blueprint = Blueprint('patients', __name__)


@patients_blueprint.route("/api/v1/patients")
def patients():
    db_session = Session(engine)

    query = db_session.query(Paciente).all()

    response_data = []

    for q in query:
        patient_data = q.__dict__
        patient_data.pop('_sa_instance_state', None)
        patient_data.pop('contraseña', None)
        response_data.append(patient_data)
    
    return jsonify(response_data), 200
