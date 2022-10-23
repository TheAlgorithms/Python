def calculate_x_and_y(eq1, eq2):
    """
    Solves the system of linear equation in 2 variables.
    :param: eq1: list of 3 numbers
    :param: eq2: list of 3 numbers
    :return: String of result
    Theory:-
    https://www.mathsisfun.com/algebra/systems-linear-equations-matrices.html
    Cramer's rule for 2x2 matrix:-
    https://www.chilimath.com/lessons/advanced-algebra/cramers-rule-with-two-variables
    a1x + b1y = = d1
    a2x + b2y = = d2
    input format : [a1, b1, d1], [a2, b2, d2]
    d_matrix = [[a1, b1], [a2, b2]]
    d is determinant of matrix d_matrix
    dx_matrix = [[d1, b1], [d2, b2]]
    dx is determinant of matrix dx_matrix
    dy_matrix = [[a1, d1], [a2, d2]]
    dy is determinant of matrix dy_matrix

    >>> calculate_x_and_y([1, 2, 3], [2, 4, 6])
    'Infinite solutions. (Consistent system)'

    >>> calculate_x_and_y([1, 2, 3], [2, 4, 7])
    'No solution. (Inconsistent system)'

    >>> calculate_x_and_y([1, 2, 3], [11, 22])
    Traceback (most recent call last):
        ...
    ValueError: Please enter a valid equation.

    >>> calculate_x_and_y([11, 2, 30], [1, 0, 4])
    'Non-Trivial Solution (Consistent system) x = 4.0, y = -7.0'

    >>> calculate_x_and_y([0, 1, 6], [0, 0, 3])
    'No solution. (Inconsistent system)'

    >>> calculate_x_and_y([0, 0, 6], [0, 0, 3])
    Both a & b of two equations can't be zero.

    >>> calculate_x_and_y([4, 7, 1], [1, 2, 0])
    'Non-Trivial Solution (Consistent system) x = 2.0, y = -1.0'

    >>> calculate_x_and_y([1, 2, 3], [1, 2, 3])
    'Infinite solutions. (Consistent system)'

    >>> calculate_x_and_y([2, 3, 0], [5, 1, 0])
    'Trivial solution. (Consistent system) x = 0 and y = 0'

    >>> calculate_x_and_y([0, 4, 50], [2, 0, 26])
    'Non-Trivial Solution (Consistent system) x = 13.0, y = 12.5'

    >>> calculate_x_and_y([0, 4, 50], [0, 3, 99])
    'No solution. (Inconsistent system)'
    """

    # Checking if the input is valid
    if len(eq1) != 3 or len(eq2) != 3:
        raise ValueError("Please enter a valid equation.")
    elif (eq1[0] == 0 and eq1[1] == 0) and (eq2[0] == 0 and eq2[1] == 0):
        print("Both a & b of two equations can't be zero.")
    else:
        # Extracting the coefficients
        a1, b1, c1 = eq1
        a2, b2, c2 = eq2

        # Calculating the determinant of matrix d_matrix, dx_matrix and dy_matrix
        d = a1 * b2 - a2 * b1
        dx = c1 * b2 - c2 * b1
        dy = a1 * c2 - a2 * c1

        # Checking if the system of linear equation has a solution (Using Cramer's rule)
        if d == 0:
            if dx == 0 and dy == 0:
                return "Infinite solutions. (Consistent system)"
            else:
                return "No solution. (Inconsistent system)"
        else:
            if dx == 0 and dy == 0:
                return f"Trivial solution. (Consistent system) x = {0} and y = {0}"
            else:
                x = dx / d
                y = dy / d
                return f"Non-Trivial Solution (Consistent system) x = {x}, y = {y}"
