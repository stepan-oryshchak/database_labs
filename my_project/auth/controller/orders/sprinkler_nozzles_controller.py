from my_project.auth.service import sprinkler_nozzles_service
from my_project.auth.controller.general_controller import GeneralController

class SprinklerNozzlesController(GeneralController):
    """
    Realisation of SprinklerNozzles controller.
    """
    _service = sprinkler_nozzles_service

    def find_by_client_id(self, client_id: int):
        return self._service.find_by_client_id(client_id)

    def find_by_id(self, nozzle_id: int):
        return self._service.find_by_id(nozzle_id)

    def create_nozzle(self, client_id: int, maximum_water_consumption: int):
        return self._service.create_nozzle(client_id, maximum_water_consumption)

    def update_nozzle(self, nozzle_id: int, maximum_water_consumption: int):
        return self._service.update_nozzle(nozzle_id, maximum_water_consumption)

    def delete_nozzle(self, nozzle_id: int):
        return self._service.delete_nozzle(nozzle_id)
