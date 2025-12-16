"""Palindrome Checker.

This module contains functions to check if a string is a palindrome.
A palindrome is a word, phrase, or sequence that reads the same backward as forward.
"""


def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forward and backward,
    ignoring case, spaces, and punctuation.

    Args:
        text: The string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("a")
        True
        >>> is_palindrome("Madam")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    # Check if the cleaned string equals its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
