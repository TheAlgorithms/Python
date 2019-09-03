"""
Fast Polynomial Multiplication using radix-2 fast Fourier Transform.

Reference:
https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm#The_radix-2_DIT_case

For polynomials of degree m and n the algorithms has complexity 
O(n*logn + m*logm)

The main part of the algorithm is split in two parts:
    1) __DFT: We compute the discrete fourier transform (DFT) of A and B using a 
    bottom-up dynamic approach - 
    2) __multiply: Once we obtain the DFT of A*B, we can similarly
    invert it to obtain A*B

The class FFT takes two polynomials A and B with complex coefficients as arguments; 
The two polynomials should be represented as a sequence of coefficients starting
from the free term. Thus, for instance x + 2*x^3 could be represented as 
[0,1,0,2] or (0,1,0,2). The constructor adds some zeros at the end so that the 
polynomials have the same length which is a power of 2 at least the length of 
their product. 

The unit tests demonstrate how the class can be used.
"""

import mpmath  # for roots of unity
import numpy as np


class FFT:
    def __init__(self, polyA=[0], polyB=[0]):
        # Input as list
        self.polyA = list(polyA)[:]
        self.polyB = list(polyB)[:]

        # Remove leading zero coefficients
        while self.polyA[-1] == 0:
            self.polyA.pop()
        self.len_A = len(self.polyA)

        while self.polyB[-1] == 0:
            self.polyB.pop()
        self.len_B = len(self.polyB)

        # Add 0 to make lengths equal a power of 2
        self.C_max_length = int(
            2
            ** np.ceil(
                np.log2(
                    len(self.polyA) + len(self.polyB) - 1
                )
            )
        )

        while len(self.polyA) < self.C_max_length:
            self.polyA.append(0)
        while len(self.polyB) < self.C_max_length:
            self.polyB.append(0)
        # A complex root used for the fourier transform
        self.root = complex(
            mpmath.root(x=1, n=self.C_max_length, k=1)
        )

        # The product
        self.product = self.__multiply()

    # Discrete fourier transform of A and B
    def __DFT(self, which):
        if which == "A":
            dft = [[x] for x in self.polyA]
        else:
            dft = [[x] for x in self.polyB]
        # Corner case
        if len(dft) <= 1:
            return dft[0]
        #
        next_ncol = self.C_max_length // 2
        while next_ncol > 0:
            new_dft = [[] for i in range(next_ncol)]
            root = self.root ** next_ncol

            # First half of next step
            current_root = 1
            for j in range(
                self.C_max_length // (next_ncol * 2)
            ):
                for i in range(next_ncol):
                    new_dft[i].append(
                        dft[i][j]
                        + current_root
                        * dft[i + next_ncol][j]
                    )
                current_root *= root
            # Second half of next step
            current_root = 1
            for j in range(
                self.C_max_length // (next_ncol * 2)
            ):
                for i in range(next_ncol):
                    new_dft[i].append(
                        dft[i][j]
                        - current_root
                        * dft[i + next_ncol][j]
                    )
                current_root *= root
            # Update
            dft = new_dft
            next_ncol = next_ncol // 2
        return dft[0]

    # multiply the DFTs of  A and B and find A*B
    def __multiply(self):
        dftA = self.__DFT("A")
        dftB = self.__DFT("B")
        inverseC = [
            [
                dftA[i] * dftB[i]
                for i in range(self.C_max_length)
            ]
        ]
        del dftA
        del dftB

        # Corner Case
        if len(inverseC[0]) <= 1:
            return inverseC[0]
        # Inverse DFT
        next_ncol = 2
        while next_ncol <= self.C_max_length:
            new_inverseC = [[] for i in range(next_ncol)]
            root = self.root ** (next_ncol // 2)
            current_root = 1
            # First half of next step
            for j in range(self.C_max_length // next_ncol):
                for i in range(next_ncol // 2):
                    # Even positions
                    new_inverseC[i].append(
                        (
                            inverseC[i][j]
                            + inverseC[i][
                                j
                                + self.C_max_length
                                // next_ncol
                            ]
                        )
                        / 2
                    )
                    # Odd positions
                    new_inverseC[i + next_ncol // 2].append(
                        (
                            inverseC[i][j]
                            - inverseC[i][
                                j
                                + self.C_max_length
                                // next_ncol
                            ]
                        )
                        / (2 * current_root)
                    )
                current_root *= root
            # Update
            inverseC = new_inverseC
            next_ncol *= 2
        # Unpack
        inverseC = [
            round(x[0].real, 8) + round(x[0].imag, 8) * 1j
            for x in inverseC
        ]

        # Remove leading 0's
        while inverseC[-1] == 0:
            inverseC.pop()
        return inverseC

    # Overwrite __str__ for print(); Shows A, B and A*B
    def __str__(self):
        A = "A = " + " + ".join(
            [
                f"{self.polyA[i]}*x^{i}"
                for i in range(self.len_A)
            ]
        )
        B = "B = " + " + ".join(
            [
                f"{self.polyB[i]}*x^{i}"
                for i in range(self.len_B)
            ]
        )
        C = "A*B = " + " + ".join(
            [
                f"{self.product[i]}*x^{i}"
                for i in range(len(self.product))
            ]
        )

        return A + "\n \n" + B + "\n \n" + C


# Unit tests
if __name__ == "__main__":

    A = [0, 1, 0, 2]  # x+2x^3
    B = (2, 3, 4, 0)  # 2+3x+4x^2
    x = FFT(A, B)
    print(x.product)  # 2x + 3x^2 + 8x^3 + 4x^4 + 6x^5,
    # as [(-0+0j), (2+0j), (3+0j), (8+0j), (6+0j), (8+0j)]
    print(x)
