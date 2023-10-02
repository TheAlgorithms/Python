class Polynomial:
    def __init__(self, coefficients: list) -> None:
        """
        Initialize a polynomial with a list of coefficients.

        Args:
        coefficients (list): Coefficients from the highest order to the constant term.
        """
        self.coefficients = coefficients

    def __str__(self) -> str:
        """
        Return a string representation of the polynomial.

        Returns:
        str: String representation of the polynomial.
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
        """
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result)
