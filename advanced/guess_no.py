# guessnum using recursive function

import random
# from random import choice
from enum import Enum
import sys

# class guessnum(Enum): #enum is used to assign a number to a string in caps

#  ROCK = 1  # using word in caps that is constant
#  PAPER = 2  # using word in caps that is constant
#  SCISSOR = 3  # using word in caps that is constant



# print(name)

def guessnum(name):
    game_count = 0
    player_win = 0
    computer_win = 0

    # global name  
    def guess_num():
        print("")
        playerchoice = input(
            f"Welcome {name}! \nGuess the number what computer thinks \n")
        

        if playerchoice not in ["1","2","3"]:
            return guess_num()

        player=int(playerchoice)

        computerchoice = random.choice("123")

        computer =int(computerchoice)

        print(f"\n{name} chose {str(player).title()}")
        # print("\nYou choose "+ str(guessnum(player)).replace("guessnum.",'').title())
        print(f"Computer thinks about {str(computer).title()}")
        # print("Computer choose "+str(guessnum(computer)).replace("guessnum.",'').title())
       
        def game_play(player, computer):

            nonlocal player_win           
            nonlocal name           
            nonlocal computer_win           
               
            if player == computer:
                player_win += 1

                print(f"\nYou won {name}")
            elif player < 1 or player > 3 :
                print("\nInvalid input")
            else:
                print(f"\nBetter luck next time {name}")
                computer_win += 1
               

        game_play(player,computer)

        nonlocal game_count
        game_count += 1

        print("\nGame count",game_count)
        print(f"{name} Wins: {player_win}")
        # print(f"Computer: {computer_win}")
        print(f"{name}'s winning percentage is {(player_win/game_count):.2%}")




        while True:
            ask = input("\nPlay again?\nY for Yes\nN for No \n\n")

            if ask.lower() not in ["y", "n"]:
                continue
            else:
                break 
        if ask.lower() == "y":
            return guess_num()
        else:
            # sys.exit(f"Thanks for playing {name}.")
            if __name__ =="__main__":

            # playagain = False
                sys.exit(f"Bye! {name}")
            else:
                return

    return guess_num

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

    guess_number = guessnum(args.name)
    guess_number()



    
# play = guessnum()

# if __name__ == "__main__": # this line indicates if the file is main then run this play()
# #(If someone use this module it should not play automatically without calling play() , so __name__ == "__main__" is used)
# # this line used to change this file as module
#    play()





