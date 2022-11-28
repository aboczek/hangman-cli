import time
from .utils import (get_nickname, rules, guess_word, print_new_line,
                    show_highscore)


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
    print_new_line()
    print("To view highscore type in 'highscore'")
    print_new_line()
    start_input = input("'start' or 'highscore': \n")
    print_new_line()
    if start_input == "start":
        time.sleep(1)
        get_nickname()
        rules()
        guess_word()
    elif start_input == "highscore":
        time.sleep(1)
        show_highscore()
        print_new_line()
        time.sleep(1)
        return_input = input("to return type in 'return': \n")
        if return_input == "return":
            ret_to_menu()
        else:
            print("Wrong input aborting!")
    else:
        print("wrong input please try again!")
        start_game()
