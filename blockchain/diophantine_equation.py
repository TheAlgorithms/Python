from __future__ import annotations
from maths.greatest_common_divisor import greatest_common_divisor
from typing import List, Tuple

def diophantine(a: int, b: int, c: int) -> Tuple[float, float]:
    """
    Diophantine Equation : Given integers a,b,c ( at least one of a and b != 0), the
    diophantine equation a*x + b*y = c has a solution (where x and y are integers)
    iff greatest_common_divisor(a,b) divides c.
    """
    # Replaced assertion with a specific exception for better error handling
    if c % greatest_common_divisor(a, b) != 0:
        raise ValueError("No solutions exist")

    (d, x, y) = extended_gcd(a, b)
    r = c / d
    return (r * x, r * y)

def diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> List[Tuple[float, float]]:
    """
    Finding All solutions of Diophantine Equations.
    """
    # Storing the GCD in a variable to avoid duplicate calls
    gcd = greatest_common_divisor(a, b)

    # Initialize an empty list to store the solutions
    solutions = []

    (x0, y0) = diophantine(a, b, c)
    p = a // gcd
    q = b // gcd

    # Populate the solutions list instead of printing
    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        solutions.append((x, y))

    # Return the list of solutions
    return solutions

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclid's Algorithm.
    """
    if b == 0:
        return a, 1, 0

    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

    return (d, x, y)

if __name__ == "__main__":
    from doctest import testmod

    testmod(name="diophantine", verbose=True)
    testmod(name="diophantine_all_soln", verbose=True)
    testmod(name="extended_gcd", verbose=True)
    # Assuming the greatest_common_divisor tests are in the same file
    testmod(name="greatest_common_divisor", verbose=True)
