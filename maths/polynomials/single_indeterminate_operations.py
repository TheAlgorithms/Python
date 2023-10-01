import os


class Polynomial:
    """
    A class to represent a polynomial of degree n.
    """

    def __init__(self, degree: int, coefficients: list[float]):
        """
        Initializes a polynomial with the given degree and coefficients.
        """
        self.degree = degree
        self.coefficients = coefficients

    def __eq__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are equal.
        """
        if not isinstance(polynomial_2, Polynomial):
            return False

        if self.degree != polynomial_2.degree:
            return False

        for i in range(self.degree + 1):
            if self.coefficients[i] is not polynomial_2.coefficients[i]:
                return False

        return True

    def __ne__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are not equal.
        """
        return not self.__eq__(polynomial_2)


# Find the path to the current file
for root, _dirs, files in os.walk("."):
    if "single_indeterminate_operations.py" in files:
        file_path = os.path.join(root, "single_indeterminate_operations.py")
        break

# Print the file path
print(file_path)


# Changes made:
# 1. Sort the import statements in alphabetical order.
# 2. Remove the unused `Union` import.
# 3. Replace `List` with `list` for type annotations.
# 4. Use a more descriptive variable name instead of `_` for the unused `dirs` variable.
# 5. Add a space after the `:` in function definitions.
# 6. Remove the extra blank lines between function definitions.
