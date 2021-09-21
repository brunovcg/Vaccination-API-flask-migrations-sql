from flask import Blueprint, request, current_app, jsonify
from app.models.vaccine_model import VaccineModel
from datetime import datetime, timedelta

bp = Blueprint("vaccine", __name__)

@bp.post("/vaccination")
def create():
    data = request.get_json()
    new_entry = VaccineModel(
        cpf=data["cpf"],
        name=data["name"],
        vaccine_name = data["vaccine_name"],
        health_unit_name = data["health_unit_name"],
        first_shot_date = datetime.today(),
        second_shot_date = datetime.today() + timedelta(days=90)
    )

    if data['cpf'].isdigit() and len(data["cpf"]) != 11:
        return {"Error" : "CPF must have only numeric with 11 characters"}, 400
 
    session = current_app.db.session

    session.add(new_entry)
    session.commit()

    return jsonify(new_entry), 201


@bp.get("/vaccination")
def get_info():

    query = VaccineModel.query.all()

    return  jsonify([
            {"cpf": card.cpf, "name": card.name, "first_shot_date": card.first_shot_date,
             "second_shot_date" : card.second_shot_date, "vaccine_name" : card.vaccine_name, 
             "health_unit_name" : card.health_unit_name}
            for card in query
    ]), 200


@bp.get("/")
def welcome():
    return {"Entrega14" : " Vacinação"}, 200