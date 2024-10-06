import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
from dotenv import load_dotenv

class _BaseSettings(BaseSettings):
    ...


class DbSettings(_BaseSettings):
    host: str
    port: str
    user: str
    password: str
    database: str

    @property
    def dsn(self) -> PostgresDsn:
        return PostgresDsn(
            'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )


    @property
    def sync_dsn(self) -> PostgresDsn:
        return PostgresDsn(
            'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )


class LoggingSettings(_BaseSettings):
    level: str


class TelegramSettings(_BaseSettings):
    token: str


class Settings(_BaseSettings):
    logging: LoggingSettings
    db: DbSettings
    tg: TelegramSettings


@lru_cache
def get_settings() -> Settings:
    load_dotenv()
    return Settings(
        logging=LoggingSettings(
            level=os.getenv('LOGLEVEL', 'INFO'),
        ),
        db=DbSettings(
            host=os.getenv('POSTGRES_DSN', 'localhost'),
            port=os.getenv('POSTGRES_PORT', '5432'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'post'),
            database=os.getenv('POSTGRES_DATABASE', 'postgres'),
        ),
        tg=TelegramSettings(
            token=os.getenv('TELEGRAM_TOKEN', ''),
        )
    )


settings: Settings = get_settings()
