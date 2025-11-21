def integer_to_roman(n: int) -> str:
    """
    Convert an integer to a Roman numeral.

    Examples:
    >>> integer_to_roman(1)
    'I'
    >>> integer_to_roman(4)
    'IV'
    >>> integer_to_roman(9)
    'IX'
    >>> integer_to_roman(58)
    'LVIII'
    >>> integer_to_roman(1994)
    'MCMXCIV'
    >>> integer_to_roman(0)
    Traceback (most recent call last):
        ...
    ValueError: number must be between 1 and 3999
    """
    if not (1 <= n <= 3999):
        raise ValueError("number must be between 1 and 3999")

    symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, numeral in symbols:
        while n >= value:
            result.append(numeral)
            n -= value

    return "".join(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
