"""Convert a positive Decimal Number to Any Other Representation"""

from string import ascii_uppercase

ALPHABET_VALUES = {str(ord(c) - 55): c for c in ascii_uppercase}


def decimal_to_any(num: int, base: int) -> str:
    """
    Convert a positive integer to another base as str.
    >>> decimal_to_any(0, 2)
    '0'
    >>> decimal_to_any(5, 4)
    '11'
    >>> decimal_to_any(20, 3)
    '202'
    >>> decimal_to_any(58, 16)
    '3A'
    >>> decimal_to_any(243, 17)
    'E5'
    >>> decimal_to_any(34923, 36)
    'QY3'
    >>> decimal_to_any(10, 11)
    'A'
    >>> decimal_to_any(16, 16)
    '10'
    >>> decimal_to_any(36, 36)
    '10'
    >>> decimal_to_any(-45, 8)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: parameter must be positive int
    >>> decimal_to_any(34.4, 6) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: int() can't convert non-string with explicit base
    >>> decimal_to_any(5, 2.5) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> decimal_to_any(10, '16') # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: 'str' object cannot be interpreted as an integer
    >>> decimal_to_any(7, 0) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: base must be >= 2
    >>> decimal_to_any(34, 37) # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    ValueError: base must be <= 36
    """
    if isinstance(num, float):
        raise TypeError("int() can't convert non-string with explicit base")
    if isinstance(base, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if isinstance(base, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if base < 2:
        raise ValueError("base must be >= 2")
    if base > 36:
        raise ValueError("base must be <= 36")

    if num == 0:
        return "0"

    digits = []
    while num:
        num, mod = divmod(num, base)
        digits.append(ALPHABET_VALUES[str(mod)] if mod > 9 else str(mod))

    return "".join(reversed(digits))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for base in range(2, 37):
        for num in range(1000):
            assert int(decimal_to_any(num, base), base) == num, (
                num,
                base,
                decimal_to_any(num, base),
                int(decimal_to_any(num, base), base),
            )
