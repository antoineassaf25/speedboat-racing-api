from __future__ import annotations
from models.table import SQLTable
from typing import override
import bcrypt

class APIUser(SQLTable):
    """
    Class which represents an api_user who has access to this API

    Attributes:
        id (int): primary key
        username (str): the api user's username
        password_hash (str): an encrypted password
        role (str): user role, can be Admin or None

    Methods:
        create_with_plain_password(username: str, plain_password: str, role: str) -> APIUser:
            will create an APIUser and encrypt the password with hashing
    """

    def __init__(self,
        username: str,
        password_hash: str,
        role: str,
        id: int = None,
    ):

        self.table_name = "api_users"
        self.username = username
        self.id = id
        self.password_hash = password_hash
        self.role = role

    @staticmethod
    def create_with_plain_password(username: str, plain_password: str, role: str) -> APIUser:
        # hashed value is a string, but bcrypt expects a byte string and returns bytes
        hashed = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt()).decode()
        return APIUser(username, hashed, role)

    
    @override
    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }

    @override
    @staticmethod
    def from_dict(data: dict) -> SQLTable:
        return APIUser(data["username"], data["password_hash"], data["role"])
