from models.table import SQLTable
from typing import override, List

class Race(SQLTable):
    """
    Class which represents a race in a game.

    Attributes:
        race_id (int): primary key for this race
        map_name (str): the name of the map
        racer_rankings (List[int]): contains foreign keys of racers user_id, sorted from 1st place to 10th place
        race_start_time (float): the start time in seconds when the race started
    """

    def __init__(self,
        map_name: str,
        racer_rankings: List[float],
        race_start_time: float,
        race_id: int = None
    ):

        self.table_name = "races"
        self.map_name = map_name
        self.racer_rankings = racer_rankings
        self.race_start_time = race_start_time
    
    @override
    def to_dict(self) -> dict:
        return {
            "map_name": self.map_name,
            "racer_rankings": self.racer_rankings,
            "race_start_time": self.race_start_time
        }

    @override
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        return Race(data["map_name"], data["racer_rankings"], data["race_start_time"])
