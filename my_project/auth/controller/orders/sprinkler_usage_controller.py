from my_project.auth.service import sprinkler_usage_service
from my_project.auth.controller.general_controller import GeneralController

class SprinklerUsageController(GeneralController):
    """
    Realisation of SprinklerUsage controller.
    """
    _service = sprinkler_usage_service

    def find_by_location_id(self, location_id: int):
        return self._service.find_by_location_id(location_id)

    def find_by_id(self, usage_id: int):
        return self._service.find_by_id(usage_id)

    def create_usage(self, location_id: int, start_time: str, end_time: str):
        return self._service.create_usage(location_id, start_time, end_time)

    def update_usage(self, usage_id: int, start_time: str, end_time: str):
        return self._service.update_usage(usage_id, start_time, end_time)

    def delete_usage(self, usage_id: int):
        return self._service.delete_usage(usage_id)
