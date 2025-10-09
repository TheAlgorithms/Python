"""
Module to analyze homogeneous linear differential equations.

It supports:
    - Second-order equations: a*y'' + b*y' + c*y = 0
    - First-order equations:  b*y' + c*y = 0  (when a = 0)

Features:
    - Computes characteristic roots (for second-order)
    - Derives fundamental solutions
    - Calculates first derivatives
    - Evaluates the Wronskian determinant
    - Tests for linear independence

References:
    https://en.wikipedia.org/wiki/Linear_differential_equation
"""

import cmath
from sympy import symbols, exp, cos, sin, diff, simplify


def compute_characteristic_roots(
    coefficient_a: float, coefficient_b: float, coefficient_c: float
) -> tuple[complex, complex]:
    """
    Compute roots of the characteristic equation:
        a*r^2 + b*r + c = 0

    >>> compute_characteristic_roots(1, -2, 1)
    ((1+0j), (1+0j))
    >>> compute_characteristic_roots(1, 0, 1)
    ((0+1j), (0-1j))
    """
    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    sqrt_discriminant = cmath.sqrt(discriminant)
    root_1 = (-coefficient_b + sqrt_discriminant) / (2 * coefficient_a)
    root_2 = (-coefficient_b - sqrt_discriminant) / (2 * coefficient_a)
    return root_1, root_2


def construct_fundamental_solutions(root_1: complex, root_2: complex):
    """
    Construct fundamental solutions (y1, y2) of a 2nd-order ODE.

    >>> from sympy import symbols, exp
    >>> x = symbols('x')
    >>> r1, r2 = 1, 1
    >>> construct_fundamental_solutions(r1, r2)
    (exp(x), x*exp(x))
    """
    variable_x = symbols("x")

    # Case 1: Real and equal roots
    if root_1 == root_2 and root_1.imag == 0:
        solution_1 = exp(root_1.real * variable_x)
        solution_2 = variable_x * exp(root_1.real * variable_x)

    # Case 2: Real and distinct roots
    elif root_1.imag == 0 and root_2.imag == 0:
        solution_1 = exp(root_1.real * variable_x)
        solution_2 = exp(root_2.real * variable_x)

    # Case 3: Complex conjugate roots (α ± iβ)
    else:
        alpha = root_1.real
        beta = abs(root_1.imag)
        solution_1 = exp(alpha * variable_x) * cos(beta * variable_x)
        solution_2 = exp(alpha * variable_x) * sin(beta * variable_x)

    return solution_1, solution_2


def compute_wronskian(function_1, function_2):
    """
    Compute the Wronskian determinant of two functions.

    >>> from sympy import symbols, exp
    >>> x = symbols('x')
    >>> f1, f2 = exp(x), x*exp(x)
    >>> compute_wronskian(f1, f2)
    exp(2*x)
    """
    variable_x = symbols("x")
    derivative_1 = diff(function_1, variable_x)
    derivative_2 = diff(function_2, variable_x)
    wronskian = simplify(function_1 * derivative_2 - function_2 * derivative_1)
    return wronskian


def solve_first_order_equation(coefficient_b: float, coefficient_c: float) -> None:
    """
    Solve the first-order ODE: b*y' + c*y = 0
    and display its general solution and Wronskian.

    >>> solve_first_order_equation(2, 4)
    """
    variable_x = symbols("x")
    if coefficient_b == 0:
        print("Error: Both a and b cannot be zero. Not a valid differential equation.")
        return

    # Simplified form: y' + (c/b)*y = 0
    constant_k = coefficient_c / coefficient_b
    solution = exp(-constant_k * variable_x)

    derivative_solution = diff(solution, variable_x)
    wronskian = simplify(solution * derivative_solution)

    print("\n--- First-Order Differential Equation ---")
    print(f"Equation: {coefficient_b}*y' + {coefficient_c}*y = 0")
    print(f"Solution: y = C * e^(-({coefficient_c}/{coefficient_b}) * x)")
    print(f"y'(x) = {derivative_solution}")
    print(f"Wronskian (single function): {wronskian}")
    print("Linear independence: Trivial (only one solution).")


def analyze_differential_equation(
    coefficient_a: float, coefficient_b: float, coefficient_c: float
) -> None:
    """
    Determine the type of equation and analyze it accordingly.
    """
    # Case 1: Not a valid DE
    if coefficient_a == 0 and coefficient_b == 0:
        print("Error: Both 'a' and 'b' cannot be zero. Not a valid differential equation.")
        return

    # Case 2: First-order DE
    if coefficient_a == 0:
        solve_first_order_equation(coefficient_b, coefficient_c)
        return

    # Case 3: Second-order DE
    print("\n--- Second-Order Differential Equation ---")
    root_1, root_2 = compute_characteristic_roots(
        coefficient_a, coefficient_b, coefficient_c
    )

    print(f"Characteristic roots: r1 = {root_1}, r2 = {root_2}")

    function_1, function_2 = construct_fundamental_solutions(root_1, root_2)

    variable_x = symbols("x")
    derivative_1 = diff(function_1, variable_x)
    derivative_2 = diff(function_2, variable_x)
    wronskian = compute_wronskian(function_1, function_2)

    print(f"y₁(x) = {function_1}")
    print(f"y₂(x) = {function_2}")
    print(f"y₁'(x) = {derivative_1}")
    print(f"y₂'(x) = {derivative_2}")
    print(f"Wronskian: {wronskian}")

    if wronskian == 0:
        print("The functions are linearly dependent.")
    else:
        print("The functions are linearly independent.")


def main() -> None:
    """
    Entry point of the program.
    """
    print("Enter coefficients for the equation a*y'' + b*y' + c*y = 0")
    try:
        coefficient_a = float(input("a = ").strip())
        coefficient_b = float(input("b = ").strip())
        coefficient_c = float(input("c = ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values for coefficients.")
        return

    analyze_differential_equation(coefficient_a, coefficient_b, coefficient_c)


if __name__ == "__main__":
    main()
