from pathlib import Path

# 元のファイル
source = Path("practice.txt")

# 移動先フォルダ
target_dir = Path("backup")

# 移動先フォルダが存在しない場合は作成する。すでに存在していてもエラーにしない
target_dir.mkdir(parents=True, exist_ok=True)

# 移動先ファイルと変更するファイル名を指定
target = target_dir / "renamed_practice.txt"

# 移動実行
source.rename(target)
