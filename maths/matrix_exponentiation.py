"""Matrix Exponentiation"""

import timeit

"""
Matrix Exponentiation is a technique to solve linear recurrences in logarithmic time.
You read more about it here:
https://zobayer.blogspot.com/2010/11/matrix-exponentiation.html
https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/
"""


class Matrix:
    def __init__(self, arg):
        if isinstance(arg, list):  # Initializes a matrix identical to the one provided.
            self.t = arg
            self.n = len(arg)
        else:  # Initializes a square matrix of the given size and set values to zero.
            self.n = arg
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def __mul__(self, b):
        matrix = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j]
        return matrix


def modular_exponentiation(a, b):
    matrix = Matrix([[1, 0], [0, 1]])
    while b > 0:
        if b & 1:
            matrix *= a
        a *= a
        b >>= 1
    return matrix


def fibonacci_with_matrix_exponentiation(n, f1, f2):
    """
    Returns the nth number of the Fibonacci sequence that
    starts with f1 and f2
    Uses the matrix exponentiation
    >>> fibonacci_with_matrix_exponentiation(1, 5, 6)
    5
    >>> fibonacci_with_matrix_exponentiation(2, 10, 11)
    11
    >>> fibonacci_with_matrix_exponentiation(13, 0, 1)
    144
    >>> fibonacci_with_matrix_exponentiation(10, 5, 9)
    411
    >>> fibonacci_with_matrix_exponentiation(9, 2, 3)
    89
    """
    # Trivial Cases
    if n == 1:
        return f1
    elif n == 2:
        return f2
    matrix = Matrix([[1, 1], [1, 0]])
    matrix = modular_exponentiation(matrix, n - 2)
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1]


def simple_fibonacci(n, f1, f2):
    """
    Returns the nth number of the Fibonacci sequence that
    starts with f1 and f2
    Uses the definition
    >>> simple_fibonacci(1, 5, 6)
    5
    >>> simple_fibonacci(2, 10, 11)
    11
    >>> simple_fibonacci(13, 0, 1)
    144
    >>> simple_fibonacci(10, 5, 9)
    411
    >>> simple_fibonacci(9, 2, 3)
    89
    """
    # Trivial Cases
    if n == 1:
        return f1
    elif n == 2:
        return f2

    n -= 2

    while n > 0:
        f2, f1 = f1 + f2, f2
        n -= 1

    return f2


def matrix_exponentiation_time():
    setup = """
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
"""
    code = "fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)"
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100)
    print("With matrix exponentiation the average execution time is ", exec_time / 100)
    return exec_time


def simple_fibonacci_time():
    setup = """
from random import randint
from __main__ import simple_fibonacci
"""
    code = "simple_fibonacci(randint(1,70000), 1, 1)"
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100)
    print(
        "Without matrix exponentiation the average execution time is ", exec_time / 100
    )
    return exec_time


def main():
    matrix_exponentiation_time()
    simple_fibonacci_time()


if __name__ == "__main__":
    main()
