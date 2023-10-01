def is_upper(string: str) -> bool:
    """
    Check if all characters in the string are uppercase letters.

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are uppercase letters, False otherwise.

    Examples:
    >>> is_upper("HELLO")
    True
    >>> is_upper("Hello")
    False
    """
    return all(ord(char) >= 65 and ord(char) <= 90 for char in string)


def is_lower(string: str) -> bool:
    """
    Check if all characters in the string are lowercase letters.

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are lowercase letters, False otherwise.

    Examples:
    >>> is_lower("hello")
    True
    >>> is_lower("Hello")
    False
    """
    return all(ord(char) >= 97 and ord(char) <= 122 for char in string)


def is_alpha(string: str) -> bool:
    """
    Check if all characters in the string are alphabetical (letters).

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are letters, False otherwise.

    Examples:
    >>> is_alpha("Hello")
    True
    >>> is_alpha("Hello123")
    False
    """
    return all(char.isalpha() for char in string)


def is_alnum(string: str) -> bool:
    """
    Check if all characters in the string are alphanumeric (letters or digits).

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are letters or digits, False otherwise.

    Examples:
    >>> is_alnum("Hello123")
    True
    >>> is_alnum("Hello 123")
    False
    """
    return all(char.isalnum() for char in string)


def is_decimal(string: str) -> bool:
    """
    Check if all characters in the string are decimal digits.

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are decimal digits, False otherwise.

    Examples:
    >>> is_decimal("12345")
    True
    >>> is_decimal("12.345")
    False
    """
    return all(char.isdigit() for char in string)


def is_space(string: str) -> bool:
    """
    Check if all characters in the string are whitespace characters.

    Args:
        string (str): The input string.

    Returns:
        bool: True if all characters in the string are whitespace characters, False otherwise.

    Examples:
    >>> is_space("    \\t\\n")
    True
    >>> is_space("Hello")
    False
    """
    return all(char.isspace() for char in string)


def is_title(string: str) -> bool:
    """
    Check if the string is in title case (first letter of each word is capital).

    Args:
        string (str): The input string.

    Returns:
        bool: True if the string is in title case, False otherwise.

    Examples:
    >>> is_title("This Is A Title Case String")
    True
    >>> is_title("This is Not a Title Case String")
    False
    """
    return string.istitle()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
