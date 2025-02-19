# RPS using recursive function

import random
# from random import choice
from enum import Enum
import sys

class RPS(Enum): #enum is used to assign a number to a string in caps

 ROCK = 1  # using word in caps that is constant
 PAPER = 2  # using word in caps that is constant
 SCISSOR = 3  # using word in caps that is constant



# print(name)

def rps(name):
    game_count = 0
    player_win = 0
    computer_win = 0

    # global name  
    def play_rps():
        print("")
        playerchoice = input(
            f"Welcome {name}! \nEnter ....\n1 for Rock, \n2 for paper or,\n3 for scissor \n\n")
        

        if playerchoice not in ["1","2","3"]:
            return play_rps()

        player=int(playerchoice)

        computerchoice = random.choice("123")

        computer =int(computerchoice)

        print(f"\n{name} chose {str(RPS(player)).replace("RPS.",'').title()}")
        # print("\nYou choose "+ str(RPS(player)).replace("RPS.",'').title())
        print(f"Computer chose {str(RPS(computer)).replace("RPS.",'').title()}")
        # print("Computer choose "+str(RPS(computer)).replace("RPS.",'').title())
       
        def game_play(player, computer):

            nonlocal player_win           
            nonlocal name           
            nonlocal computer_win           

            if player == 1 and computer == 3:
                player_win += 1
                print(f"\n{name} win!")
               
            elif player == 2 and computer == 1:
                player_win += 1
                print(f"\n{name} win!")
               

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
        print(f"{name}: {player_win}")
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
            # sys.exit(f"Thanks for playing {name}.")
            if __name__ =="__main__":

            # playagain = False
                sys.exit(f"Bye! {name}")
            else:
                return

    return play_rps

if __name__ =="__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Display name for who plays the game"
    )

    parser.add_argument(
        "-n", "--name",metavar="name",
        required=True,help="Enter name to display when you are playing"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()



    
# play = rps()

# if __name__ == "__main__": # this line indicates if the file is main then run this play()
# #(If someone use this module it should not play automatically without calling play() , so __name__ == "__main__" is used)
# # this line used to change this file as module
#    play()





