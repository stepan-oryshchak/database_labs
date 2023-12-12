from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.sprinkler_location import SprinklerLocation


class SprinklerLocationDAO(GeneralDAO):
    """
    Realisation of SprinklerLocation data access layer.
    """
    _domain_type = SprinklerLocation

    def find_by_client_id(self, client_id: int) -> List[SprinklerLocation]:
        """
        Gets SprinklerLocation objects from database table by field 'client_ID'.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(SprinklerLocation).filter(SprinklerLocation.client_ID == client_id).all()

    def find_by_location_name(self, location_name: str) -> List[SprinklerLocation]:
        """
        Gets SprinklerLocation objects from database table by field 'location_name'.
        :param location_name: location name value
        :return: search objects
        """
        return self._session.query(SprinklerLocation).filter(SprinklerLocation.location_name == location_name).all()
