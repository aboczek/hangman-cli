import requests

# words_from_list = ["kit", "cute", "set", "palm", "child", "layer", "sailor",
#                    "gloom", "sit", "monk", "automatic", "mail", "fence",
#                    "prince", "pleasant", "iron", "definite", "fame",
#                    "injection", "identity"]
with open("game/helpers/words-for-hangman.txt", "r", encoding="utf-8") as f:
    words_from_list = f.readlines()
words_to_string = str(words_from_list)


def words_to_play():
    """
    Pulls random words from API and uses them for hangman game
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10",
                       timeout=10)
    _playable_words = req.text
    if req.status_code == 503:
        _playable_words = words_to_string
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
