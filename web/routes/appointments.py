from datetime import datetime

import simplejson
from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from web.create_db import Cita

engine = create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

auth = HTTPBasicAuth()
appointments_blueprint = Blueprint('appointments', __name__)


@appointments_blueprint.route('/api/v1/appointments/')
@auth.login_required
def appointments():
    all_rows = session.query(Cita).all()
    response = simplejson.dumps(all_rows)
    return response


@appointments_blueprint.route('/api/v1/appointments/<int:number>/')
def appointment_id(number):
    all_rows = session.query(Cita).get(number)
    response = simplejson.dumps(all_rows)
    return response


@appointments_blueprint.route('/api/v1/appointments/new/', methods=['POST'])
@auth.login_required
def add_appointment_post():
    id_medico = request.form.get('medico')
    id_paciente = request.form.get('paciente')
    fecha = request.form.get('fecha')
    fecha = datetime.strptime(fecha, '%d/%m/%y %H:%M:%S')
    tipo = request.form.get('tipo')
    motivo = request.form.get('motivo')
    precio = request.form.get('precio')
    cita = Cita(0, int(id_medico), int(id_paciente), fecha, str(tipo), motivo, precio)
    session.add(cita)
    session.commit()


@appointments_blueprint.route('/api/v1/appointments/delete/<int:identifier>')
@auth.login_required
def delete_appointment(identifier: int):
    session.query(Cita).filter_by(id=identifier).delete()


@auth.verify_password
def verify_password(username, password):
    return username == "admin" and password == "admin"
