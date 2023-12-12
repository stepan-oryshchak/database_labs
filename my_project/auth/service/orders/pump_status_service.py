from typing import List
from my_project.auth.model.pump_status import PumpStatus  # Підключіть вашу модель для pump_status
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class PumpStatusDAO(BaseDAO):
    """
    Realisation of PumpStatus data access layer.
    """
    _model = PumpStatus  # Замініть це на вашу модель

    def find_by_pump_id(self, pump_id: int) -> List[PumpStatus]:
        """
        Gets PumpStatus objects from database table by pump ID.
        :param pump_id: pump ID
        :return: search objects
        """
        return self._session.query(PumpStatus).filter(PumpStatus.pump_ID == pump_id).all()

    def find_by_id(self, status_id: int) -> PumpStatus:
        """
        Gets PumpStatus object from database table by ID.
        :param status_id: pump status ID
        :return: PumpStatus object
        """
        return self._session.query(PumpStatus).filter(PumpStatus.id == status_id).first()

    # Інші методи CRUD тут, зроблені аналогічно
    # ...
