"""
Pearson Correlation Coefficient: Measures the linear relationship between two
variables. The result is a value between -1 and 1, where:
    1  = perfect positive correlation
    0  = no correlation
   -1  = perfect negative correlation

It is widely used in data analysis, statistics, and machine learning to
understand relationships between features in a dataset.

Reference: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
"""


def pearson_correlation(x: list[float], y: list[float]) -> float:
    """
    Calculate the Pearson Correlation Coefficient between two lists.

    Parameters
    ----------
    x: list[float], first list of numbers
    y: list[float], second list of numbers

    Returns
    -------
    float: Pearson correlation coefficient between -1 and 1

    >>> pearson_correlation([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    1.0
    >>> pearson_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    -1.0
    >>> pearson_correlation([1, 2, 3], [4, 5, 6])
    1.0
    >>> round(pearson_correlation([1, 2, 3, 4], [1, 2, 1, 2]), 4)
    0.4472
    >>> pearson_correlation([], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: lists must not be empty
    >>> pearson_correlation([1, 2, 3], [1, 2])
    Traceback (most recent call last):
        ...
    ValueError: lists must have the same length
    >>> pearson_correlation([1, 1, 1], [2, 2, 2])
    Traceback (most recent call last):
        ...
    ValueError: standard deviation of x or y is zero
    """
    if not x or not y:
        raise ValueError("lists must not be empty")
    if len(x) != len(y):
        raise ValueError("lists must have the same length")

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    std_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    std_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5

    if std_x == 0 or std_y == 0:
        raise ValueError("standard deviation of x or y is zero")

    return round(numerator / (std_x * std_y), 10)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Pearson correlation: {pearson_correlation(x, y)}")
