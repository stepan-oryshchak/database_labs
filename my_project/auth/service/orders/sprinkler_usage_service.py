from typing import List
from my_project.auth.model.sprinkler_usage import SprinklerUsage  # Підключіть вашу модель для sprinkler_usage
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class SprinklerUsageDAO(BaseDAO):
    """
    Realisation of SprinklerUsage data access layer.
    """
    _model = SprinklerUsage  # Замініть це на вашу модель

    def find_by_location_id(self, location_id: int) -> List[SprinklerUsage]:
        """
        Gets SprinklerUsage objects from database table by sprinkler location ID.
        :param location_id: sprinkler location ID value
        :return: search objects
        """
        return self._session.query(SprinklerUsage).filter(SprinklerUsage.sprinkler_location_ID == location_id).all()

    def find_by_id(self, usage_id: int) -> SprinklerUsage:
        """
        Gets SprinklerUsage object from database table by ID.
        :param usage_id: sprinkler usage ID
        :return: SprinklerUsage object
        """
        return self._session.query(SprinklerUsage).filter(SprinklerUsage.id == usage_id).first()

    def create_usage(self, location_id: int, start_time: str, end_time: str) -> SprinklerUsage:
        """
        Create a new SprinklerUsage object and add it to the database.
        :param location_id: ID of the associated sprinkler location
        :param start_time: start time of usage
        :param end_time: end time of usage
        :return: newly created SprinklerUsage object
        """
        new_usage = SprinklerUsage(sprinkler_location_ID=location_id, start_time=start_time, end_time=end_time)
        self._add_to_session(new_usage)
        return new_usage

    def update_usage(self, usage_id: int, start_time: str, end_time: str) -> SprinklerUsage:
        """
        Update an existing SprinklerUsage object in the database.
        :param usage_id: ID of the sprinkler usage entry to update
        :param start_time: updated start time
        :param end_time: updated end time
        :return: updated SprinklerUsage object
        """
        usage = self.find_by_id(usage_id)
        if usage:
            usage.start_time = start_time
            usage.end_time = end_time
            self._commit_session()
        return usage

    def delete_usage(self, usage_id: int) -> bool:
        """
        Delete a SprinklerUsage object from the database.
        :param usage_id: ID of the sprinkler usage entry to delete
        :return: True if deletion is successful, False otherwise
        """
        usage = self.find_by_id(usage_id)
        if usage:
            self._delete_from_session(usage)
            return True
        return False
