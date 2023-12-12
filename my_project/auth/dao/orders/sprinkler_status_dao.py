from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.sprinkler_status import SprinklerStatus


class SprinklerStatusDAO(GeneralDAO):
    """
    Realisation of SprinklerStatus data access layer.
    """
    _domain_type = SprinklerStatus

    def find_by_sprinkler_location_id(self, sprinkler_location_id: int) -> List[SprinklerStatus]:
        """
        Gets SprinklerStatus objects from database table by field 'sprinkler_location_ID'.
        :param sprinkler_location_id: sprinkler location ID value
        :return: search objects
        """
        return self._session.query(SprinklerStatus).filter(SprinklerStatus.sprinkler_location_ID == sprinkler_location_id).all()

    def find_by_work_status(self, work_status: str) -> List[SprinklerStatus]:
        """
        Gets SprinklerStatus objects from database table by field 'work_status'.
        :param work_status: work status value
        :return: search objects
        """
        return self._session.query(SprinklerStatus).filter(SprinklerStatus.work_status == work_status).all()

    def find_by_status_column(self, status_column: str) -> List[SprinklerStatus]:
        """
        Gets SprinklerStatus objects from database table by field 'sprinkler_statuscol'.
        :param status_column: sprinkler status column value
        :return: search objects
        """
        return self._session.query(SprinklerStatus).filter(SprinklerStatus.sprinkler_statuscol == status_column).all()
