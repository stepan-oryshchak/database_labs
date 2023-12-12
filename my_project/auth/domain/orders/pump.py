from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Pump(db.Model, IDto):
    """
    Model declaration for Pump.
    """
    __tablename__ = "pump"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_ID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    time_on = db.Column(db.String(45), nullable=False)
    time_off = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Pump({self.ID}, {self.client_ID}, '{self.name}', '{self.time_on}', '{self.time_off}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "client_ID": self.client_ID,
            "name": self.name,
            "time_on": self.time_on,
            "time_off": self.time_off,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Pump:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Pump(
            client_ID=dto_dict.get("client_ID"),
            name=dto_dict.get("name"),
            time_on=dto_dict.get("time_on"),
            time_off=dto_dict.get("time_off"),
        )
        return obj
