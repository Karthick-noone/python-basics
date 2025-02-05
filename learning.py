# print("Hello karthick")

# name = "Karthick"

# Age = 23

# height = 6.2

# is_developer = True 

# print(name, Age, height, is_developer)
# ///////////////////////////////////////
# # This program will ask for user's name and age, then display a message
# name = input("What's your name? ")
# age = int(input("How old are you? "))  # Convert input to integer

# # Output formatted message
# print(f"Hello, {name}! You are {age} years old.")
# ////////////////////////////////////////////

# Example: Age check
# age = int(input("How old are you? "))

# if age >= 18:
#     print("You are an adult!")
# else:
#     print("You are a minor!")
# ///////////////////////////
# a = 10 
# b = 25 
# print(a+b)


# ///////////////////////////
# # Ask the user for input
# user_input = input("How old are you? ")

# # Extract the number from the input
# age = int(''.join(filter(str.isdigit, user_input)))  # Filter only digits

# print(f"You are {age} years old.")
# ////////////////////////////////////////////
# question = input("how old are you?")

# age = int(''.join(filter(str.isdigit,question)))

# if age >= 18:
#     print("You are an adult!")
# else:
#     print("You are a minor!")

# ///////////////////////////////////

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number) 
# //////////////

# Example: Print numbers until 5
# count = 1
# while count <= 5:
#     print(count)
#     count += 1  # This increments the value of count by 1
# ///////////////////

# # Creating a list
# fruits = ["apple", "banana", "cherry"]

# # Accessing list items
# # print(fruits[0])  # Output: apple

# # Adding an item
# fruits.append("orange")

# # Removing an item
# fruits.remove("banana")

# # Loop through the list
# for fruit in fruits:
#     print(fruit)
# //////////////////////

# Define a function
# def greet(name):
#     print(f"Hello, {name}!")

# # Call the function
# greet("Alice")  # Output: Hello, Alice!
# greet("Bob")  # Output: Hello, Bob!

# ////////////////////

# import array

# # Array of integers
# numbers_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' means integer type
# print(numbers_array[3])

# ////////////////////////


# question = (input('How old are you?'))
 
# age = (''.join(filter(str.isdigit,question)))
# print(f'You are {age} years old.')


# # if age >= 18:
# #     print('You are an adult')
# # else:
# #     print('You are minor')

# //////////////////////

# fruits = ['Apple', 'Banana', 'Mango', 'Orange','Grapes']

# fruits.append('Guva')

# # fruits.pop(2)  
# # fruits.remove('Mango')  

# # for fruit in fruits:
# #     print(fruit)

# print(fruits)

# //////////////////////
# string usage
# name = input("Whats your name?")

# color = input("What is your favourite color?")

# print(f"Hii {name}! your favourite color is {color}")

# ////////////////////////

# Odd or even
# def num(number1):
#     if number1 % 2 == 0:
#         print(f"Even")
#     else:
#         print(f"ODD")

# question = int(input("Enter a number:"))

# num(question)
    # ///////////////////////


# positive or negative number

# def check_num(num):
#     if num > 0:
#         print('positive number')
#     elif num < 0:
#         print("negative number")
#     else:
#         print("it is zero")

# number = int(input("enter a number")) 
# check_num(number)       

# def sum_of_numbers(n):
#     return sum(range(1, n+2))

# # Example usage:
# n = int(input("Enter a number: "))
# print(f"Sum of first {n} numbers is: {sum_of_numbers(n)}")

# def calculator(num1, num2, operator):
#     if operator == '+':
#           return(num1 + num2)
#     elif operator == '-':
#          return(num1-num2)
#     elif operator == '*':
#          return(num1 * num2)
#     elif operator == '/':
#          if num2 != 0:
#               return(num1 / num2)
#          else:
#               return "Error" 
#     else:
#          return("invalid operators")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# operator = input('enter + or - or % or  *')

# print(f"The result is: {calculator(num1, num2, operator)}")


# ///////////////

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# # Example usage:
# n = int(input("Enter a number: "))
# print(f"Factorial of {n} is: {factorial(n)}")


# ///////////////

# def is_palindrome(p):
    
#     p = p.replace(" ","").lower()

#     return p == p[::-1]

# word = input("Enter a word to find its palindrome or not : ")

# if is_palindrome(word):
#     print("This is palindrome word")
# else:
#     print("its not palindrome")

# def fibonacci(n):
#     sequence = [0, 1]
    
#     # Generate the sequence
#     for i in range(2, n):
#         sequence.append(sequence[-1] + sequence[-2])
    
#     return sequence

# # Example usage
# n = int(input("Enter the number of terms for the Fibonacci sequence: "))
# print(f"The Fibonacci sequence up to {n} terms: {fibonacci(n)}")


# ///////////////////////

# Megna = "died"

# if Megna == "died":
#     print("Surya meets Priya")
# else:
#         print("surya weds Megna")

# question = input("Is Magna is alive? ").lower()

# if question == "yes":
#     print("Surya weds Megna")
# else:
#     print("Surya weds Priya")

# mark = int(input("what is your mark? "))

# if (mark >= 35):
#     print("You are pass")
# else:
#     print("You are fail")

# salary = int(input("How much is your salary? "))

# if (salary >= 7000):
#     print("You are not eligible for scholarship")
# else:
#     print("You are eligible for scholarship")

# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("Number is divisible by 3 and 5")
# else:
#     print("Number is not divisible by 3 and 5")

# ///////////////////odd or even

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# score = int(input("Enter your score: "))

# if score < 35 :
#     print("Poor student")
# elif score <= 70 :
#     print("Average student")
# elif score >= 90 and score <= 100:
#     print("Good student")
# else: 
#     print("Invalid input")

# ////////////mini calcaulator
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# operator = input("Enter anyone of these :+ ,-,*, /  :")

# def calculator(num1, num2, operator):
#     if operator == '+' :
#       return num1 + num2
#     elif operator == '-' :
#         return num1 - num2
#     elif operator == '*' :
#         return num1 * num2
#     elif operator == '/' :
#          if num2 != 0:
#             return num1 / num2
#          else :
#             return "invalid input"
#     else:
#         return "invalid operator" 

# print(f"result is {calculator(num1, num2, operator)}")        


# score = int(input("Enter your score:"))

# # dep = input("Enter your department: ")
# # loca = input("Enter your location: ")
# if score >= 70 :
#     name = input("Enter your name: ")
#     Dep = input("Enter your Department: ")
#     location = input("Enter location")
#     print(f"Your name is {name} , your department is {Dep} , your location is {location}")
# else:
#     print("you are not eligible")

# //////////

# salary = int(input("Enter your salary: "))
# age = int(input("Enter your age: "))

# if salary >= 20000 or age <= 25 :

#     loan=int(input("Enter your required loan amount: "))
#     if loan <= 200000 :
#         print("You are eligible for apply loan")
#     else :
#         print("We only give loan amount upto 2L only")
# else:
#     print("you are not eligible to get loan")

# /////////////////////

# a = int(input("Enter your Maths score: "))
# b = int(input("Enter your HCI score: "))
# c = int(input("Enter your Security score: "))
# d = int(input("Enter your IoT score: "))
# e = int(input("Enter your Cloud score: "))

# average =((a+b+c+d+e)/5)

# if average <= 35:
#     print(f"Your average score is {average}")
#     print("You need additional class")
# else:
#     print(f"Your average score is {average}")
#     print("You are good to go")

# n = int(input("Enter a number: "))

# if n  % 2 == 0 :
#     # print("Even")
#       if(n>=2) and (n<=5):
#         print("Not Weird")
#       elif(n >=6) and (n<=20 ):
#         print("Weired")
#       elif(n>20):
#         print("Not Weird")
# else:
#     print("Weird")

# ////////////

# n = int(input())

# for i in range(1, n+1):
#     print(i, end="")

   
# num = int(input())

# Thousand sorry

# n = int(input())

# for _ in range(n):
#     print("Sorry")

# if len(num) == 10 and num[0] in  [7, 8 ,9] and num.isdigit() :
#     print("Yes")
# else:
#     print("No")
# n = int(input())
# for _ in range(n):
#     print("Sorry")
# /////////////////////
# def validate_mobile_number(number):
#     if len(number) == 10 and number[0] in ['7', '8', '9'] and number.isdigit():
#         return "YES"
#     else:
#         return "NO"

# # Sample input
# n = int(input())

# # Loop for multiple inputs
# for _ in range(n):
#     number = input().strip()
#     print(validate_mobile_number(number))



# def validate_number(number):

#     if len(number) == 10 and number[0] in ['7','8','9'] and number.isdigit() :
#         return("Yes")
#     else:
#         return("No")

# n = int(input())
# for _ in range(n):

#     number =input().strip()
#     print(validate_number(number))


# def is_valid_email(email):
#     # Check if the email contains exactly one '@' and at least one '.'
#     if '@' in email and email.count('@') == 1:
#         local_part, domain_part = email.split('@')
#         if '.' in domain_part and len(local_part) > 0 and len(domain_part) > 0:
#             return True
#     return False

# # Input number of entries
# n = int(input())

# for _ in range(n):
#     # Read the input line (Name <email>)
#     name_and_email = input().strip()

#     # Extract the email using string slicing (remove '<' and '>')
#     name, email = name_and_email.split('<')
#     email = email.rstrip('>')

#     # Validate the email
#     if is_valid_email(email):
#         print(f"{name.strip()} <{email}>")



# exersice

# def is_valid_email(email):

#     if '@' in email and email.count('@') == 1 :
#         localpart, domainpart = email.split('@')

#         if '.' in domainpart and len(localpart) and len(domainpart) >0 :
#             return True

#     return False


