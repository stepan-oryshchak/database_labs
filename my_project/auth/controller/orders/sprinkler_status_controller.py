from my_project.auth.service import sprinkler_status_service
from my_project.auth.controller.general_controller import GeneralController

class SprinklerStatusController(GeneralController):
    """
    Realisation of SprinklerStatus controller.
    """
    _service = sprinkler_status_service

    def find_by_sprinkler_location_id(self, sprinkler_location_id: int):
        return self._service.find_by_sprinkler_location_id(sprinkler_location_id)

    def find_by_id(self, status_id: int):
        return self._service.find_by_id(status_id)

    def create_status(self, sprinkler_location_id: int, work_status: str, sprinkler_statuscol: str):
        return self._service.create_status(sprinkler_location_id, work_status, sprinkler_statuscol)

    def update_status(self, status_id: int, work_status: str, sprinkler_statuscol: str):
        return self._service.update_status(status_id, work_status, sprinkler_statuscol)

    def delete_status(self, status_id: int):
        return self._service.delete_status(status_id)
