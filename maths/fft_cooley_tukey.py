"""
Fast Fourier Transform (FFT) using Cooley-Tukey algorithm.

The Fast Fourier Transform is an efficient algorithm to compute the Discrete Fourier
Transform (DFT) and its inverse. The Cooley-Tukey algorithm is a divide-and-conquer
algorithm that recursively breaks down a DFT of any composite size N = N1*N2 into
many smaller DFTs of sizes N1 and N2.

Time Complexity: O(N log N)
Space Complexity: O(N)

Reference: https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
"""

import math
from typing import Optional


def fft_cooley_tukey(signal: list[complex]) -> list[complex]:
    """
    Compute the Fast Fourier Transform using Cooley-Tukey algorithm.

    Args:
        signal: Input signal as a list of complex numbers

    Returns:
        FFT of the input signal

    Examples:
        >>> signal = [1, 2, 3, 4]
        >>> fft_result = fft_cooley_tukey([complex(x) for x in signal])
        >>> len(fft_result)
        4

        >>> signal = [0, 1, 0, -1]
        >>> fft_result = fft_cooley_tukey([complex(x) for x in signal])
        >>> abs(fft_result[1]) > 1.9  # Should be close to 2
        True
    """
    n = len(signal)

    # Base case
    if n <= 1:
        return signal

    # Ensure n is a power of 2 by zero-padding
    if n & (n - 1) != 0:
        next_power_of_2 = 1 << (n - 1).bit_length()
        signal = signal + [0] * (next_power_of_2 - n)
        n = next_power_of_2

    # Divide
    even = fft_cooley_tukey(signal[0::2])
    odd = fft_cooley_tukey(signal[1::2])

    # Combine
    result = [0] * n
    for k in range(n // 2):
        t = odd[k] * complex(
            math.cos(-2 * math.pi * k / n), math.sin(-2 * math.pi * k / n)
        )
        result[k] = even[k] + t
        result[k + n // 2] = even[k] - t

    return result


def ifft_cooley_tukey(fft_signal: list[complex]) -> list[complex]:
    """
    Compute the Inverse Fast Fourier Transform using Cooley-Tukey algorithm.

    Args:
        fft_signal: FFT signal as a list of complex numbers

    Returns:
        Inverse FFT of the input signal

    Examples:
        >>> signal = [1, 2, 3, 4]
        >>> fft_result = fft_cooley_tukey([complex(x) for x in signal])
        >>> ifft_result = ifft_cooley_tukey(fft_result)
        >>> all(abs(ifft_result[i] - signal[i]) < 1e-10 for i in range(len(signal)))
        True
    """
    n = len(fft_signal)

    # Conjugate the input
    conjugated = [x.conjugate() for x in fft_signal]

    # Apply forward FFT
    fft_conjugated = fft_cooley_tukey(conjugated)

    # Conjugate and normalize
    result = [x.conjugate() / n for x in fft_conjugated]

    return result


def fft_magnitude_phase(fft_result: list[complex]) -> tuple[list[float], list[float]]:
    """
    Extract magnitude and phase from FFT result.

    Args:
        fft_result: FFT result as a list of complex numbers

    Returns:
        Tuple of (magnitudes, phases)

    Examples:
        >>> signal = [1, 0, -1, 0]
        >>> fft_result = fft_cooley_tukey([complex(x) for x in signal])
        >>> magnitudes, phases = fft_magnitude_phase(fft_result)
        >>> len(magnitudes) == len(phases)
        True
    """
    magnitudes = [abs(x) for x in fft_result]
    phases = [math.atan2(x.imag, x.real) for x in fft_result]

    return magnitudes, phases


def fft_frequency_bins(sample_rate: float, n_samples: int) -> list[float]:
    """
    Generate frequency bins for FFT result.

    Args:
        sample_rate: Sampling rate in Hz
        n_samples: Number of samples

    Returns:
        List of frequency values in Hz

    Examples:
        >>> bins = fft_frequency_bins(1000, 8)
        >>> len(bins)
        8
        >>> bins[0]
        0.0
    """
    return [i * sample_rate / n_samples for i in range(n_samples)]


if __name__ == "__main__":
    # Example usage
    import matplotlib.pyplot as plt

    # Create a test signal
    sample_rate = 1000
    duration = 1
    t = [i / sample_rate for i in range(int(sample_rate * duration))]

    # Signal with multiple frequencies
    signal = [
        math.sin(2 * math.pi * 50 * x) + 0.5 * math.sin(2 * math.pi * 120 * x)
        for x in t
    ]

    # Apply FFT
    fft_result = fft_cooley_tukey([complex(x) for x in signal])

    # Extract magnitude and phase
    magnitudes, phases = fft_magnitude_phase(fft_result)

    # Generate frequency bins
    frequencies = fft_frequency_bins(sample_rate, len(signal))

    # Plot results
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(t[:100], signal[:100])
    plt.title("Original Signal (first 100 samples)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 2, 2)
    plt.plot(frequencies[: len(frequencies) // 2], magnitudes[: len(magnitudes) // 2])
    plt.title("FFT Magnitude Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.subplot(2, 2, 3)
    plt.plot(frequencies[: len(frequencies) // 2], phases[: len(phases) // 2])
    plt.title("FFT Phase Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")

    # Test inverse FFT
    ifft_result = ifft_cooley_tukey(fft_result)
    reconstructed = [x.real for x in ifft_result]

    plt.subplot(2, 2, 4)
    plt.plot(t[:100], reconstructed[:100])
    plt.title("Reconstructed Signal (first 100 samples)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

    print("FFT implementation completed successfully!")
    peak_frequencies = [
        f
        for f, m in zip(
            frequencies[: len(frequencies) // 2], magnitudes[: len(magnitudes) // 2]
        )
        if m > max(magnitudes[: len(magnitudes) // 2]) * 0.1
    ]
    print(f"Peak frequencies detected: {peak_frequencies}")
