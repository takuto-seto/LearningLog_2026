from pathlib import Path

p = Path.cwd()

for item in p.iterdir():
    print(item.name)