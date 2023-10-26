from functools import lru_cache

from cacheout import Cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv = load_dotenv()


class Settings(BaseSettings):
    APP_VERSION: str
    # COUNTRIES
    COUNTRIES_BASE_URL: str
    COUNTRIES_BASE_URL_QUERY: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def URL(self) -> str:
        return self.COUNTRIES_BASE_URL + "/{name}" + self.COUNTRIES_BASE_URL_QUERY


@lru_cache
def _settings():
    return Settings()


settings = _settings()
V = int(settings.APP_VERSION)
cache = Cache(ttl=1200)
