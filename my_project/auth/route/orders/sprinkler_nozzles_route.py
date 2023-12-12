from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import sprinkler_nozzles_controller
from my_project.auth.domain import SprinklerNozzle

sprinkler_nozzles_bp = Blueprint('sprinkler_nozzles', __name__, url_prefix='/sprinkler-nozzles')

@sprinkler_nozzles_bp.get('/all')
def get_all_sprinkler_nozzles() -> Response:
    return make_response(jsonify(sprinkler_nozzles_controller.find_all()), HTTPStatus.OK)

@sprinkler_nozzles_bp.get('/<int:sprinkler_nozzle_id>')
def get_sprinkler_nozzle(sprinkler_nozzle_id: int) -> Response:
    return make_response(jsonify(sprinkler_nozzles_controller.find_by_id(sprinkler_nozzle_id)), HTTPStatus.OK)

@sprinkler_nozzles_bp.post('')
def create_sprinkler_nozzle() -> Response:
    content = request.get_json()
    sprinkler_nozzle = SprinklerNozzle.create_from_dto(content)
    sprinkler_nozzles_controller.create(sprinkler_nozzle)
    return make_response(jsonify(sprinkler_nozzle.put_into_dto()), HTTPStatus.CREATED)

@sprinkler_nozzles_bp.put('/<int:sprinkler_nozzle_id>')
def update_sprinkler_nozzle(sprinkler_nozzle_id: int) -> Response:
    content = request.get_json()
    sprinkler_nozzle = SprinklerNozzle.create_from_dto(content)
    sprinkler_nozzles_controller.update(sprinkler_nozzle_id, sprinkler_nozzle)
    return make_response("Sprinkler nozzle updated", HTTPStatus.OK)

@sprinkler_nozzles_bp.delete('/<int:sprinkler_nozzle_id>')
def delete_sprinkler_nozzle(sprinkler_nozzle_id: int) -> Response:
    sprinkler_nozzles_controller.delete(sprinkler_nozzle_id)
    return make_response("Sprinkler nozzle deleted", HTTPStatus.OK)
