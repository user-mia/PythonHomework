"""
this is homework file fow week 6
SWE19033 HeWenxin
"""

import random
from functools import reduce


class BankAccount:
    """
    所有账户类的父类
    """

    def __init__(self):
        self.__id = '719033' + reduce(lambda x, y: str(x) + str(y),
                                      random.choices(range(0, 10), k=13))
        self.__balance = 0

    def deposit(self, amount_deposited):
        """存款，存款金额需 >= 0"""
        assert amount_deposited >= 0
        self.__balance += amount_deposited
        return self.__balance

    def withdraw(self, withdrawal_amount):
        """取款，取款金额 <= 账户余额"""
        assert self.__balance - withdrawal_amount >= 0
        self.__balance -= withdrawal_amount
        return self.__balance

    def balance(self):
        """返回账户余额"""
        return self.__balance

    def id(self):
        """返回账户id"""
        return self.__id

    def __str__(self):
        return f'账户:{self.__id}\t, 余额:{self.__balance:.3f}\t'


class SavingsAccount(BankAccount):
    """存款账户，继承自银行账户类"""

    def __init__(self):
        BankAccount.__init__(self)
        self.__account_type = 'deposit'
        self.__interest_rate = 0.025

    def raise_interest_rates(self, increment):
        """加息，利息可以为负"""
        self.__interest_rate += increment
        return self.__interest_rate

    def __str__(self):
        return BankAccount.__str__(self) + f', 账户种类：{self.__account_type}\t, ' \
                                           f'存款利率：{self.__interest_rate:+.4f}'


account = SavingsAccount()

print(account)
account.deposit(1)
print(account)
account.withdraw(0.1)
print(account)
account.raise_interest_rates(-0.2)
print(account)

print(BankAccount.id(account))
