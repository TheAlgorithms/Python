"""Convert a positive Decimal Number to Any Other Representation"""


def decimal_to_any(num: int, base: int) -> str:

    """
        Convert a Integer Decimal Number to a Binary Number as str.
        >>> decimal_to_any(0, 2)
        '0'
        >>> decimal_to_any(5, 4)
        '11'
        >>> decimal_to_any(20, 3)
        '202'
        >>> decimal_to_any(58, 16)
        '3A'
        >>> # negatives will error
        >>> decimal_to_any(-45, 8) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        ValueError: parameter must be positive int
        >>> # floats will error
        >>> decimal_to_any(34.4, 6) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'float' object cannot be interpreted as an integer
        >>> #a float base will error
        >>> decimal_to_any(5, 2.5) # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'float' object cannot be interpreted as an integer
        >>> # a str base will error
        >>> decimal_to_any(10, '16') # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: 'str' object cannot be interpreted as an integer
    """
    if isinstance(num, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if type(base) == str:
        raise TypeError("'str' object cannot be interpreted as an integer")
    if type(base) == float:
        raise TypeError("'float' object cannot be interpreted as an integer")

    HEXADECIMAL = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    new_value = ""
    mod = 0
    div = 0
    if base in (0, 1):
        return
    while div not in (0, 1):
        div, mod = divmod(num, base)
        if base == 16 and 9 < mod < 16:
            actual_value = HEXADECIMAL[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = num // base
        num = div
        if div == 0:
            if base != 16:
                return str(new_value[::-1])
            else:
                if new_value[::-1] in HEXADECIMAL:
                    return HEXADECIMAL[new_value[::-1]]
                return new_value[::-1]
        elif div == 1:
            new_value += str(div)
            if base != 16:
                return str(new_value[::-1])
            else:
                if new_value[::-1] in HEXADECIMAL:
                    return HEXADECIMAL[new_value[::-1]]
                return new_value[::-1]

    return new_value[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
