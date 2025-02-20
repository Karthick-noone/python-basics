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
        self.amount = amount
        dept_amount = self.amount + self.balance
        print(f"\nFor account {self.name} {self.amount} is deposited\nBalance amount is {dept_amount}")

    def viable_amount(self, amount):
        if self.balance >= amount:
            return
        raise BalanceException(f"Insufficient Balance, account only has {self.balance}")


    def withdraw(self,amount):
        try:
            self.viable_amount(amount)
            self.balance - amount
            print("Withdraw completed")
            self.get_balance()
        except BalanceException as error:
            print(f"Error during withdraw {error}" )


