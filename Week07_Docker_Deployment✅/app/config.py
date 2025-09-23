# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = False
    secret_key: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
