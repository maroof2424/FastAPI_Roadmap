import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env: str = "dev"
    app_name: str = "FastAPI App"
    debug: bool = False
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

def get_settings():
    env = os.getenv("ENV", "dev")
    if env == "test":
        return Settings(_env_file=".env.test")
    return Settings()

settings = get_settings()
