# https://www.chilimath.com/lessons/advanced-algebra/cramers-rule-with-two-variables
# https://en.wikipedia.org/wiki/Cramer%27s_rule


def cramers_rule_2x2(equation1: list[int], equation2: list[int]) -> tuple[float, float]:
    """
    Solves the system of linear equation in 2 variables.
    :param: equation1: list of 3 numbers
    :param: equation2: list of 3 numbers
    :return: String of result
    input format : [a1, b1, d1], [a2, b2, d2]
    determinant = [[a1, b1], [a2, b2]]
    determinant_x = [[d1, b1], [d2, b2]]
    determinant_y = [[a1, d1], [a2, d2]]

    >>> cramers_rule_2x2([2, 3, 0], [5, 1, 0])
    (0.0, 0.0)
    >>> cramers_rule_2x2([0, 4, 50], [2, 0, 26])
    (13.0, 12.5)
    >>> cramers_rule_2x2([11, 2, 30], [1, 0, 4])
    (4.0, -7.0)
    >>> cramers_rule_2x2([4, 7, 1], [1, 2, 0])
    (2.0, -1.0)

    >>> cramers_rule_2x2([1, 2, 3], [2, 4, 6])
    Traceback (most recent call last):
        ...
    ValueError: Infinite solutions. (Consistent system)
    >>> cramers_rule_2x2([1, 2, 3], [2, 4, 7])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    >>> cramers_rule_2x2([1, 2, 3], [11, 22])
    Traceback (most recent call last):
        ...
    ValueError: Please enter a valid equation.
    >>> cramers_rule_2x2([0, 1, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    >>> cramers_rule_2x2([0, 0, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: Both a & b of two equations can't be zero.
    >>> cramers_rule_2x2([1, 2, 3], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Infinite solutions. (Consistent system)
    >>> cramers_rule_2x2([0, 4, 50], [0, 3, 99])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    """

    # Check if the input is valid
    if not len(equation1) == len(equation2) == 3:
        raise ValueError("Please enter a valid equation.")
    if equation1[0] == equation1[1] == equation2[0] == equation2[1] == 0:
        raise ValueError("Both a & b of two equations can't be zero.")

    # Extract the coefficients
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Calculate the determinants of the matrices
    determinant = a1 * b2 - a2 * b1
    determinant_x = c1 * b2 - c2 * b1
    determinant_y = a1 * c2 - a2 * c1

    # Check if the system of linear equations has a solution (using Cramer's rule)
    if determinant == 0:
        if determinant_x == determinant_y == 0:
            raise ValueError("Infinite solutions. (Consistent system)")
        else:
            raise ValueError("No solution. (Inconsistent system)")
    else:
        if determinant_x == determinant_y == 0:
            # Trivial solution (Inconsistent system)
            return (0.0, 0.0)
        else:
            x = determinant_x / determinant
            y = determinant_y / determinant
            # Non-Trivial Solution (Consistent system)
            return (x, y)
