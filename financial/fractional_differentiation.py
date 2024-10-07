"""Implementation of fractional differentiation from the book
`Advances in Financial Machine Learning` by Marcos Lopez de Prado.

Fractional differentiation is a technique to make time series stationary
while preserving the memory of the original data.

This implementation utilizes a fixed window size to calculate the
fractional differentiation. Note that this implementation is a simplified
version compared to the one presented in the book by Marcos Lopez de Prado.
Here, we do not consider the weight loss. In the book, weight loss is
calculated to account for the fact that the initial points in
the series carry different amounts of information than the final points.

In the calculation of fractional differentiation,
the price is convolved with the weights to obtain the
fractional differentiated series. This process enables the
transformation of the time series into a stationary form while
retaining the memory of the original data.

To determine the optimal degree of differentiation,
one needs to find the minimum value of the differentiation degree,
a value between 0 and 1, that renders the time series stationary.

Reference
---------
https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3257419

"""

from collections.abc import Sequence
from math import nan


def calculate_weights(degree: float, length: int) -> list[float]:
    r"""Calculate the weights for fractional differentiation.

    .. math::

        w_{0} = 1
        w_{k} = -w_{k-1} * (d - k + 1) / k

    Parameters
    ----------
    degree : float
        The degree of differentiation.
    length : int
        The length of the weights.

    Returns
    -------
    list[float]
        The weights for fractional differentiation.

    Examples
    --------
    >>> calculate_weights(0.5, 3)
    [1.0, -0.5, -0.125]
    >>> calculate_weights(0.5, 4)
    [1.0, -0.5, -0.125, -0.0625]
    """
    weights = [1.0]
    for k in range(1, length):
        weights.append(-1 * weights[-1] * (degree - k + 1) / k)
    return weights


def fracdiff_fixedwindow(
    price_series: Sequence[float], degree: float, window_size: int
) -> list[float]:
    """Calculate the fractional differentiation with a fixed window size.

    Parameters
    ----------
    price_series : Sequence[float]
        The price series to calculate the fractional differentiation.
    degree : float
        The degree of differentiation.

    Returns
    -------
    list[float]
        The fractional differentiated series.

    Examples
    --------
    >>> price_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> fracdiff_fixedwindow(price_series, 0.5, 3)
    [nan, nan, nan, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5]
    """
    weights = calculate_weights(degree=degree, length=len(price_series))
    frac_diff_series = [nan] * window_size
    for i in range(window_size, len(price_series)):
        frac_diff_series.append(
            sum(weights[j] * price_series[i - j] for j in range(window_size))
        )
    return frac_diff_series


if __name__ == "__main__":
    import doctest

    doctest.testmod()
