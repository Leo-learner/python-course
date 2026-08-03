def is_blank(input_str):
    return input_str == ""

def input_string(prompt):
    input_str = input("请输入" + prompt + ": ").strip()
    while is_blank(input_str):
        input_str = input("输入不能为空，不能包含空格或其他符号，请重新输入: ").strip()
    return input_str

def input_num(prompt):
    input_str = input("请输入" + prompt + ": ").strip()
    while not input_str.isdigit():
        input_str = input("输入必须为整数且不能为空，不能包含空格或其他字符，请重新输入: ").strip()
    return input_str
records = []
print("欢迎使用支出记录系统!\n")
while True:
    print("1. 添加支出")
    print("2. 按金额排序列出全部")
    print("3. 分类汇总")
    print("0. 退出")
    choice = input("请选择操作:")
    if choice == "1":
        category = input_string("分类")
        amount = input_num("金额")
        notes = input_string("备注")
        records.append({"分类": category, "金额": amount, "备注": notes})
    elif choice == "2":
        if not records:
            print("\n没有支出记录\n")
            continue
        for record in sorted(records, key=lambda r: r["金额"]):
            print(f"分类: {record['分类']}, 金额: {record['金额']:.2f}, 备注: {record['备注']}")
    elif choice == "3":
        if not records:
            print("\n没有支出记录\n")
            continue
        summary = {}
        number = {}
        for record in records:
            category = record["分类"]
            amount = record["金额"]
            if category in summary:
                summary[category] += amount
                number[category] += 1
            else:
                summary[category] = amount
                number[category] = 1
        for category, total in summary.items():
            print(f"{category}: {total:.2f}, 笔数: {number[category]}")
    elif choice == "0":
        print("退出系统，感谢使用!")
        break
    else:
        print("无效的选择，请重新输入。")
