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
    print_new_line()
    print("To start game type in 'start'")
    print_new_line()
    print("To view highscore type in 'highscore'")
    print_new_line()
    start_input = input("'start' or 'highscore': \n")
    start = start_input.lower()
    print_new_line()
    if start == "start":
        time.sleep(1)
        get_nickname()
        rules()
        guess_word()
    elif start == "highscore":
        time.sleep(1)
        show_highscore()
        print_new_line()
        time.sleep(1)
        return_input = input("Press Enter to return to main menu!\n")
        go_back = return_input.lower()
        if go_back == "return":
            ret_to_menu()
        else:
            ret_to_menu()

    else:
        print("wrong input please try again!")
        start_game()
