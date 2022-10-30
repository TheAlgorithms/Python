"""

This module implements a single indeterminate polynomials class
with some basic operations

Reference: https://en.wikipedia.org/wiki/Polynomial

"""

from __future__ import annotations

from collections.abc import MutableSequence


class Polynomial:
    def __init__(self, degree: int, coefficients: MutableSequence[float]) -> None:
        """
        The coefficients should be in order of degree, from smallest to largest.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p = Polynomial(2, [1, 2, 3, 4])
        Traceback (most recent call last):
        ...
        ValueError: The number of coefficients should be equal to the degree + 1.

        """
        if len(coefficients) != degree + 1:
            raise ValueError(
                "The number of coefficients should be equal to the degree + 1."
            )

        self.coefficients: list[float] = list(coefficients)
        self.degree = degree

    def __add__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial addition
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p + q
        6x^2 + 4x + 2
        """

        if self.degree > polynomial_2.degree:
            coefficients = self.coefficients[:]
            for i in range(polynomial_2.degree + 1):
                coefficients[i] += polynomial_2.coefficients[i]
            return Polynomial(self.degree, coefficients)
        else:
            coefficients = polynomial_2.coefficients[:]
            for i in range(self.degree + 1):
                coefficients[i] += self.coefficients[i]
            return Polynomial(polynomial_2.degree, coefficients)

    def __sub__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial subtraction
        >>> p = Polynomial(2, [1, 2, 4])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p - q
        1x^2
        """
        return self + polynomial_2 * Polynomial(0, [-1])

    def __neg__(self) -> Polynomial:
        """
        Polynomial negation
        >>> p = Polynomial(2, [1, 2, 3])
        >>> -p
         - 3x^2 - 2x - 1
        """
        return Polynomial(self.degree, [-c for c in self.coefficients])

    def __mul__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial multiplication
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p * q
        9x^4 + 12x^3 + 10x^2 + 4x + 1
        """
        coefficients: list[float] = [0] * (self.degree + polynomial_2.degree + 1)
        for i in range(self.degree + 1):
            for j in range(polynomial_2.degree + 1):
                coefficients[i + j] += (
                    self.coefficients[i] * polynomial_2.coefficients[j]
                )

        return Polynomial(self.degree + polynomial_2.degree, coefficients)

    def evaluate(self, substitution: int | float) -> int | float:
        """
        Evaluates the polynomial at x.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.evaluate(2)
        17
        """
        result: int | float = 0
        for i in range(self.degree + 1):
            result += self.coefficients[i] * (substitution**i)
        return result

    def __str__(self) -> str:
        """
        >>> p = Polynomial(2, [1, 2, 3])
        >>> print(p)
        3x^2 + 2x + 1
        """
        polynomial = ""
        for i in range(self.degree, -1, -1):
            if self.coefficients[i] == 0:
                continue
            elif self.coefficients[i] > 0:
                if polynomial:
                    polynomial += " + "
            else:
                polynomial += " - "

            if i == 0:
                polynomial += str(abs(self.coefficients[i]))
            elif i == 1:
                polynomial += str(abs(self.coefficients[i])) + "x"
            else:
                polynomial += str(abs(self.coefficients[i])) + "x^" + str(i)

        return polynomial

    def __repr__(self) -> str:
        """
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p
        3x^2 + 2x + 1
        """
        return self.__str__()

    def derivative(self) -> Polynomial:
        """
        Returns the derivative of the polynomial.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.derivative()
        6x + 2
        """
        coefficients: list[float] = [0] * self.degree
        for i in range(self.degree):
            coefficients[i] = self.coefficients[i + 1] * (i + 1)
        return Polynomial(self.degree - 1, coefficients)

    def integral(self, constant: int | float = 0) -> Polynomial:
        """
        Returns the integral of the polynomial.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.integral()
        1.0x^3 + 1.0x^2 + 1.0x
        """
        coefficients: list[float] = [0] * (self.degree + 2)
        coefficients[0] = constant
        for i in range(self.degree + 1):
            coefficients[i + 1] = self.coefficients[i] / (i + 1)
        return Polynomial(self.degree + 1, coefficients)

    def __eq__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are equal.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p == q
        True
        """
        if not isinstance(polynomial_2, Polynomial):
            return False

        if self.degree != polynomial_2.degree:
            return False

        for i in range(self.degree + 1):
            if self.coefficients[i] != polynomial_2.coefficients[i]:
                return False

        return True

    def __ne__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are not equal.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p != q
        False
        """
        return not self.__eq__(polynomial_2)
