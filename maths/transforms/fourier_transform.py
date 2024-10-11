from typing import List, Union
import numpy as np


def fourier_transform(signal: list[int | float]) -> list[complex]:
    """
    Compute the discrete Fourier transform (DFT) of a signal.

    Args:
        signal (list[int | float]): A list of numerical values representing the input signal.

    Returns:
        list[complex]: The Fourier transform of the input signal as a list of complex numbers.

    Example:
        >>> fourier_transform([1, 2, 3, 4])
        [(10+0j), (-2+2j), (-2+0j), (-2-2j)]

    Note:
        This is a basic implementation of the DFT and can be optimized using FFT for larger datasets.
    """
    n = len(signal)
    result = []
    for k in range(n):
        summation = 0 + 0j
        for t in range(n):
            angle = -2j * np.pi * t * k / n
            summation += signal[t] * np.exp(angle)
        result.append(summation)
    return result


if __name__ == "__main__":
    sample_signal = [1, 2, 3, 4]
    result = fourier_transform(sample_signal)
    print("Fourier Transform of the signal:", result)
