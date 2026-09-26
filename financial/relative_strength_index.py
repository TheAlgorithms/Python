"""
Calculate the relative strength index (RSI) on a series of stciks prices
Wikipedia Reference: https://en.wikipedia.org/wiki/Relative_strength_index
Other Reference: https://www.investopedia.com/terms/r/rsi.asp

RSI is a technical indicator used in finance to measure the speed and magnitude of
recent price changes of a stock. Its value ranges from 0 to 100, where a low number
indicates the stock may be oversold, and a high number indicates the stock may be
overbought.
"""

from collections.abc import Sequence


def relative_strength_index(
    stock_prices: Sequence[float], window_size: int
) -> list[float | None]:
    """
    Returns the relative strength index from inputted stock prices
    >>> relative_strength_index([44, 44.5, 43, 45, 44.5, 46, 46.5], 3)
    [None, None, None, 52.631578947368425, 72.3076923076923, 77.07006369426752]

    Formula:
    rsi = 100 - (100 / (1 + rs))

    Where,
    rs : Relative strength which is the average gain divided by the average loss.

    Relative strength index (RSI) returns a number between 0 and 100 and is a method
    of determining if a stock may be overbought (greater than 70) or oversold (less
    than 30). This function uses the Wilder smoothing implementation of RSI.
    """

    # Check inputs are reasonable
    if window_size <= 0:
        raise ValueError("window_size must be greater than 0")

    if len(stock_prices) <= 1:
        raise ValueError("stocks_prices needs to have at least 2 entries")

    if len(stock_prices) <= window_size:
        raise ValueError(
            "stock_prices needs to be have more entries than the value of window_size"
        )

    # Calculate price changes
    price_changes = [
        stock_prices[i] - stock_prices[i - 1] for i in range(1, len(stock_prices))
    ]

    # Separate gains and losses
    gains = [max(price_change, 0) for price_change in price_changes]
    losses = [abs(min(price_change, 0)) for price_change in price_changes]

    # Initialise none values for entries before the window
    rsi_values: list[float | None] = [None] * window_size

    # Calculate initial average gains and losses as floats
    avg_gain: float = sum(gains[:window_size]) / float(window_size)
    avg_loss: float = sum(losses[:window_size]) / float(window_size)

    # Compute RSI using Wilder smoothing method
    for i in range(window_size, len(price_changes)):
        gain = float(gains[i])
        loss = float(losses[i])

        avg_gain = (avg_gain * (window_size - 1) + gain) / window_size
        avg_loss = (avg_loss * (window_size - 1) + loss) / window_size

        if avg_loss == 0:
            rsi = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi = 100.0 - (100.0 / (1.0 + rs))

        rsi_values.append(rsi)

    return rsi_values


if __name__ == "__main__":
    stock_prices = [
        44,
        44.15,
        43.9,
        44.35,
        44.7,
        45,
        45.1,
        44.9,
        45.3,
        45.7,
        46.2,
        45.9,
        46.3,
        46.8,
        47.1,
    ]
    window_size = 5
    rsi = relative_strength_index(stock_prices, window_size)
    print(f"Stock prices: {stock_prices}")
    print(f"Windows size: {window_size}")
    print(f"RSI: {rsi}")
