from pathlib import Path

p = Path.cwd()

for item in p.glob("*.md"):
    print(item.name)