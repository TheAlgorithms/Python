"""
Value at Risk (VaR) via historical simulation.

References:
- https://en.wikipedia.org/wiki/Value_at_risk
- https://www.investopedia.com/terms/v/var.asp

Value at Risk measures the maximum loss a portfolio can suffer over a given
period at a chosen confidence level. Historical simulation is a
non-parametric method: it reuses the observed returns and reads the quantile
from the empirical distribution, so no assumption is made about the shape of
the loss distribution. The result is the negative of the corresponding return
quantile, i.e. a positive loss magnitude when the tail of the distribution
contains losses.
"""

from collections.abc import Sequence
from math import isfinite


def _linear_interpolated_quantile(
    sorted_values: Sequence[float], quantile: float
) -> float:
    """
    Linear interpolation between the closest ranks (NumPy default, type 7).

    >>> _linear_interpolated_quantile([-10.0, -5.0, -2.0, 1.0, 4.0], 0.05)
    -9.0
    >>> _linear_interpolated_quantile([1.0, 2.0, 3.0], 1.0)
    3.0
    """
    position = (len(sorted_values) - 1) * quantile
    lower_index = int(position)
    fraction = position - lower_index
    if lower_index == len(sorted_values) - 1:
        return sorted_values[-1]
    return sorted_values[lower_index] * (1 - fraction) + (
        sorted_values[lower_index + 1] * fraction
    )


def value_at_risk(returns: Sequence[float], confidence_level: float = 0.95) -> float:
    """
    Calculate the historical-simulation Value at Risk of a portfolio.

    The confidence level is the probability that the loss will not exceed the
    returned value. The default of 0.95 means that 95% of the observed returns
    are better (higher) than the VaR threshold, and the remaining 5% are worse.

    Examples:
    >>> value_at_risk([-10, -5, -2, 1, 4], 0.95)
    9.0
    >>> value_at_risk([-2, -1, 0, 1, 2, 3], 0.90)
    1.5
    >>> value_at_risk([5, 10, 15], 0.75)
    -7.5
    >>> value_at_risk([], 0.95)
    Traceback (most recent call last):
    ...
    ValueError: returns must not be empty
    >>> value_at_risk([-1, 0, 1], 1.0)
    Traceback (most recent call last):
    ...
    ValueError: confidence_level must be strictly between 0 and 1
    >>> value_at_risk([-1, float("nan"), 1], 0.95)
    Traceback (most recent call last):
    ...
    ValueError: returns must contain only finite numbers

    Time complexity: O(n log n), where n = len(returns), for sorting.
    Space complexity: O(n) for the sorted copy.
    """
    if not returns:
        raise ValueError("returns must not be empty")
    if not all(isfinite(value) for value in returns):
        raise ValueError("returns must contain only finite numbers")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be strictly between 0 and 1")

    sorted_returns = sorted(returns)
    threshold = _linear_interpolated_quantile(sorted_returns, 1 - confidence_level)
    return -threshold


if __name__ == "__main__":
    import doctest

    doctest.testmod()
