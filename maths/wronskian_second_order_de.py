"""
wronskian_second_order_de.py
A symbolic and numerical exploration of the Wronskian 
for second-order linear differential equations.

This program:
1. Takes coefficients (a, b, c) for a*y'' + b*y' + c*y = 0.
2. Computes characteristic roots.
3. Classifies the solution type.
4. Constructs the general solution.
5. Demonstrates Wronskian computation.

Author: Venkat Thadi

References: https://tutorial.math.lamar.edu/classes/de/wronskian.aspx
"""

import cmath


def compute_characteristic_roots(
    a: float, b: float, c: float
) -> tuple[complex, complex]:
    """
    Compute characteristic roots for a second-order homogeneous linear DE.
    a, b, c -> coefficients

    >>> compute_characteristic_roots(1, -3, 2)
    (2.0, 1.0)
    >>> compute_characteristic_roots(1, 2, 5)
    ((-1+2j), (-1-2j))
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a second-order equation.")

    discriminant = b**2 - 4 * a * c
    sqrt_disc = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)

    # Simplify if roots are purely real
    if abs(root1.imag) < 1e-12:
        root1 = float(root1.real)
    if abs(root2.imag) < 1e-12:
        root2 = float(root2.real)

    return root1, root2


def classify_solution_type(root1: complex, root2: complex) -> str:
    """
    Classify the nature of the roots.

    >>> classify_solution_type(2, 1)
    'Distinct Real Roots'
    >>> classify_solution_type(1+2j, 1-2j)
    'Complex Conjugate Roots'
    >>> classify_solution_type(3, 3)
    'Repeated Real Roots'
    """
    if isinstance(root1, complex) and isinstance(root2, complex) and root1.imag != 0:
        return "Complex Conjugate Roots"
    elif root1 == root2:
        return "Repeated Real Roots"
    else:
        return "Distinct Real Roots"


from typing import Callable

def compute_wronskian(
    function_1: Callable[[float], float],
    function_2: Callable[[float], float],
    derivative_1: Callable[[float], float],
    derivative_2: Callable[[float], float],
    evaluation_point: float
) -> float:
    """
    Compute the Wronskian of two functions at a given point.

    Parameters:
    function_1 (Callable[[float], float]): The first function f(x).
    function_2 (Callable[[float], float]): The second function g(x).
    derivative_1 (Callable[[float], float]): Derivative of the first function f'(x).
    derivative_2 (Callable[[float], float]): Derivative of the second function g'(x).
    evaluation_point (float): The point x at which to evaluate the Wronskian.

    Returns:
    float: Value of the Wronskian at the given point.
    """
    return function_1(evaluation_point) * derivative_2(evaluation_point) - \
           function_2(evaluation_point) * derivative_1(evaluation_point)


def construct_general_solution(root1: complex, root2: complex) -> str:
    """
    Construct the general solution based on the roots.

    >>> construct_general_solution(2, 1)
    'y(x) = C1 * e^(2x) + C2 * e^(1x)'
    >>> construct_general_solution(3, 3)
    'y(x) = (C1 + C2 * x) * e^(3x)'
    >>> construct_general_solution(-1+2j, -1-2j)
    'y(x) = e^(-1x) * (C1 * cos(2x) + C2 * sin(2x))'
    """
    if isinstance(root1, complex) and root1.imag != 0:
        alpha = round(root1.real, 10)
        beta = round(abs(root1.imag), 10)
        return f"y(x) = e^({alpha:g}x) * (C1 * cos({beta:g}x) + C2 * sin({beta:g}x))"
    elif root1 == root2:
        return f"y(x) = (C1 + C2 * x) * e^({root1:g}x)"
    else:
        return f"y(x) = C1 * e^({root1:g}x) + C2 * e^({root2:g}x)"


def analyze_differential_equation(a: float, b: float, c: float) -> None:
    """
    Analyze the DE and print the roots, type, and general solution.
    a, b, c -> coefficients

    >>> analyze_differential_equation(1, -3, 2)  # doctest: +ELLIPSIS
    Characteristic Roots: (2.0, 1.0)
    Solution Type: Distinct Real Roots
    General Solution: y(x) = C1 * e^(2x) + C2 * e^(1x)
    """
    roots = compute_characteristic_roots(a, b, c)
    root1, root2 = roots
    sol_type = classify_solution_type(root1, root2)
    general_solution = construct_general_solution(root1, root2)

    print(f"Characteristic Roots: ({root1:.1f}, {root2:.1f})")
    print(f"Solution Type: {sol_type}")
    print(f"General Solution: {general_solution}")


def main() -> None:
    """
    Main function to run the second-order differential equation Wronskian analysis.

    Interactive input is expected, so this function is skipped in doctests.
    """
    print("Enter coefficients for the equation a*y'' + b*y' + c*y = 0")

    # Skipping main in doctests because input() cannot be tested directly
    a = float(input("a = ").strip())  # doctest: +SKIP
    b = float(input("b = ").strip())  # doctest: +SKIP
    c = float(input("c = ").strip())  # doctest: +SKIP

    if a == 0:
        print("Invalid input: coefficient 'a' cannot be zero.")
        return

    analyze_differential_equation(a, b, c)


if __name__ == "__main__":
    main()  # doctest: +SKIP

