from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class SprinklerUsage(db.Model, IDto):
    """
    Model declaration for SprinklerUsage.
    """
    __tablename__ = "sprinkler_usage"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sprinkler_location_ID = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"SprinklerUsage({self.ID}, {self.sprinkler_location_ID}, '{self.start_time}', '{self.end_time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "sprinkler_location_ID": self.sprinkler_location_ID,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SprinklerUsage:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SprinklerUsage(
            sprinkler_location_ID=dto_dict.get("sprinkler_location_ID"),
            start_time=dto_dict.get("start_time"),
            end_time=dto_dict.get("end_time"),
        )
        return obj
