import random
from art import tprint
import gspread

words = "test"
guess = []
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


def guess_word():
    """
    Draws random word from list and makes it guessable
    """
    for word in words:
        print("_", end=" ")
    guess_input = input("\nYour guessed letter: ")
    for letter in words:
        if guess_input == letter:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def start_game():
    """
    Starts the game when user types in "start"
    """
    start_input = input("To start game type in 'start': ")
    if start_input == "start":
        guess_word()
    else:
        print("wrong input please try again")
        start_game()


start_game()


def print_guess_word():
    """
    prints guessed letter in word if it is correct
    """
    

