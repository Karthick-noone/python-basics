#rps using while loop

import random
from random import choice
from enum import Enum
import sys

class RPS(Enum): #enum is used to assign a number to a string in caps

 ROCK = 1  # using word in caps that is constant
 PAPER = 2  # using word in caps that is constant
 SCISSOR = 3  # using word in caps that is constant

playagain = True

while playagain:
    print("")
    playerchoice = input(
        "Enter ....\n1 for Rock, \n2 for paper or,\n3 for scissor \n\n")



    player=int(playerchoice)

    if player <1 or player>3:
        sys.exit("You must enter 1, 2 or 3")  # this method will exit the function



    computerchoice = random.choice("123")

    computer =int(computerchoice)

    print("You choose "+ str(RPS(player)).replace("RPS.",'').title())
    print("Computer choose "+str(RPS(computer)).replace("RPS.",'').title())

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

    ask = input("Do you want to play again?\nEnter Y for Yes\nEnter N for No \n\n")

    if ask.lower() =="y":
        continue
    else:
        playagain = False
        sys.exit("Thanks for playing")
        