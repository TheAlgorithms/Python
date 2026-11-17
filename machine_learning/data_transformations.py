"""
Data transformations are useful for preparing data for machine learning algorithms.
Different algorithms perform better with different data transformations.
Two common data transformations are normalization and standardization.

Normalization:
    Normalization scales all numeric variables in the range [0, 1].
    One possible formula is given below:
    x_norm = (x - x_min) / (x_max - x_min)
    Source: https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)

Standardization:
    Standardization transforms data to have a mean of 0 and a standard deviation of 1.
    One possible formula is given below:
    x_std = (x - mean) / standard_deviation
    Source: https://en.wikipedia.org/wiki/Feature_scaling#Standardization_(Z-score_Normalization)

Choosing between Normalization & Standardization is more of an art than a science, but
it is often recommended to run experiments with both to see which performs better.
Additionally, a few rules of thumb are:
    1. gaussian (normal) distributions work better with standardization
    2. non-gaussian (non-normal) distributions work better with normalization
    3. If a column or list of values has extreme values / outliers, use standardization
"""

from statistics import mean, stdev


def normalization(data: list[float], ndigits: int = 3) -> list[float]:
    """
    Return a normalized list of values.

    @params: data, a list of values to normalize
    @returns: a list of normalized values (rounded to ndigits decimal places)
    @examples:
    >>> normalization([2, 7, 10, 20, 30, 50])
    [0.0, 0.104, 0.167, 0.375, 0.583, 1.0]
    >>> normalization([5, 10, 15, 20, 25])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    >>> normalization([])
    Traceback (most recent call last):
        ...
    ValueError: Input data list cannot be empty.
    >>> normalization([5, 5, 5])
    Traceback (most recent call last):
        ...
    ValueError: Cannot normalize data where all values are identical.
    """
    if not data:
        raise ValueError("Input data list cannot be empty.")

    x_min = min(data)
    x_max = max(data)

    if x_max == x_min:
        raise ValueError("Cannot normalize data where all values are identical.")

    return [round((x - x_min) / (x_max - x_min), ndigits) for x in data]


def standardization(data: list[float], ndigits: int = 3) -> list[float]:
    """
    Return a standardized list of values.

    @params: data, a list of values to standardize
    @returns: a list of standardized values (rounded to ndigits decimal places)
    @examples:
    >>> standardization([2, 7, 10, 20, 30, 50])
    [-0.999, -0.719, -0.551, 0.009, 0.57, 1.69]
    >>> standardization([5, 10, 15, 20, 25])
    [-1.265, -0.632, 0.0, 0.632, 1.265]
    >>> standardization([5])
    Traceback (most recent call last):
        ...
    ValueError: Input data list must contain at least two values.
    >>> standardization([5, 5, 5])
    Traceback (most recent call last):
        ...
    ValueError: Cannot standardize data where all values are identical.
    """
    if len(data) < 2:
        raise ValueError("Input data list must contain at least two values.")

    mu = mean(data)
    sigma = stdev(data)

    if sigma == 0:
        raise ValueError("Cannot standardize data where all values are identical.")

    return [round((x - mu) / sigma, ndigits) for x in data]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
