from math import sqrt
from typing import Tuple


def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]:
    """
    Given the numerical coefficients a, b and c,
    prints the solutions for a quadratic equation, for a*x*x + b*x + c.

    >>> QuadraticEquation(a=1, b=3, c=-4)
    ('1.0', '-4.0')
    >>> QuadraticEquation(5, 6, 1)
    ('-0.2', '-1.0')
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.")
    delta = b * b - 4 * a * c
    if delta >= 0:
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a))
    """
    Treats cases of Complexes Solutions(i = imaginary unit)
    Ex.: a = 5, b = 2, c = 1
    Solution1 = (- 2 + 4.0 *i)/2 and Solution2 = (- 2 + 4.0 *i)/ 10
    """
    snd = sqrt(-delta)
    if b == 0:
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}"
    b = -abs(b)
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}"


def main():
    solutions = QuadraticEquation(a=5, b=6, c=1)
    print("The equation solutions are: {} and {}".format(*solutions))
    # The equation solutions are: -0.2 and -1.0


if __name__ == "__main__":
    main()
