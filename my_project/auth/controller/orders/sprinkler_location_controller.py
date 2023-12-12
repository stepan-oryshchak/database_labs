from my_project.auth.service import sprinkler_location_service
from my_project.auth.controller.general_controller import GeneralController

class SprinklerLocationController(GeneralController):
    """
    Realisation of SprinklerLocation controller.
    """
    _service = sprinkler_location_service

    def find_by_client_id(self, client_id: int):
        return self._service.find_by_client_id(client_id)

    def find_by_id(self, location_id: int):
        return self._service.find_by_id(location_id)

    def create_location(self, client_id: int, location_name: str, gps_latitude: str, gps_longitude: str):
        return self._service.create_location(client_id, location_name, gps_latitude, gps_longitude)

    def update_location(self, location_id: int, location_name: str, gps_latitude: str, gps_longitude: str):
        return self._service.update_location(location_id, location_name, gps_latitude, gps_longitude)

    def delete_location(self, location_id: int):
        return self._service.delete_location(location_id)
