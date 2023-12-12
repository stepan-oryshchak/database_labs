from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pump_water_usage_controller
from my_project.auth.domain import PumpWaterUsage

pump_water_usage_bp = Blueprint('pump_water_usages', __name__, url_prefix='/pump-water-usages')

@pump_water_usage_bp.get('/all')
def get_all_pump_water_usages() -> Response:
    return make_response(jsonify(pump_water_usage_controller.find_all()), HTTPStatus.OK)

@pump_water_usage_bp.get('/<int:pump_water_usage_id>')
def get_pump_water_usage(pump_water_usage_id: int) -> Response:
    return make_response(jsonify(pump_water_usage_controller.find_by_id(pump_water_usage_id)), HTTPStatus.OK)

@pump_water_usage_bp.post('')
def create_pump_water_usage() -> Response:
    content = request.get_json()
    pump_water_usage = PumpWaterUsage.create_from_dto(content)
    pump_water_usage_controller.create(pump_water_usage)
    return make_response(jsonify(pump_water_usage.put_into_dto()), HTTPStatus.CREATED)

@pump_water_usage_bp.put('/<int:pump_water_usage_id>')
def update_pump_water_usage(pump_water_usage_id: int) -> Response:
    content = request.get_json()
    pump_water_usage = PumpWaterUsage.create_from_dto(content)
    pump_water_usage_controller.update(pump_water_usage_id, pump_water_usage)
    return make_response("Pump water usage updated", HTTPStatus.OK)

@pump_water_usage_bp.delete('/<int:pump_water_usage_id>')
def delete_pump_water_usage(pump_water_usage_id: int) -> Response:
    pump_water_usage_controller.delete(pump_water_usage_id)
    return make_response("Pump water usage deleted", HTTPStatus.OK)
