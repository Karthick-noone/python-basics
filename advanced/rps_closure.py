# RPS using recursive function

import random
# from random import choice
from enum import Enum
import sys

class RPS(Enum): #enum is used to assign a number to a string in caps

 ROCK = 1  # using word in caps that is constant
 PAPER = 2  # using word in caps that is constant
 SCISSOR = 3  # using word in caps that is constant

def rps():
    game_count = 0
    player_win = 0
    computer_win = 0
    def play_rps():
        print("")
        playerchoice = input(
            "Enter ....\n1 for Rock, \n2 for paper or,\n3 for scissor \n\n")
        

        if playerchoice not in ["1","2","3"]:
            return play_rps()

        player=int(playerchoice)

        computerchoice = random.choice("123")

        computer =int(computerchoice)

        print(f"\nYou choose {str(RPS(player)).replace("RPS.",'').title()}")
        # print("\nYou choose "+ str(RPS(player)).replace("RPS.",'').title())
        print(f"Computer choose {str(RPS(computer)).replace("RPS.",'').title()}")
        # print("Computer choose "+str(RPS(computer)).replace("RPS.",'').title())
       
        def game_play(player, computer):

            nonlocal player_win           
            nonlocal computer_win           

            if player == 1 and computer == 3:
                player_win += 1
                print("\nYou win!")
               
            elif player == 2 and computer == 1:
                player_win += 1
                print("\nYou win!")
               

            elif player == 3 and computer == 2:
                player_win += 1
                print("\nYou win")
               
            elif player == computer:
                print("\nTie")
            elif player < 1 or player > 3 :
                print("\nInvalid input")
            else:
                print("\nComputer wins")
                computer_win += 1
               

        game_play(player,computer)

        nonlocal game_count
        game_count += 1

        print("\nGame count",game_count)
        print(f"Player: {player_win}")
        print(f"Computer: {computer_win}")

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

    return play_rps
    
play = rps()

if __name__ == "__main__": # this line indicates if the file is main then run this play()
#(If someone use this module it should not play automatically without calling play() , so __name__ == "__main__" is used)
# this line used to change this file as module
   play()





