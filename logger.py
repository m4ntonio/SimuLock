from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/log.txt")

def log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {message}\n")