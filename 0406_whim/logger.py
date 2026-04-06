from datetime import datetime
from pathlib import Path
import os.path

base_path = Path(__file__).parent
file_path = base_path / "log.txt"

def logger_message(message):
    today = datetime.now().strftime("%Y-%m-%d %H %M %S ")

    with open(file_path, "a") as f:
        f.write(f"{today}:{message}\n")


logger_message("test")