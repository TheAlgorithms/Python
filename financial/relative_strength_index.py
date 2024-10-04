from typing import List

def calculate_rsi(prices: List[float], period: int = 14) -> List[float]:
    """
    Calculate the Relative Strength Index (RSI) for a given list of prices.

    RSI is a momentum oscillator that measures the speed and change of price movements.
    It is typically used to identify overbought or oversold conditions in a market.

    Args:
        prices (List[float]): A list of prices for a financial asset.
        period (int): The number of periods to use in the calculation (default is 14).

    Returns:
        List[float]: A list of RSI values corresponding to the input price data.

    Example:
        >>> rsi_values = calculate_rsi([44.0, 44.15, 44.09, 44.20, 44.30, 44.25, 44.40, 44.35, 44.50, 44.60, 44.55, 44.75, 44.80, 44.70, 44.85], 14)
        >>> print(rsi_values)  # doctest: +ELLIPSIS
        [78.91..., 80.99...]
        
    Reference:
        https://en.wikipedia.org/wiki/Relative_strength_index
    """
    # Validate that there are enough prices to calculate RSI
    if len(prices) < period:
        raise ValueError("Not enough price data to calculate RSI.")

    gains = []
    losses = []

    # Calculate price changes between consecutive days
    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        gains.append(max(0, delta))
        losses.append(max(0, -delta))

    # Initial averages for gain and loss
    avg_gain = float(sum(gains[:period]) / period)
    avg_loss = float(sum(losses[:period]) / period)

    # Initialize RSI list and first RSI value
    rsi_values: List[float] = []

    if avg_loss == 0:
        rsi = 100.0
    else:
        rs = avg_gain / avg_loss
        rsi = 100.0 - (100.0 / (1.0 + rs))

    rsi_values.append(rsi)

    # Calculate subsequent RSI values
    for i in range(period, len(prices)):
        delta = prices[i] - prices[i - 1]
        gain = max(0, delta)
        loss = max(0, -delta)

        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

        if avg_loss == 0:
            rsi = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi = 100.0 - (100.0 / (1.0 + rs))

        rsi_values.append(rsi)

    return rsi_values


if __name__ == "__main__":
    prices = [44.0, 44.15, 44.09, 44.20, 44.30, 44.25, 44.40, 44.35, 44.50, 44.60, 44.55, 44.75, 44.80, 44.70, 44.85]
    rsi = calculate_rsi(prices, 14)
    print("RSI Values:", rsi)
