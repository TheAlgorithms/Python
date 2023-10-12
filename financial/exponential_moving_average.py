"""
    Calculate the exponential moving average (EMA) on the series of numbers.
    Wikipedia Reference: https://en.wikipedia.org/wiki/Exponential_smoothing
    https://www.investopedia.com/terms/e/ema.asp#toc-what-is-an-exponential
    -moving-average-ema

    Exponential moving average is used in finance to analyze changes stock prices.
    EMA is used in conjunction with Simple moving average (SMA), EMA reacts to the
    changes in the value quicker than SMA, which is one of the advantages of using EMA.
"""

from collections.abc import Iterator


def exponential_moving_average(
    series: Iterator[float], window_size: int
) -> Iterator[float]:
    """
    Returns the generator which generates exponential moving average of the given
    series
    >>> list(exponential_moving_average(iter([2, 5, 3, 8.2, 6, 9, 10]), 3))
    [2.0, 3.5, 3.25, 5.725, 5.8625, 7.43125, 8.715625]

    :param series: Generator which generates numbers
    :param window_size: Window size for calculating average (window_size > 0)
    :return: Returns generator of which returns exponentially averaged numbers

    Formula:

    st = alpha * xt + (1 - alpha) * st_prev

    Where,
    st : Exponential moving average at timestamp t
    xt : Datapoint in series at timestamp t
    st_prev : Exponential moving average at timestamp t-1
    alpha : 2/(1 + window_size) - smoothing factor

    Exponential moving average (EMA) is a rule of thumb technique for
    smoothing time series data using the exponential window function.
    """

    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    # Calculating smoothing factor
    alpha = 2 / (1 + window_size)

    # Defining timestamp t
    timestamp = 0

    # Exponential average at timestamp t
    exponential_average = 0.0

    for datapoint in series:
        if timestamp <= window_size:
            # Assigning simple moving average till the window_size for the first time
            # is reached
            exponential_average = (
                float(datapoint)
                if timestamp == 0
                else (exponential_average + datapoint) * 0.5
            )
        else:
            # Calculating exponential moving average based on current timestamp data
            # point and previous exponential average value
            exponential_average = (alpha * datapoint) + (
                (1 - alpha) * exponential_average
            )
        timestamp += 1
        yield exponential_average


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_series = [2, 5, 3, 8.2, 6, 9, 10]
    test_window_size = 3
    result = exponential_moving_average(
        series=iter(test_series), window_size=test_window_size
    )
    print("Test series: ", test_series)
    print("Window size: ", test_window_size)
    print("Result: ", list(result))
