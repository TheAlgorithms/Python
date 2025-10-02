# https://www.investopedia.com

from __future__ import annotations


def simple_interest(
    principal: float, daily_interest_rate: float, days_between_payments: float
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
    ValueError: principal must be > 0
    >>> simple_interest(5500.0, 0.01, -5)
    Traceback (most recent call last):
        ...
    ValueError: days_between_payments must be > 0
    """
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return principal * daily_interest_rate * days_between_payments


def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
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
    ValueError: principal must be > 0
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    """
    Calculate the interest earned using daily compounded APR.

    Args:
        principal: Initial amount of money (must be > 0).
        nominal_annual_percentage_rate: APR as a decimal (must be >= 0).
        number_of_years: Number of years money is invested (must be > 0).

    Returns:
        Total interest earned.

    Raises:
        ValueError: If any input is invalid.

    Examples:
        >>> apr_interest(10000.0, 0.05, 3)
        1618.223072263547
        >>> apr_interest(10000.0, 0.05, 1)
        512.6749646744732
    """
    DAYS_IN_YEAR = 365

    def validate(name: str, value: float, min_value: float, include_equal: bool = False):
        if include_equal:
            if value < min_value:
                raise ValueError(f"{name} must be >= {min_value}")
        else:
            if value <= min_value:
                raise ValueError(f"{name} must be > {min_value}")

    validate("principal", principal, 0)
    validate("nominal_annual_percentage_rate", nominal_annual_percentage_rate, 0, True)
    validate("number_of_years", number_of_years, 0)

    daily_rate = nominal_annual_percentage_rate / DAYS_IN_YEAR
    total_days = number_of_years * DAYS_IN_YEAR

    return compound_interest(principal, daily_rate, total_days)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
