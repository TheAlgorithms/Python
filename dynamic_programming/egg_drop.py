"""
Egg Dropping Problem is a well-known problem in computer science.
The task is to find the minimum number of attempts required in the
worst case to find the highest floor from which an egg can be dropped
without breaking, given a certain number of floors and eggs.

Wikipedia: https://en.wikipedia.org/wiki/Dynamic_programming#Egg_dropping_puzzle
"""


def egg_drop(eggs: int, floors: int) -> int:
    """
    Calculate the minimum number of attempts required in the worst case
    to determine the highest floor from which an egg can be dropped
    without breaking it.

    Parameters:
    eggs (int): Number of eggs available.
    floors (int): Number of floors to test.

    Returns:
    int: Minimum number of attempts required in the worst case.

    Example:
    >>> egg_drop(2, 10)
    4

    >>> egg_drop(3, 14)
    4
    """
    # Initialize dp table with integers
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

    # Fill dp table for one egg (we have to try all floors)
    for i in range(1, floors + 1):
        dp[1][i] = i

    # Fill the rest of the dp table
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            dp[e][f] = floors + 1  # Start with an arbitrary large integer
            for k in range(1, f + 1):
                res = 1 + max(dp[e - 1][k - 1], dp[e][f - k])
                dp[e][f] = min(dp[e][f], res)

    return dp[eggs][floors]
