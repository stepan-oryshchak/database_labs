from my_project.auth.service import client_service
from my_project.auth.controller.general_controller import GeneralController

class ClientController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = client_service

    def client_find_solar_panels(self, client_id: int):
        return self._service.client_find_solar_panels(client_id)

    def find_orders(self, client_id: int):
        return self._service.find_orders(client_id)

    def find_owners(self, client_id: int):
        return self._service.find_owners(client_id)