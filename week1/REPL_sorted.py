records = [
    {"分类": "餐饮", "金额": "33.5"},
    {"分类": "交通", "金额": "12.0"},
    {"分类": "餐饮", "金额": "88.0"},
]
print(sorted(records, key=lambda r: r["金额"]))

print(sorted(records, key=lambda r: r["金额"], reverse=True))

print(sorted(records, key=lambda r: (r["分类"], r["金额"])))
