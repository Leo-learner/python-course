print("我的 __name__ 是：", __name__)
class ContactNotFound(Exception):
    pass
def is_blank(input_str):
    return input_str.strip() == ""
def blank_resolver(input_str):
    while is_blank(input_str):
        input_str = input("输入不能为空，请重新输入: ").strip()
    return input_str
def show_all_contacts(contacts):
    if contacts:
        print("所有联系人:")
        for name, phone in contacts.items():
            print(f"{name} - {phone}")
    else:
        print("通讯录为空")
#=================================================
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone):
        self.contacts[name] = phone
            
    def delete(self, name):
        del self.contacts[name]
    
    def find(self, name):
        try: 
            return self.contacts[name]
        except KeyError :
            raise ContactNotFound(f"联系人{name}不存在")

    def check(self, name):
        return name in self.contacts

    def show_all(self):
        return self.contacts.copy()

#=================================================
def main():
    customer = ContactBook()
    while True:
        print("\n1. 添加联系人")
        print("2. 删除联系人")
        print("3. 查找联系人")
        print("4. 显示所有联系人")
        print("0. 退出系统")
        choice = input("请输入您的选择: ")

        if choice == '1':
            name = blank_resolver(input("请输入联系人姓名: "))
            if customer.check(name):
                print(f"联系人 {name} 已存在，是否覆盖？(y/n): ")
                if input().lower() == 'y':
                    phone = blank_resolver(input("请输入联系人电话: "))
                    customer.add(name, phone)
                    print(f"已更新联系人: {name} - {phone}")
                else:
                    print("取消更新。")
            else:
                phone = blank_resolver(input("请输入联系人电话: "))
                customer.add(name, phone)
                print(f"已添加联系人: {name} - {phone}")
        elif choice == '2':
            name = blank_resolver(input("请输入要删除的联系人姓名: "))
            if customer.check(name):
                customer.delete(name)
                print(f"已删除联系人: {name}")
            else:
                print(f"联系人 {name} 不存在")
        elif choice == '3':
            name = blank_resolver(input("请输入要查找的联系人姓名: "))
            try:
                phone = customer.find(name)
                print(f"联系人信息: {name} - {phone}")
            except ContactNotFound as e:
                print(e)
        elif choice == '4':
            contacts = customer.show_all()
            show_all_contacts(contacts)
        elif choice == '0':
            print("退出系统，感谢使用!")
            break
        else:
            print("无效的选择，请重新输入")
if __name__ == "__main__":
    main()