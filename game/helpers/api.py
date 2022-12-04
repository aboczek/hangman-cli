import random
import requests


def words_to_play():
    """
    Pulls random words from API and uses them for hangman game
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10",
                       timeout=10)
    _playable_words = req.text
    return _playable_words


def word_formatter(string):
    """
    Formating word from API list
    """
    current_word = ""
    new_list = []

    for char in string:
        if char.isalpha():
            current_word += char
        elif char == "," or char == "]":
            new_list.append(current_word)
            current_word = ""

    return new_list


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
