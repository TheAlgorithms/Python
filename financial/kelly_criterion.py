"""
Kelly Criterion for optimal position sizing in betting and trading.

The Kelly Criterion is a formula used to determine the optimal size of a series of bets
or investments to maximize logarithmic wealth over time. It was developed by John L.
Kelly Jr. in 1956.

Wikipedia Reference: https://en.wikipedia.org/wiki/Kelly_criterion
Investopedia: https://www.investopedia.com/articles/trading/04/091504.asp

The Kelly Criterion is widely used in:
- Sports betting and gambling to determine optimal bet sizes
- Investment portfolio management to size positions
- Trading strategies to manage risk and maximize growth
"""

from __future__ import annotations


def kelly_criterion(win_probability: float, win_loss_ratio: float) -> float:
    """
    Calculate the optimal fraction of bankroll to bet using the Kelly Criterion.

    The Kelly Criterion formula:
    f* = (p * b - q) / b

    Where:
    f* = fraction of bankroll to bet (Kelly fraction)
    p = probability of winning
    q = probability of losing (1 - p)
    b = win/loss ratio (amount won per unit staked / amount lost per unit staked)

    :param win_probability: Probability of winning (0 < p < 1)
    :param win_loss_ratio: Ratio of win amount to loss amount (b > 0)
    :return: Optimal fraction of bankroll to bet

    >>> round(kelly_criterion(0.6, 2.0), 4)
    0.4
    >>> round(kelly_criterion(0.55, 1.0), 4)
    0.1
    >>> kelly_criterion(0.5, 1.0)
    0.0
    >>> round(kelly_criterion(0.7, 3.0), 4)
    0.6
    >>> round(kelly_criterion(0.3, 2.0), 4)
    -0.05
    >>> kelly_criterion(0.0, 1.0)
    Traceback (most recent call last):
        ...
    ValueError: win_probability must be between 0 and 1 (exclusive)
    >>> kelly_criterion(1.0, 1.0)
    Traceback (most recent call last):
        ...
    ValueError: win_probability must be between 0 and 1 (exclusive)
    >>> kelly_criterion(0.5, 0.0)
    Traceback (most recent call last):
        ...
    ValueError: win_loss_ratio must be > 0
    >>> kelly_criterion(0.5, -1.0)
    Traceback (most recent call last):
        ...
    ValueError: win_loss_ratio must be > 0
    """
    if win_probability <= 0 or win_probability >= 1:
        raise ValueError("win_probability must be between 0 and 1 (exclusive)")
    if win_loss_ratio <= 0:
        raise ValueError("win_loss_ratio must be > 0")

    loss_probability = 1 - win_probability
    kelly_fraction = (win_probability * win_loss_ratio - loss_probability) / (
        win_loss_ratio
    )

    return kelly_fraction


def kelly_criterion_extended(
    win_probability: float, win_amount: float, loss_amount: float
) -> float:
    """
    Calculate the Kelly fraction using explicit win and loss amounts.

    This is a more general form of the Kelly Criterion that accepts
    absolute win and loss amounts rather than a ratio.

    Formula:
    f* = (p * W - q * L) / (W * L)

    Where:
    p = probability of winning
    q = probability of losing (1 - p)
    W = amount won per unit bet
    L = amount lost per unit bet (positive value)

    :param win_probability: Probability of winning (0 < p < 1)
    :param win_amount: Amount won per unit bet (W > 0)
    :param loss_amount: Amount lost per unit bet (L > 0)
    :return: Optimal fraction of bankroll to bet

    >>> round(kelly_criterion_extended(0.6, 2.0, 1.0), 4)
    0.4
    >>> round(kelly_criterion_extended(0.55, 1.5, 1.5), 4)
    0.1
    >>> kelly_criterion_extended(0.5, 1.0, 1.0)
    0.0
    >>> round(kelly_criterion_extended(0.7, 3.0, 1.0), 4)
    0.6
    >>> kelly_criterion_extended(0.0, 1.0, 1.0)
    Traceback (most recent call last):
        ...
    ValueError: win_probability must be between 0 and 1 (exclusive)
    >>> kelly_criterion_extended(0.5, 0.0, 1.0)
    Traceback (most recent call last):
        ...
    ValueError: win_amount must be > 0
    >>> kelly_criterion_extended(0.5, 1.0, 0.0)
    Traceback (most recent call last):
        ...
    ValueError: loss_amount must be > 0
    """
    if win_probability <= 0 or win_probability >= 1:
        raise ValueError("win_probability must be between 0 and 1 (exclusive)")
    if win_amount <= 0:
        raise ValueError("win_amount must be > 0")
    if loss_amount <= 0:
        raise ValueError("loss_amount must be > 0")

    loss_probability = 1 - win_probability
    # Convert to win/loss ratio format: b = win_amount / loss_amount
    # Then apply Kelly formula: (p * b - q) / b
    win_loss_ratio = win_amount / loss_amount
    kelly_fraction = (win_probability * win_loss_ratio - loss_probability) / (
        win_loss_ratio
    )

    return kelly_fraction


def fractional_kelly(
    win_probability: float, win_loss_ratio: float, fraction: float = 0.5
) -> float:
    """
    Calculate a fractional Kelly bet size to reduce volatility.

    Many practitioners use a fraction of the Kelly Criterion (e.g., half-Kelly)
    to reduce risk and volatility while still achieving good growth. This is
    because the full Kelly can lead to large drawdowns.

    Formula:
    f*_fractional = fraction * f*

    Where f* is the Kelly Criterion optimal fraction.

    :param win_probability: Probability of winning (0 < p < 1)
    :param win_loss_ratio: Ratio of win amount to loss amount (b > 0)
    :param fraction: Fraction of Kelly to use (0 < fraction <= 1), default 0.5
    :return: Fractional Kelly bet size

    >>> round(fractional_kelly(0.6, 2.0, 0.5), 4)
    0.2
    >>> round(fractional_kelly(0.55, 1.0, 0.25), 4)
    0.025
    >>> round(fractional_kelly(0.7, 3.0, 1.0), 4)
    0.6
    >>> fractional_kelly(0.6, 2.0, 0.0)
    Traceback (most recent call last):
        ...
    ValueError: fraction must be between 0 and 1 (exclusive for 0, inclusive for 1)
    >>> fractional_kelly(0.6, 2.0, 1.5)
    Traceback (most recent call last):
        ...
    ValueError: fraction must be between 0 and 1 (exclusive for 0, inclusive for 1)
    >>> fractional_kelly(0.0, 2.0, 0.5)
    Traceback (most recent call last):
        ...
    ValueError: win_probability must be between 0 and 1 (exclusive)
    """
    if fraction <= 0 or fraction > 1:
        raise ValueError(
            "fraction must be between 0 and 1 (exclusive for 0, inclusive for 1)"
        )

    full_kelly = kelly_criterion(win_probability, win_loss_ratio)
    return fraction * full_kelly


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example: A bet with 60% win probability and 2:1 odds
    win_prob = 0.6
    odds = 2.0
    full_kelly = kelly_criterion(win_prob, odds)
    half_kelly = fractional_kelly(win_prob, odds, 0.5)

    print(f"Win probability: {win_prob}")
    print(f"Win/loss ratio: {odds}")
    print(f"Full Kelly fraction: {full_kelly:.2%}")
    print(f"Half Kelly fraction: {half_kelly:.2%}")
