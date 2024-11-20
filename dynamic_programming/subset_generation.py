def subset_combinations(elements: list[int], n: int) -> list:
    """
    Compute n-element combinations from a given list using dynamic programming.
    Args:
        elements: The list of elements from which combinations will be generated.
        n: The number of elements in each combination.
    Returns:
        A list of tuples, each representing a combination of n elements.
        >>> subset_combinations(elements=[10, 20, 30, 40], n=2)
        [(10, 20), (10, 30), (10, 40), (20, 30), (20, 40), (30, 40)]
        >>> subset_combinations(elements=[1, 2, 3], n=1)
        [(1,), (2,), (3,)]
        >>> subset_combinations(elements=[1, 2, 3], n=3)
        [(1, 2, 3)]
        >>> subset_combinations(elements=[42], n=1)
        [(42,)]
        >>> subset_combinations(elements=[6, 7, 8, 9], n=4)
        [(6, 7, 8, 9)]
        >>> subset_combinations(elements=[10, 20, 30, 40, 50], n=0)
        [()]
        >>> subset_combinations(elements=[1, 2, 3, 4], n=2)
        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        >>> subset_combinations(elements=[1, 'apple', 3.14], n=2)
        [(1, 'apple'), (1, 3.14), ('apple', 3.14)]
        >>> subset_combinations(elements=['single'], n=0)
        [()]
        >>> subset_combinations(elements=[], n=9)
        []
        >>> from itertools import combinations
        >>> all(subset_combinations(items, n) == list(combinations(items, n))
        ...     for items, n in (
        ...         ([10, 20, 30, 40], 2), ([1, 2, 3], 1), ([1, 2, 3], 3), ([42], 1),
        ...         ([6, 7, 8, 9], 4), ([10, 20, 30, 40, 50], 1), ([1, 2, 3, 4], 2),
        ...         ([1, 'apple', 3.14], 2), (['single'], 0), ([], 9)))
        True
    """
    r = len(elements)
    if n > r:
        return []

    dp: list[list[tuple]] = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for prev_combination in dp[j - 1]:
                dp[j].append((*prev_combination, elements[i - 1]))

    try:
        return sorted(dp[n])
    except TypeError:
        return dp[n]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{subset_combinations(elements=[10, 20, 30, 40], n=2) = }")
