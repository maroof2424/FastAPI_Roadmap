from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = False
    database_url: str

    model_config = SettingsConfigDict(env_file=".env",extra="ignore")


settings = Settings()