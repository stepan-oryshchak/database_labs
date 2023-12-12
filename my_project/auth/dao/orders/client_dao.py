from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.client import Client


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[Client]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_phone_number(self, phone_number: str) -> List[Client]:
        """
        Gets Client objects from database table by field 'phone_number'.
        :param phone_number: phone number value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.phone_number == phone_number).order_by(Client.phone_number.desc()).all()
