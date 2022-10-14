def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
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
    >>> capitalize("ö")
    'Ö'
    """
    if not sentence:
        return ""
    return sentence[0].upper() + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
