def wave(txt: str) -> list:
    """
    >>> wave('cat')
    ['Cat', 'cAt', 'caT']
    >>> wave('one')
    ['One', 'oNe', 'onE']
    >>> wave('book')
    ['Book', 'bOok', 'boOk', 'booK']
    """

    """this algorithm returns a so called 'wave' of
    a given string [ a list of each of it's capitalized
    characters one by one??? ]"""

    return [
        txt[:a] + txt[a].upper() + txt[a + 1 :]
        for a in range(len(txt))
        if txt[a].isalpha()
    ]


if __name__ == "__main__":
    __import__("doctest").testmod()
