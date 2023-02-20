import os
from string import ascii_letters

LETTERS_AND_SPACE = ascii_letters + " \t\n"


def load_dictionary() -> dict[str, None]:
    path = os.path.split(os.path.realpath(__file__))
    english_words: dict[str, None] = {}
    with open(path[0] + "/dictionary.txt") as dictionary_file:
        for word in dictionary_file.read().split("\n"):
            english_words[word] = None
    return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(message: str) -> float:
    '''
    >>> get_english_count(55)
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute 'upper'

    >>> get_english_count("hi my name is programmer")
    0.4

    '''
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()
    matches = len([word for word in possible_words if word in ENGLISH_WORDS])
    return float(matches) / len(possible_words)


def remove_non_letters(message: str) -> str:
    '''
    >>> remove_non_letters("hi my name is 84214182814")
    'hi my name is '
    '''

    return "".join(symbol for symbol in message if symbol in LETTERS_AND_SPACE)


def is_english(
    message: str, word_percentage: int = 20, letter_percentage: int = 85
) -> bool:
    """
    >>> is_english('Hello World')
    True
    >>> is_english('llold HorWd')
    False
    """
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = (float(num_letters) / len(message)) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match


if __name__ == "__main__":
    import doctest

    doctest.testmod()
