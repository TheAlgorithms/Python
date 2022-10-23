# https://www.chilimath.com/lessons/advanced-algebra/cramers-rule-with-two-variables
# https://en.wikipedia.org/wiki/Cramer%27s_rule


def calculate_x_and_y(equation1: list[int], equation2: list[int]) -> str:
    """
    Solves the system of linear equation in 2 variables.
    :param: equation1: list of 3 numbers
    :param: equation2: list of 3 numbers
    :return: String of result
    input format : [a1, b1, d1], [a2, b2, d2]
    d --> determinant or determinant_matrix
    dx --> determinant_x or determinant_matrix_x
    dy --> determinant_x or determinant_matrix_y

    >>> calculate_x_and_y([1, 2, 3], [2, 4, 6])
    Traceback (most recent call last):
        ...
    ValueError: Infinite solutions. (Consistent system)
    >>> calculate_x_and_y([1, 2, 3], [2, 4, 7])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    >>> calculate_x_and_y([1, 2, 3], [11, 22])
    Traceback (most recent call last):
        ...
    ValueError: Please enter a valid equation.
    >>> calculate_x_and_y([11, 2, 30], [1, 0, 4])
    'Non-Trivial Solution (Consistent system) x = 4.0, y = -7.0'
    >>> calculate_x_and_y([0, 1, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    >>> calculate_x_and_y([0, 0, 6], [0, 0, 3])
    Traceback (most recent call last):
        ...
    ValueError: Both a & b of two equations can't be zero.
    >>> calculate_x_and_y([4, 7, 1], [1, 2, 0])
    'Non-Trivial Solution (Consistent system) x = 2.0, y = -1.0'
    >>> calculate_x_and_y([1, 2, 3], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Infinite solutions. (Consistent system)
    >>> calculate_x_and_y([2, 3, 0], [5, 1, 0])
    'Trivial solution. (Consistent system) x = 0 and y = 0'
    >>> calculate_x_and_y([0, 4, 50], [2, 0, 26])
    'Non-Trivial Solution (Consistent system) x = 13.0, y = 12.5'
    >>> calculate_x_and_y([0, 4, 50], [0, 3, 99])
    Traceback (most recent call last):
        ...
    ValueError: No solution. (Inconsistent system)
    """

    # Checking if the input is valid
    if not len(equation1) == len(equation2) == 3:
        raise ValueError("Please enter a valid equation.")
    elif equation1[0] == equation1[1] == equation2[0] == equation2[1] == 0:
        raise ValueError("Both a & b of two equations can't be zero.")

    # Extracting the coefficients
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Calculating the determinant of matrix d_matrix, dx_matrix and dy_matrix
    d = a1 * b2 - a2 * b1
    dx = c1 * b2 - c2 * b1
    dy = a1 * c2 - a2 * c1

    # Checking if the system of linear equation has a solution (Using Cramer's rule)
    if d == 0:
        if dx == dy == 0:
            raise ValueError("Infinite solutions. (Consistent system)")
        else:
            raise ValueError("No solution. (Inconsistent system)")
    else:
        if dx == dy == 0:
            return "Trivial solution. (Consistent system) x = 0 and y = 0"
        else:
            x = dx / d
            y = dy / d
            return f"Non-Trivial Solution (Consistent system) x = {x}, y = {y}"
