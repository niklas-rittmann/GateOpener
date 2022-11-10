from pathlib import Path

from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings


class Envs(BaseSettings):
    """Wrapper for environmental infos"""

    gate_pin: int
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


TEMPLATES_DIR = Jinja2Templates(directory=Path(__file__).parents[1] / "templates")
STATIC_DIR = Path(__file__).parents[1] / "static"
