"""
Convert a single character to its ASCII integer value.

Example:
    >>> char_to_ascii('A')
    65
    >>> char_to_ascii('a')
    97
    >>> char_to_ascii('$')
    36
    >>> char_to_ascii('AB')
    Traceback (most recent call last):
        ...
    ValueError: Input must be a single character

References:
    https://en.wikipedia.org/wiki/ASCII
"""

def char_to_ascii(char: str) -> int:
    """
    Convert a single character to its ASCII integer value.

    Args:
        char (str): A single character string.

    Returns:
        int: ASCII integer value corresponding to the character.

    Raises:
        ValueError: If input is not a single character.

    >>> char_to_ascii('A')
    65
    >>> char_to_ascii('a')
    97
    >>> char_to_ascii('$')
    36
    >>> char_to_ascii('')
    Traceback (most recent call last):
        ...
    ValueError: Input must be a single character
    """
    if not isinstance(char, str):
        raise TypeError("Input must be a string.")
    if len(char) != 1:
        raise ValueError("Input must be a single character")
    return ord(char)
