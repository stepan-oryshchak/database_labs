from typing import List
from my_project.auth.model.sprinkler_location import SprinklerLocation  # Це ваша модель для таблиці sprinkler_location
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class SprinklerLocationDAO(BaseDAO):
    """
    Realisation of SprinklerLocation data access layer.
    """
    _model = SprinklerLocation  # Замініть це на вашу модель

    def find_by_location_name(self, location_name: str) -> List[SprinklerLocation]:
        """
        Gets SprinklerLocation objects from database table by location_name field.
        :param location_name: location name value
        :return: search objects
        """
        return self._session.query(SprinklerLocation).filter(SprinklerLocation.location_name == location_name).all()

    def find_by_id(self, location_id: int) -> SprinklerLocation:
        """
        Gets SprinklerLocation object from database table by ID.
        :param location_id: location ID
        :return: SprinklerLocation object
        """
        return self._session.query(SprinklerLocation).filter(SprinklerLocation.id == location_id).first()

    def create_location(self, client_id: int, location_name: str, gps_latitude: str, gps_longitude: str) -> SprinklerLocation:
        """
        Create a new SprinklerLocation object and add it to the database.
        :param client_id: ID of the associated client
        :param location_name: location name
        :param gps_latitude: latitude value
        :param gps_longitude: longitude value
        :return: newly created SprinklerLocation object
        """
        new_location = SprinklerLocation(client_ID=client_id, location_name=location_name, gps_latitude=gps_latitude, gps_longitude=gps_longitude)
        self._add_to_session(new_location)
        return new_location

    def update_location(self, location_id: int, location_name: str, gps_latitude: str, gps_longitude: str) -> SprinklerLocation:
        """
        Update an existing SprinklerLocation object in the database.
        :param location_id: ID of the location to update
        :param location_name: updated location name
        :param gps_latitude: updated latitude value
        :param gps_longitude: updated longitude value
        :return: updated SprinklerLocation object
        """
        location = self.find_by_id(location_id)
        if location:
            location.location_name = location_name
            location.gps_latitude = gps_latitude
            location.gps_longitude = gps_longitude
            self._commit_session()
        return location

    def delete_location(self, location_id: int) -> bool:
        """
        Delete a SprinklerLocation object from the database.
        :param location_id: ID of the location to delete
        :return: True if deletion is successful, False otherwise
        """
        location = self.find_by_id(location_id)
        if location:
            self._delete_from_session(location)
            return True
        return False
