from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class SprinklerStatus(db.Model, IDto):
    """
    Model declaration for SprinklerStatus.
    """
    __tablename__ = "sprinkler_status"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sprinkler_location_ID = db.Column(db.Integer, nullable=False)
    work_status = db.Column(db.String(3), nullable=False)
    sprinkler_statuscol = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"SprinklerStatus({self.ID}, {self.sprinkler_location_ID}, '{self.work_status}', '{self.sprinkler_statuscol}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "sprinkler_location_ID": self.sprinkler_location_ID,
            "work_status": self.work_status,
            "sprinkler_statuscol": self.sprinkler_statuscol,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SprinklerStatus:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SprinklerStatus(
            sprinkler_location_ID=dto_dict.get("sprinkler_location_ID"),
            work_status=dto_dict.get("work_status"),
            sprinkler_statuscol=dto_dict.get("sprinkler_statuscol"),
        )
        return obj
