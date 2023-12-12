from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class SprinklerNozzles(db.Model, IDto):
    """
    Model declaration for SprinklerNozzles.
    """
    __tablename__ = "sprinkler_nozzles"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_ID = db.Column(db.Integer, nullable=False)
    maximum_water_consumption = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"SprinklerNozzles({self.ID}, {self.client_ID}, {self.maximum_water_consumption})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "client_ID": self.client_ID,
            "maximum_water_consumption": self.maximum_water_consumption,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SprinklerNozzles:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SprinklerNozzles(
            client_ID=dto_dict.get("client_ID"),
            maximum_water_consumption=dto_dict.get("maximum_water_consumption"),
        )
        return obj
