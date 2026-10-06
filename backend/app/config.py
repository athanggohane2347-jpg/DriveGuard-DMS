from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DriveGuard DMS"
    environment: str = "development"
    database_url: str = "sqlite:///./data/driveguard.db"
    secret_key: str = "change-this-in-production"
    access_token_expire_minutes: int = 1440
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    simulation_mode: bool = True
    camera_index: int = 0
    recording_enabled: bool = False
    recordings_path: str = "./recordings"
    model_path: str = "./models"
    yolo_model_path: str | None = None
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]

    def ensure_paths(self) -> None:
        for value in ("./data", self.recordings_path, "./logs", self.model_path):
            Path(value).mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.ensure_paths()
    return settings
