from bank_accounts import *

Karthick = BankAccount(5000,"Karthick")
Sura = BankAccount(3000,"Mareeswaran")

# Karthick.get_balance()

Karthick.deposit_amount(4000)

Karthick.withdraw(100)

# Sura.withdraw(4000)

Karthick.transaction(2000,Sura)

Nagesh = InterestRewardAcc(300, "Nagesh")

Nagesh.deposit_amount(500)

Rahul = SavingsAcc(500, "Rahul")
Rahul.withdraw(300)