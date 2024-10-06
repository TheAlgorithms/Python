import numpy as np
from sympy import lambdify, symbols, sympify


def get_inputs() -> tuple:
    """
    Get user input for the function, lower limit, and upper limit.

    Returns:
        tuple: A tuple containing the function as a string, the lower limit (a),
               and the upper limit (b) as floats.

    Example:
        >>> from unittest.mock import patch
        >>> inputs = ['1/(1+x**2)', 1.0, -1.0]
        >>> with patch('builtins.input', side_effect=inputs):
        ...     get_inputs()
        ('1/(1+x**2)', 1.0, -1.0)
    """
    func = input("Enter function with variable as x: ")
    a = float(input("Enter lower limit: "))
    b = float(input("Enter upper limit: "))
    return func, a, b


def safe_function_eval(func_str) -> float:
    """
    Safely evaluates the function by substituting x value using sympy.

    Args:
        func_str (str): Function expression as a string.

    Returns:
        float: The evaluated function result.
    """
    x = symbols("x")
    func_expr = sympify(func_str)

    # Convert the function to a callable lambda function
    lambda_func = lambdify(x, func_expr, modules=["numpy"])
    return lambda_func


def compute_table(func, a, b, acc) -> tuple:
    """
    Compute the table of function values based on the limits and accuracy.

    Args:
        func (str): The mathematical function with the variable 'x' as a string.
        a (float): The lower limit of the integral.
        b (float): The upper limit of the integral.
        acc (int): The number of subdivisions for accuracy.

    Returns:
        tuple: A tuple containing the table of values and the step size (h).

    Example:
        >>> compute_table(
        ...     safe_function_eval('1/(1+x**2)'), 1, -1, 1
        ... )
        (array([0.5       , 0.69230769, 0.9       , 1.        , 0.9       ,
               0.69230769, 0.5       ]), -0.3333333333333333)
    """
    # Weddle's rule requires number of intervals as a multiple of 6 for accuracy
    n_points = acc * 6 + 1
    h = (b - a) / (n_points - 1)
    x_vals = np.linspace(a, b, n_points)

    # Evaluate function values at all points
    table = func(x_vals)
    return table, h


def apply_weights(table) -> list:
    """
    Apply Simpson's rule weights to the values in the table.

    Args:
        table (list): A list of computed function values.

    Returns:
        list: A list of weighted values.

    Example:
        >>> apply_weights([0.0, 0.866, 1.0, 0.866, 0.0, -0.866, -1.0])
        [4.33, 1.0, 5.196, 0.0, -4.33]
    """
    add = []
    for i in range(1, len(table) - 1):
        if i % 2 == 0 and i % 3 != 0:
            add.append(table[i])
        if i % 2 != 0 and i % 3 != 0:
            add.append(5 * table[i])
        elif i % 6 == 0:
            add.append(2 * table[i])
        elif i % 3 == 0 and i % 2 != 0:
            add.append(6 * table[i])
    return add


def compute_solution(add, table, h) -> float:
    """
    Compute the final solution using the weighted values and table.

    Args:
        add (list): A list of weighted values from apply_weights.
        table (list): A list of function values.
        h (float): The step size (h) calculated from the limits and accuracy.

    Returns:
        float: The final computed integral solution.

    Example:
        >>> compute_solution([4.33, 6.0, 0.0, -4.33], [0.0, 0.866, 1.0, 0.866, 0.0,
        ... -0.866, -1.0], 0.5235983333333333)
        0.7853975
    """
    return 0.3 * h * (sum(add) + table[0] + table[-1])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    # func, a, b = get_inputs()
    # acc = 1
    # solution = None

    # while acc <= 100_000:
    #     table, h = compute_table(func, a, b, acc)
    #     add = apply_weights(table)
    #     solution = compute_solution(add, table, h)
    #     acc *= 10

    # print(f'Solution: {solution}')
