from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import sprinkler_location_controller
from my_project.auth.domain import SprinklerLocation

sprinkler_location_bp = Blueprint('sprinkler_location', __name__, url_prefix='/sprinkler-locations')

@sprinkler_location_bp.get('/all')
def get_all_sprinkler_locations() -> Response:
    return make_response(jsonify(sprinkler_location_controller.find_all()), HTTPStatus.OK)

@sprinkler_location_bp.get('/<int:sprinkler_location_id>')
def get_sprinkler_location(sprinkler_location_id: int) -> Response:
    return make_response(jsonify(sprinkler_location_controller.find_by_id(sprinkler_location_id)), HTTPStatus.OK)

@sprinkler_location_bp.post('')
def create_sprinkler_location() -> Response:
    content = request.get_json()
    sprinkler_location = SprinklerLocation.create_from_dto(content)
    sprinkler_location_controller.create(sprinkler_location)
    return make_response(jsonify(sprinkler_location.put_into_dto()), HTTPStatus.CREATED)

@sprinkler_location_bp.put('/<int:sprinkler_location_id>')
def update_sprinkler_location(sprinkler_location_id: int) -> Response:
    content = request.get_json()
    sprinkler_location = SprinklerLocation.create_from_dto(content)
    sprinkler_location_controller.update(sprinkler_location_id, sprinkler_location)
    return make_response("Sprinkler location updated", HTTPStatus.OK)

@sprinkler_location_bp.delete('/<int:sprinkler_location_id>')
def delete_sprinkler_location(sprinkler_location_id: int) -> Response:
    sprinkler_location_controller.delete(sprinkler_location_id)
    return make_response("Sprinkler location deleted", HTTPStatus.OK)
