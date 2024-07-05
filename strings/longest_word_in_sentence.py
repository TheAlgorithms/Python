def longest_word(sentence: str) -> str:
    """
    Finds the longest word in a sentence.

    >>> longest_word("The quick brown fox jumped over the lazy dog")
    'jumped'
    >>> longest_word("Python is amazing")
    'amazing'
    >>> longest_word("")
    ''
    >>> longest_word("a")
    'a'
    """
    words = sentence.split()
    return max(words, key=len) if words else ""


if __name__ == "__main__":
    from doctest import testmod

    testmod()
