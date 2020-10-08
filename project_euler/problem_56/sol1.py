"""
https://projecteuler.net/problem=56

A googol (10**100) is a massive number: one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?
"""


def maximum_digital_sum(a: int, b: int) -> int:
    """
    Returns the maximum from the list of SUMs of the list of INT
    converted from STR of BASE raised to the POWER
    >>> maximum_digital_sum(10,10)
    45
    >>> maximum_digital_sum(100,100)
    972
    >>> maximum_digital_sum(100,200)
    1872
    """

    return max(
        sum(int(x) for x in str(base ** power))
        for base in range(a)
        for power in range(b)
    )


def solution(a: int = 100, b: int = 100) -> int:
    """Returns maximum digital sum"""
    return maximum_digital_sum(a, b)


if __name__ == "__main__":
    print(f"{solution(100, 100)}")
