from typing import List
from my_project.auth.model.pump import Pump  # Підключіть вашу модель для pump
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class PumpDAO(BaseDAO):
    """
    Realisation of Pump data access layer.
    """
    _model = Pump  # Замініть це на вашу модель

    def find_by_client_id(self, client_id: int) -> List[Pump]:
        """
        Gets Pump objects from database table by client ID.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(Pump).filter(Pump.client_ID == client_id).all()

    def find_by_id(self, pump_id: int) -> Pump:
        """
        Gets Pump object from database table by ID.
        :param pump_id: pump ID
        :return: Pump object
        """
        return self._session.query(Pump).filter(Pump.id == pump_id).first()

    def create_pump(self, client_id: int, name: str, time_on: str, time_off: str) -> Pump:
        """
        Create a new Pump object and add it to the database.
        :param client_id: ID of the associated client
        :param name: pump name
        :param time_on: time when the pump is turned on
        :param time_off: time when the pump is turned off
        :return: newly created Pump object
        """
        new_pump = Pump(client_ID=client_id, name=name, time_on=time_on, time_off=time_off)
        self._add_to_session(new_pump)
        return new_pump

    def update_pump(self, pump_id: int, name: str, time_on: str, time_off: str) -> Pump:
        """
        Update an existing Pump object in the database.
        :param pump_id: ID of the pump to update
        :param name: updated pump name
        :param time_on: updated time when the pump is turned on
        :param time_off: updated time when the pump is turned off
        :return: updated Pump object
        """
        pump = self.find_by_id(pump_id)
        if pump:
            pump.name = name
            pump.time_on = time_on
            pump.time_off = time_off
            self._commit_session()
        return pump

    def delete_pump(self, pump_id: int) -> bool:
        """
        Delete a Pump object from the database.
        :param pump_id: ID of the pump to delete
        :return: True if deletion is successful, False otherwise
        """
        pump = self.find_by_id(pump_id)
        if pump:
            self._delete_from_session(pump)
            return True
        return False
