from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pump_status_controller
from my_project.auth.domain import PumpStatus

pump_status_bp = Blueprint('pump_statuses', __name__, url_prefix='/pump-statuses')

@pump_status_bp.get('/all')
def get_all_pump_statuses() -> Response:
    return make_response(jsonify(pump_status_controller.find_all()), HTTPStatus.OK)

@pump_status_bp.get('/<int:pump_status_id>')
def get_pump_status(pump_status_id: int) -> Response:
    return make_response(jsonify(pump_status_controller.find_by_id(pump_status_id)), HTTPStatus.OK)

@pump_status_bp.post('')
def create_pump_status() -> Response:
    content = request.get_json()
    pump_status = PumpStatus.create_from_dto(content)
    pump_status_controller.create(pump_status)
    return make_response(jsonify(pump_status.put_into_dto()), HTTPStatus.CREATED)

@pump_status_bp.put('/<int:pump_status_id>')
def update_pump_status(pump_status_id: int) -> Response:
    content = request.get_json()
    pump_status = PumpStatus.create_from_dto(content)
    pump_status_controller.update(pump_status_id, pump_status)
    return make_response("Pump status updated", HTTPStatus.OK)

@pump_status_bp.delete('/<int:pump_status_id>')
def delete_pump_status(pump_status_id: int) -> Response:
    pump_status_controller.delete(pump_status_id)
    return make_response("Pump status deleted", HTTPStatus.OK)
