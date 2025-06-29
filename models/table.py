from abc import ABC, abstractmethod

 # allows for forward reference
from __future__ import annotations

class SQLTable(ABC):
    """
        SQLTable is an abstract class which SQL table represntations extend.

        Subclasses of SQLTable must include:

            to_dict(): Converts the SQLTable instance into a dictionary
            from_dict(data: dict): Creates a SQLTable instance into a dictionary, also STATIC
    """

    @abstractmethod
    def to_dict(self) -> dict:
        pass
    

    @abstractmethod
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        pass
