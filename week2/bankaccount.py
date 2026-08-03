class BankError(Exception):
    pass
class InvalidAmountError(BankError):
    pass
class InsufficientFundsError(BankError):
    pass
class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def check(self):
        print(f"{self.account}账户的余额为：{self.balance}")

    def deposit(self, num):
        if num <= 0:
            raise ValueError(f"存款金额必须大于零！试图存款{num}")
        self.balance += num
        return self.balance

    def withdraw(self, num):
        if num <= 0:
            raise InvalidAmountError(f"取款金额必须大于零！试图取款{num}")
        if num > self.balance:
            raise InsufficientFundsError(f"余额不足：余额 {self.balance} 试图取款{num}")
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
try:
    a1.withdraw(15)
except (ValueError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
a1.check()
try:
    a1.withdraw(5000)
except (ValueError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
a1.check()
try:
    a1.deposit(-10)
except (ValueError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
a1.check()
try:
    a1.withdraw(-10)
except (ValueError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
a1.check()
try:
    a1.withdraw(0)
except (ValueError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
a1.check()