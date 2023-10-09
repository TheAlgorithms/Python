# Print all subset combinations of n element in given set of r element.


def subset_combinations_dp(elements, n):
    """
    Generate all subset combinations of 'n' elements using dynamic programming.

    Args:
    elements (list): The input list of elements.
    n (int): The number of elements in each combination.

    Returns:
    list: A list of tuples, where each tuple represents a combination.

    Examples:
    >>> elements = [1, 2, 3, 4]
    >>> n = 2
    >>> subset_combinations_dp(elements, n)
    [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    >>> elements = [1, 2, 3]
    >>> n = 3
    >>> subset_combinations_dp(elements, n)
    [(1, 2, 3)]

    >>> elements = [1, 2, 3]
    >>> n = 0
    >>> subset_combinations_dp(elements, n)
    [()]
    """
    r = len(elements)

    dp = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for prev_combination in dp[j - 1]:
                dp[j].append(tuple(prev_combination) + (elements[i - 1],))

    combinations = dp[n]

    return combinations

if __name__ == "__main__":
    import doctest
    doctest.testmod()
