"""
A Kaprekar number for a given base is a non-negative integer, the
representation of whose square in that base can be split into two parts that
add up to the original number again.

For example, 45 is a Kaprekar number because:
    45^2 = 2025   ->  split as  20 + 25 = 45  ✓

9 is a Kaprekar number because:
    9^2 = 81      ->  split as  8 + 1 = 9  ✓

297 is a Kaprekar number because:
    297^2 = 88209 ->  split as  88 + 209 = 297  ✓

Note: The number 1 is a trivial Kaprekar number in every base.

Reference: https://en.wikipedia.org/wiki/Kaprekar_number
OEIS sequence: https://oeis.org/A006886
"""


def is_kaprekar_number(number: int, base: int = 10) -> bool:
    """
    Return True if *number* is a Kaprekar number in the given *base*,
    False otherwise.

    A Kaprekar number n satisfies: let s = n^2 represented in *base*.
    Split s into a right part r (non-empty) and a left part l such that
    l + r == n.  We try every valid split position.

    Parameters
    ----------
    number : int
        A positive integer to test.
    base : int
        The numeric base to use (default 10).  Must be >= 2.

    Raises
    ------
    ValueError
        If *number* is not a positive integer or *base* < 2.

    >>> is_kaprekar_number(1)
    True
    >>> is_kaprekar_number(9)
    True
    >>> is_kaprekar_number(45)
    True
    >>> is_kaprekar_number(55)
    True
    >>> is_kaprekar_number(99)
    True
    >>> is_kaprekar_number(297)
    True
    >>> is_kaprekar_number(703)
    True
    >>> is_kaprekar_number(999)
    True
    >>> is_kaprekar_number(2)
    False
    >>> is_kaprekar_number(10)
    False
    >>> is_kaprekar_number(0)
    Traceback (most recent call last):
        ...
    ValueError: number=0 must be a positive integer
    >>> is_kaprekar_number(-9)
    Traceback (most recent call last):
        ...
    ValueError: number=-9 must be a positive integer
    >>> is_kaprekar_number(9.0)
    Traceback (most recent call last):
        ...
    ValueError: number=9.0 must be a positive integer
    >>> is_kaprekar_number(9, base=1)
    Traceback (most recent call last):
        ...
    ValueError: base=1 must be an integer >= 2
    """
    if not isinstance(number, int) or isinstance(number, bool) or number < 1:
        msg = f"{number=} must be a positive integer"
        raise ValueError(msg)
    if not isinstance(base, int) or isinstance(base, bool) or base < 2:
        msg = f"{base=} must be an integer >= 2"
        raise ValueError(msg)

    # 1 is a trivial Kaprekar number in every base (1^2 = 1, special case)
    if number == 1:
        return True

    square = number * number

    # Convert square to a list of digits in the given base (most-significant first)
    digits: list[int] = []
    temp = square
    while temp > 0:
        digits.append(temp % base)
        temp //= base
    digits.reverse()

    num_digits = len(digits)

    # Try every split position.
    # The right part must be NON-EMPTY and NON-ZERO (right == 0 gives trivial
    # splits like 10^2=100 -> 10+0=10 which are excluded by convention).
    for split in range(1, num_digits):
        # Left part: digits[0 : split]
        left = 0
        for d in digits[:split]:
            left = left * base + d

        # Right part: digits[split:]
        right = 0
        for d in digits[split:]:
            right = right * base + d

        if right > 0 and left + right == number:
            return True

    return False


def get_kaprekar_numbers(limit: int, base: int = 10) -> list[int]:
    """
    Return a list of all Kaprekar numbers in the range [1, limit] for the
    given *base*.

    Parameters
    ----------
    limit : int
        Upper bound (inclusive) for the search range.  Must be >= 1.
    base : int
        The numeric base to use (default 10).  Must be >= 2.

    Raises
    ------
    ValueError
        If *limit* < 1 or *base* < 2.

    >>> get_kaprekar_numbers(1000)
    [1, 9, 45, 55, 99, 297, 703, 999]
    >>> get_kaprekar_numbers(100)
    [1, 9, 45, 55, 99]
    >>> get_kaprekar_numbers(10)
    [1, 9]
    >>> get_kaprekar_numbers(1)
    [1]
    >>> get_kaprekar_numbers(0)
    Traceback (most recent call last):
        ...
    ValueError: limit=0 must be a positive integer (>= 1)
    >>> get_kaprekar_numbers(10, base=1)
    Traceback (most recent call last):
        ...
    ValueError: base=1 must be an integer >= 2
    """
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        msg = f"{limit=} must be a positive integer (>= 1)"
        raise ValueError(msg)
    if not isinstance(base, int) or isinstance(base, bool) or base < 2:
        msg = f"{base=} must be an integer >= 2"
        raise ValueError(msg)

    return [n for n in range(1, limit + 1) if is_kaprekar_number(n, base)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Kaprekar numbers up to 10,000:")
    print(get_kaprekar_numbers(10_000))
