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
