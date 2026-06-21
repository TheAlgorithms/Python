"""
Fast Fourier Transform (FFT) using Divide and Conquer

The Fast Fourier Transform is a divide-and-conquer algorithm that computes the
Discrete Fourier Transform (DFT) of a sequence in O(n log n) time, compared to
O(n²) for the naive DFT computation.

The algorithm works by:
1. Recursively dividing the DFT computation into smaller subproblems
2. Using the symmetry and periodicity properties of complex exponentials
3. Combining results using the "butterfly" operation

Key mathematical insight:
- DFT of even-indexed elements and odd-indexed elements can be computed separately
- Results are combined using complex exponentials (twiddle factors)

Time complexity: O(n log n)
Space complexity: O(n log n) due to recursion

References:
- https://en.wikipedia.org/wiki/Fast_Fourier_transform
- Cooley-Tukey FFT algorithm (1965)
"""

from __future__ import annotations

import cmath
from collections.abc import Sequence


def fft(x: Sequence[float | complex]) -> list[complex]:
    """
    Compute the Fast Fourier Transform of a sequence using divide and conquer.

    This implementation uses the Cooley-Tukey algorithm, which recursively
    divides the DFT computation into smaller subproblems.

    Args:
        x: Input sequence (list of real or complex numbers)

    Returns:
        List of complex numbers representing the DFT of the input sequence

    Raises:
        ValueError: If input length is not a power of 2

    Examples:
    >>> import math
    >>> # Test with delta function [1, 0, 0, 0] -> constant spectrum [1, 1, 1, 1]
    >>> result = fft([1, 0, 0, 0])
    >>> all(abs(abs(x) - 1) < 1e-10 for x in result)  # All should have magnitude 1
    True

    >>> # Test with impulse at second position
    >>> result = fft([0, 1, 0, 0])
    >>> all(abs(abs(x) - 1) < 1e-10 for x in result)  # All should have magnitude 1
    True

    >>> # Test with real sine wave
    >>> n = 8
    >>> signal = [math.sin(2 * math.pi * k / n) for k in range(n)]
    >>> result = fft(signal)
    >>> len(result) == n
    True
    """
    n = len(x)

    # Check if length is power of 2
    if n <= 0 or (n & (n - 1)) != 0:
        raise ValueError("Input length must be a power of 2")

    # Base case
    if n == 1:
        return [complex(x[0])]

    # Divide: separate even and odd indexed elements
    even = [x[i] for i in range(0, n, 2)]
    odd = [x[i] for i in range(1, n, 2)]

    # Conquer: recursively compute FFT of even and odd parts
    fft_even = fft(even)
    fft_odd = fft(odd)

    # Combine: merge the results using butterfly operation
    result = [complex(0)] * n
    for k in range(n // 2):
        # Twiddle factor: e^(-2πik/n)
        twiddle = cmath.exp(-2j * cmath.pi * k / n)

        # Butterfly operation
        butterfly = twiddle * fft_odd[k]
        result[k] = fft_even[k] + butterfly
        result[k + n // 2] = fft_even[k] - butterfly

    return result


def ifft(x: Sequence[complex]) -> list[complex]:
    """
    Compute the Inverse Fast Fourier Transform using divide and conquer.

    The IFFT is computed by taking the conjugate of the input, applying FFT,
    taking conjugate again, and scaling by 1/n.

    Args:
        x: Input sequence (list of complex numbers)

    Returns:
        List of complex numbers representing the IFFT of the input sequence

    Examples:
    >>> # Test round-trip: FFT followed by IFFT should give original signal
    >>> original = [1, 2, 3, 4]
    >>> recovered = ifft(fft(original))
    >>> all(abs(recovered[i] - original[i]) < 1e-10 for i in range(len(original)))
    True

    >>> # Test with complex input
    >>> original = [1+2j, 3-1j, 0+0j, 2+3j]
    >>> recovered = ifft(fft(original))
    >>> all(abs(recovered[i] - original[i]) < 1e-10 for i in range(len(original)))
    True
    """
    n = len(x)

    # Conjugate input
    x_conj = [complex(val.real, -val.imag) for val in x]

    # Apply FFT
    result = fft(x_conj)

    # Conjugate result and scale by 1/n
    return [complex(val.real / n, -val.imag / n) for val in result]


def dft_naive(x: Sequence[float | complex]) -> list[complex]:
    """
    Compute the Discrete Fourier Transform using the naive O(n²) algorithm.

    This is provided for comparison and testing purposes.

    Args:
        x: Input sequence (list of real or complex numbers)

    Returns:
        List of complex numbers representing the DFT of the input sequence

    Examples:
    >>> # Compare with FFT result
    >>> signal = [1, 2, 3, 4]
    >>> fft_result = fft(signal)
    >>> dft_result = dft_naive(signal)
    >>> all(abs(fft_result[i] - dft_result[i]) < 1e-10 for i in range(len(signal)))
    True
    """
    n = len(x)
    result = []

    for k in range(n):
        sum_val = complex(0)
        for j in range(n):
            # Compute e^(-2πijk/n)
            angle = -2 * cmath.pi * j * k / n
            sum_val += x[j] * cmath.exp(1j * angle)
        result.append(sum_val)

    return result


def pad_to_power_of_2(x: Sequence[float | complex]) -> list[float | complex]:
    """
    Pad input sequence with zeros to make its length a power of 2.

    Args:
        x: Input sequence

    Returns:
        Padded sequence with length as power of 2

    Examples:
    >>> pad_to_power_of_2([1, 2, 3])
    [1, 2, 3, 0]
    >>> pad_to_power_of_2([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5, 0, 0, 0]
    """
    n = len(x)
    if n <= 0:
        return list(x)

    # Find next power of 2
    next_power = 1
    while next_power < n:
        next_power *= 2

    # Pad with zeros
    return list(x) + [0] * (next_power - n)


def fft_magnitude_spectrum(x: Sequence[float | complex]) -> list[float]:
    """
    Compute the magnitude spectrum of a signal using FFT.

    Args:
        x: Input signal

    Returns:
        List of magnitudes of the FFT coefficients

    Examples:
    >>> # Test with a simple signal
    >>> signal = [1, 0, 1, 0]
    >>> spectrum = fft_magnitude_spectrum(signal)
    >>> len(spectrum) == len(signal)
    True
    >>> all(mag >= 0 for mag in spectrum)  # All magnitudes should be non-negative
    True
    """
    # Pad to power of 2 if necessary
    if len(x) & (len(x) - 1) != 0:
        x = pad_to_power_of_2(x)

    # Compute FFT
    fft_result = fft(x)

    # Return magnitudes
    return [abs(val) for val in fft_result]


def convolution_fft(a: Sequence[float], b: Sequence[float]) -> list[float]:
    """
    Compute convolution of two sequences using FFT.

    Convolution in time domain equals pointwise multiplication in frequency domain.
    This provides an O(n log n) alternative to the naive O(n²) convolution.

    Args:
        a: First sequence
        b: Second sequence

    Returns:
        Convolution of a and b

    Examples:
    >>> # Test convolution property
    >>> a = [1, 2, 3]
    >>> b = [1, 1]
    >>> result = convolution_fft(a, b)
    >>> len(result) >= len(a) + len(b) - 1
    True
    """
    if not a or not b:
        return []

    # Result length should be len(a) + len(b) - 1
    result_len = len(a) + len(b) - 1

    # Pad both sequences to the same power of 2 length
    padded_len = 1
    while padded_len < result_len:
        padded_len *= 2

    a_padded = list(a) + [0] * (padded_len - len(a))
    b_padded = list(b) + [0] * (padded_len - len(b))

    # Compute FFT of both sequences
    fft_a = fft(a_padded)
    fft_b = fft(b_padded)

    # Pointwise multiplication in frequency domain
    fft_product = [fft_a[i] * fft_b[i] for i in range(len(fft_a))]

    # Inverse FFT to get convolution result
    conv_result = ifft(fft_product)

    # Return only the valid part (real parts, since convolution of real signals is real)
    return [val.real for val in conv_result[:result_len]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage and demonstration
    print("Fast Fourier Transform Demonstration")
    print("=" * 40)

    # Example 1: Simple signal
    print("\n1. Simple 4-point signal:")
    signal = [1, 2, 3, 4]
    print(f"Input: {signal}")

    fft_result = fft(signal)
    print("FFT result:")
    for i, val in enumerate(fft_result):
        print(f"  X[{i}] = {val:.3f}")

    # Verify with naive DFT
    dft_result = dft_naive(signal)
    matches_dft = all(
        abs(fft_result[i] - dft_result[i]) < 1e-10 for i in range(len(signal))
    )
    print(f"\nVerification - FFT matches DFT: {matches_dft}")

    # Test round-trip
    recovered = ifft(fft_result)
    print(f"Round-trip test (IFFT of FFT): {[f'{val.real:.3f}' for val in recovered]}")

    # Example 2: Magnitude spectrum
    print("\n2. Magnitude spectrum:")
    spectrum = fft_magnitude_spectrum(signal)
    print(f"Magnitudes: {[f'{mag:.3f}' for mag in spectrum]}")

    # Example 3: Convolution using FFT
    print("\n3. Convolution using FFT:")
    a = [1, 2, 3]
    b = [1, 1, 1]
    conv_result = convolution_fft(a, b)
    print(f"Convolution of {a} and {b}: {[f'{val:.3f}' for val in conv_result]}")
