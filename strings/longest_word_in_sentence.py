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
    >>> longest_word("A journey of a thousand miles begins with a single step")
    'thousand'
    >>> longest_word("To be or not to be that is the question")
    'question'
    >>> longest_word("Beauty is in the eye of the beholder")
    'beholder'
    >>> longest_word("A picture is worth a thousand words")
    'thousand'
    >>> longest_word("All that glitters is not gold")
    'glitters'
    """
    words = sentence.split()
    return max(words, key=len) if words else ""


if __name__ == "__main__":
    from doctest import testmod

    testmod()
