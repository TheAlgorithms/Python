ASCII_UPPERCASE_START = ord("A")
ASCII_UPPERCASE_END = ord("Z")
ASCII_CASE_OFFSET = ord("a") - ord("A")


def lower(word: str) -> str:
    """
    Convert ASCII uppercase letters in a string to lowercase.

    >>> lower("wow")
    'wow'
    >>> lower("HellZo")
    'hellzo'
    >>> lower("WHAT")
    'what'
    >>> lower("wh[]32")
    'wh[]32'
    >>> lower("whAT")
    'what'
    """
    result = []

    for char in word:
        code = ord(char)
        if ASCII_UPPERCASE_START <= code <= ASCII_UPPERCASE_END:
            char = chr(code + ASCII_CASE_OFFSET)
        result.append(char)

    return "".join(result)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
