from my_project.auth.service import pump_status_service
from my_project.auth.controller.general_controller import GeneralController

class PumpStatusController(GeneralController):
    """
    Realisation of PumpStatus controller.
    """
    _service = pump_status_service

    def find_by_pump_id(self, pump_id: int):
        return self._service.find_by_pump_id(pump_id)

    def find_by_id(self, status_id: int):
        return self._service.find_by_id(status_id)

    def create_status(self, pump_id: int, work_status: str, pump_statuscol: str):
        return self._service.create_status(pump_id, work_status, pump_statuscol)

    def update_status(self, status_id: int, work_status: str, pump_statuscol: str):
        return self._service.update_status(status_id, work_status, pump_statuscol)

    def delete_status(self, status_id: int):
        return self._service.delete_status(status_id)
