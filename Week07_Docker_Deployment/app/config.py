from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./test.db"  # ✅ SQLite default

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
