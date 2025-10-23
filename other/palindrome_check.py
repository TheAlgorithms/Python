def is_palindrome(text: str) -> bool:
    """
    Checks if a string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward. This implementation is case-sensitive
    and includes spaces and punctuation in the check.

    Args:
        text: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples (Doctests):
    >>> is_palindrome("madam")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("A man, a plan, a canal: Panama")
    False
    >>> is_palindrome("level")
    True
    >>> is_palindrome("hello")
    False
    """
    # Core logic: The simplest and most Pythonic way to reverse a string
    # is using slicing: text[::-1].
    # We compare the original string with its reversed version.
    return text == text[::-1]


if __name__ == "__main__":
    # Standard boilerplate for running documentation examples as tests.
    import doctest
    doctest.testmod()
    