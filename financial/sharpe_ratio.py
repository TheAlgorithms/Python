"""
Sharpe Ratio for measuring risk-adjusted returns in investment portfolios.

The Sharpe Ratio is a measure of risk-adjusted return developed by Nobel laureate
William F. Sharpe. It calculates the excess return per unit of risk (standard deviation)
and is widely used to compare the performance of investment portfolios.

Wikipedia Reference: https://en.wikipedia.org/wiki/Sharpe_ratio
Investopedia: https://www.investopedia.com/terms/s/sharperatio.asp

The Sharpe Ratio is used for:
- Comparing performance of different investment strategies
- Evaluating mutual funds and hedge funds
- Portfolio optimization and risk management
- Assessing risk-adjusted returns in trading strategies
"""

from __future__ import annotations


def sharpe_ratio(returns: list[float], risk_free_rate: float = 0.0) -> float:
    """
    Calculate the Sharpe Ratio for a series of returns.

    The Sharpe Ratio formula:
    S = (R - Rf) / std_dev

    Where:
    S = Sharpe Ratio
    R = Average return of the investment
    Rf = Risk-free rate of return
    std_dev = Standard deviation of returns (volatility)

    :param returns: List of periodic returns (e.g., daily, monthly)
    :param risk_free_rate: Risk-free rate of return per period, default 0.0
    :return: Sharpe Ratio

    >>> round(sharpe_ratio([0.1, 0.2, 0.15, 0.05, 0.12]), 4)
    2.2164
    >>> sharpe_ratio([0.05, 0.05, 0.05, 0.05, 0.05])
    inf
    >>> round(sharpe_ratio([0.1, 0.2, 0.15, 0.05, 0.12], 0.02), 4)
    1.8589
    >>> sharpe_ratio([0.0, 0.0, 0.0, 0.0, 0.0])
    0.0
    >>> round(sharpe_ratio([-0.05, -0.1, -0.08, -0.12, -0.15]), 4)
    -2.6261
    >>> sharpe_ratio([])
    Traceback (most recent call last):
        ...
    ValueError: returns list must not be empty
    >>> sharpe_ratio([0.1])
    Traceback (most recent call last):
        ...
    ValueError: returns list must contain at least 2 values
    """
    if not returns:
        raise ValueError("returns list must not be empty")
    if len(returns) < 2:
        raise ValueError("returns list must contain at least 2 values")

    # Calculate mean return
    mean_return = sum(returns) / len(returns)

    # Calculate excess return
    excess_return = mean_return - risk_free_rate

    # Calculate standard deviation (using sample standard deviation with n-1)
    variance = sum((r - mean_return) ** 2 for r in returns) / (len(returns) - 1)
    std_dev = variance**0.5

    # Handle zero volatility case
    if std_dev == 0:
        return float("inf") if excess_return > 0 else 0.0

    return excess_return / std_dev


def annualized_sharpe_ratio(
    returns: list[float], risk_free_rate: float = 0.0, periods_per_year: int = 252
) -> float:
    """
    Calculate the annualized Sharpe Ratio for a series of periodic returns.

    The annualized Sharpe Ratio accounts for the time period of returns:
    S_annual = S_periodic * sqrt(periods_per_year)

    Common periods_per_year values:
    - Daily returns: 252 (trading days)
    - Weekly returns: 52
    - Monthly returns: 12
    - Quarterly returns: 4

    :param returns: List of periodic returns
    :param risk_free_rate: Risk-free rate per period, default 0.0
    :param periods_per_year: Number of periods in a year, default 252 (daily)
    :return: Annualized Sharpe Ratio

    >>> round(annualized_sharpe_ratio(
    ...     [0.001, 0.002, 0.0015, 0.0005, 0.0012], 0.0, 252), 4)
    35.1844
    >>> round(annualized_sharpe_ratio([0.01, 0.02, 0.015, 0.005, 0.012], 0.0, 12), 4)
    7.6779
    >>> round(annualized_sharpe_ratio([0.05, 0.06, 0.055, 0.045, 0.052], 0.0, 4), 4)
    18.7322
    >>> round(annualized_sharpe_ratio([0.001, 0.002, 0.0015], 0.0001, 252), 4)
    44.4486
    >>> round(annualized_sharpe_ratio([0.001, 0.002], 0.0, 252), 4)
    33.6749
    >>> annualized_sharpe_ratio([0.001, 0.002, 0.0015], 0.0, 0)
    Traceback (most recent call last):
        ...
    ValueError: periods_per_year must be > 0
    >>> annualized_sharpe_ratio([0.001, 0.002, 0.0015], 0.0, -252)
    Traceback (most recent call last):
        ...
    ValueError: periods_per_year must be > 0
    """
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be > 0")

    periodic_sharpe = sharpe_ratio(returns, risk_free_rate)

    # Annualize by multiplying by square root of periods
    if periodic_sharpe == float("inf"):
        return float("inf")

    return periodic_sharpe * (periods_per_year**0.5)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example: Calculate Sharpe Ratio for a series of monthly returns
    monthly_returns = [0.02, 0.03, -0.01, 0.04, 0.01, 0.02, -0.02, 0.03, 0.02, 0.01]
    risk_free = 0.002  # 0.2% monthly risk-free rate

    sharpe = sharpe_ratio(monthly_returns, risk_free)
    annualized = annualized_sharpe_ratio(monthly_returns, risk_free, 12)

    print(f"Monthly returns: {monthly_returns}")
    print(f"Risk-free rate: {risk_free:.2%}")
    print(f"Sharpe Ratio: {sharpe:.4f}")
    print(f"Annualized Sharpe Ratio: {annualized:.4f}")
