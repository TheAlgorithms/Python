"""
This is a pure Python implementation of the greedy coin change algorithm.

For more information on the coin change problem see: https://en.wikipedia.org/wiki/Change-making_problem

This algorithm computes the needed coins from a given set of coins that make up a given amount.
It works greedy, so it chooses the biggest possible coin that fits in the remaining amount until
the remaining sum is <=0.

As seen in the third test, the greedy algorithm is not always optimal. For more information: https://stackoverflow.com/questions/13557979/why-does-the-greedy-coin-change-algorithm-not-work-for-some-coin-sets
"""

import typing


def compute_coins(amount: int, coin_set: set[int]) -> list[int]:
    """
    Implementation of the greedy coin change algorithm.
    :param amount: Amount to compute the coin change for
    :param coin_set: Set of coins to use for the coin change
    :return: List of coins that make up the amount or empty list if not possible with greedy

    Examples:
    >>> compute_coins(34, {1, 2, 5, 10, 20, 50})
    [20, 10, 2, 2]
    >>> compute_coins(23, {2, 4, 6})
    []
    >>> compute_coins(10, {2, 6, 5})
    [6, 2, 2]
    >>> compute_coins(130, {200, 150, 100, 50, 1})
    [100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    coins: list = []

    coin_set = sorted(coin_set, reverse=True)

    while amount > 0:
        coin_fit = False
        for coin in coin_set:
            if coin <= amount:
                coins.append(coin)
                amount -= coin
                coin_fit = True
                break

        if not coin_fit:
            return []

    return coins


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input_coin_set = input("Enter coins seperated by a comma: ").strip()
    coin_set = {int(coin) for coin in user_input_coin_set.split(",")}

    user_input_amount = input("Enter amount: ").strip()
    amount = int(user_input_amount)

    print(f"Coin set: {compute_coins(amount, coin_set)}")
