# https://www.investopedia.com/terms/r/returnoninvestment.asp

from __future__ import annotations


def return_on_investment(
    gain_from_investment: float, cost_of_investment: float
) -> float:
    """
    Return on Investment (ROI) measures the profitability of an investment
    relative to its cost, expressed as a percentage.

    Formula: ROI = (Gain - Cost) / Cost * 100

    >>> return_on_investment(1000.0, 500.0)
    100.0
    >>> return_on_investment(500.0, 500.0)
    0.0
    >>> return_on_investment(200.0, 500.0)
    -60.0
    >>> return_on_investment(0.0, 500.0)
    -100.0
    >>> return_on_investment(1000.0, 0.0)
    Traceback (most recent call last):
        ...
    ValueError: cost_of_investment must be > 0
    >>> return_on_investment(1000.0, -100.0)
    Traceback (most recent call last):
        ...
    ValueError: cost_of_investment must be > 0
    """
    if cost_of_investment <= 0:
        raise ValueError("cost_of_investment must be > 0")
    return round(
        (gain_from_investment - cost_of_investment) / cost_of_investment * 100, 2
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
