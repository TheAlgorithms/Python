def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("hello")
    False
    """
    return text == text[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
