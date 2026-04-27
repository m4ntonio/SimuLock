from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/log.txt")

def log(message):
    LOG_FILE.parent.mkdir(exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")