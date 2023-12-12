from typing import List
from my_project.auth.model.client import Client  # Це ваша модель для таблиці client
from my_project.auth.dao.base_dao import BaseDAO  # Потрібно підключити базовий DAO

class ClientDAO(BaseDAO):
    """
    Realisation of Client data access layer.
    """
    _model = Client  # Замініть це на вашу модель

    def find_by_name(self, name: str) -> List[Client]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_id(self, client_id: int) -> Client:
        """
        Gets Client object from database table by ID.
        :param client_id: client ID
        :return: Client object
        """
        return self._session.query(Client).filter(Client.id == client_id).first()

    def create_client(self, name: str, mail: str, phone_number: str) -> Client:
        """
        Create a new Client object and add it to the database.
        :param name: client name
        :param mail: client email
        :param phone_number: client phone number
        :return: newly created Client object
        """
        new_client = Client(name=name, mail=mail, phone_number=phone_number)
        self._add_to_session(new_client)
        return new_client

    def update_client(self, client_id: int, name: str, mail: str, phone_number: str) -> Client:
        """
        Update an existing Client object in the database.
        :param client_id: ID of the client to update
        :param name: updated client name
        :param mail: updated client email
        :param phone_number: updated client phone number
        :return: updated Client object
        """
        client = self.find_by_id(client_id)
        if client:
            client.name = name
            client.mail = mail
            client.phone_number = phone_number
            self._commit_session()
        return client

    def delete_client(self, client_id: int) -> bool:
        """
        Delete a Client object from the database.
        :param client_id: ID of the client to delete
        :return: True if deletion is successful, False otherwise
        """
        client = self.find_by_id(client_id)
        if client:
            self._delete_from_session(client)
            return True
        return False
