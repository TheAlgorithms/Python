from __future__ import annotations

from cmath import sqrt


def quadratic_roots(a: int, b: int, c: int) -> tuple[complex, complex]:
    """
    Given the numerical coefficients a, b and c,
    calculates the roots for any quadratic equation of the form ax^2 + bx + c

    >>> quadratic_roots(a=1, b=3, c=-4)
    (1.0, -4.0)
    >>> quadratic_roots(5, 6, 1)
    (-0.2, -1.0)
    >>> quadratic_roots(1, -6, 25)
    ((3+4j), (3-4j))
    """

    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero.")
    delta = b * b - 4 * a * c

    root_1 = (-b + sqrt(delta)) / (2 * a)
    root_2 = (-b - sqrt(delta)) / (2 * a)

    return (
        root_1.real if not root_1.imag else root_1,
        root_2.real if not root_2.imag else root_2,
    )


def main():
    solution1, solution2 = quadratic_roots(a=5, b=6, c=1)
    print(f"The solutions are: {solution1} and {solution2}")


if __name__ == "__main__":
    main()

"""
Quadratic equation root calculator
"""

def roots(a,b,c):

  D = (b*b - 4*a*c) ** 0.5
  x_1 = (-b + D) / (2*a)
  x_2 = (-b - D) /( 2*a)

  print("x1 : {0}" .format(x_1))
  print("x2 : {0}" .format(x_2))

if __name__ == "__main__":
  a = input()
  b = input()
  c = input()

  roots(float(a), float(b), float(c))

  
   
  
