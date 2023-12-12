from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class ClientLocation(db.Model, IDto):
    """
    Model declaration for ClientLocation.
    """
    __tablename__ = "client_location"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_ID = db.Column(db.Integer, nullable=False)
    location_name = db.Column(db.String(45), nullable=False)
    gps_latitude = db.Column(db.String(45), nullable=False)
    gps_longitude = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"ClientLocation({self.ID}, {self.client_ID}, '{self.location_name}', '{self.gps_latitude}', '{self.gps_longitude}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "client_ID": self.client_ID,
            "location_name": self.location_name,
            "gps_latitude": self.gps_latitude,
            "gps_longitude": self.gps_longitude,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientLocation:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ClientLocation(
            client_ID=dto_dict.get("client_ID"),
            location_name=dto_dict.get("location_name"),
            gps_latitude=dto_dict.get("gps_latitude"),
            gps_longitude=dto_dict.get("gps_longitude"),
        )
        return obj
