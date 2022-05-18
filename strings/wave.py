def wave(txt: str) -> list:
    """
    >>> wave('wave algorithm')
    ['Wave algorithm', 'wAve algorithm', 'waVe algorithm', 'wavE algorithm', 'wave Algorithm', 'wave aLgorithm', 'wave alGorithm', 'wave algOrithm', 'wave algoRithm', 'wave algorIthm', 'wave algoriThm', 'wave algoritHm', 'wave algorithM']
    >>> wave('one')
    ['One', 'oNe', 'onE']
    >>> wave('book')
    ['Book', 'bOok', 'boOk', 'booK']
    """

    """this algorithm returns a so called 'wave' of
    a given string [ a list of each of it's capitalized
    charachters one by one??? ]"""

    return [
        txt[:a] + txt[a].upper() + txt[a + 1 :]
        for a in range(len(txt))
        if txt[a].isalpha()
    ]


if __name__ == "__main__":
    __import__("doctest").testmod()
