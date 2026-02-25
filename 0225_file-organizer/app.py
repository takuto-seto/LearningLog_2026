from pathlib import Path

# キーが拡張子、値が移動先フォルダの辞書を作成
rules = {
    ".txt": "Documents",
    ".csv": "Data",
    ".pdf": "Reports",
    ".log": "logs"
}

p = Path(__file__).parent

# このファイルと同じ階層にrules.valueのfolderを作成する。すでにある場合はエラーにしない
for folder_name in rules.values():
    folder_path = p / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    

# itemに同じ階層のファイルを入れる
for item in p.iterdir():
    # itemがファイルかつこのファイルと異なる名前のとき、
    if item.is_file() and item.name != Path(__file__).name:
        # extにitemの拡張子を入れる
        ext = item.suffix

        # rulesにext(例えば.txt)があれば、
        if ext in rules:
            #target_dirにこのファイルと同じ階層までのファイルパス/rules[key](.txtならDocuments)を入れる
            target_dir = p / rules[ext]
            target_path = target_dir / item.name

            item.rename(target_path)
            print(f"移動：{item.name} -> {rules[ext]}")