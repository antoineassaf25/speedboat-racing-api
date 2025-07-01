from models.table import SQLTable
from typing import override

class Participant(SQLTable):
    """
    Class which represents a participant for one Race, linked to a User.

    Attributes:
        participant_id (int): Primary Key 
        user_id (int): Foreign Key linked to a User's user_id
        race_id (str): Foreign Key linked to a specific race
        finish_time (float): how long it took for the racer to complete the race in seconds
        boat_style (str): the style of the boat that is being used in this race
        boat_speed (int): The speed stat of the boat
        boat_acceleration (int): The acceleration stat of the boat
        boat_steering (int): The steering stat of the boat 
    """

    def __init__(self,
        user_id: int,
        race_id: int,
        finish_time: float,
        boat_style: str,
        boat_speed: int,
        boat_acceleration: int,
        boat_steering: int,
        participant_id: int = None
    ):

        self.table_name = "participants"
        self.user_id = user_id
        self.race_id = race_id
        self.finish_time = finish_time
        self.boat_style = boat_style
        self.boat_speed = boat_speed
        self.boat_acceleration = boat_acceleration
        self.boat_steering = boat_steering
        self.participant_id = participant_id
    
    @override
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "race_id": self.race_id,
            "finish_time": self.finish_time
            "boat_style": self.boat_style,
            "boat_speed": self.boat_speed,
            "boat_acceleration": self.boat_acceleration,
            "boat_steering": self.boat_steering
        }

    @override
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        return Participant(data["user_id"], data["race_id"], data["finish_time"], data["boat_style"], data["boat_speed"], data["boat_acceleration"], data["boat_steering"])
