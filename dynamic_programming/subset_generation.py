# return all subset combinations of n element in given set of r element.


def subset_combinations_dp(elements: list[int], n: int) -> list[tuple[int, ...]]:
    """
    Compute n-element combinations from a given list using dynamic programming.
    Args:
        elements (list): The list of elements from which combinations will be generated.
        n (int): The number of elements in each combination.
    Returns:
        list: A list of tuples, each representing a combination of n elements.
        >>> subset_combinations_dp(elements=[10, 20, 30, 40], n=2)
        [(10, 20), (10, 30), (10, 40), (20, 30), (20, 40), (30, 40)]
        >>> subset_combinations_dp(elements=[1, 2, 3], n=1)
        [(1,), (2,), (3,)]
        >>> subset_combinations_dp(elements=[1, 2, 3], n=3)
        [(1, 2, 3)]
        >>> subset_combinations_dp(elements=[42], n=1)
        [(42,)]
        >>> subset_combinations_dp(elements=[6, 7, 8, 9], n=4)
        [(6, 7, 8, 9)]
        >>> subset_combinations_dp(elements=[10, 20, 30, 40, 50], n=0)
        [()]
        >>> subset_combinations_dp(elements=[1, 2, 3, 4], n=2)
        [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        >>> subset_combinations_dp(elements=[1, 'apple', 3.14], n=2)
        [(1, 'apple'), (1, 3.14), ('apple', 3.14)]\
    """
    r = len(elements)
    if n > r:
        return []

    dp: list[list[tuple]] = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for prev_combination in dp[j - 1]:
                dp[j].append(tuple(prev_combination) + (elements[i - 1],))

    element_type = type(elements[0])
    if all(isinstance(e, element_type) for e in elements):
        combinations = sorted(dp[n])
    else:
        combinations = dp[n]

    return combinations


if __name__ == "__main__":
    from itertools import combinations

    for items, n in (
        ([10, 20, 30, 40], 2),
        ([1, 2, 3], 1),
        ([1, 2, 3], 3),
        ([42], 1),
        ([6, 7, 8, 9], 4),
        ([10, 20, 30, 40, 50], 1),
        ([1, 2, 3, 4], 2),
        ([1, "apple", 3.14], 2),
        (["single"], 0),
        ([], 9),
    ):
        actual = subset_combinations_dp(items, n)
        expected = list(combinations(items, n))
        assert actual == expected, f"items, n: {actual} != {expected}"
    print(f"{subset_combinations_dp(elements=[10, 20, 30, 40], n=2) = }")

    import doctest

    doctest.testmod()
