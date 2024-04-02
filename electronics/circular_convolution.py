# https://en.wikipedia.org/wiki/Circular_convolution

"""
Circular convolution, also known as cyclic convolution,
is a special case of periodic convolution, which is the convolution of two
periodic functions that have the same period. Periodic convolution arises,
for example, in the context of the discrete-time Fourier transform (DTFT).
In particular, the DTFT of the product of two discrete sequences is the periodic
convolution of the DTFTs of the individual sequences. And each DTFT is a periodic
summation of a continuous Fourier transform function.

Source: https://en.wikipedia.org/wiki/Circular_convolution
"""

import doctest
from collections import deque

import numpy as np


class CircularConvolution:
    """
    This class stores the first and second signal and performs the circular convolution
    """

    def __init__(self) -> None:
        """
        First signal and second signal are stored as 1-D array
        """

        self.first_signal = [2, 1, 2, -1]
        self.second_signal = [1, 2, 3, 4]

    def circular_convolution(self) -> list[float]:
        """
        This function performs the circular convolution of the first and second signal
        using matrix method

        Usage:
        >>> convolution = CircularConvolution()
        >>> convolution.circular_convolution()
        [10, 10, 6, 14]

        >>> convolution.first_signal = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
        >>> convolution.second_signal = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
        >>> convolution.circular_convolution()
        [5.2, 6.0, 6.48, 6.64, 6.48, 6.0, 5.2, 4.08]

        >>> convolution.first_signal = [-1, 1, 2, -2]
        >>> convolution.second_signal = [0.5, 1, -1, 2, 0.75]
        >>> convolution.circular_convolution()
        [6.25, -3.0, 1.5, -2.0, -2.75]

        >>> convolution.first_signal = [1, -1, 2, 3, -1]
        >>> convolution.second_signal = [1, 2, 3]
        >>> convolution.circular_convolution()
        [8, -2, 3, 4, 11]

        """

        length_first_signal = len(self.first_signal)
        length_second_signal = len(self.second_signal)

        max_length = max(length_first_signal, length_second_signal)

        # create a zero matrix of max_length x max_length
        matrix = [[0] * max_length for i in range(max_length)]

        # fills the smaller signal with zeros to make both signals of same length
        if length_first_signal < length_second_signal:
            self.first_signal += [0] * (max_length - length_first_signal)
        elif length_first_signal > length_second_signal:
            self.second_signal += [0] * (max_length - length_second_signal)

        """
        Fills the matrix in the following way assuming 'x' is the signal of length 4
        [
            [x[0], x[3], x[2], x[1]],
            [x[1], x[0], x[3], x[2]],
            [x[2], x[1], x[0], x[3]],
            [x[3], x[2], x[1], x[0]]
        ]
        """
        for i in range(max_length):
            rotated_signal = deque(self.second_signal)
            rotated_signal.rotate(i)
            for j, item in enumerate(rotated_signal):
                matrix[i][j] += item

        # multiply the matrix with the first signal
        final_signal = np.matmul(np.transpose(matrix), np.transpose(self.first_signal))

        # rounding-off to two decimal places
        return [round(i, 2) for i in final_signal]


if __name__ == "__main__":
    doctest.testmod()
