files = ["layout_01.dwg", "schema_02.dwg", "layout_02.dwg", "manual.pdf", "layout_03.dwg"]
count = 0

for file in files:
    if "layout" in file:
        print(file)
        count = count + 1
    
print(f"合計: {count}個")