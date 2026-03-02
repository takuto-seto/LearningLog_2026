from pathlib import Path

p = Path.cwd()

fix_count = 0

for item in p.glob("20260224*"):
    fix_name = item.name.replace("20260224_", "")

    if  "20260224" in item.name:
        item.rename(item.parent / fix_name)
        fix_count = fix_count + 1

print(f"日付削除回数{fix_count}回")
    