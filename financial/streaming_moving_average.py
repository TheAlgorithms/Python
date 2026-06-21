"""This module contains a class that
calculates the moving average in real-time.

Reference
---------
https://en.wikipedia.org/wiki/Moving_average
"""

from collections import deque


class StreamingMovingAverage:
    """Streaming Moving Average calculator that updates
    the average in real-time.

    Attributes
    ----------
    window_size : int
        The size of the moving average window.

    Methods
    -------
    update(new_value: float) -> None
        Update the moving average with a new data point.
    mov_avg() -> float
        Return the current moving average value.

    Raises
    ------
    ValueError
        If the window size is less than 1.


    Examples
    --------
    >>> mov_avg_calculator = StreamingMovingAverage(3)
    >>> mov_avg_calculator.update(10.)
    >>> mov_avg_calculator.update(12.)
    >>> mov_avg_calculator.update(2.)
    >>> mov_avg_calculator.update(1.)
    >>> mov_avg_calculator.mov_avg
    5.0
    >>> mov_avg_calculator = StreamingMovingAverage(5)
    >>> mov_avg_calculator.update(2.)
    >>> mov_avg_calculator.update(3.)
    >>> mov_avg_calculator.mov_avg
    2.5
    """

    def __init__(self, window_size: int) -> None:
        if window_size < 1:
            raise ValueError("Window size must be a positive integer")
        self.window_size = window_size
        self.window: deque[float] = deque(maxlen=window_size)
        self._mov_avg: float = 0.0  # Placeholder for online moving average.

    def update(self, new_value: float) -> None:
        """Update the moving average with a new data point.

        Parameters
        ----------
        new_value : float
            The new data point to update the moving average.

        Raises
        ------
        TypeError
            If the type of new value is not float.
        """
        if not isinstance(new_value, float):
            raise TypeError("Type of new_value must be either float.")
        self.window.append(new_value)
        self._mov_avg = sum(self.window) / len(self.window)

    @property
    def mov_avg(self) -> float:
        """Return the current moving average value."""
        return self._mov_avg


if __name__ == "__main__":
    import doctest
    import random

    doctest.testmod()
    moving_average_calculator = StreamingMovingAverage(window_size=3)
    example_data = [float(random.randint(a=1, b=10)) for _ in range(10)]
    for value in example_data:
        print(f"adding {value=} to streaming data.")
        moving_average_calculator.update(new_value=value)
        print(f"updated moving average={moving_average_calculator.mov_avg}")
