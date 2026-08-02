class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def check(self):
        print(f"{self.account}账户的余额为{self.balance}")

    def deposit(self, num):
        self.balance += num
        return self.balance

    def withdraw(self, num):
        self.balance -= num
        return self.balance

a1 = BankAccount("张三", 100)
a2 = BankAccount("李四", 199)

#test
print(a1.account)
print(a2.account)
a1.check()
a2.check()
a1.deposit(100)
a1.check()