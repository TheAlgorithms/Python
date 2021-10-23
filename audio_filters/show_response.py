from math import pi
from typing import Protocol

import matplotlib.pyplot as plt
import numpy as np


class FilterType(Protocol):
    def process(self, sample: float) -> float:
        """
        Calculate y[n]

        >>> issubclass(FilterType, Protocol)
        True
        """
        return 0.0


def show_frequency_response(filter: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> show_frequency_response(filt, 48000)
    """

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter.process(item) for item in inputs]

    filler = [0] * (samplerate - size)  # zero-padding
    outputs += filler
    fft_out = np.abs(np.fft.fft(outputs))
    fft_db = 20 * np.log10(fft_out)

    # Frequencies on log scale from 24 to nyquist frequency
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    # Display within reasonable bounds
    lowest = min([-20, np.min(fft_db[1 : samplerate // 2 - 1])])
    highest = max([20, np.max(fft_db[1 : samplerate // 2 - 1])])
    plt.ylim(max([-80, lowest]), min([80, highest]))
    plt.ylabel("Gain (dB)")

    plt.plot(fft_db)
    plt.show()


def show_phase_response(filter: FilterType, samplerate: int) -> None:
    """
    Show phase response of a filter

    >>> from audio_filters.iir_filter import IIRFilter
    >>> filt = IIRFilter(4)
    >>> show_phase_response(filt, 48000)
    """

    size = 512
    inputs = [1] + [0] * (size - 1)
    outputs = [filter.process(item) for item in inputs]

    filler = [0] * (samplerate - size)  # zero-padding
    outputs += filler
    fft_out = np.angle(np.fft.fft(outputs))

    # Frequencies on log scale from 24 to nyquist frequency
    plt.xlim(24, samplerate / 2 - 1)
    plt.xlabel("Frequency (Hz)")
    plt.xscale("log")

    plt.ylim(-2 * pi, 2 * pi)
    plt.ylabel("Phase shift (Radians)")
    plt.plot(np.unwrap(fft_out, -2 * pi))
    plt.show()
