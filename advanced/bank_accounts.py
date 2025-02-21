class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created,\nBalance = {self.balance}")

    def get_balance(self):
        print(f"\nAccount {self.name} \nBalance = {self.balance}")

    def deposit_amount(self, amount):
        self.balance = self.balance + amount
        print(f"\nFor account {self.name} {amount} is deposited\nBalance amount is {self.balance}")

    def viable_amount(self, amount):
        if self.balance >= amount:
            return
        raise BalanceException(f"Insufficient Balance, account only has {self.balance}")


    def withdraw(self,amount):
        try:
            self.viable_amount(amount)
            self.balance = self.balance - amount
            print(f"Withdraw completed\nwithdraw amount is {amount}")
            self.get_balance()
        except BalanceException as error:
            print(f"Error during withdraw {error}" )


    def transaction(self, amount, account):
        try:
            self.viable_amount(amount)
            self.withdraw(amount)
            account.deposit_amount(amount)
            print(f"Amount {amount} transfered successfully.")
            # self.get_balance()
        except BalanceException as error:
            print(f"Transaction is not completed {error}")  



class InterestRewardAcc(BankAccount):
    def deposit_amount(self, amount):    
        # self.account = account
        self.balance = self.balance  + (amount * 1.05) # 5 % interest
        self.get_balance()
        print(f"***************************************")
        print(f"\nDeposited, balance amount is {self.balance}")


class SavingsAcc(InterestRewardAcc):

    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 10


    def withdraw(self, amount):
        try:

            self.viable_amount(amount)
            self.balance = self.balance - ( amount + self.fee)
            self.get_balance()
            print("=============================================")
            print(f"withdrawn completed from savings account")
        except BalanceException as error:
            print(error)