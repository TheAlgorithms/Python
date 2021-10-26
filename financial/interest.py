# https://www.investopedia.com

from __future__ import annotations


def simple_interest(
    principle: float, daily_interest_rate: float, days_between_payments: int
) -> float:
    """
    >>> simple_interest(18000.0, 0.06, 3)
    3240.0
    >>> simple_interest(0.5, 0.06, 3)
    0.09
    >>> simple_interest(18000.0, 0.01, 10)
    1800.0
    >>> simple_interest(18000.0, 0.0, 3)
    0.0
    >>> simple_interest(5500.0, 0.01, 100)
    5500.0
    >>> simple_interest(10000.0, -0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: daily_interest_rate must be >= 0
    >>> simple_interest(-10000.0, 0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: principle must be > 0
    >>> simple_interest(5500.0, 0.01, -5)
    Traceback (most recent call last):
        ...
    ValueError: days_between_payments must be > 0
    """
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")
    if principle <= 0:
        raise ValueError("principle must be > 0")
    return principle * daily_interest_rate * days_between_payments


def compound_interest(
    principle: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: int,
) -> float:
    """
    >>> compound_interest(10000.0, 0.05, 3)
    1576.2500000000014
    >>> compound_interest(10000.0, 0.05, 1)
    500.00000000000045
    >>> compound_interest(0.5, 0.05, 3)
    0.07881250000000006
    >>> compound_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_compounding_periods must be > 0
    >>> compound_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_interest_rate_percentage must be >= 0
    >>> compound_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principle must be > 0
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principle <= 0:
        raise ValueError("principle must be > 0")

    return principle * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
