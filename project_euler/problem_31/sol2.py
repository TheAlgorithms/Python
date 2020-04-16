"""
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def solution(pence):
    """Returns the number of different ways to make X pence using any number of coins. solution is
    based on dynamic programming paradigm in bottom up fashion.

    >>> solution(500)
    6295434
    >>> solution(200)
    73682
    >>> solution(50)
    451
    >>> solution(10)
    11
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    number_of_ways = [0] * (pence + 1)
    number_of_ways[0] = 1  # base case: 1 way to make 0 pence
    for i in range(len(coins)):
        for j in range(coins[i], pence + 1, 1):
            number_of_ways[j] += number_of_ways[j - coins[i]]
    return number_of_ways[pence]


if __name__ == "__main__":
    assert solution(200) == 73682
