"""
    Calculates exponential moving average (EMA) on the series of numbers
    Wikipedia Reference: https://en.wikipedia.org/wiki/Exponential_smoothing
    Reference: https://www.investopedia.com/terms/e/ema.asp#toc-what-is-an-exponential-moving-average-ema

    Exponential moving average is used in finance to analyze changes stock prices.
    EMA is used in conjunction with Simple moving average (SMA), EMA reacts to the
    changes in the value quicker than SMA, which is one of the advantages of using EMA.
"""


def exponential_moving_average(series: list[float], window_size: int) -> list[float]:
    """
    Returns the exponential moving average of the given array list
    >>> exponential_moving_average([2, 5, 3, 8.2, 6, 9, 10], 3)
    [2.0, 3.5, 3.25, 5.725, 5.8625, 7.43125, 8.715625]

    :param series: Array of numbers (Time series data)
    :param window_size: Window size for calculating average (window_size > 0)
    :return: Resulting array of exponentially averaged numbers

    Formula:

    st = alpha * xt + (1 - alpha) * st_prev
    alpha = 2/(1 + window_size) - smoothing factor

    Exponential moving average (EMA) is a rule of thumb technique for
    smoothing time series data using the exponential window function.
    """

    if window_size <= 0:
        raise ValueError("window_size must be > 0")
    elif window_size >= len(series):
        raise ValueError("window_size must be < length of series")

    # Resultent array
    exp_averaged_arr: list[float] = []

    # Calculating smoothing factor
    alpha = 2 / (1 + window_size)

    # Exponential average at timestamp t
    st = series[0]

    for t in range(len(series)):
        if t <= window_size:
            # Assigning simple moving average till the window_size for the first time
            # is reached
            st = (st + series[t]) * 0.5
            exp_averaged_arr.append(st)
        else:
            # Calculating exponential moving average based on current timestamp data
            # point and previous exponential average value
            st = (alpha * series[t]) + ((1 - alpha) * st)
            exp_averaged_arr.append(st)

    return exp_averaged_arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    test_series = [2, 5, 3, 8.2, 6, 9, 10]
    test_window_size = 3
    result = exponential_moving_average(test_series, test_window_size)
    print("Test series: ", test_series)
    print("Window size: ", test_window_size)
    print("Result: ", result)
