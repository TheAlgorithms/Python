"""

Calculate the nth Catalan number

Source:
    https://en.wikipedia.org/wiki/Catalan_number

"""


def catalan(number: int) -> int:
    """
    :param number: nth catalan number to calculate
    :return: the nth catalan number
    Note: A catalan number is only defined for positive integers

    >>> catalan(5)
    14
    >>> catalan(0)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=0] must be > 0
    >>> catalan(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=-1] must be > 0
    >>> catalan(5.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=5.0] must be an integer
    """

    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")

    if number < 1:
        raise ValueError(f"Input value of [number={number}] must be > 0")

    current_number = 1

    for i in range(1, number):
        current_number *= 4 * i - 2
        current_number //= i + 1

    return current_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
