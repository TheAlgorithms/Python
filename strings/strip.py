def strip(user_string: str, characters: str = " \t\n\r") -> str:
    """
    Remove leading and trailing characters (whitespace by default) from a string.

    Args:
        user_string (str): The input string to be stripped.
        characters (str, optional): Optional characters to be removed
                (default is whitespace).

    Returns:
        str: The stripped string.

    Examples:
        >>> strip("   hello   ")
        'hello'
        >>> strip("...world...", ".")
        'world'
        >>> strip("123hello123", "123")
        'hello'
        >>> strip("")
        ''
    """

    start = 0
    end = len(user_string)

    while start < end and user_string[start] in characters:
        start += 1

    while end > start and user_string[end - 1] in characters:
        end -= 1

    return user_string[start:end]
