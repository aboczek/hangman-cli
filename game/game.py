import time
from .utils import (get_nickname, rules, guess_word, print_new_line,
                   show_highscore)


def start_game():
    """
    Starts the game when user types in "start"
    """
    time.sleep(1)
    print_new_line()
    print("To start game type in 'start', 's' or '1'")
    print_new_line()
    print("To view highscore type in 'highscore, 'h' or '2'")
    print_new_line()
    start_input = input("'start' or 'highscore': \n")

    print_new_line()
    if start_input.lower() in ["start", "s", "1"]:
        time.sleep(1)
        get_nickname()
        rules()
        guess_word()
    elif start_input.lower() in ["highscore", "h", "2"]:
        time.sleep(1)
        show_highscore()
        print_new_line()
        time.sleep(1)
        return_input = input("Press Enter to return to main menu!\n")
        if return_input.lower() == "return":
            start_game()
        else:
            start_game()

    else:
        print("wrong input please try again!")
        start_game()
