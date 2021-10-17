"""
Calculating fibonacci numbers using matrix form and repeated squaring.
https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
"""

PRIME = 30011


def matmul(A: list, B: list) -> list:
    """
    >>> matmul([[1, 0], [0, 1]], [[1, 0], [0, 1]])
    [[1, 0], [0, 1]]
    """
    result = list()
    for i in range(len(A)):
        result.append(list())
        for j in range(len(B[0])):
            column = [x[j] for x in B]
            result[i].append(dot(A[i], column))
    return result


def dot(x: list, y: list) -> list:
    """
    >>> dot([1,2,3,4,5], [1,1,1,1,1])
    15
    """
    result = 0
    for xi, yi in zip(x, y):
        result += xi * yi
    return result % PRIME


def square(A: list) -> list:
    """
    >>> square([[1, 0], [0, 1]])
    [[1, 0], [0, 1]]
    """
    return matmul(A, A)


def power(X: list, n: int) -> list:
    """
    >>> power([[1, 0], [0, 1]], 1)
    [[1, 0], [0, 1]]
    >>> power([[1, 0], [0, 1]], 5)
    [[1, 0], [0, 1]]
    >>> power([[1, 0], [0, 1]], 10)
    [[1, 0], [0, 1]]
    """
    if n < 0:
        return X
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return X
    if n % 2 == 0:
        return square(power(X, n / 2))
    if n % 2 != 0:
        return matmul(square(power(X, (n - 1) / 2)), X)


def FibRepSq(n: int):
    """
    >>> FibRepSq(1)
    1
    >>> FibRepSq(5)
    5
    >>> FibRepSq(10)
    55
    """
    if n == 0:
        return 0
    magic_mat = [[1, 1], [1, 0]]
    f1_f0 = [[1], [0]]
    magic_mat = power(magic_mat, n - 1)
    result = matmul(magic_mat, f1_f0)
    return result[0][0]
