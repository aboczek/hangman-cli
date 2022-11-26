import time
from art import tprint
from .ascii_art import (print_hangman)
from .settings import (word, highscore, GUESSES, GUESS_MISTAKE,
                       FINISHED, SCORE, SHEET, RULES_LIST, stringing)


tprint("                Welcome")
tprint("                To")
tprint("                Hangman")


def print_new_line():
    """
    Prints new line
    """
    print("")


def nickname():
    """
    Takes users nickname and displays it
    """
    # global highscore
    time.sleep(1)
    user_input = input("Put your nickname here: ")
    # nick = user_input
    # highscore.update_cell(9, 2, nick)
    print_new_line()
    time.sleep(1)
    print(f"Your nickname is {user_input}.")
    print_new_line()


def center_text(text_to_be_printed):
    """
    Prints tprint into countdown in rules function
    """
    tprint(f"                {text_to_be_printed}")


def rules():
    """
    Displays rules after setting your nickname up.
    """
    time.sleep(1)
    center_text("Rules")
    print_new_line()
    time.sleep(1)
    for index, rule in enumerate(RULES_LIST, start=1):
        print(index, rule)
        print_new_line()
        time.sleep(1)
    print("Enjoy the Hangman game.")
    print_new_line()
    for number in reversed(range(1, 6)):
        center_text(number)
        time.sleep(1)


# def show_highscore():


def guess_word():
    """
    Draws random word from list and makes it guessable
    """
    global word, GUESSES, GUESS_MISTAKE, FINISHED, SCORE, nick
    while not FINISHED:
        for letter in word:
            if letter.lower() in GUESSES:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print_new_line()

        guess_input = input("Guess the letter: ")
        GUESSES.append(guess_input.lower())

        if guess_input == "":
            print("\n Warning! your input cannot be empty")

        if guess_input.lower() not in word.lower():
            GUESS_MISTAKE -= 1
            print_hangman(GUESS_MISTAKE)
            if GUESS_MISTAKE == 0:
                break

        FINISHED = True
        for letter in word:
            if letter.lower() not in GUESSES:
                FINISHED = False

    if FINISHED:
        SCORE += 1
        print("Congratulations you guessed the word")
        print_new_line()
        print(f"your score is {SCORE}")
        print_new_line()
        finished_input = input("Do you want to 'continue' or 'finish'?\n")
        print_new_line()
        if finished_input == "continue":
            center_text("Next Word: ")
            time.sleep(1)
            FINISHED = False
            GUESSES.clear()
            time.sleep(1)
            guess_word()
        elif finished_input == "finish":
            print_new_line()
            print("saving..")
            # highscore.update_cell(9, 3, SCORE)
            return SCORE
    else:
        print("You lost all of ur lifes")
