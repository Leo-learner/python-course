from pathlib import Path
p = Path('week1/rename_test')
# i = 0
# for item in p.iterdir():
#     i += 1
#     item.stem = '照片_' + f"{i:02}" 
#     item.suffix = '.jpg'
#     print(item.name)
items = list(p.iterdir())
for i, item in enumerate(items, start=1):
    new_name = f"照片_{i:02}.jpg"
    new_path = item.with_name(new_name)
    item.rename(new_path)
    print(f"Renamed {item.name} to {new_name}")
