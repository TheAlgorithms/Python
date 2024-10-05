from math import *


def get_inputs():
    """
    Get user input for the function, lower limit, and upper limit.

    Returns:
        tuple: A tuple containing the function as a string, the lower limit (a), and the upper limit (b) as floats.

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


def compute_table(func, a, b, acc):
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
        >>> compute_table('1/(1+x**2)', 1, -1, 1)
        ([0.5, 0.4235294117647058, 0.36, 0.3076923076923077, 0.26470588235294124, 0.22929936305732482, 0.2], -0.3333333333333333)
    """
    h = (b - a) / (acc * 6)
    table = [0 for _ in range(acc * 6 + 1)]
    for j in range(acc * 6 + 1):
        x = a + j / (acc * 6)
        table[j] = eval(func)
    return table, h


def apply_weights(table):
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


def compute_solution(add, table, h):
    """
    Compute the final solution using the weighted values and table.

    Args:
        add (list): A list of weighted values from apply_weights.
        table (list): A list of function values.
        h (float): The step size (h) calculated from the limits and accuracy.

    Returns:
        float: The final computed integral solution.

    Example:
        >>> compute_solution([4.33, 6.0, 0.0, -4.33], [0.0, 0.866, 1.0, 0.866, 0.0, -0.866, -1.0], 0.5235983333333333)
        0.7853975
    """
    return 0.3 * h * (sum(add) + table[0] + table[-1])


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    
    func, a, b = get_inputs()
    acc = 1
    solution = None

    while acc <= 100000:
        table, h = compute_table(func, a, b, acc)
        add = apply_weights(table)
        solution = compute_solution(add, table, h)
        acc *= 10

    print(f'Solution: {solution}')