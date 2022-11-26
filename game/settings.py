import random
import gspread
from google.oauth2.service_account import Credentials
from .helpers.api import words_to_play, word_formatter

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman")


def stringing():
    """
    Function pulls list of words from word_formatter and,
    loops through allowing lower letters
    """
    for string in words:
        lower_string = string.lower()
        return lower_string


dicto = ["house", "leave", "letter", "Python", "Java"]
highscore = SHEET.worksheet("hangman_sheet")
words = word_formatter(words_to_play())
word = stringing()
test = words_to_play()
print(f"Type Word: {type(test)}")
print(f"Type: {type(word)}")
print(f"Words: {words_to_play()}")
print(f"Word: {stringing()}")
GUESSES = []
GUESS_MISTAKE = 7
FINISHED = False
SCORE = 0
RULES_LIST = ["Random word is printed out and you have to guess it",
              "Guess 1 letter at a time if its correct it will be displayed",
              "If not you lose one life out of seven"]
