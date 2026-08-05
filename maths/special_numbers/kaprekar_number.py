"""
A Kaprekar number is a non-negative integer whose square can be split into two parts
that sum back to the original number.

For example:
- 9: 9² = 81, and 8 + 1 = 9
- 45: 45² = 2025, and 20 + 25 = 45
- 297: 297² = 88209, and 88 + 209 = 297

Note: The right part may have leading zeros (e.g., 1: 1² = 1, split as 0 + 1 = 1).

On-Line Encyclopedia of Integer Sequences entry: https://oeis.org/A006886

References:
- https://en.wikipedia.org/wiki/Kaprekar_number
"""


def is_kaprekar_number(number: int) -> bool:
    """
    Return True if the given number is a Kaprekar number, False otherwise.

    A Kaprekar number n has the property that n² can be split into two parts
    (right part must be non-empty) whose sum equals n.

    >>> is_kaprekar_number(1)
    True
    >>> is_kaprekar_number(9)
    True
    >>> is_kaprekar_number(45)
    True
    >>> is_kaprekar_number(297)
    True
    >>> is_kaprekar_number(2223)
    True
    >>> is_kaprekar_number(2)
    False
    >>> is_kaprekar_number(10)
    False
    >>> is_kaprekar_number(0)
    Traceback (most recent call last):
        ...
    ValueError: number=0 must be a positive integer
    >>> is_kaprekar_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: number=-1 must be a positive integer
    >>> is_kaprekar_number(1.5)
    Traceback (most recent call last):
        ...
    ValueError: number=1.5 must be a positive integer
    """
    if not isinstance(number, int) or number <= 0:
        msg = f"{number=} must be a positive integer"
        raise ValueError(msg)

    square = number * number
    square_str = str(square)
    n_digits = len(square_str)

    # Try every split position; left part may be empty (treated as 0),
    # but right part must be positive (non-zero) to avoid trivial splits.
    for split in range(n_digits):
        left = int(square_str[:split]) if split > 0 else 0
        right = int(square_str[split:])
        if right > 0 and left + right == number:
            return True

    return False


def kaprekar_numbers(limit: int) -> list[int]:
    """
    Return a list of all Kaprekar numbers up to and including the given limit.

    >>> kaprekar_numbers(1)
    [1]
    >>> kaprekar_numbers(100)
    [1, 9, 45, 55, 99]
    >>> kaprekar_numbers(1000)
    [1, 9, 45, 55, 99, 297, 703, 999]
    >>> kaprekar_numbers(0)
    Traceback (most recent call last):
        ...
    ValueError: limit=0 must be a positive integer
    >>> kaprekar_numbers(-5)
    Traceback (most recent call last):
        ...
    ValueError: limit=-5 must be a positive integer
    """
    if not isinstance(limit, int) or limit <= 0:
        msg = f"{limit=} must be a positive integer"
        raise ValueError(msg)

    return [n for n in range(1, limit + 1) if is_kaprekar_number(n)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Kaprekar numbers up to 10000:")
    print(kaprekar_numbers(10000))
