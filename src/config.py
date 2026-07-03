import os
from pathlib import Path

from src.env import load_env


SCRIPT_DIR = Path(__file__).resolve().parent
load_env(SCRIPT_DIR.parent / ".env")


OLLAMA_URL = os.getenv("OLLAMA_URL", "")
MODEL = os.getenv("MODEL", "")

LATITUDE = float(os.getenv("LATITUDE", 0))
LONGITUDE = float(os.getenv("LONGITUDE", 0))

GIT_REPO_PATH = os.getenv("GIT_REPO_PATH", os.getcwd())

WAIT_TIMEOUT_SEC = 120
QUIT_TIMEOUT_SEC = 0.3
POLL_INTERVAL_SEC = 2

