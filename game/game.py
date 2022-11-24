import time
from .utils import (nickname, rules, guess_word)


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
