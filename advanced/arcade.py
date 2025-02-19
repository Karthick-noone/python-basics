from rps_in_cmdlineargs import rps
from guess_no import guessnum
import sys
# name = rps_in_cmdlineargs.argparse(args.name)

def play_game(name = "Karthick"):

    Welcome_back = False

    while True:
        if Welcome_back == True:
            print(f"Welcome back to the arcade menu {name}\n")

        player_choice=input(f"Enter number \n1 for play Rock, Paper, Scissor,\n2 for Guess the number or \nenter x for exit\n\n")

        if player_choice not in ["1","2","x"]:
            print(f"{name} please enter number 1, 2 or x")
            return play_game(name)
        Welcome_back = True

        if player_choice == "1":
            rock_paper_scissor = rps(name)
            rock_paper_scissor()
        elif player_choice == "2":
            guess_number = guessnum(name)
            guess_number()
        else:
            sys.exit(f"Bye {name}")
        
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide name to play game"
    )

    parser.add_argument(
        "-n","--name", metavar="Name",
        required=True,help="Enter name to play game"
    )

    args = parser.parse_args()
    print(f"{args.name}! Welcome to the arcade")

    play_game(args.name)

