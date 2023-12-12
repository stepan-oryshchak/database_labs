from typing import List
from my_project.auth.model.sprinkler_status import SprinklerStatus  # Підключіть вашу модель для sprinkler_status
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class SprinklerStatusDAO(BaseDAO):
    """
    Realisation of SprinklerStatus data access layer.
    """
    _model = SprinklerStatus  # Замініть це на вашу модель

    def find_by_location_id(self, location_id: int) -> List[SprinklerStatus]:
        """
        Gets SprinklerStatus objects from database table by location ID.
        :param location_id: sprinkler location ID
        :return: search objects
        """
        return self._session.query(SprinklerStatus).filter(SprinklerStatus.sprinkler_location_ID == location_id).all()

    def find_by_id(self, status_id: int) -> SprinklerStatus:
        """
        Gets SprinklerStatus object from database table by ID.
        :param status_id: sprinkler status ID
        :return: SprinklerStatus object
        """
        return self._session.query(SprinklerStatus).filter(SprinklerStatus.id == status_id).first()

    # Інші методи CRUD тут, зроблені аналогічно
    # ...
