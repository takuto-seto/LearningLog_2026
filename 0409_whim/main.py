import json
from pathlib import Path
from logger import log_message

base_path = Path(__file__).parent
config_path = base_path / "config.json"

with open(config_path, "r", encoding="utf-8") as f:

    conf = json.load(f)
    name = input("あなたのお名前を入力してください：")
    word = conf.get("greeting_word") or "こんにちは！"
    role = conf.get("user_role") or "さすらいの"
    message = f"{word}、{role} / {name}さん"


log_message(message)