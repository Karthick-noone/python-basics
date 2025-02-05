# def painter():
#     print("painting")
# painter()

# def add():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(a+b)

# def sub():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter b number: "))
#     print(a-b)
# add()
# sub()


# def painter(msg):
#     print("Message: ",msg)
# painter("Paint my room")

# def findevenorodd(num):
#     # num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print("Even")
#     else: 
#         print("Odd")


# a = int(input("Enter a number: "))
# findevenorodd(a)

# pass or fail

# def passorfail(score):
#     if score >= 35 and score <= 100:
#         print("Pass")
#     elif score <35:
#         print("Fail")
#     else:
#         print("Invalid score")

# score = int(input("Enter your score: "))     
# passorfail(score)

def printrange(c,d):

    for i in range(c,d):
        print(i)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
printrange(a,b)
