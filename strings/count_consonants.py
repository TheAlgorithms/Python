def count_consonants(s: str) -> int:
    """
    Count the number of consonants in a given string.

    :param s: Input string to count consonants in.
    :return: Number of consonants in the input string.

    Examples:
    >>> count_consonants("hello world")
    7
    >>> count_consonants("HELLO WORLD")
    7
    >>> count_consonants("123 hello world")
    7
    >>> count_consonants("")
    0
    >>> count_consonants("a quick brown fox")
    10
    >>> count_consonants("the quick BROWN fox")
    13
    >>> count_consonants("PYTHON")
    5
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
