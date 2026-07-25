def is_blank(input_str):
    if input_str == "":
        return True
    else:
        return False

def INPUT(str):
    input_str = input("请输入" + str + ": ").strip()
    while is_blank(input_str):
        input_str = input("输入不能为空，不能包含空格或其他符号，请重新输入: ").strip()
    return input_str

def INPUT_NUM(str):
    input_str = input("请输入" + str + ": ").strip()
    while not input_str.isdigit() or is_blank(input_str):
        input_str = input("输入必须为整数且不能为空，不能包含空格或其他字符，请重新输入: ").strip()
    return int(input_str)
records = []
print("欢迎使用支出记录系统!\n")
while True:
    print("1. 添加支出")
    print("2. 按金额排序列出全部")
    print("3. 分类汇总")
    print("0. 退出")
    choice = input("请选择操作: ")
    if choice == "1":
        category = INPUT("分类")
        amount = INPUT_NUM("金额")
        notes = INPUT("备注")
        records.append({"分类": category, "金额": amount, "备注": notes})
    elif choice == "2":
        print(sorted(sorted(records, key=lambda r: r["金额"])))
    elif choice == "3":
        if records == []:
            print("\n没有支出记录\n")
            continue
        summary = {}
        for record in records:
            category = record["分类"]
            amount = float(record["金额"])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        for category, total in summary.items():
            print(f"{category}: {total:.2f }")

#支出记录之所以用list而不用dict是因为支出记录可能包含相同的分类和金额，而字典要求键是唯一的。如果使用字典来存储支出记录，可能会导致数据覆盖或丢失。