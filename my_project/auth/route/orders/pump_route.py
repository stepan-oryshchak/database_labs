from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pump_controller
from my_project.auth.domain import Pump

pump_bp = Blueprint('pumps', __name__, url_prefix='/pumps')

@pump_bp.get('/all')
def get_all_pumps() -> Response:
    return make_response(jsonify(pump_controller.find_all()), HTTPStatus.OK)

@pump_bp.get('/<int:pump_id>')
def get_pump(pump_id: int) -> Response:
    return make_response(jsonify(pump_controller.find_by_id(pump_id)), HTTPStatus.OK)

@pump_bp.post('')
def create_pump() -> Response:
    content = request.get_json()
    pump = Pump.create_from_dto(content)
    pump_controller.create(pump)
    return make_response(jsonify(pump.put_into_dto()), HTTPStatus.CREATED)

@pump_bp.put('/<int:pump_id>')
def update_pump(pump_id: int) -> Response:
    content = request.get_json()
    pump = Pump.create_from_dto(content)
    pump_controller.update(pump_id, pump)
    return make_response("Pump updated", HTTPStatus.OK)

@pump_bp.delete('/<int:pump_id>')
def delete_pump(pump_id: int) -> Response:
    pump_controller.delete(pump_id)
    return make_response("Pump deleted", HTTPStatus.OK)
