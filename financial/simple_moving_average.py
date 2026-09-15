"""
The Simple Moving Average (SMA) is a statistical calculation used to analyze data points
by creating a constantly updated average price over a specific time period.
In finance, SMA is often used in time series analysis to smooth out price data
and identify trends.

Reference: https://en.wikipedia.org/wiki/Moving_average
"""

from collections.abc import Sequence


def simple_moving_average(
    data: Sequence[float], window_size: int
) -> list[float | None]:
    """
    Calculate the simple moving average (SMA) for some given time series data.

    :param data: A list of numerical data points.
    :param window_size: An integer representing the size of the SMA window.
    :return: A list of SMA values with the same length as the input data.

    Examples:
    >>> sma = simple_moving_average([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 3)
    >>> [round(value, 2) if value is not None else None for value in sma]
    [None, None, 12.33, 13.33, 14.0, 14.33, 16.0, 17.0, 18.0, 19.0]
    >>> simple_moving_average([10, 12, 15], 5)
    [None, None, None]
    >>> simple_moving_average([10, 12, 15, 13, 14, 16, 18, 17, 19, 21], 0)
    Traceback (most recent call last):
    ...
    ValueError: Window size must be a positive integer
    """
    if window_size < 1:
        raise ValueError("Window size must be a positive integer")

    sma: list[float | None] = []

    for i in range(len(data)):
        if i < window_size - 1:
            sma.append(None)  # SMA not available for early data points
        else:
            window = data[i - window_size + 1 : i + 1]
            sma_value = sum(window) / window_size
            sma.append(sma_value)
    return sma


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example data (replace with your own time series data)
    data = [10, 12, 15, 13, 14, 16, 18, 17, 19, 21]

    # Specify the window size for the SMA
    window_size = 3

    # Calculate the Simple Moving Average
    sma_values = simple_moving_average(data, window_size)

    # Print the SMA values
    print("Simple Moving Average (SMA) Values:")
    for i, value in enumerate(sma_values):
        if value is not None:
            print(f"Day {i + 1}: {value:.2f}")
        else:
            print(f"Day {i + 1}: Not enough data for SMA")
