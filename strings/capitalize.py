def capitalize(sentence: str) -> str:
    """
    Capitalizes the first letter of a sentence or word.

    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    >>> capitalize("a")
    'A'
    >>> capitalize("")
    ''
    """
    if not sentence:
        return ""

    # Capitalize the first character if it's a lowercase letter
    # Concatenate the capitalized character with the rest of the string
    return sentence[0].upper() + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
