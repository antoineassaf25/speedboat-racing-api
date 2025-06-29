import psycopg2
import os

class Connection(object):

    # ensures only one connection with Singleton pattern
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Connection, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    connection = None

    def connect(self):
        if self.connection:
            return self.connection

        self.connection = psycopg2.connect(
            dbname=os.getenv("DB_DBNAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOSTNAME"),
            port=os.getenv("DB_PORT")
        )

        return self.connection
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
