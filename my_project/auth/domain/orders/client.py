from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Client(db.Model, IDto):
    """
    Model declaration for Client.
    """
    __tablename__ = "client"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    mail = db.Column(db.String(45), nullable=True)
    phone_number = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Client({self.ID}, '{self.name}', '{self.mail}', '{self.phone_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "name": self.name,
            "mail": self.mail,
            "phone_number": self.phone_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Client(
            name=dto_dict.get("name"),
            mail=dto_dict.get("mail"),
            phone_number=dto_dict.get("phone_number"),
        )
        return obj
