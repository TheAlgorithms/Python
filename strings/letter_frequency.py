def letter_frequency(sentence: str) -> dict:
    """
    Find the number of occurrences of letters in a sentence.
    https://stackoverflow.com/questions/40985203/
    >>> letter_frequency("Peter Piper")
    {'e': 3, 'i': 1, 'p': 3, 'r': 2, 't': 1}
    >>> letter_frequency("Blueberry Pie.")
    {'b': 2, 'e': 3, 'i': 1, 'l': 1, 'r': 2, 'u': 1, 'y': 1}
    """

    letters = { letter: sentence.lower().count(letter) \
        for letter in list(map(chr, range(97, 123))) if letter in sentence}
    return letters
    
    


if __name__ == "__main__":
    from doctest import testmod

    testmod()
