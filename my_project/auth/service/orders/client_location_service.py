from typing import List
from my_project.auth.model.client_location import ClientLocation  # Підключіть вашу модель для client_location
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class ClientLocationDAO(BaseDAO):
    """
    Realisation of ClientLocation data access layer.
    """
    _model = ClientLocation  # Замініть це на вашу модель

    def find_by_client_id(self, client_id: int) -> List[ClientLocation]:
        """
        Gets ClientLocation objects from database table by client ID.
        :param client_id: client ID value
        :return: search objects
        """
        return self._session.query(ClientLocation).filter(ClientLocation.client_ID == client_id).all()

    def find_by_id(self, location_id: int) -> ClientLocation:
        """
        Gets ClientLocation object from database table by ID.
        :param location_id: client location ID
        :return: ClientLocation object
        """
        return self._session.query(ClientLocation).filter(ClientLocation.id == location_id).first()

    def create_location(self, client_id: int, location_name: str, gps_latitude: str, gps_longitude: str) -> ClientLocation:
        """
        Create a new ClientLocation object and add it to the database.
        :param client_id: ID of the associated client
        :param location_name: name of the location
        :param gps_latitude: latitude of the location
        :param gps_longitude: longitude of the location
        :return: newly created ClientLocation object
        """
        new_location = ClientLocation(client_ID=client_id, location_name=location_name, gps_latitude=gps_latitude, gps_longitude=gps_longitude)
        self._add_to_session(new_location)
        return new_location

    def update_location(self, location_id: int, location_name: str, gps_latitude: str, gps_longitude: str) -> ClientLocation:
        """
        Update an existing ClientLocation object in the database.
        :param location_id: ID of the client location entry to update
        :param location_name: updated name of the location
        :param gps_latitude: updated latitude of the location
        :param gps_longitude: updated longitude of the location
        :return: updated ClientLocation object
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
        Delete a ClientLocation object from the database.
        :param location_id: ID of the client location entry to delete
        :return: True if deletion is successful, False otherwise
        """
        location = self.find_by_id(location_id)
        if location:
            self._delete_from_session(location)
            return True
        return False
