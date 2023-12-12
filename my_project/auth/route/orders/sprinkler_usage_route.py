from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import sprinkler_usage_controller
from my_project.auth.domain import SprinklerUsage

sprinkler_usage_bp = Blueprint('sprinkler_usages', __name__, url_prefix='/sprinkler-usages')

@sprinkler_usage_bp.get('/all')
def get_all_sprinkler_usages() -> Response:
    return make_response(jsonify(sprinkler_usage_controller.find_all()), HTTPStatus.OK)

@sprinkler_usage_bp.get('/<int:sprinkler_usage_id>')
def get_sprinkler_usage(sprinkler_usage_id: int) -> Response:
    return make_response(jsonify(sprinkler_usage_controller.find_by_id(sprinkler_usage_id)), HTTPStatus.OK)

@sprinkler_usage_bp.post('')
def create_sprinkler_usage() -> Response:
    content = request.get_json()
    sprinkler_usage = SprinklerUsage.create_from_dto(content)
    sprinkler_usage_controller.create(sprinkler_usage)
    return make_response(jsonify(sprinkler_usage.put_into_dto()), HTTPStatus.CREATED)

@sprinkler_usage_bp.put('/<int:sprinkler_usage_id>')
def update_sprinkler_usage(sprinkler_usage_id: int) -> Response:
    content = request.get_json()
    sprinkler_usage = SprinklerUsage.create_from_dto(content)
    sprinkler_usage_controller.update(sprinkler_usage_id, sprinkler_usage)
    return make_response("Sprinkler usage updated", HTTPStatus.OK)

@sprinkler_usage_bp.delete('/<int:sprinkler_usage_id>')
def delete_sprinkler_usage(sprinkler_usage_id: int) -> Response:
    sprinkler_usage_controller.delete(sprinkler_usage_id)
    return make_response("Sprinkler usage deleted", HTTPStatus.OK)
