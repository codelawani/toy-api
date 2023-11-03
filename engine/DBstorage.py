from os import getenv

from sqlalchemy import create_engine

DB_URI = getenv("DB_URI")


class DBStorage:
    """Interface to the Database"""
    engine = None
    session = None

    def __init__(self) -> None:
        self.engine = create_engine(DB_URI, pool_pre_ping=True)
