"""
Autocorrelation measures the correlation of a signal with a delayed
copy of itself. It is widely used in time series analysis, signal
processing, and statistics.

Reference: https://en.wikipedia.org/wiki/Autocorrelation
"""


def autocorrelation(data: list[float], lag: int) -> float:
    """
    Calculate the autocorrelation of a time series at a given lag.

    :param data: A list of numerical values representing the time series.
    :param lag: The number of time steps to shift the series.
    :return: The autocorrelation coefficient at the given lag.

    >>> round(autocorrelation([1, 2, 3, 4, 5], 1), 4)
    0.4
    >>> round(autocorrelation([1, 2, 3, 4, 5], 0), 4)
    1.0
    >>> autocorrelation([1, 2, 3], 5)
    Traceback (most recent call last):
        ...
    ValueError: Lag must be less than the length of the data.
    """
    if lag >= len(data):
        raise ValueError("Lag must be less than the length of the data.")

    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n

    if variance == 0:
        raise ValueError("Variance of data is zero, autocorrelation undefined.")

    covariance = (
        sum((data[i] - mean) * (data[i - lag] - mean) for i in range(lag, n)) / n
    )

    return covariance / variance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    data = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    for lag in range(5):
        print(f"Lag {lag}: {autocorrelation(data, lag):.4f}")
