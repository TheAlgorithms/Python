"""
Convert an ASCII integer (0-255) to its corresponding character.

Example:
    >>> ascii_to_char(65)
    'A'
    >>> ascii_to_char(97)
    'a'
    >>> ascii_to_char(36)
    '$'
    >>> ascii_to_char(300)
    Traceback (most recent call last):
        ...
    ValueError: ASCII value must be in the range 0-255.

Reference:
    https://en.wikipedia.org/wiki/ASCII
"""

def ascii_to_char(ascii_value: int) -> str:
    """
    Convert an ASCII integer (0-255) into its corresponding character.

    Args:
        ascii_value (int): Integer representing an ASCII code (0-255).

    Returns:
        str: The corresponding character.

    Raises:
        ValueError: If the input is not within 0-255 inclusive.

    >>> ascii_to_char(65)
    'A'
    >>> ascii_to_char(97)
    'a'
    >>> ascii_to_char(36)
    '$'
    >>> ascii_to_char(300)
    Traceback (most recent call last):
        ...
    ValueError: ASCII value must be in the range 0-255.
    """
    if not isinstance(ascii_value, int):
        raise TypeError("Input must be an integer.")
    if not 0 <= ascii_value <= 255:
        raise ValueError("ASCII value must be in the range 0-255.")
    return chr(ascii_value)
