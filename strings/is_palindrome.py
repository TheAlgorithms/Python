def is_palindrome(input_string: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forward and backward.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("12321")
        True
    """
    normalized = input_string.lower().replace(" ", "")
    return normalized == normalized[::-1]
