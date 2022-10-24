import math
import sys


def minimum_squares_to_represent_a_number(number: int) -> int:
    """
    Count the number of minimum squares to represent a number
    >>> minimum_squares_to_represent_a_number(25)
    1
    >>> minimum_squares_to_represent_a_number(37)
    2
    >>> minimum_squares_to_represent_a_number(21)
    3
    >>> minimum_squares_to_represent_a_number(58)
    2
    >>> minimum_squares_to_represent_a_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    dp = [-1 for x in range(number + 1)]
    dp[0] = 0
    for i in range(1, number + 1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            currAns = 1 + dp[i - (j**2)]
            ans = min(ans, currAns)
        dp[i] = ans
    return dp[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
