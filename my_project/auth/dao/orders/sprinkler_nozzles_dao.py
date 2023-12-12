from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.sprinkler_nozzles import SprinklerNozzles


class SprinklerNozzlesDAO(GeneralDAO):
    """
    Realisation of SprinklerNozzles data access layer.
    """
    _domain_type = SprinklerNozzles

    def find_by_client_id(self, client_id: int) -> List[SprinklerNozzles]:
        """
        Gets SprinklerNozzles objects from database table by field 'client_ID'.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(SprinklerNozzles).filter(SprinklerNozzles.client_ID == client_id).all()

    def find_by_maximum_water_consumption(self, max_water_consumption: int) -> List[SprinklerNozzles]:
        """
        Gets SprinklerNozzles objects from database table by field 'maximum_water_consumption'.
        :param max_water_consumption: maximum water consumption value
        :return: search objects
        """
        return self._session.query(SprinklerNozzles).filter(SprinklerNozzles.maximum_water_consumption == max_water_consumption).all()
