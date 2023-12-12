from my_project.auth.service import pump_water_usage_service
from my_project.auth.controller.general_controller import GeneralController

class PumpWaterUsageController(GeneralController):
    """
    Realisation of PumpWaterUsage controller.
    """
    _service = pump_water_usage_service

    def find_by_pump_id(self, pump_id: int):
        return self._service.find_by_pump_id(pump_id)

    def find_by_id(self, usage_id: int):
        return self._service.find_by_id(usage_id)

    def create_water_usage(self, pump_id: int, date_time_info: str, water_amount: str):
        return self._service.create_water_usage(pump_id, date_time_info, water_amount)

    def update_water_usage(self, usage_id: int, date_time_info: str, water_amount: str):
        return self._service.update_water_usage(usage_id, date_time_info, water_amount)

    def delete_water_usage(self, usage_id: int):
        return self._service.delete_water_usage(usage_id)
