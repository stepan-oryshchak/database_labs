from my_project.auth.service import sensor_service
from my_project.auth.controller.general_controller import GeneralController

class SensorController(GeneralController):
    """
    Realisation of Sensor controller.
    """
    _service = sensor_service

    def find_client(self, sensor_id: int):
        return self._service.find_client(sensor_id)

    def sensor_find_weather(self, sensor_id: int):
        return self._service.sensor_find_weather(sensor_id)

    def find_all_sensors_and_weather(self):
        all_sensors = self._service.find_all()
        all_weather = self._service.find_all_weather()

        combined_data = {
            'sensors': [sensor.put_into_dto() for sensor in all_sensors],
            'weather_data': [weather.put_into_dto() for weather in all_weather],
        }

        return combined_data

    def find_all_sensors_with_clients(self):
        all_sensors = self._service.find_all()
        all_clients = self._service.find_all_clients()

        combined_data = {
            'sensors': [sensor.put_into_dto() for sensor in all_sensors],
            'clients': [client.put_into_dto() for client in all_clients],
        }

        return combined_data

    def add_client_to_sensor(self, sensor_id: int, client_id: int):
        self._service.add_client_to_sensor(sensor_id, client_id)

    def remove_client_from_sensor(self, sensor_id: int, client_id: int):
        self._service.remove_client_from_sensor(sensor_id, client_id)

    def find_by_id_with_clients(self, sensor_id: int):
        return self._service.find_by_id_with_clients(sensor_id)
