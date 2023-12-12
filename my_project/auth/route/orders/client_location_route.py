from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import client_location_controller
from my_project.auth.domain import ClientLocation

client_location_bp = Blueprint('client_locations', __name__, url_prefix='/client_locations')

@client_location_bp.get('/all')
def get_all_client_locations() -> Response:
    return make_response(jsonify(client_location_controller.find_all()), HTTPStatus.OK)

@client_location_bp.get('/<int:client_location_id>')
def get_client_location(client_location_id: int) -> Response:
    return make_response(jsonify(client_location_controller.find_by_id(client_location_id)), HTTPStatus.OK)

@client_location_bp.post('')
def create_client_location() -> Response:
    content = request.get_json()
    client_location = ClientLocation.create_from_dto(content)
    client_location_controller.create(client_location)
    return make_response(jsonify(client_location.put_into_dto()), HTTPStatus.CREATED)

@client_location_bp.put('/<int:client_location_id>')
def update_client_location(client_location_id: int) -> Response:
    content = request.get_json()
    client_location = ClientLocation.create_from_dto(content)
    client_location_controller.update(client_location_id, client_location)
    return make_response("Client Location updated", HTTPStatus.OK)

@client_location_bp.delete('/<int:client_location_id>')
def delete_client_location(client_location_id: int) -> Response:
    client_location_controller.delete(client_location_id)
    return make_response("Client Location deleted", HTTPStatus.OK)
