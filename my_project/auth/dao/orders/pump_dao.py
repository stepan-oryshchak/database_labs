from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.pump import Pump


class PumpDAO(GeneralDAO):
    """
    Realisation of Pump data access layer.
    """
    _domain_type = Pump

    def find_by_client_id(self, client_id: int) -> List[Pump]:
        """
        Gets Pump objects from database table by field 'client_ID'.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(Pump).filter(Pump.client_ID == client_id).all()

    def find_by_name(self, name: str) -> List[Pump]:
        """
        Gets Pump objects from database table by field 'name'.
        :param name: pump name value
        :return: search objects
        """
        return self._session.query(Pump).filter(Pump.name == name).all()
