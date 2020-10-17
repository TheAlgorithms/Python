"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up
that amount.
https://leetcode.com/problems/coin-change/
"""

from typing import Iterable


def min_coins(coins: Iterable[int], total_amount: int) -> int:
    """
    >>> min_coins([1, 2, 3], 3)
    1
    >>> min_coins([1, 2, 3], 8)
    3
    >>> min_coins([1, 2, 3], 0)
    0
    >>> min_coins([4, 1, 6], 9)
    3
    >>> min_coins([2,3], 1)
    -1
    """

    # dp[i] represents the minimum number of coins necessary to give
    # total_amount of change using coins
    dp = [float("inf")] * (total_amount + 1)
    dp[0] = 0

    for amount in range(1, total_amount + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    if dp[total_amount] == float("inf"):
        return -1
    return dp[total_amount]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
