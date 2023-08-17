"""
Financial ratios are quantitative metrics used to analyze and assess the relationships
between different financial elements in a company's financial statements, providing
insights into its performance, profitability, liquidity, and overall financial health.

Reference: https://en.wikipedia.org/wiki/Current_ratio
The Current Ratio is a liquidity ratio that measures whether a firm has enough
resources to meet its short-term obligations.

Reference: https://en.wikipedia.org/wiki/Quick_ratio
The quick ratio, also known as the acid-test ratio, is a financial ratio that measures
a company's ability to cover its short-term liabilities with its most liquid assets,
excluding inventory. It is calculated by dividing the sum of cash, marketable
securities, and accounts receivable by the total current liabilities. The quick ratio
provides a more conservative assessment of a company's liquidity compared to the
current ratio, as it excludes inventory, which may not be as readily convertible
to cash in the short term. A higher quick ratio indicates a stronger
ability to meet short-term obligations.
"""


def current_ratio(current_assets: int, current_liabilities) -> float:
    """
    >>> current_ratio(1000, 1000)
    1.0
    >>> current_ratio(200000, 125000)
    1.6
    >>> current_ratio(1000000, 1500000)
    0.67
    """
    return round(current_assets / current_liabilities, ndigits=2)


def quick_ratio(liquid_assets: int, quick_liabilities) -> float:
    """
    >>> quick_ratio(10000, 10000)
    1.0
    >>> quick_ratio(2000000, 1250000)
    1.6
    >>> quick_ratio(2000000, 2500000)
    0.8
    """
    return round(liquid_assets / quick_liabilities, ndigits=2)


def quick_ratio(
    cash: int, marketable_securities: int, accounts_receivable: int, current_liabilities
) -> float:
    """
    >>> quick_ratio(1000000, 150000, 500000, 2000000)
    0.82
    >>> quick_ratio(200000, 125000, 50000, 5000000)
    0.07
    >>> quick_ratio(1000000, 1500000, 250000, 1000000)
    2.75
    """
    return round(
        (cash + marketable_securities + accounts_receivable) / current_liabilities,
        ndigits=2,
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
