import random
from art import tprint
import gspread
import time


dicto = ["house", "leave", "letter", "Python", "Java"]
word = random.choice(dicto)
guesses = []
GUESS_MISTAKE = 7
FINISHED = False


tprint("Welcome")
tprint("To")
tprint("Hangman")


def nickname():
    """
    Takes users nickname and displays it
    """
    user_input = input("Put your nickname here: ")
    print("")
    time.sleep(1)
    print(f"Your nickname is {user_input}.")
    print("")


nickname()


def rules():
    """
    Displays rules after setting your nickname up.
    """
    time.sleep(1)
    tprint("Rules")
    print("")
    time.sleep(1)
    print("1.Random word is printed out and you have to guess it")
    print("")
    time.sleep(1)
    print("2.You guess 1 letter at a time if its correct it will be displayed")
    print("")
    time.sleep(1)
    print("3.If not you lose one life out of 7")
    print("")
    time.sleep(1)
    print("Enjoy the Hangman game.")
    print("")
    time.sleep(1)


rules()


def guess_word():
    """
    Draws random word from list and makes it guessable
    """
    global word, guesses, GUESS_MISTAKE, FINISHED
    while not FINISHED:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess_input = input("Guess the letter: ")
        guesses.append(guess_input.lower())

        if guess_input == "":
            print("\n Warning! your input cannot be empty")

        if guess_input.lower() not in word.lower():
            GUESS_MISTAKE -= 1
            if GUESS_MISTAKE == 0:
                break

        FINISHED = True
        for letter in word:
            if letter.lower() not in guesses:
                FINISHED = False

    if FINISHED:
        print("Congratulations you guessed the word")
        FINISHED = False
        guesses.clear()
        time.sleep(1)
        guess_word()
    else:
        print("You lost all of ur lifes")


def start_game():
    """
    Starts the game when user types in "start"
    """
    start_input = input("To start game type in 'start': ")
    print("")
    if start_input == "start":
        time.sleep(1)
        guess_word()
    else:
        print("wrong input please try again")
        start_game()


start_game()
