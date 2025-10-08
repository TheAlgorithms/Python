"""
This module finds all possible ways to combine given coin denominations
to sum up to a specified target amount using a backtracking method.

The time complexity grows exponentially based on the amount and the set of coins.
"""

from __future__ import annotations
from typing import List


def inverse_coin_change(amount: int, coins: List[int]) -> List[List[int]]:
    """
    Computes every possible combination of coins that add up exactly to the target amount.
    Coins can be chosen multiple times.

    :param amount: The total amount to form with the coins.
    :param coins: Available coin denominations.

    Example 1:
    >>> inverse_coin_change(4, [1, 2])
    [[1, 1, 1, 1], [1, 1, 2], [2, 2]]

    Example 2:
    >>> inverse_coin_change(3, [2])
    []

    Example 3:
    >>> inverse_coin_change(0, [1, 2])
    [[]]
    """
    results: List[List[int]] = []

    def backtrack(remaining: int, current_combo: List[int], start_index: int) -> None:
        if remaining == 0:
            results.append(current_combo.copy())
            return
        for i in range(start_index, len(coins)):
            coin = coins[i]
            if coin <= remaining:
                current_combo.append(coin)
                backtrack(remaining - coin, current_combo, i)  # Allow coin reuse
                current_combo.pop()

    coins.sort()
    backtrack(amount, [], 0)
    return results


# Uncomment the lines below to accept user input
# print("Please enter the target amount:")
# target_amount = int(input())
# print("Enter the coin denominations separated by spaces:")
# coin_values = list(map(int, input().split()))
# combinations = inverse_coin_change(target_amount, coin_values)
# print(combinations)


if __name__ == "__main__":
    print("Possible combinations for amount = 4 with coins [1, 2]:")
    print(inverse_coin_change(4, [1, 2]))

    print("\nPossible combinations for amount = 5 with coins [1, 3, 5]:")
    print(inverse_coin_change(5, [1, 3, 5]))
