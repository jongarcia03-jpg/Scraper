# src/utils.py
import json
from pathlib import Path
from datetime import date, datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def save_json(obj: dict):
    today = date.today().isoformat()  # YYYY-MM-DD
    timestamp = datetime.utcnow().strftime("%H%M%S")
    filename = DATA_DIR / f"{today}_{timestamp}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    return filename

