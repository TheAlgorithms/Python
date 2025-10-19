"""
Convert a given ASCII value to its corresponding character.
"""


def ascii_to_char(ascii_value: int) -> str:
    """
    Converts an ASCII integer value to its character equivalent.

    >>> ascii_to_char(65)
    'A'
    >>> ascii_to_char(97)
    'a'
    >>> ascii_to_char(48)
    '0'
    """
    return chr(ascii_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    input_value = input("Enter an ASCII value to convert to a character: ").strip()
    try:
        ascii_val = int(input_value)
        if 0 <= ascii_val <= 127:
            print(
                f"The character for ASCII value {ascii_val} is: {ascii_to_char(ascii_val)}"
            )
        else:
            print("Please enter a valid ASCII value (0-127).")
    except ValueError:
        print("Invalid input. Please enter an integer.")
