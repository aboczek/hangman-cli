import random
import time
from art import tprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman")


dicto = ["house", "leave", "letter", "Python", "Java"]
word = random.choice(dicto)
GUESSES = []
GUESS_MISTAKE = 7
FINISHED = False
highscore = SHEET.worksheet("hangman_sheet")
SCORE = 0


tprint("                Welcome")
tprint("                To")
tprint("                Hangman")


def nickname():
    """
    Takes users nickname and displays it
    """
    time.sleep(1)
    user_input = input("Put your nickname here: ")
    print("")
    time.sleep(1)
    print(f"Your nickname is {user_input}.")
    print("")


def rules():
    """
    Displays rules after setting your nickname up.
    """
    time.sleep(1)
    tprint("                Rules")
    print("")
    time.sleep(1)
    print("1.Random word is printed out and you have to guess it")
    print("")
    time.sleep(1)
    print("2.You guess 1 letter at a time if its correct it will be displayed")
    print("")
    time.sleep(1)
    print("3.If not you lose one life out of seven")
    print("")
    time.sleep(1)
    print("Enjoy the Hangman game.")
    print("")
    time.sleep(3)
    tprint("                5")
    time.sleep(1)
    tprint("                4")
    time.sleep(1)
    tprint("                3")
    time.sleep(1)
    tprint("                2")
    time.sleep(1)
    tprint("                1")
    time.sleep(1)


# def show_highscore():


def guess_word():
    """
    Draws random word from list and makes it guessable
    """
    global word, GUESSES, GUESS_MISTAKE, FINISHED, SCORE
    while not FINISHED:
        for letter in word:
            if letter.lower() in GUESSES:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess_input = input("Guess the letter: ")
        GUESSES.append(guess_input.lower())

        if guess_input == "":
            print("\n Warning! your input cannot be empty")

        if guess_input.lower() not in word.lower():
            GUESS_MISTAKE -= 1
            if GUESS_MISTAKE == 0:
                break

        FINISHED = True
        for letter in word:
            if letter.lower() not in GUESSES:
                FINISHED = False

    if FINISHED:
        SCORE += 1
        print("Congratulations you guessed the word")
        print("")
        print(f"your score is {SCORE}")
        print("")
        finished_input = input("Do you want to 'continue' or 'finish'?\n")
        print("")
        if finished_input == "continue":
            tprint("Next word:")
            time.sleep(1)
            FINISHED = False
            GUESSES.clear()
            time.sleep(1)
            guess_word()
        elif finished_input == "finish":
            print("")
            print("saving..")
    else:
        print("You lost all of ur lifes")


def ret_to_menu():
    """
    Returns from highscore to main menu
    """
    start_game()


def start_game():
    """
    Starts the game when user types in "start"
    """
    time.sleep(1)
    print("To start game type in 'start'")
    print("")
    print("To view highscore type in 'highscore'")
    print("")
    start_input = input("'start' or 'highscore': ")
    print("")
    if start_input == "start":
        time.sleep(1)
        nickname()
        rules()
        guess_word()
    elif start_input == "highscore":
        time.sleep(1)
        print("score placeholder")
        print("")
        time.sleep(1)
        return_input = input("to return type in 'return': ")
        if return_input == "return":
            ret_to_menu()
        # show_highscore()
    else:
        print("wrong input please try again")
        start_game()


start_game()
