"""
== Kaprekar Number ==
A number n is a Kaprekar number if its square can be split into two parts
(left and right) that add up to n, where the right part is non-zero.

Examples: 1, 9, 45, 55, 99, 297, 703, 999, 2223, 4950, 5050, 7272, 9999
Reference: https://en.wikipedia.org/wiki/Kaprekar_number
"""


def is_kaprekar(number: int) -> bool:
    """
    Returns True if number is a Kaprekar number, False otherwise.

    >>> is_kaprekar(1)
    True
    >>> is_kaprekar(9)
    True
    >>> is_kaprekar(45)
    True
    >>> is_kaprekar(55)
    True
    >>> is_kaprekar(10)
    False
    >>> is_kaprekar(0)
    False
    >>> is_kaprekar(-1)
    False
    >>> is_kaprekar(2223)
    True
    >>> is_kaprekar(1.5)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=1.5] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        return False
    if number == 1:
        return True
    square = number**2
    digits = len(str(square))
    for split in range(1, digits):
        right = square % (10**split)
        left = square // (10**split)
        if right > 0 and left + right == number:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
