"""Convert ASCII integer values to their corresponding characters."""


def ascii_to_char(ascii_value: int) -> str:
    """
    Convert an ASCII integer value to its corresponding character.

    Args:
        ascii_value: An integer representing an ASCII value (0-127 for standard ASCII,
                     0-255 for extended ASCII)

    Returns:
        str: The character corresponding to the ASCII value

    Raises:
        TypeError: If ascii_value is not an integer
        ValueError: If ascii_value is outside the valid ASCII range (0-255)

    Examples:
        >>> ascii_to_char(65)
        'A'
        >>> ascii_to_char(97)
        'a'
        >>> ascii_to_char(48)
        '0'
        >>> ascii_to_char(32)
        ' '
        >>> ascii_to_char(72)
        'H'
        >>> ascii_to_char(33)
        '!'
        >>> ascii_to_char(126)
        '~'
        >>> ascii_to_char(0)
        '\\x00'
        >>> ascii_to_char(255)
        'ÿ'
        >>> ascii_to_char(-1)
        Traceback (most recent call last):
            ...
        ValueError: ASCII value must be between 0 and 255
        >>> ascii_to_char(256)
        Traceback (most recent call last):
            ...
        ValueError: ASCII value must be between 0 and 255
        >>> ascii_to_char("65")
        Traceback (most recent call last):
            ...
        TypeError: ASCII value must be an integer
        >>> ascii_to_char(65.5)
        Traceback (most recent call last):
            ...
        TypeError: ASCII value must be an integer
    """
    if not isinstance(ascii_value, int):
        raise TypeError("ASCII value must be an integer")

    if not 0 <= ascii_value <= 255:
        raise ValueError("ASCII value must be between 0 and 255")

    return chr(ascii_value)


def string_to_ascii(text: str) -> list[int]:
    """
    Convert a string to a list of ASCII values.

    Args:
        text: A string to convert

    Returns:
        list[int]: List of ASCII values for each character in the string

    Raises:
        TypeError: If text is not a string

    Examples:
        >>> string_to_ascii("Hello")
        [72, 101, 108, 108, 111]
        >>> string_to_ascii("ABC")
        [65, 66, 67]
        >>> string_to_ascii("123")
        [49, 50, 51]
        >>> string_to_ascii("")
        []
        >>> string_to_ascii(123)
        Traceback (most recent call last):
            ...
        TypeError: Input must be a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return [ord(char) for char in text]


def ascii_list_to_string(ascii_list: list[int]) -> str:
    """
    Convert a list of ASCII values back to a string.

    Args:
        ascii_list: A list of integers representing ASCII values

    Returns:
        str: The string formed by converting each ASCII value to its character

    Raises:
        TypeError: If ascii_list is not a list or contains non-integer values
        ValueError: If any ASCII value is outside the valid range (0-255)

    Examples:
        >>> ascii_list_to_string([72, 101, 108, 108, 111])
        'Hello'
        >>> ascii_list_to_string([65, 66, 67])
        'ABC'
        >>> ascii_list_to_string([49, 50, 51])
        '123'
        >>> ascii_list_to_string([])
        ''
        >>> ascii_list_to_string([65, "66", 67])
        Traceback (most recent call last):
            ...
        TypeError: All elements must be integers
        >>> ascii_list_to_string([65, 256, 67])
        Traceback (most recent call last):
            ...
        ValueError: ASCII value must be between 0 and 255
        >>> ascii_list_to_string("not a list")
        Traceback (most recent call last):
            ...
        TypeError: Input must be a list
    """
    if not isinstance(ascii_list, list):
        raise TypeError("Input must be a list")

    result = []
    for value in ascii_list:
        if not isinstance(value, int):
            raise TypeError("All elements must be integers")
        if not 0 <= value <= 255:
            raise ValueError("ASCII value must be between 0 and 255")
        result.append(chr(value))

    return "".join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("ASCII to Character Converter")
    print("Enter an ASCII value (0-255) or 'q' to quit:")

    while True:
        user_input = input("\nASCII value: ").strip()

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            ascii_val = int(user_input)
            char = ascii_to_char(ascii_val)
            print(f"Character: '{char}'")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
