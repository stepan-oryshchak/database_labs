from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import sprinkler_status_controller
from my_project.auth.domain import SprinklerStatus

sprinkler_status_bp = Blueprint('sprinkler_statuses', __name__, url_prefix='/sprinkler-statuses')

@sprinkler_status_bp.get('/all')
def get_all_sprinkler_statuses() -> Response:
    return make_response(jsonify(sprinkler_status_controller.find_all()), HTTPStatus.OK)

@sprinkler_status_bp.get('/<int:sprinkler_status_id>')
def get_sprinkler_status(sprinkler_status_id: int) -> Response:
    return make_response(jsonify(sprinkler_status_controller.find_by_id(sprinkler_status_id)), HTTPStatus.OK)

@sprinkler_status_bp.post('')
def create_sprinkler_status() -> Response:
    content = request.get_json()
    sprinkler_status = SprinklerStatus.create_from_dto(content)
    sprinkler_status_controller.create(sprinkler_status)
    return make_response(jsonify(sprinkler_status.put_into_dto()), HTTPStatus.CREATED)

@sprinkler_status_bp.put('/<int:sprinkler_status_id>')
def update_sprinkler_status(sprinkler_status_id: int) -> Response:
    content = request.get_json()
    sprinkler_status = SprinklerStatus.create_from_dto(content)
    sprinkler_status_controller.update(sprinkler_status_id, sprinkler_status)
    return make_response("Sprinkler status updated", HTTPStatus.OK)

@sprinkler_status_bp.delete('/<int:sprinkler_status_id>')
def delete_sprinkler_status(sprinkler_status_id: int) -> Response:
    sprinkler_status_controller.delete(sprinkler_status_id)
    return make_response("Sprinkler status deleted", HTTPStatus.OK)
