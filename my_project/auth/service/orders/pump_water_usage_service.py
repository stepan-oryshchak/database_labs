from typing import List
from my_project.auth.model.pump_water_usage import PumpWaterUsage  # Підключіть вашу модель для pump_water_usage
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class PumpWaterUsageDAO(BaseDAO):
    """
    Realisation of PumpWaterUsage data access layer.
    """
    _model = PumpWaterUsage  # Замініть це на вашу модель

    def find_by_pump_id(self, pump_id: int) -> List[PumpWaterUsage]:
        """
        Gets PumpWaterUsage objects from database table by pump ID.
        :param pump_id: pump ID value
        :return: search objects
        """
        return self._session.query(PumpWaterUsage).filter(PumpWaterUsage.pump_ID == pump_id).all()

    def find_by_id(self, water_usage_id: int) -> PumpWaterUsage:
        """
        Gets PumpWaterUsage object from database table by ID.
        :param water_usage_id: water usage ID
        :return: PumpWaterUsage object
        """
        return self._session.query(PumpWaterUsage).filter(PumpWaterUsage.id == water_usage_id).first()

    def create_water_usage(self, pump_id: int, date_time_info: str, water_amount: str) -> PumpWaterUsage:
        """
        Create a new PumpWaterUsage object and add it to the database.
        :param pump_id: ID of the associated pump
        :param date_time_info: date and time information
        :param water_amount: amount of water used
        :return: newly created PumpWaterUsage object
        """
        new_water_usage = PumpWaterUsage(pump_ID=pump_id, date_time_info=date_time_info, water_amount=water_amount)
        self._add_to_session(new_water_usage)
        return new_water_usage

    def update_water_usage(self, water_usage_id: int, date_time_info: str, water_amount: str) -> PumpWaterUsage:
        """
        Update an existing PumpWaterUsage object in the database.
        :param water_usage_id: ID of the water usage entry to update
        :param date_time_info: updated date and time information
        :param water_amount: updated amount of water used
        :return: updated PumpWaterUsage object
        """
        water_usage = self.find_by_id(water_usage_id)
        if water_usage:
            water_usage.date_time_info = date_time_info
            water_usage.water_amount = water_amount
            self._commit_session()
        return water_usage

    def delete_water_usage(self, water_usage_id: int) -> bool:
        """
        Delete a PumpWaterUsage object from the database.
        :param water_usage_id: ID of the water usage entry to delete
        :return: True if deletion is successful, False otherwise
        """
        water_usage = self.find_by_id(water_usage_id)
        if water_usage:
            self._delete_from_session(water_usage)
            return True
        return False
