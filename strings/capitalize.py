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

    # will see more
    return sentence[0].upper() + sentence[1:] if sentence[0].isalpha() else sentence


if __name__ == "__main__":
    from doctest import testmod

    testmod()
