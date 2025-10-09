"""
Coin Change Problem - Dynamic Programming Approach
--------------------------------------------------

Given a list of coin denominations and a target amount,
this function returns the minimum number of coins needed
to make up that amount. If it's not possible, returns -1.

Example:
    >>> coin_change([1, 2, 5], 11)
    3
    # Explanation: 11 = 5 + 5 + 1
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Calculate the minimum number of coins required
    to make up the given amount using dynamic programming.

    Args:
        coins (List[int]): List of coin denominations.
        amount (int): The target amount.

    Returns:
        int: Minimum number of coins required, or -1 if not possible.
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Minimum coins required: {coin_change(coins, amount)}")
