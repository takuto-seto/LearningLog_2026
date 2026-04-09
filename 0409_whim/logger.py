from pathlib import Path
from datetime import datetime

base_path = Path(__file__).parent
target_file = "log.txt"
file_path = base_path / target_file

def log_message(message):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"{today}|{message}\n")



if __name__ == "__main__":
    log_message("test")