# RPS using recursive function

import random
# from random import choice
from enum import Enum
import sys

class RPS(Enum): #enum is used to assign a number to a string in caps

 ROCK = 1  # using word in caps that is constant
 PAPER = 2  # using word in caps that is constant
 SCISSOR = 3  # using word in caps that is constant

# playagain = True
game_count =  0
# while playagain:
def play_rps():
    print("")
    playerchoice = input(
        "Enter ....\n1 for Rock, \n2 for paper or,\n3 for scissor \n\n")
    

    if playerchoice not in ["1","2","3"]:
        return play_rps()

    player=int(playerchoice)

    # if player <1 or player>3:
    #     sys.exit("You must enter 1, 2 or 3")  # this method will exit the function



    computerchoice = random.choice("123")

    computer =int(computerchoice)

    print("You choose "+ str(RPS(player)).replace("RPS.",'').title())
    print("Computer choose "+str(RPS(computer)).replace("RPS.",'').title())

    def game_play(player, computer):

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
    game_play(player,computer)

    global game_count
    game_count += 1

    print("Game count",game_count)

    while True:
        ask = input("\nPlay again?\nY for Yes\nN for No \n\n")

        if ask.lower() not in ["y", "n"]:
            continue
        else:
            break 
    if ask.lower() == "y":
        return play_rps()
    else:
        sys.exit("Thanks for playing")
        # playagain = False
            # sys.exit("Thanks for playing")

play_rps()
        