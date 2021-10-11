"""
Solves linear equations in two variables
Inputs : Co-efficients of x and y in a pair of equations, Dependents
Outputs : Values of x and y
"""

def solve(
    x_coefficient_1: float,
    y_coefficient_1: float,
    dependent_1: float,
    x_coefficient_2: float,
    y_coefficient_2: float,
    dependent_2: float,
) -> list:
    """
    >>> solve(4,5,20,1,2,13)
    [-8.333333333333332, 10.666666666666666]
    """
    import numpy

    coefficients = numpy.array(
        [[x_coefficient_1, y_coefficient_1], [x_coefficient_2, y_coefficient_2]]
    )
    dependents = numpy.array([dependent_1, dependent_2])
    answers = numpy.linalg.solve(coefficients, dependents)
    return list(answers)

if __name__ == "__main__":
  from doctest import testmod

  testmod()
