from models.table import SQLTable
from typing import override

class User(SQLTable):
    """
    Class which represents a user in the game, can either be a user or a CPU.

    Attributes:
        user_id (int): The player's userid on Roblox, (or an integer 1-10 if a CPU)
        is_cpu (bool): Is the User a CPU? (a bot)
        username (str): The Roblox username of the user, or the NPC name
    """

    def __init__(self,
        user_id: int,
        is_cpu: bool,
        username: str
    ):

        self.table_name = "users"
        self.user_id = user_id
        self.is_cpu = is_cpu
        self.username = username
    
    @override
    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "is_cpu": self.is_cpu,
            "username": self.username
        }

    @override
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        return User(data["user_id"], data["is_cpu"], data["username"])
