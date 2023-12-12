from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import sensor_controller
from my_project.auth.domain import Sensor

sensor_bp = Blueprint('sensors', __name__, url_prefix='/sensors')

@sensor_bp.get('/all')
def get_all_sensors() -> Response:
    return make_response(jsonify(sensor_controller.find_all()), HTTPStatus.OK)

@sensor_bp.get('/<int:sensor_id>')
def get_sensor(sensor_id: int) -> Response:
    return make_response(jsonify(sensor_controller.find_by_id(sensor_id)), HTTPStatus.OK)

@sensor_bp.post('')
def create_sensor() -> Response:
    content = request.get_json()
    sensor = Sensor.create_from_dto(content)
    sensor_controller.create(sensor)
    return make_response(jsonify(sensor.put_into_dto()), HTTPStatus.CREATED)

@sensor_bp.put('/<int:sensor_id>')
def update_sensor(sensor_id: int) -> Response:
    content = request.get_json()
    sensor = Sensor.create_from_dto(content)
    sensor_controller.update(sensor_id, sensor)
    return make_response("Sensor updated", HTTPStatus.OK)

@sensor_bp.delete('/<int:sensor_id>')
def delete_sensor(sensor_id: int) -> Response:
    sensor_controller.delete(sensor_id)
    return make_response("Sensor deleted", HTTPStatus.OK)
