from collections.abc import Sequence


def assign_ranks(data: Sequence[float]) -> list[float]:
    """
    Assigns ranks to elements in the array, averaging the ranks of tied values.

    :param data: List of floats.
    :return: List of floats representing the averaged ranks.

    Example:
    >>> assign_ranks([3.2, 1.5, 4.0, 2.7, 5.1])
    [3.0, 1.0, 4.0, 2.0, 5.0]

    >>> assign_ranks([10.5, 8.1, 12.4, 9.3, 11.0])
    [3.0, 1.0, 5.0, 2.0, 4.0]

    Tied values share the mean of their ordinal positions (the standard
    midrank / "fractional" convention required by Spearman's definition
    and used by ``scipy.stats.rankdata``):

    >>> assign_ranks([1, 2, 2, 4])
    [1.0, 2.5, 2.5, 4.0]
    """
    ranked_data = sorted((value, index) for index, value in enumerate(data))
    ranks = [0.0] * len(data)
    i = 0
    n = len(ranked_data)
    while i < n:
        j = i
        # Walk forward while the values stay equal, collecting the tied run.
        while j + 1 < n and ranked_data[j + 1][0] == ranked_data[i][0]:
            j += 1
        # The tied run occupies ordinal positions [i+1, j+1]; average them.
        # (i + j) / 2 + 1 is the same as the mean of (i+1, i+2, ..., j+1)
        # when written without the per-run accumulator.
        avg_rank = (i + j) / 2.0 + 1
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
    >>> round(calculate_spearman_rank_correlation(x, y), 6)
    0.410391

    Tied values are ranked by their midrank before the coefficient is
    computed, matching the standard Spearman convention:

    >>> x = [1, 2, 2, 4]
    >>> y = [1, 2, 3, 4]
    >>> round(calculate_spearman_rank_correlation(x, y), 6)
    0.948683
    """
    n = len(variable_1)
    if len(variable_2) != n:
        raise ValueError(
            f"variable_1 and variable_2 must have the same length, "
            f"got {n} and {len(variable_2)}"
        )
    if n < 2:
        raise ValueError(
            f"need at least 2 data points to compute Spearman's "
            f"rank correlation, got {n}"
        )

    rank_var1 = assign_ranks(variable_1)
    rank_var2 = assign_ranks(variable_2)

    # Pearson correlation of the averaged ranks is the formal definition
    # of Spearman's rho and handles tied ranks without losing precision,
    # unlike the closed-form 1 - 6 * d² / (n * (n² - 1)) shortcut that
    # assumes no ties.
    mean1 = sum(rank_var1) / n
    mean2 = sum(rank_var2) / n
    cov = sum((r1 - mean1) * (r2 - mean2) for r1, r2 in zip(rank_var1, rank_var2))
    var1 = sum((r1 - mean1) ** 2 for r1 in rank_var1)
    var2 = sum((r2 - mean2) ** 2 for r2 in rank_var2)
    if var1 == 0 or var2 == 0:
        # One (or both) of the inputs is constant; rho is undefined and
        # matches the scipy ConstantInputWarning behaviour.
        raise ValueError(
            "variable_1 and variable_2 must each contain at least one "
            "distinct value to compute Spearman's rank correlation"
        )
    rho = cov / (var1 * var2) ** 0.5

    return float(rho)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    print(
        f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) = }"
    )

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) = }")

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 1, 2, 9, 5]) = }")
