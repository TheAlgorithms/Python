"""
Calculate the minimum number of attempts needed in the worst case to find the
critical floor from which eggs start breaking when dropped.
"""

# The Egg Dropping Problem is a classic dynamic programming problem.
# - You are given `k` eggs and a building with `n` floors. Your goal is to determine
#   the minimum number of attempts required to find the highest floor `F` from which
#   if an egg is dropped, it will break. If an egg breaks from floor `F`, it will
#   also break from any floor above `F`. The challenge is to minimize the worst-case
#   number of attempts.


def egg_dropping(eggs: int, floors: int) -> int:
    """
    Calculate the minimum number of attempts needed in the worst case for `eggs`
    and `floors` using dynamic programming.

    >>> egg_dropping(1, 5)
    5
    >>> egg_dropping(2, 6)
    3
    >>> egg_dropping(2, 10)
    4
    """

    # Base case: No floors require 0 trials, one floor requires 1 trial.
    if floors in (0, 1):
        return floors
    if eggs == 1:
        return floors

    # Create a DP table to store the results of subproblems.
    dp = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]

    # Fill the base cases for one egg (i.e., we need `i` attempts for `i` floors).
    for i in range(1, floors + 1):
        dp[1][i] = i

    # Compute the minimum number of trials in the worst case for each combination.
    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            dp[e][f] = 10**9  # Initialize to infinity.
            for x in range(1, f + 1):
                res = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                dp[e][f] = min(dp[e][f], res)

    return dp[eggs][floors]


if __name__ == "__main__":
    print("\n********* Egg Dropping Problem Using Dynamic Programming ************\n")
    print("\n*** Enter -1 at any time to quit ***")
    print("\nEnter the number of eggs and floors separated by a space: ", end="")
    try:
        while True:
            input_data = input().strip()
            if input_data == "-1":
                print("\n********* Goodbye!! ************")
                break
            else:
                eggs, floors = map(int, input_data.split())
                print(
                    f"The minimum number of attempts required with {eggs} eggs and "
                    f"{floors} floors is:"
                )
                print(egg_dropping(eggs, floors))
                print("Try another combination of eggs and floors: ", end="")
    except (NameError, ValueError):
        print("\n********* Invalid input, goodbye! ************\n")
