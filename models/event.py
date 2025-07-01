from models.table import SQLTable
from typing import override, Tuple

class Event(SQLTable):
    """
    Class which represents an event during a race.

    Attributes:
        event_id (int): primary key unique
        event_type (str): type of event ("participant hit", "supersonic", "item used", "participant stuck", etc)
        event_details (str): additional information explaining the event (who hit the participant, what item hit, etc)
        race_id (int): foreign key linked with associated race
        location (Tuple[float, float, float]): coordinates of where the event took place, relative to center of map
        time_at (float): seconds after the race start when the event happened
    """

    def __init__(self,
        event_type: str,
        event_details: str,
        race_id: int,
        location: Tuple[float, float, float],
        time_at: float,
        event_id: int = None
    ):

        self.table_name = "events"
        self.event_type = event_type
        self.event_details = event_details
        self.race_id = race_id
        self.location = location
        self.time_at = time_at
        self.event_id = event_id
    
    @override
    def to_dict(self) -> dict:
        return {
            "event_type": self.event_type,
            "event_details": self.event_details,
            "race_id": self.race_id,
            "location": self.location,
            "time_at": self.time_at,
        }

    @override
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        return Event(data["event_type"], data["event_details"], data["race_id"], data["location"], data["time_at"])
