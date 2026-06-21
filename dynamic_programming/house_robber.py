def house_robber(houses: list[int]) -> int:
    """
    Solves the House Robber problem using memoization (caching).
    Returns the maximum amount of money that can be robbed without triggering alarms.
    Problem URL: https://leetcode.com/problems/house-robber/

    Args:
        houses: A list of integers representing the amount of money in each house.
    Returns:
        int: The maximum amount of money that can be robbed without triggering alarms.
    Raises:
        ValueError: If there are no houses in the input list.

    Examples:
        >>> house_robber([2, 3, 2])
        4
        >>> house_robber([1, 2, 3, 1])
        4
        >>> house_robber([0, 0, 0, 0])
        0
        >>> house_robber([10, 15, 20, 25])
        40
        >>> house_robber([50])
        50
        >>> house_robber([5, 15, 5, 15, 5])
        30
    """
    number_of_houses = len(houses)
    if number_of_houses == 0:
        raise ValueError("There must be at least one house")

    memo = [-1 for _ in range(number_of_houses)]

    def dp(n: int) -> int:
        if n >= number_of_houses:
            return 0
        # If the house has been visited before, avoid revisiting (Memoization)
        if memo[n] != -1:
            return memo[n]

        # Decide to rob this house and skip the next, or skip this one
        rob = houses[n] + dp(n + 2)
        dont_rob = dp(n + 1)

        memo[n] = max(rob, dont_rob)
        return memo[n]

    return dp(0)
