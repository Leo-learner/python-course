from pathlib import Path
dry_run = True
p = Path('week1/rename_test')
items = list(p.iterdir())
sorted_items = sorted(items, key=lambda x: x, reverse=False)
for i, item in enumerate(sorted_items, start=1):
    new_stem = f"照片_{i:02}"
    new_path = item.with_stem(new_stem)
    if new_path.exists():
        print(f"Error: {new_path.name} already exists. Skipping {item.name}.")
        continue
    if not dry_run:
        item.rename(new_path)
        print(f"Renamed {item.name} to {new_path.name}")
    else:
        print(f"Dry run: {item.name} would be renamed to {new_path.name}")        
    