"""
Normalization.

Wikipedia: https://en.wikipedia.org/wiki/Normalization
Normalization is the process of converting numerical data to a standard range of values.
This range is typically between [0, 1] or [-1, 1]. The equation for normalization is
x_norm = (x - x_min)/(x_max - x_min) where x_norm is the normalized value, x is the
value, x_min is the minimum value within the column or list of data, and x_max is the
maximum value within the column or list of data. Normalization is used to speed up the
training of data and put all of the data on a similar scale. This is useful because
variance in the range of values of a dataset can heavily impact optimization
(particularly Gradient Descent).

Standardization Wikipedia: https://en.wikipedia.org/wiki/Standardization
Standardization is the process of converting numerical data to a normally distributed
range of values. This range will have a mean of 0 and standard deviation of 1. This is
also known as z-score normalization. The equation for standardization is
x_std = (x - mu)/(sigma) where mu is the mean of the column or list of values and sigma
is the standard deviation of the column or list of values.

Choosing between Normalization & Standardization is more of an art of a science, but it
is often recommended to run experiments with both to see which performs better.
Additionally, a few rules of thumb are:
    1. gaussian (normal) distributions work better with standardization
    2. non-gaussian (non-normal) distributions work better with normalization
    3. If a column or list of values has extreme values / outliers, use standardization
"""

from statistics import mean, stdev


def normalization(data: list, ndigits: int = 3) -> list:
    """
    Return a normalized list of values.

    @params: data, a list of values to normalize
    @returns: a list of normalized values (rounded to ndigits decimal places)
    @examples:
    >>> normalization([2, 7, 10, 20, 30, 50])
    [0.0, 0.104, 0.167, 0.375, 0.583, 1.0]
    >>> normalization([5, 10, 15, 20, 25])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # variables for calculation
    x_min = min(data)
    x_max = max(data)
    # normalize data
    return [round((x - x_min) / (x_max - x_min), ndigits) for x in data]


def standardization(data: list, ndigits: int = 3) -> list:
    """
    Return a standardized list of values.

    @params: data, a list of values to standardize
    @returns: a list of standardized values (rounded to ndigits decimal places)
    @examples:
    >>> standardization([2, 7, 10, 20, 30, 50])
    [-0.999, -0.719, -0.551, 0.009, 0.57, 1.69]
    >>> standardization([5, 10, 15, 20, 25])
    [-1.265, -0.632, 0.0, 0.632, 1.265]
    """
    # variables for calculation
    mu = mean(data)
    sigma = stdev(data)
    # standardize data
    return [round((x - mu) / (sigma), ndigits) for x in data]
