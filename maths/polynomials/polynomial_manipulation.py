from typing import List


class Polynomial:
    def __init__(self, coefficients: List[int]) -> None:
        """
        Initialize a polynomial with a list of coefficients.
        Args:
        coefficients (List[int]): Coefficients from the highest order to constant term.
        """
        self.coefficients = coefficients

    def __str__(self) -> str:
        """
        Return a string representation of the polynomial.
        Returns:
        str: String representation of the polynomial.
        Examples:
        >>> poly = Polynomial([1, 2, 3])
        >>> str(poly)
        '3x^2 + 2x + 1'
        """
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                else:
                    terms.append(f"{coeff}x^{i}")
        return " + ".join(terms[::-1])

    def add(self, other: "Polynomial") -> "Polynomial":
        """
        Add two polynomials.
        Args:
        other (Polynomial): Another Polynomial object to add to this one.
        Returns:
        Polynomial: A new Polynomial representing the sum.
        Examples:
        >>> poly1 = Polynomial([1, 2, 3])
        >>> poly2 = Polynomial([2, 0, 1])
        >>> result = poly1.add(poly2)
        >>> str(result)
        '2x^3 + 3x^2 + 3x + 1'
        """
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len

        for i in range(len(self.coefficients)):
            result[i] += self.coefficients[i]

        for i in range(len(other.coefficients)):
            result[i] += other.coefficients[i]

        return Polynomial(result)

    def multiply(self, other: "Polynomial") -> "Polynomial":
        """
        Multiply two polynomials.
        Args:
        other (Polynomial): Another Polynomial object to multiply with this one.
        Returns:
        Polynomial: A new Polynomial representing the product.
        Examples:
        >>> poly1 = Polynomial([1, 2, 3])
        >>> poly2 = Polynomial([2, 0, 1])
        >>> result = poly1.multiply(poly2)
        >>> str(result)
        '6x^5 + 2x^4 + 3x^3 + x^2'
        """
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All tests passed.")
