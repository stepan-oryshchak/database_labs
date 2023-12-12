from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Sensor(db.Model, IDto):
    """
    Model declaration for Sensor.
    """
    __tablename__ = "sensor"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_ID = db.Column(db.Integer, nullable=False)
    date_time_info = db.Column(db.String(45), nullable=False)
    humidity_level = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    illumination = db.Column(db.String(45), nullable=False)
    gps_latitude = db.Column(db.String(45), nullable=False)
    gps_longitude = db.Column(db.String(45), nullable=False)
    sensorcol = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Sensor({self.ID}, {self.client_ID}, '{self.date_time_info}', {self.humidity_level}, {self.temperature}, '{self.illumination}', '{self.gps_latitude}', '{self.gps_longitude}', '{self.sensorcol}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "ID": self.ID,
            "client_ID": self.client_ID,
            "date_time_info": self.date_time_info,
            "humidity_level": self.humidity_level,
            "temperature": self.temperature,
            "illumination": self.illumination,
            "gps_latitude": self.gps_latitude,
            "gps_longitude": self.gps_longitude,
            "sensorcol": self.sensorcol,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Sensor:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Sensor(
            client_ID=dto_dict.get("client_ID"),
            date_time_info=dto_dict.get("date_time_info"),
            humidity_level=dto_dict.get("humidity_level"),
            temperature=dto_dict.get("temperature"),
            illumination=dto_dict.get("illumination"),
            gps_latitude=dto_dict.get("gps_latitude"),
            gps_longitude=dto_dict.get("gps_longitude"),
            sensorcol=dto_dict.get("sensorcol"),
        )
        return obj
