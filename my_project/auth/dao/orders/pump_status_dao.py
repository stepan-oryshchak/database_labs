from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.pump_status import PumpStatus


class PumpStatusDAO(GeneralDAO):
    """
    Realisation of PumpStatus data access layer.
    """
    _domain_type = PumpStatus

    def find_by_pump_id(self, pump_id: int) -> List[PumpStatus]:
        """
        Gets PumpStatus objects from database table by field 'pump_ID'.
        :param pump_id: pump ID value
        :return: search objects
        """
        return self._session.query(PumpStatus).filter(PumpStatus.pump_ID == pump_id).all()

    def find_by_work_status(self, work_status: str) -> List[PumpStatus]:
        """
        Gets PumpStatus objects from database table by field 'work_status'.
        :param work_status: work status value
        :return: search objects
        """
        return self._session.query(PumpStatus).filter(PumpStatus.work_status == work_status).all()

    def find_by_status_column(self, status_column: str) -> List[PumpStatus]:
        """
        Gets PumpStatus objects from database table by field 'pump_statuscol'.
        :param status_column: pump status column value
        :return: search objects
        """
        return self._session.query(PumpStatus).filter(PumpStatus.pump_statuscol == status_column).all()
