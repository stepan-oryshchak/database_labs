from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.pump_water_usage import PumpWaterUsage


class PumpWaterUsageDAO(GeneralDAO):
    """
    Realisation of PumpWaterUsage data access layer.
    """
    _domain_type = PumpWaterUsage

    def find_by_pump_id(self, pump_id: int) -> List[PumpWaterUsage]:
        """
        Gets PumpWaterUsage objects from database table by field 'pump_ID'.
        :param pump_id: pump ID value
        :return: search objects
        """
        return self._session.query(PumpWaterUsage).filter(PumpWaterUsage.pump_ID == pump_id).all()

    def find_by_date_time(self, date_time: str) -> List[PumpWaterUsage]:
        """
        Gets PumpWaterUsage objects from database table by field 'date_time_info'.
        :param date_time: date and time information
        :return: search objects
        """
        return self._session.query(PumpWaterUsage).filter(PumpWaterUsage.date_time_info == date_time).all()
