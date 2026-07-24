contacts = {}

while True:
    print("\n1. 添加联系人")
    print("2. 删除联系人")
    print("3. 查找联系人")
    print("4. 显示所有联系人")
    print("0. 退出系统")
    choice = input("请输入您的选择: ")

    if choice == '1':
        name = input("请输入联系人姓名: ").strip()  
        if name == "":
            print("联系人姓名不能为空，请重新输入。")
            continue
        if name in contacts:
            print(f"联系人 {name} 已存在，是否覆盖？(y/n): ")
            if input().lower() == 'y':
                phone = input("请输入联系人电话: ").strip()
                if phone == "":
                    print("联系人电话不能为空，请重新输入。")
                    continue
                contacts[name] = phone
                print(f"已更新联系人: {name} - {phone}")
            else:
                print("取消更新。")
        else:
            phone = input("请输入联系人电话: ").strip()
            if phone == "":
                print("联系人电话不能为空，请重新输入。")
                continue
            contacts[name] = phone
            print(f"已添加联系人: {name} - {phone}")
    elif choice == '2':
        name = input("请输入要删除的联系人姓名: ").strip()
        if name == "":
            print("联系人姓名不能为空，请重新输入。")
            continue
        if name in contacts:
            del contacts[name]
            print(f"已删除联系人: {name}")
        else:
            print(f"联系人 {name} 不存在")
    elif choice == '3':
        name = input("请输入要查找的联系人姓名: ").strip()
        if name == "":
            print("联系人姓名不能为空，请重新输入。")
            continue
        if name in contacts:
            print(f"联系人信息: {name} - {contacts[name]}")
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

   
