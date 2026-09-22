"""
Expected Shortfall (ES), also known as Conditional Value at Risk (CVaR),
estimated with historical simulation.

References:
- https://en.wikipedia.org/wiki/Expected_shortfall
- https://www.investopedia.com/terms/c/conditional_value_at_risk.asp

Expected Shortfall measures the average loss that occurs in the tail of the
loss distribution beyond the Value at Risk threshold. Unlike Value at Risk,
which only reports a quantile boundary, Expected Shortfall captures how bad
the losses actually are when the worst cases happen, and it is a coherent
risk measure.
"""

from collections.abc import Sequence
from math import isfinite


def _linear_interpolated_quantile(
    sorted_values: Sequence[float], quantile: float
) -> float:
    """
    Linear interpolation between the closest ranks (NumPy default, type 7).

    >>> _linear_interpolated_quantile([-10.0, -5.0, -2.0, 1.0, 4.0], 0.25)
    -5.0
    """
    position = (len(sorted_values) - 1) * quantile
    lower_index = int(position)
    fraction = position - lower_index
    if lower_index == len(sorted_values) - 1:
        return sorted_values[-1]
    return sorted_values[lower_index] * (1 - fraction) + (
        sorted_values[lower_index + 1] * fraction
    )


def expected_shortfall(
    returns: Sequence[float], confidence_level: float = 0.95
) -> float:
    """
    Calculate the historical-simulation Expected Shortfall of a portfolio.

    The confidence level is the probability that the loss will not exceed the
    corresponding Value at Risk threshold. The tail contains every observed
    return at or below that threshold, and the result is the negative of the
    average of that tail, i.e. a positive loss magnitude when the tail contains
    losses.

    Examples:
    >>> expected_shortfall([-10, -5, -2, 1, 4], 0.95)
    10.0
    >>> expected_shortfall([-10, -5, -2, 1, 4], 0.75)
    7.5
    >>> expected_shortfall([], 0.95)
    Traceback (most recent call last):
    ...
    ValueError: returns must not be empty
    >>> expected_shortfall([-1, 0, 1], 0.0)
    Traceback (most recent call last):
    ...
    ValueError: confidence_level must be strictly between 0 and 1
    >>> expected_shortfall([-1, float("inf"), 1], 0.95)
    Traceback (most recent call last):
    ...
    ValueError: returns must contain only finite numbers

    Time complexity: O(n log n), where n = len(returns), for sorting.
    Space complexity: O(n) for the sorted copy and the tail.
    """
    if not returns:
        raise ValueError("returns must not be empty")
    if not all(isfinite(value) for value in returns):
        raise ValueError("returns must contain only finite numbers")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be strictly between 0 and 1")

    sorted_returns = sorted(returns)
    threshold = _linear_interpolated_quantile(sorted_returns, 1 - confidence_level)
    tail = [value for value in sorted_returns if value <= threshold]
    return -sum(tail) / len(tail)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
