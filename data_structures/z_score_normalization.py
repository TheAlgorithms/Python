"""
Z-Score Normalization: Standardizes data by converting each value to the number
of standard deviations it is from the mean. The result has a mean of 0 and a
standard deviation of 1.

Formula: z = (x - mean) / standard_deviation

Z-score normalization is widely used in machine learning preprocessing,
statistics, and data analysis to bring features to the same scale.

Reference: https://en.wikipedia.org/wiki/Standard_score
"""


def z_score_normalization(data: list[float]) -> list[float]:
    """
    Normalize a list of numbers using Z-score normalization.

    Parameters
    ----------
    data: list[float], the input list of numbers

    Returns
    -------
    list[float]: list of z-scores for each element

    >>> z_score_normalization([2, 4, 4, 4, 5, 5, 7, 9])
    [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]
    >>> z_score_normalization([1, 1, 1, 1])
    Traceback (most recent call last):
        ...
    ValueError: standard deviation is zero — all elements are identical
    >>> z_score_normalization([])
    Traceback (most recent call last):
        ...
    ValueError: data cannot be empty
    >>> z_score_normalization([10])
    Traceback (most recent call last):
        ...
    ValueError: data must contain at least two elements
    >>> z_score_normalization([0, 0, 1, 1])
    [-1.0, -1.0, 1.0, 1.0]
    >>> z_score_normalization([-5, 0, 5])
    [-1.2247448714, 0.0, 1.2247448714]
    """
    if not data:
        raise ValueError("data cannot be empty")
    if len(data) < 2:
        raise ValueError("data must contain at least two elements")

    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5

    if std_dev == 0:
        raise ValueError("standard deviation is zero — all elements are identical")

    return [round((x - mean) / std_dev, 10) for x in data]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(f"Original data: {data}")
    print(f"Z-score normalized: {z_score_normalization(data)}")
