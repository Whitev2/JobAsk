from pydantic import BaseSettings


class AppConfig(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = ".env"

        env_file_encoding = "utf-8"


config = AppConfig()
