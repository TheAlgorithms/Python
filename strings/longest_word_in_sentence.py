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
    >>> longest_word("A tie between words")
    'between'
    >>> longest_word("All words are same length")
    'All'
    >>> longest_word("Multiple words with the same longest length")
    'Multiple'
    >>> longest_word("Trailing spaces at the end ")
    'Trailing'
    >>> longest_word("  Leading spaces at the start")
    'Leading'
    >>> longest_word("Special characters !@#$%^&*() should be ignored")
    'characters'
    """
    words = sentence.split()
    return max(words, key=len) if words else ""


if __name__ == "__main__":
    from doctest import testmod

    testmod()
