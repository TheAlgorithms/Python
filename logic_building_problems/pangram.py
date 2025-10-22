"""Pangram Checker.

This module contains functions to check if a string is a pangram.
A pangram is a sentence that contains every letter of the alphabet at least once.
"""

import string


def is_pangram(text: str) -> bool:
    """
    Check if a given string is a pangram.

    A pangram is a string that contains every letter of the alphabet
    at least once, ignoring case and non-alphabetic characters.

    Args:
        text: The string to check

    Returns:
        True if the string is a pangram, False otherwise

    Examples:
        >>> is_pangram("The quick brown fox jumps over the lazy dog")
        True
        >>> is_pangram("Hello World")
        False
        >>> is_pangram("Pack my box with five dozen liquor jugs")
        True
        >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
        True
        >>> is_pangram("")
        False
        >>> is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        True
    """
    # Convert text to lowercase and get all unique letters
    letters = set(char.lower() for char in text if char.isalpha())
    # Check if all 26 letters of the alphabet are present
    return len(letters) == 26


if __name__ == "__main__":
    import doctest

    doctest.testmod()
