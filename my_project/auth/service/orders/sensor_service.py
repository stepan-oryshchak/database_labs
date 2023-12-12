from my_project.auth.dao import sensor_dao
from my_project.auth.service.general_service import GeneralService


class SensorService(GeneralService):
    """
    Realisation of Sensor service.
    """
    _dao = sensor_dao

    def find_by_id(self, sensor_id: int):
        return self._dao.find_by_id(sensor_id)

    def find_by_client_id(self, client_id: int):
        return self._dao.find_by_client_id(client_id)

    def add_sensor_data(self, client_id: int, date_time_info: str, humidity_level: int,
                        temperature: int, illumination: str, gps_latitude: str,
                        gps_longitude: str, sensorcol: str):
        return self._dao.add_sensor_data(client_id, date_time_info, humidity_level,
                                         temperature, illumination, gps_latitude,
                                         gps_longitude, sensorcol)

    def update_sensor_data(self, sensor_id: int, date_time_info: str, humidity_level: int,
                           temperature: int, illumination: str, gps_latitude: str,
                           gps_longitude: str, sensorcol: str):
        return self._dao.update_sensor_data(sensor_id, date_time_info, humidity_level,
                                            temperature, illumination, gps_latitude,
                                            gps_longitude, sensorcol)

    def delete_sensor(self, sensor_id: int):
        return self._dao.delete_sensor(sensor_id)
