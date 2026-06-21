"""
Moving Average: Given a stream of integers and a window size k, calculate the
moving average of all integers in the sliding window.

The moving average is the average of the last k elements in the stream.
It is widely used in data analysis, finance, and signal processing to smooth
out short-term fluctuations and highlight longer-term trends.

Reference: https://en.wikipedia.org/wiki/Moving_average
"""


def moving_average(data: list[float], window_size: int) -> list[float]:
    """
    Calculate the moving average of a list of numbers given a window size.

    Parameters
    ----------
    data: list[float], the input list of numbers
    window_size: int, the size of the sliding window

    Returns
    -------
    list[float]: list of moving averages for each window position

    >>> moving_average([1, 2, 3, 4, 5], 3)
    [2.0, 3.0, 4.0]
    >>> moving_average([10, 20, 30, 40, 50], 2)
    [15.0, 25.0, 35.0, 45.0]
    >>> moving_average([5], 1)
    [5.0]
    >>> moving_average([1, 2, 3], 1)
    [1.0, 2.0, 3.0]
    >>> moving_average([1, 2, 3], 3)
    [2.0]
    >>> moving_average([], 3)
    Traceback (most recent call last):
        ...
    ValueError: data cannot be empty
    >>> moving_average([1, 2, 3], 0)
    Traceback (most recent call last):
        ...
    ValueError: window_size must be a positive integer
    >>> moving_average([1, 2, 3], 5)
    Traceback (most recent call last):
        ...
    ValueError: window_size cannot be greater than the length of data
    """
    if not data:
        raise ValueError("data cannot be empty")
    if window_size <= 0:
        raise ValueError("window_size must be a positive integer")
    if window_size > len(data):
        raise ValueError("window_size cannot be greater than the length of data")

    result = []
    window_sum = sum(data[:window_size])
    result.append(window_sum / window_size)

    for i in range(window_size, len(data)):
        window_sum += data[i] - data[i - window_size]
        result.append(window_sum / window_size)

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    data = [10, 20, 30, 40, 50, 60, 70]
    window = 3
    print(f"Data: {data}")
    print(f"Window size: {window}")
    print(f"Moving averages: {moving_average(data, window)}")
