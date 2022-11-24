import time
from art import tprint
from .ascii_art import (print_hangman)
from .settings import (word, highscore, GUESSES, GUESS_MISTAKE,
                       FINISHED, SCORE, SHEET)


tprint("                Welcome")
tprint("                To")
tprint("                Hangman")


def nickname():
    """
    Takes users nickname and displays it
    """
    # global highscore
    time.sleep(1)
    user_input = input("Put your nickname here: ")
    # nick = user_input
    # highscore.update_cell(9, 2, nick)
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
    global word, GUESSES, GUESS_MISTAKE, FINISHED, SCORE, nick
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
            # highscore.update_cell(9, 3, SCORE)
            return SCORE
    else:
        print("You lost all of ur lifes")
