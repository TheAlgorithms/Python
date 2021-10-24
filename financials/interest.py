from __future__ import annotations

def simple_interest(principle:float, daily_interest_rate:float, number_of_days_between_payments:int) -> float:
    """
    >>> simple_interest(18000,0.06,3)
    3240.0
    """
    result = principle * daily_interest_rate * number_of_days_between_payments
    return result

def compound_interest(principle:float, nominal_annual_interest_rate_percentage:float, number_of_compounding_periods:int)-> float:
    """
    >>> compound_interest(10000,0.05,3)
    1576.2500000000014
    """
    result = principle * ((1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods - 1)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
