def rankdata(arr):
    """
    Assigns ranks to elements in the array.
    """
    ranked = sorted((value, index) for index, value in enumerate(arr))
    ranks = [0] * len(arr)

    for pos, (_, index) in enumerate(ranked):
        ranks[index] = pos + 1

    return ranks


def spearman_rank_correlation(x, y):
    """
    Calculates Spearman's rank correlation coefficient.

    Example Usage :

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [5, 4, 3, 2, 1]
    >>> spearman_rank_correlation(x, y)
    -1.0

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> spearman_rank_correlation(x, y)
    1.0

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [5, 1, 2, 9, 5]
    >>> spearman_rank_correlation(x, y)
    0.6

    """
    n = len(x)
    rank_x = rankdata(x)
    rank_y = rankdata(y)

    # Calculate differences of ranks
    d = [rx - ry for rx, ry in zip(rank_x, rank_y)]

    # Calculate the sum of squared differences
    d_squared = sum(di**2 for di in d)

    # Calculate the Spearman's rank correlation coefficient
    rho = 1 - (6 * d_squared) / (n * (n**2 - 1))

    return rho


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 4, 6, 8, 10]
    rho1 = spearman_rank_correlation(x1, y1)
    print(f"Spearman's rank correlation coefficient (Example 1): {rho1}")

    x2 = [1, 2, 3, 4, 5]
    y2 = [5, 4, 3, 2, 1]
    rho2 = spearman_rank_correlation(x2, y2)
    print(f"Spearman's rank correlation coefficient (Example 2): {rho2}")

    x3 = [1, 2, 3, 4, 5]
    y3 = [5, 1, 2, 9, 5]
    rho3 = spearman_rank_correlation(x3, y3)
    print(f"Spearman's rank correlation coefficient (Example 3): {rho3}")
