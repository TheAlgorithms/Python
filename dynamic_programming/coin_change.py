"""
Coin Change - Dynamic Programming Algorithm

This module implements the classic coin change problem:
finding the minimum number of coins required to make up a given amount.

Doctests:
>>> coin_change([1, 2, 5], 11)
3
>>> coin_change([2], 3)
-1
>>> coin_change([1], 0)
0
>>> coin_change([1, 2, 5], 100)
20
"""


def coin_change(coins: list[int], amount: int) -> int:
    """
    Calculate the minimum number of coins required to make up the given amount.

    Args:
        coins (list[int]): List of coin denominations.
        amount (int): Total amount to make.

    Returns:
        int: Minimum number of coins needed to make up the amount,
             or -1 if it's not possible.

    >>> coin_change([1, 2, 5], 11)
    3
    >>> coin_change([2], 3)
    -1
    >>> coin_change([1], 0)
    0
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = dp[amount]
    return result if result != float("inf") else -1
