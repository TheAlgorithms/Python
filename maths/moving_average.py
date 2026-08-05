from typing import List


def moving_average(values: List[float], window: int) -> List[float]:
    """
    Compute the moving average of a list of numbers with a given window size.

    >>> moving_average([1, 2, 3, 4, 5], 2)
    [1.5, 2.5, 3.5, 4.5]
    >>> moving_average([10, 20, 30], 3)
    [20.0]
    >>> moving_average([1, 2], 3)
    Traceback (most recent call last):
        ...
    ValueError: Window size cannot be larger than list length.
    """
    if window > len(values):
        raise ValueError("Window size cannot be larger than list length.")
    return [
        sum(values[i : i + window]) / window for i in range(len(values) - window + 1)
    ]
