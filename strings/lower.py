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
    start = ASCII_UPPERCASE_START
    end = ASCII_UPPERCASE_END
    offset = ASCII_CASE_OFFSET

    return "".join(
        [
            chr(code + offset) if start <= (code := ord(char)) <= end else char
            for char in word
        ]
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()
