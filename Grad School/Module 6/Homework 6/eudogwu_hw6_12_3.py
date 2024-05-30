"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: December 7 2019
Homework Problem: 12.3
ATM Machine class

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
    # Creates empty list for account
    accounts = []
    for i in range(0, 10):
        account = Account(i, 100)
        accounts.append(account)
    # Loops for input
    while True:
        account_id = float(input("Enter account id: "))

        while True:
            # ATM menu for user input
            print(
                "\n Main Menu \n 1: View Balance \n 2: Withdraw \n 3: Deposit \n "
                "4: Exit ")

            choice = int(input("\nEnter your choice: "))
            # creates input account
            for item in accounts:
                if item.get_id() == account_id:
                    input_account = item
                    break
            # User Choices and results
            if choice == 1:
                print("Your balance is", input_account.get_balance())

            elif choice == 2:
                input_amount = float(input("\nEnter amount to withdraw: "))
                input_account.set_withdraw(input_amount)
                print("Your account balance is",
                      input_account.get_total_balance())

            elif choice == 3:
                input_amount = float(input("\nEnter amount to Deposit: "))
                input_account.set_deposit(input_amount)
                print("Your account balance is",
                      input_account.get_total_balance())

            elif choice == 4:
                print("ATM will close because Transaction has completed")
                break  # breaks to loop
