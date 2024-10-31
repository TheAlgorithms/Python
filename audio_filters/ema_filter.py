"""
By @Shreya123714

https://en.wikipedia.org/wiki/Moving_average
"""

import numpy as np


class EMAFilter:
    """
    A class for applying an Exponential Moving Average (EMA) filter
    to audio data.

    Attributes:
        alpha (float): Smoothing factor where 0 < alpha <= 1.
        ema_value (float): Stores the most recent EMA value
        for the ongoing calculation.
    """

    def __init__(self, alpha: float) -> None:
        """
        Initialize the Exponential Moving Average (EMA) filter.

        Parameters:
        alpha (float): Smoothing factor where 0 < alpha <= 1.

        Raises:
            ValueError: If alpha is not within the range (0, 1].
        """
        if not (0 < alpha <= 1):
            raise ValueError("Alpha must be between 0 and 1.")
        self.alpha = alpha
        self.ema_value = 0.0

    def apply(self, audio_signal: list[float]) -> np.ndarray:
        """
        Apply the EMA filter to a sequence of
        audio signal values.

        Parameters:
        audio_signal (list[float]): List of numerical values
        representing the audio signal.

        Returns:
        np.ndarray: Array containing the smoothed audio signal.

        Example:
        >>> ema_filter = EMAFilter(0.2)
        >>> np.allclose(ema_filter.apply([0.1, 0.5, 0.8, 0.6, 0.3, 0.9, 0.4]),
        ...             [0.1, 0.18, 0.304, 0.3632, 0.35056, 0.460448, 0.4483584],
        ...              rtol=1e-5, atol=1e-8)
        True
        """
        if not audio_signal:
            return np.array([])

        ema_signal: list[float] = []
        self.ema_value = audio_signal[0]
        ema_signal.append(self.ema_value)

        for sample in audio_signal[1:]:
            if self.ema_value is None:
                self.ema_value = self.alpha * sample + (1 - self.alpha) * self.ema_value
                ema_signal.append(self.ema_value)
        return np.array(ema_signal)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
