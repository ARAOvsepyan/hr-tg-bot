import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).parent


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))

    class FSM:
        STORAGE = BASE_DIR / "storage"
        STORAGE.mkdir(exist_ok=True)