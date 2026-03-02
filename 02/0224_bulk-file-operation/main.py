from pathlib import Path

p = Path.cwd()
count = 0
skip_count = 0

for item in p.glob("*test*.txt"):
    new_name = f"20260224_{item.name}"

    if "20260224" in item.name:
        print("日付入ってました。スキップします！")
        skip_count = skip_count + 1
        continue

    item.rename(item.parent / new_name)
    count = count + 1

print(f"リネームは合計{count}回")
print(f"SKIPは合計{skip_count}回")