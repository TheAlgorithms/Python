from itertools import permutations

import nltk

try:
    from nltk.corpus import words
except LookupError:
    nltk.download('words')

dictionary = set(w.lower() for w in words.words())


def get_actual_word(test_word: str) -> set :

    """[Unscrambles the input into a meaningful word/words]

    Args:
        test_word (str): [Input jumbled word]

    Raises:
        Exception: [Not a string]

    Returns:
        set: [Set of meaningful English words from the input]
    >>> get_actual_word("clodu") == {'cloud', 'could'}
    True
    >>> get_actual_word("cl@#$")
    Traceback (most recent call last):
    ...
    ValueError: NOT-A-STRING
    >>> get_actual_word("")
    Traceback (most recent call last):
    ...
    ValueError: NOT-A-STRING
    """

    if not test_word.isalpha():
        raise ValueError("NOT-A-STRING")

    scrambled_words = [''.join(i) for i in permutations(test_word)]
    solutions = []

    for word in set(scrambled_words):
        if word in dictionary :
            solutions.append(word)

    return set(solutions)


if __name__ == "__main__":
    import doctest
    doctest.testmod()