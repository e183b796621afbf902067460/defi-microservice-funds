from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
import os
from urllib.parse import quote_plus

from head.interfaces.db.settings.interface import ISettings


class ORMSettings(ISettings):
    DB_ADDRESS = os.getenv('DB_ADDRESS', 'localhost')
    DB_USER = os.getenv('DB_USER', 'username')
    DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD', '111222'))
    DB_NAME = os.getenv('DB_NAME', 'funds')

    DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}'
    DB_ENGINE = create_engine(DB_URL)

    @classmethod
    def get_engine(cls) -> Engine:
        return cls.DB_ENGINE

    @classmethod
    def get_uri(cls) -> str:
        return cls.DB_URL
