import random
from art import tprint
import gspread


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
    dicto = ["house", "leave", "letter"]
    word = random.choice(dicto)
    guesses = []
    guess_mistakes = 7
    finished = False

    while not finished:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess_input = input("Guess the letter: ")
        guesses.append(guess_input.lower())

        if guess_input.lower() not in word.lower():
            guess_mistakes -= 1
            if guess_mistakes == 0:
                break

    finished = True
    for letter in word:
        if letter.lower() not in guesses:
            finished = False

    if finished:
        print("Congratulations you guessed the word")

    else:
        print("You lost all of ur lifes")


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
