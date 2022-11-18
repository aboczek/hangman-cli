import random
from art import tprint
import gspread

word = ["test"]
user_nickname = []
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
