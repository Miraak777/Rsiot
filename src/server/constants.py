from pathlib import Path
from dataclasses import dataclass

SERVER_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Paths:
    PATH_TO_CONFIG = str(Path(SERVER_DIR, "config.yml"))


@dataclass(frozen=True)
class ServerConstants:
    HOST: str = "host"
    PORT: str = "port"
    POST: str = "POST"
    GET: str = "GET"
    ID: str = "id"
    NAMING: str = "naming"
    PRICE: str = "price"
    CATEGORY: str = "category"
