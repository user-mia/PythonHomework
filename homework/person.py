"""
test file
SWE19033 hwx
"""


class BankAccount:
    id = ''
    saving = 0

    def __init__(self, id, saving):
        self.id = id
        self.saving = saving

    def info(self):
        print('账号：', self.id)
        print('当前余额：', self.saving)

    def deposit(self, money):
        self.saving += money

    def withdraw(self, money):
        self.saving -= money

    def do(self, change, money):
        if change == '存款':
            self.deposit(money)
        else:
            self.withdraw(money)


class SavingsAccount(BankAccount):
    interest = 0

    def __init__(self, id, saving, interest):
        super().__init__(id, saving)
        self.interest = interest

    def increase_interest(self):
        self.saving *= (1 + self.interest)
        print('结息(利率%.2f)：' % self.interest)
        BankAccount.info(self)


customer = SavingsAccount('001', 10000, 0.03)
customer.info()
customer.do('存款', 5000)
customer.info()
customer.increase_interest()
customer.do('取款', 2000)
customer.info()
