"""
ascii_to_char.py
----------------
Converts an ASCII value (integer) to its corresponding character.

Example:
>>> ascii_to_char(65)
'A'
>>> ascii_to_char(97)
'a'
"""

def ascii_to_char(ascii_value: int) -> str:
    """
    Convert an ASCII value to its corresponding character.
    Raises ValueError if the ASCII value is not valid.
    """
    if not (0 <= ascii_value <= 127):
        raise ValueError("ASCII value must be between 0 and 127.")
    return chr(ascii_value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
