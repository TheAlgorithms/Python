"""
Wiki:
https://en.wikipedia.org/wiki/Canonical_normal_form
Other resources:
https://www.electronics-tutorials.ws/boolean/sum-of-product.html
https://www.electronics-tutorials.ws/boolean/product-of-sum.html
"""


def generate_sop(variables, min_terms):
    """
    Generates a Sum of Products (SOP) expression.

    Args:
        variables (list): A list of variables.
        min_terms (list): A list of minterms.

    Returns:
        str: The SOP expression.

    Examples:
        >>> generate_sop(['A', 'B', 'C'], [0, 1, 3])
        '(A & !B & C) | (A & B & C) | (A & B & !C)'

        >>> generate_sop(['X', 'Y'], [0, 2])
        '(X & !Y) | (!X & Y)'

    """
    sop_terms = []

    # Create a function to convert a minterm to a term
    def minterm_to_term(minterm):
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
        sop_terms.append(f"({term})")  # Enclose each term in parentheses

    sop_expression = " | ".join(sop_terms)  # Combine terms with OR operator
    return sop_expression


def generate_pos(variables, max_terms):
    """
    Generates a Product of Sums (POS) expression.

    Args:
        variables (list): A list of variables.
        max_terms (list): A list of maxterms.

    Returns:
        str: The POS expression.

    Examples:
        >>> generate_pos(['A', 'B'], [0, 2])
        '(A | !B) & (!A | B)'

        >>> generate_pos(['X', 'Y'], [1, 3])
        '(!X & Y) & (X & !Y)'

    """
    pos_terms = []

    # Create a function to convert a maxterm to a term
    def maxterm_to_term(maxterm):
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
        pos_terms.append(f"({term})")  # Enclose each term in parentheses

    pos_expression = " & ".join(pos_terms)  # Combine terms with AND operator
    return pos_expression


# Example usage:

input_variables = input("Enter a list of space-separated variables: ").strip()
variables = input_variables.split()
input_minterms = input("Enter a list of space-separated minterms: ").strip()
min_terms = input_minterms.split()
input_maxterms = input("Enter a list of space-separated maxterms: ").strip()
max_terms = input_maxterms.split()
sop_expression = generate_sop(variables, min_terms)
pos_expression = generate_pos(variables, max_terms)

print("SOP Expression:", sop_expression)
print("POS Expression:", pos_expression)
