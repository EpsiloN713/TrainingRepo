"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 7.1
Creating Rectangle Class
"""


class Account:
    """Constructs Account object and all it's contents and defaults"""
    def __init__(self, id=0, balance=100, annual_interest_rate=0, deposit=0,
                 withdraw=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate
        self.__deposit = deposit
        self.__withdraw = withdraw

    def __str__(self):
        """Returns Print string for account object"""
        return ("Account: {id}, Balance: {balance}, Monthly Interest Rate: {"
                "MIR}, Monthly Interest: {MI}".format(id=self.__id,
                                                      balance=self.get_total_balance(),
                                                      MIR=self.get_monthly_interest_rate(),
                                                      MI=self.get_monthly_interest()))

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annual_interest_rate(self):
        return self.__get_annual_interest_rate

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate

    def set_id(self, id):
        self.__id = id

    def set_balance(self, balance):
        self.__balance = balance

    def get_monthly_interest_rate(self):
        """Calculates Monthly Interest Rate"""
        monthly_interest_rate = (self.__annual_interest_rate / 1200) * 100
        return monthly_interest_rate

    def get_deposit(self):
        return self.__deposit

    def get_withdraw(self):
        return self.__withdraw

    def get_monthly_interest(self):
        """Calculates monthly interest"""
        monthly_interest = self.get_balance() * self.get_monthly_interest_rate()
        return monthly_interest

    def set_withdraw(self, withdraw):
        self.__withdraw = withdraw

    def set_deposit(self, deposit):
        self.__deposit = deposit

    def get_total_balance(self):
        """Calculates the total balance so that it could be used later"""
        total_balance = self.get_balance() + self.__deposit - self.__withdraw
        return total_balance


if __name__ == '__main__':
    # Accounts set up for testing. Results are printed
    my_account1 = Account(id=1122, balance=20000, annual_interest_rate=4.5)
    my_account1.set_withdraw(2500)
    print(my_account1)
    my_account2 = Account(id=1122, balance=20000, annual_interest_rate=4.5)
    my_account2.set_deposit(3000)
    print(my_account2)
