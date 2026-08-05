def capitalize(sentence: str) -> str:
    """
    Capitalizes the first alphabetical character of a sentence.

    Examples:
    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("  hello world")
    '  Hello world'
    >>> capitalize("123 abc")
    '123 abc'
    >>> capitalize("ñandú bird")
    'Ñandú bird'
    >>> capitalize("")
    ''
    """

    if not sentence:
        return ""

    # Find the first alphabetic character and capitalize it
    for idx, char in enumerate(sentence):
        if char.isalpha():
            return sentence[:idx] + char.upper() + sentence[idx + 1 :]

    # If no alphabetic character exists, return the original string
    return sentence
