def string_replace(
    text: str, input_string: str, replace_with_string: str, occurrence: int
) -> str:
    """
    https://docs.python.org/3/library/stdtypes.html#str.replace
    The replace() method replaces a specified string with another specified string.
    The occurrence parameter can be skipped in order to consider all text.
    Note: input and replace_with strings are case-sensitive.
    >>> text = "One Two Two Three Four Five"
    >>> string_val = string_replace(text, "Two", "Seven", 1)
    >>> print(string_val)
    One Seven Two Three Four Five

    >>> text = "In the morning, the cat is running behind the mouse."
    >>> string_val = string_replace(text, "the", "a", 10)
    >>> print(string_val)
    In a morning, a cat is running behind a mouse.
    """
    return text.replace(input_string, replace_with_string, occurrence)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
