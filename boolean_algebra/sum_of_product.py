"""
Wiki:
https://en.wikipedia.org/wiki/Canonical_normal_form
Other resources:
https://www.electronics-tutorials.ws/boolean/sum-of-product.html
https://www.electronics-tutorials.ws/boolean/product-of-sum.html
"""

from __future__ import annotations


def generate_sum_of_product(variables: list[str], min_terms: list[int]) -> str:
    """
    Generates a Sum of Products (sum_of_product) expression.

    Args:
        variables (list): A list of variables.
        min_terms (list): A list of minterms.

    Returns:
        str: The sum_of_product expression.

    Examples:
        >>> generate_sum_of_product(['A', 'B', 'C'], [0, 1, 3])
        '(A & !B & C) | (A & B & C) | (A & B & !C)'

        >>> generate_sum_of_product(['X', 'Y'], [0, 2])
        '(X & !Y) | (!X & Y)'

    """
    sum_of_product_terms = []

    # Create a function to convert a minterm to a term
    def minterm_to_term(minterm: int) -> str:
        """
        Converts a minterm to a term.

        Args:
            minterm (int): The minterm to be converted.

        Returns:
            str: The term representation of the minterm.

        Examples:
            >>> minterm_to_term(0)
            '!A & !B & !C'

            >>> minterm_to_term(5)
            'A & !B & C'

            >>> minterm_to_term(7)
            'A & B & C'
        """
        term = []
        minterm = int(minterm)  # Convert minterm to an integer
        for i, var in enumerate(variables):
            # Check if the i-th bit of the minterm is 0
            if (minterm >> i) & 1 == 0:
                term.append(f"!{var}")  # Append negated variable if bit is 0
            else:
                term.append(var)  # Append variable if bit is 1
        return " & ".join(term)  # Combine variables with AND operator

    for minterm in min_terms:
        term = minterm_to_term(minterm)
        sum_of_product_terms.append(f"({term})")  # Enclose each term in parentheses

    sum_of_product_expression = " | ".join(
        sum_of_product_terms
    )  # Combine terms with OR operator
    return sum_of_product_expression


def generate_product_of_sum(variables: list[str], max_terms: list[int]) -> str:
    """
    Generates a Product of Sums (product_of_sum) expression.

    Args:
        variables (list): A list of variables.
        max_terms (list): A list of maxterms.

    Returns:
        str: The product_of_sum expression.

    Examples:
        >>> generate_product_of_sum(['A', 'B'], [0, 2])
        '(A | !B) & (!A | B)'

        >>> generate_product_of_sum(['X', 'Y'], [1, 3])
        '(!X & Y) & (X & !Y)'

    """
    product_of_sum_terms = []

    # Create a function to convert a maxterm to a term
    def maxterm_to_term(maxterm: int) -> str:
        """
        Converts a maxterm to a term.

        Args:
            maxterm (int): The maxterm to be converted.

        Returns:
            str: The term representation of the maxterm.

        Examples:
            >>> maxterm_to_term(0)
            'A | B | C'

            >>> maxterm_to_term(3)
            '!A | !B | C'

            >>> maxterm_to_term(5)
            '!A | B | !C'
        """
        term = []
        maxterm = int(maxterm)  # Convert maxterm to an integer
        for i, var in enumerate(variables):
            # Check if the i-th bit of the maxterm is 0
            if (maxterm >> i) & 1 == 0:
                term.append(var)  # Append variable if bit is 0
            else:
                term.append(f"!{var}")  # Append negated variable if bit is 1
        return " | ".join(term)  # Combine variables with OR operator

    for maxterm in max_terms:
        term = maxterm_to_term(maxterm)
        product_of_sum_terms.append(f"({term})")  # Enclose each term in parentheses

    product_of_sum_expression = " & ".join(
        product_of_sum_terms
    )  # Combine terms with AND operator
    return product_of_sum_expression


# Example usage:

input_variables = input("Enter a list of space-separated variables: ").strip()
variables = input_variables.split()
input_minterms = input("Enter a list of space-separated minterms: ").strip()
min_terms = [
    int(term) for term in input_minterms.split()
]  # Convert input to list of integers
input_maxterms = input("Enter a list of space-separated maxterms: ").strip()
max_terms = [
    int(term) for term in input_maxterms.split()
]  # Convert input to list of integers
sum_of_product_expression = generate_sum_of_product(variables, min_terms)
product_of_sum_expression = generate_product_of_sum(variables, max_terms)

print("sum_of_product Expression:", sum_of_product_expression)
print("product_of_sum Expression:", product_of_sum_expression)
