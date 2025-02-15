# closure
# used for  data hiding, callback functions, and decorators.

# once the function is returns then we donot have access to the functions variables , so we use closure 

# Eg: 
# def example():
#     x = 10  # x is a local variable
#     return x

# print(example())  # ✅ Output: 10
# print(x)  # ❌ NameError: name 'x' is not defined


# def parent_function(n):
#     def inner_function():
#         return n
#     return inner_function #here parent function return inner funtion


# print( parent_function(5)()) # so we use this method to print 5 or below method

# output = parent_function(6)
# print(output()) # this output () calls the innerfunction


# def daddy(child, coins):
#     # coins = 5 

#     def play_game():
        
#         nonlocal coins 
#         coins -= 1

#         if coins > 1:
#             print (f"{child} has {coins} coins left")
#         elif coins == 1 :
#             print(f"{child} has {coins} coin left")
#         else:
#             print(f"{child} out of coins")
#     return play_game

# karthick = daddy("Karthick",5)

# karthick()
# karthick()
# # karthick()
# # karthick()
# # karthick()
# nagesh = daddy("Nagesh", 7)
# print('')
# nagesh()
# nagesh()


# def multi_mulipier(n):
#     def multiplier(x):
#         return n * x
#     return multiplier

# times3 = multi_mulipier(5)
# print(times3(3))

# times5 = multi_mulipier(5)
# print(times5(8))

# print(times5(times3(3)))


# def bank_account(initial_amount):
#     balance =  initial_amount
#     def transaction(amount):

#         nonlocal balance

#         if amount > 0 :
#             newbalance = balance + amount
#             print(f"Deposited amount is {amount}, Balance amount is {newbalance}")
#         elif amount < 0 and abs(amount) <= balance:

#             newbalance = balance + amount
#             print(f"Withdrawn amount is {abs(amount)} balance amount is {newbalance}")
#         else:
#             print("Insufficient balance")
#     return transaction

# user = bank_account(50000)

# user(2000)
# user(-5000)
# user(-60000)


# amount = -6000

# print(amount)  # o/p -6000
# print(abs(amount)) #o/p 6000