from typing import List
from my_project.auth.model.sprinkler_nozzles import SprinklerNozzles  # Вам потрібно підключити вашу модель для sprinkler_nozzles
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class SprinklerNozzlesDAO(BaseDAO):
    """
    Realisation of SprinklerNozzles data access layer.
    """
    _model = SprinklerNozzles  # Замініть це на вашу модель

    def find_by_client_id(self, client_id: int) -> List[SprinklerNozzles]:
        """
        Gets SprinklerNozzles objects from database table by client ID.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(SprinklerNozzles).filter(SprinklerNozzles.client_ID == client_id).all()

    def find_by_id(self, nozzles_id: int) -> SprinklerNozzles:
        """
        Gets SprinklerNozzles object from database table by ID.
        :param nozzles_id: nozzles ID
        :return: SprinklerNozzles object
        """
        return self._session.query(SprinklerNozzles).filter(SprinklerNozzles.id == nozzles_id).first()

    def create_nozzles(self, client_id: int, maximum_water_consumption: int) -> SprinklerNozzles:
        """
        Create a new SprinklerNozzles object and add it to the database.
        :param client_id: ID of the associated client
        :param maximum_water_consumption: maximum water consumption value
        :return: newly created SprinklerNozzles object
        """
        new_nozzles = SprinklerNozzles(client_ID=client_id, maximum_water_consumption=maximum_water_consumption)
        self._add_to_session(new_nozzles)
        return new_nozzles

    def update_nozzles(self, nozzles_id: int, maximum_water_consumption: int) -> SprinklerNozzles:
        """
        Update an existing SprinklerNozzles object in the database.
        :param nozzles_id: ID of the nozzles to update
        :param maximum_water_consumption: updated maximum water consumption value
        :return: updated SprinklerNozzles object
        """
        nozzles = self.find_by_id(nozzles_id)
        if nozzles:
            nozzles.maximum_water_consumption = maximum_water_consumption
            self._commit_session()
        return nozzles

    def delete_nozzles(self, nozzles_id: int) -> bool:
        """
        Delete a SprinklerNozzles object from the database.
        :param nozzles_id: ID of the nozzles to delete
        :return: True if deletion is successful, False otherwise
        """
        nozzles = self.find_by_id(nozzles_id)
        if nozzles:
            self._delete_from_session(nozzles)
            return True
        return False
