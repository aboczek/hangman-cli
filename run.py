import random
from art import tprint
import gspread

word = ["test"]
GUESS_MISTAKES = 7

tprint("Welcome")
tprint("To")
tprint("Hangman")


def nickname():
    """
    Takes users nickname and displays it
    """
    user_input = input("Put your nickname here: ")
    print(f"Your nickname is {user_input}.")


nickname()


def start_game():
    """
    Starts the game when user types in "start"
    """
    start_input = input("To start game type in 'start': ")
    if start_input == "start":
        print("game started")


start_game()