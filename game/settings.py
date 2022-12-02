import gspread
import random
import requests
from google.oauth2.service_account import Credentials
from .helpers.api import (words_to_play, word_formatter)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman")


def make_string_lover_case():
    """
    Function pulls list of words from word_formatter and,
    loops through allowing lower letters
    """
    words = word_formatter(words_to_play())
    for string in words:
        lower_string = string.lower()
        return lower_string


with open("game/helpers/words-for-hangman.txt", "r", encoding="utf-8") as f:
    words_from_list = f.readlines()


def get_response_from_api():
    """
    Function checks if API is down returning 503 error
    if 503 it will use txt file with random words
    if its up it will use API
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10",
                       timeout=10)
    if req.status_code == 503:
        word = random.choice(words_from_list)[:-1]
    else:
        word = make_string_lover_case()
    return word


highscore = SHEET.worksheet("hangman_sheet")
word = get_response_from_api()
print(f"{word}")
first_place = highscore.row_values(2)
second_place = highscore.row_values(3)
third_place = highscore.row_values(4)
SCORE_LIST = []
GUESSES = []
GUESS_MISTAKE = 7
FINISHED = False
SCORE = 0
RULES_LIST = ["Random word is printed out and you have to guess it",
              "Guess 1 letter at a time if its correct it will be displayed",
              "If not you lose one life out of seven"]
