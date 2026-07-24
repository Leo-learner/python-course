contacts = {}

while True:
#直接使用 while choice != '0': 也可以实现相同的功能，甚至更简单。
    print("\n1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查找联系人")
    print("4. 显示所有联系人")
    print("0. 退出系统")
    choice = input("请输入您的选择: ")

    if choice == '1':
        name = input("请输入联系人姓名: ")
        if name == "":
            print("联系人姓名不能为空，请重新输入。")
            continue
        phone = input("请输入联系人电话: ")
        contacts[name] = phone
        print(f"已添加联系人: {name} - {phone}")
    elif choice == '2':
        name = input("请输入要删除的联系人姓名: ")
        if name in contacts:
            del contacts[name]
            print(f"已删除联系人: {name}")
        else:
            print(f"联系人 {name} 不存在")
    elif choice == '3':
        name = input("请输入要查找的联系人姓名: ")
        # if name == "":
        #     print("联系人姓名不能为空，请重新输入。")
        #     continue
        if name in contacts:
            print(f"联系人信息: {name} - {contacts.get(name)}")
        else:
            print(f"联系人 {name} 不存在")
    elif choice == '4':
        if contacts:
            print("所有联系人:")
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        else:
            print("通讯录为空")
    elif choice == '0':
        print("退出系统，感谢使用!")
        break
    else:
        print("无效的选择，请重新输入")

   
