# # rock paper scissors game method1

# import random

# computer1 = ["rock", "paper","scissor"]

# computerchoice =random.choice(computer1)
# # print(computer)

# def game(playerchoice):
#     if playerchoice == "rock" and computerchoice == "rock":
#         print("🤜🤛Tie")
#     elif playerchoice == "paper" and computerchoice == "paper":
#         print("🤜🤛Tie")
#     elif playerchoice == "scissor" and computerchoice == "scissor":
#         print("🤜🤛Tie")
#     elif playerchoice == "rock" and computerchoice == "scissor":
#         print("👌 You win")
#     elif playerchoice == "scissor" and computerchoice =="rock":
#         print("😒 Computer wins")
#     elif playerchoice == "rock" and computerchoice == "paper":
#         print("😒 Computer wins")
#     elif playerchoice == "paper" and computerchoice == "rock":
#         print("👌 You win")
#     elif playerchoice == "scissor" and computerchoice == "paper":
#         print("👌 You win")
#     elif playerchoice == "paper" and computerchoice == "scissor":
#         print("😒 Computer wins")
#     else:
#         print("Invalid input")


# a = input("Enter : ")
# game(a)

#method2
import random
from random import choice
from enum import Enum
import sys

class RPS(Enum): #enum is used to assign a number to a string in caps

 ROCK = 1  # using word in caps that is constant
 PAPER = 2  # using word in caps that is constant
 SCISSOR = 3  # using word in caps that is constant

# print(RPS())


print("")
playerchoice = input(
    "Enter ....\n1 for Rock, \n2 for paper or,\n3 for scissor \n\n")



player=int(playerchoice)

# if player <1 or player>3:
#     sys.exit("You must enter 1, 2 or 3")  # this method will exit the function



computerchoice = random.choice("123")

computer =int(computerchoice)

print("You choose "+ str(RPS(player)).replace("RPS.",'').title())
print("Computer choose "+str(RPS(computer)).replace("RPS.",'').title())


# print(player)
# print(computer)

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win")
elif player == computer:
    print("Tie")
elif player < 1 or player > 3 :
    print("Invalid input")
else:
    print("Computer wins")
    