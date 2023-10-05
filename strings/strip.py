def strip(user_string: str, characters: str = None) -> str:
    """
    Remove leading and trailing characters (whitespace by default) from a string.

    Args:
        user_string: The input string to be stripped.
        characters: Optional characters to be removed (default is whitespace).

    Returns:
        The stripped string.

    Examples:
        >>> strip("   Hello, World!   ")
        'Hello, World!'

        >>> strip("   Hello, World!   ", " H!")
        'ello, World'

        >>> strip("   Hello, World!   ", "!")
        '   Hello, World!   '

        >>> strip("   Hello, World!   ", "123")
        '   Hello, World!   '

        >>> strip("   ", " ")
        ''

        >>> strip("NoWhitespaceHere")
        'NoWhitespaceHere'
    """
    if characters is None:
        return user_string.strip()
    else:
        left_stripped = user_string.lstrip(characters)
        right_stripped = user_string.rstrip(characters)
        return left_stripped.rstrip(characters)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
