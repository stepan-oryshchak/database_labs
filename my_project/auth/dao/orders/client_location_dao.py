from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.client_location import ClientLocation


class ClientLocationDAO(GeneralDAO):
    """
    Realisation of ClientLocation data access layer.
    """
    _domain_type = ClientLocation

    def find_by_client_id(self, client_id: int) -> List[ClientLocation]:
        """
        Gets ClientLocation objects from database table by field 'client_ID'.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(ClientLocation).filter(ClientLocation.client_ID == client_id).all()

    def find_by_location_name(self, location_name: str) -> List[ClientLocation]:
        """
        Gets ClientLocation objects from database table by field 'location_name'.
        :param location_name: location name value
        :return: search objects
        """
        return self._session.query(ClientLocation).filter(ClientLocation.location_name == location_name).all()

    def find_by_gps_latitude(self, gps_latitude: str) -> List[ClientLocation]:
        """
        Gets ClientLocation objects from database table by field 'gps_latitude'.
        :param gps_latitude: GPS latitude value
        :return: search objects
        """
        return self._session.query(ClientLocation).filter(ClientLocation.gps_latitude == gps_latitude).all()

    def find_by_gps_longitude(self, gps_longitude: str) -> List[ClientLocation]:
        """
        Gets ClientLocation objects from database table by field 'gps_longitude'.
        :param gps_longitude: GPS longitude value
        :return: search objects
        """
        return self._session.query(ClientLocation).filter(ClientLocation.gps_longitude == gps_longitude).all()
