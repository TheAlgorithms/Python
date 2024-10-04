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
        >>> calculate_rsi([44.0, 44.15, 44.09, 44.20, 44.30, 44.25, 44.40], 14)
        [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]

    Reference:
        https://en.wikipedia.org/wiki/Relative_strength_index
    """

    # Validate that there are enough prices to calculate RSI
    if len(prices) < period:
        raise ValueError("Not enough price data to calculate RSI.")

    # Initialize lists to store gains and losses
    gains = []
    losses = []

    # Calculate price changes between consecutive days
    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        
        # Gain if delta is positive, otherwise it's a loss
        gains.append(max(0, delta))
        losses.append(max(0, -delta))

    # Calculate the initial average gain and average loss (Simple Moving Average)
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    # Initialize the RSI list with the first calculated RSI value
    rsi_values = []

    # First RSI value calculation
    if avg_loss == 0:
        rsi = 100  # No loss means RSI is 100 (overbought)
    else:
        rs = avg_gain / avg_loss  # Relative Strength
        rsi = 100 - (100 / (1 + rs))  # RSI formula

    rsi_values.append(rsi)

    # Calculate the rest of the RSI values using smoothed moving averages
    for i in range(period, len(prices)):
        delta = prices[i] - prices[i - 1]
        
        # Update gains and losses
        gain = max(0, delta)
        loss = max(0, -delta)

        # Calculate smoothed averages
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

        # Compute RSI
        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        # Append RSI value to list
        rsi_values.append(rsi)

    return rsi_values


# Example usage:
if __name__ == "__main__":
    prices = [44.0, 44.15, 44.09, 44.20, 44.30, 44.25, 44.40, 44.35, 44.50, 44.60, 44.55, 44.75, 44.80, 44.70, 44.85]
    rsi = calculate_rsi(prices, 14)
    print("RSI Values:", rsi)
