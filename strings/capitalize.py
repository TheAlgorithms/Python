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
    return sentence.capitalize()