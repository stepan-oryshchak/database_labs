from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class PumpStatus(db.Model, IDto):
    """
    Model declaration for PumpStatus.
    """
    __tablename__ = "pump_status"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pump_ID = db.Column(db.Integer, nullable=False)
    work_status = db.Column(db.String(10), nullable=False)
    pump_statuscol = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"PumpStatus({self.ID}, {self.pump_ID}, '{self.work_status}', '{self.pump_statuscol}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "pump_ID": self.pump_ID,
            "work_status": self.work_status,
            "pump_statuscol": self.pump_statuscol,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PumpStatus:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = PumpStatus(
            pump_ID=dto_dict.get("pump_ID"),
            work_status=dto_dict.get("work_status"),
            pump_statuscol=dto_dict.get("pump_statuscol"),
        )
        return obj
