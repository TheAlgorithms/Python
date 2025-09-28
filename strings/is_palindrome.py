def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a word, number, phrase, or other sequence of 
    characters which reads the same backward as forward.

    Reference: https://en.wikipedia.org/wiki/Palindrome

    Examples:
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("level")
    True
    """
    return text == text[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
