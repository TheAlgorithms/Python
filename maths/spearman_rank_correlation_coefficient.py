from collections.abc import Sequence


def assign_ranks(data: Sequence[float]) -> list[float]:
    """
    Assigns ranks to elements in the array.

    :param data: List of floats.
    :return: List of floats representing the ranks.

    Example:
    >>> assign_ranks([3.2, 1.5, 4.0, 2.7, 5.1])
    [3.0, 1.0, 4.0, 2.0, 5.0]

    >>> assign_ranks([10.5, 8.1, 12.4, 9.3, 11.0])
    [3.0, 1.0, 5.0, 2.0, 4.0]

    >>> assign_ranks([1, 1, 1, 1])
    [2.5, 2.5, 2.5, 2.5]
    """
    n = len(data)
    ranked_data = sorted((value, index) for index, value in enumerate(data))
    ranks = [0.0] * n

    i = 0
    while i < n:
        j = i
        while j < n - 1 and ranked_data[j + 1][0] == ranked_data[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1  # average rank of positions i to j
        for k in range(i, j + 1):
            ranks[ranked_data[k][1]] = avg_rank
        i = j + 1
    return ranks


def calculate_spearman_rank_correlation(
    variable_1: Sequence[float], variable_2: Sequence[float]
) -> float:
    """
    Calculates Spearman's rank correlation coefficient.

    :param variable_1: List of floats representing the first variable.
    :param variable_2: List of floats representing the second variable.
    :return: Spearman's rank correlation coefficient.
    :raises ValueError: If less than 2 data points are provided.

    Example Usage:

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [5, 4, 3, 2, 1]
    >>> calculate_spearman_rank_correlation(x, y)
    -1.0

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> calculate_spearman_rank_correlation(x, y)
    1.0

    >>> x = [1, 2, 3, 4, 5]
    >>> y = [5, 1, 2, 9, 5]
    >>> calculate_spearman_rank_correlation(x, y)
    0.4

    >>> x = [5]
    >>> y = [9]
    >>> calculate_spearman_rank_correlation(x, y)
    Traceback (most recent call last):
        ...
    ValueError: Need at least 2 data points to calculate correlation
    """
    n = len(variable_1)

    if n < 2:
        raise ValueError("Need at least 2 data points to calculate correlation")

    rank_var1 = assign_ranks(variable_1)
    rank_var2 = assign_ranks(variable_2)

    # Calculate differences of ranks
    d = [rx - ry for rx, ry in zip(rank_var1, rank_var2)]

    # Calculate the sum of squared differences
    d_squared = sum(di**2 for di in d)

    # Calculate the Spearman's rank correlation coefficient
    rho = 1 - (6 * d_squared) / (n * (n**2 - 1))

    return round(rho, 1)  # rounding to avoid floating point arithmetic issues


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    print(
        f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) = }"
    )

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) = }")

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 1, 2, 9, 5]) = }")

    print(
        f"{calculate_spearman_rank_correlation([5], [9]) = }"
    )  # This will raise a ValueError
