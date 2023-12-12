from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class PumpWaterUsage(db.Model, IDto):
    """
    Model declaration for PumpWaterUsage.
    """
    __tablename__ = "pump_water_usage"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pump_ID = db.Column(db.Integer, nullable=False)
    date_time_info = db.Column(db.String(45), nullable=False)
    water_amount = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"PumpWaterUsage({self.ID}, {self.pump_ID}, '{self.date_time_info}', '{self.water_amount}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "pump_ID": self.pump_ID,
            "date_time_info": self.date_time_info,
            "water_amount": self.water_amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PumpWaterUsage:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = PumpWaterUsage(
            pump_ID=dto_dict.get("pump_ID"),
            date_time_info=dto_dict.get("date_time_info"),
            water_amount=dto_dict.get("water_amount"),
        )
        return obj
