from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    ORIGINS: str = "*"
    ROOT_PATH: str = ""
    ENV: str = "DEV"
    LOG_LEVEL: str = "DEBUG"

    POSTGRES_SCHEMA: str = "hospital"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_DB: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: SecretStr = "postgres"
    POSTGRES_PASSWORD: SecretStr = "postgres"
    POSTGRES_RECONNECT_INTERVAL_SEC: int = 1

    @property
    def postgres_url(self) -> str:
        creds = f"{self.POSTGRES_USER.get_secret_value()}:{self.POSTGRES_PASSWORD.get_secret_value()}"
        return f"postgresql+asyncpg://{creds}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
