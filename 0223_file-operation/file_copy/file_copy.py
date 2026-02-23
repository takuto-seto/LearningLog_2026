from pathlib import Path
import shutil

# source = Path("renamed_practice.txt")

# target_dir = Path("backup")

# target_dir.mkdir(parents=True, exist_ok=True)

# target = target_dir / "renamed2_practice.txt"

# source.rename(target)

target_dir2 = Path("copy")
target_dir2.mkdir(parents=True, exist_ok=True)

source_file = Path("backup") / "renamed2_practice.txt"
copy_target = Path("copy") / "copy_practice.txt"

shutil.copy(source_file, copy_target)