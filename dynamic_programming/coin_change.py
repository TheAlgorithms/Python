"""
You have m types of coins available in infinite quantities
where the value of each coins is given in the array S=[S0,... Sm-1]
Can you determine number of ways of making change for n units using
the given types of coins?
https://www.hackerrank.com/challenges/coin-change/problem
"""


def dp_count(S, n):
    """
    >>> dp_count([1, 2, 3], 4)
    4
    >>> dp_count([1, 2, 3], 7)
    8
    >>> dp_count([2, 5, 3, 6], 10)
    5
    >>> dp_count([10], 99)
    0
    >>> dp_count([4, 5, 6], 0)
    1
    >>> dp_count([1, 2, 3], -5)
    0
    """
    if n < 0:
        return 0
    # table[i] represents the number of ways to get to amount i
    table = [0] * (n + 1)

    # There is exactly 1 way to get to zero(You pick no coins).
    table[0] = 1

    # Pick all coins one by one and update table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for coin_val in S:
        for j in range(coin_val, n + 1):
            table[j] += table[j - coin_val]

    return table[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
