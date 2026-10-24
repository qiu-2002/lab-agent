from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# 后端项目的根目录
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:root@localhost:3306/lab_agent?charset=utf8mb4"

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")

settings = Settings()




