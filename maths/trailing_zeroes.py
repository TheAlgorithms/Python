"""
https://en.wikipedia.org/wiki/Trailing_zero
"""


def trailing_zeroes(num: int) -> int:
    """
    Finding the Trailing Zeroes i.e. zeroes present at the end of number
    Args:
        num: A integer.
    Returns:
        No. of zeroes in the end of an integer.

    >>> trailing_zeroes(1000)
    3
    >>> trailing_zeroes(102983100000)
    5
    >>> trailing_zeroes(0)
    1
    >>> trailing_zeroes(913273)
    0
    """
    ans = 0
    if num < 0:
        return -1
    if num == 0:
        return 1
    while num > 0:
        if num % 10 == 0:
            ans += 1
        else:
            break
        num /= 10
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
