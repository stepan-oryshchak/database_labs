from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.sprinkler_usage import SprinklerUsage


class SprinklerUsageDAO(GeneralDAO):
    """
    Realisation of SprinklerUsage data access layer.
    """
    _domain_type = SprinklerUsage

    def find_by_sprinkler_location_id(self, sprinkler_location_id: int) -> List[SprinklerUsage]:
        """
        Gets SprinklerUsage objects from database table by field 'sprinkler_location_ID'.
        :param sprinkler_location_id: sprinkler location ID value
        :return: search objects
        """
        return self._session.query(SprinklerUsage).filter(SprinklerUsage.sprinkler_location_ID == sprinkler_location_id).all()

    def find_by_start_time(self, start_time: str) -> List[SprinklerUsage]:
        """
        Gets SprinklerUsage objects from database table by field 'start_time'.
        :param start_time: start time value
        :return: search objects
        """
        return self._session.query(SprinklerUsage).filter(SprinklerUsage.start_time == start_time).all()

    def find_by_end_time(self, end_time: str) -> List[SprinklerUsage]:
        """
        Gets SprinklerUsage objects from database table by field 'end_time'.
        :param end_time: end time value
        :return: search objects
        """
        return self._session.query(SprinklerUsage).filter(SprinklerUsage.end_time == end_time).all()
