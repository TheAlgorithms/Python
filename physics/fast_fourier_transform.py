"""
# Fast Fourier Transform (FFT) Implementation in Python

This Python script provides a basic demonstration of the Fast Fourier Transform (FFT)
algorithm without the use of external libraries like NumPy.
The FFT is a mathematical algorithm used to transform a signal from the time domain
to the frequency domain, revealing its frequency components.

"""

import math


# Define a function to compute the DFT
def dft(signal):
    n = len(signal)
    dft_result = []

    for k in range(n):
        xk_real, xk_imag = 0, 0
        for b in range(n):
            angle = 2 * math.pi * k * b / n
            xk_real += signal[b] * math.cos(angle)
            xk_imag -= signal[b] * math.sin(angle)
        dft_result.append((xk_real, xk_imag))

    return dft_result


# Sample signal (complex values)
signal = [1, 2, 3, 4]

# Calculate the DFT
dft_result = dft(signal)

# Print the DFT result
for k, (real, imag) in enumerate(dft_result):
    print(f"X({k}) = {real} + {imag}i")
