from os import environ
from typing import NamedTuple

__all__ = ("Config", "Postgresql", "WeatherAPIs")


class Config(NamedTuple):
    TOKEN = environ.get("BOT_TOKEN")
    GITHUB_URL = environ.get("GITHUB_URL", "https://github.com/Xithrius/Xythrion")


class WeatherAPIs(NamedTuple):
    EARTH = environ.get("OPENWEATHERMAP_TOKEN")
    MARS = environ.get("NASA_TOKEN")


class Postgresql(NamedTuple):
    USER = environ.get("POSTGRES_USER")
    PASSWORD = environ.get("POSTGRES_PASSWORD")
    DATABASE = environ.get("POSTGRES_DB")
    HOST = environ.get("POSTGRES_HOST")

    asyncpg_config = {
        "user": USER,
        "password": PASSWORD,
        "database": DATABASE,
        "host": HOST,
    }
    asyncpg_config_url = f"postgres://{USER}:{PASSWORD}@{HOST}:5432/{DATABASE}"
    asyncpg_default_docker_config = {
        "user": "postgres",
        "database": "postgres",
        "host": "localhost",
    }
