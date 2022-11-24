import random
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
highscore = SHEET.worksheet("hangman_sheet")
word = random.choice(dicto)
GUESSES = []
GUESS_MISTAKE = 7
FINISHED = False
SCORE = 0
RULES_LIST = ["Random word is printed out and you have to guess it",
              "You guess 1 letter at a time if its correct it will be displayed",
              "If not you lose one life out of seven"]