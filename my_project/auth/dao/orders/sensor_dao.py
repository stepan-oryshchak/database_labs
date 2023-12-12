from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.sensor import Sensor


class SensorDAO(GeneralDAO):
    """
    Realisation of Sensor data access layer.
    """
    _domain_type = Sensor

    def find_by_client_id(self, client_id: int) -> List[Sensor]:
        """
        Gets Sensor objects from database table by field 'client_ID'.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(Sensor).filter(Sensor.client_ID == client_id).order_by(Sensor.date_time_info).all()

    def find_by_date_time(self, date_time: str) -> List[Sensor]:
        """
        Gets Sensor objects from database table by field 'date_time_info'.
        :param date_time: date and time information
        :return: search objects
        """
        return self._session.query(Sensor).filter(Sensor.date_time_info == date_time).order_by(Sensor.date_time_info).all()
