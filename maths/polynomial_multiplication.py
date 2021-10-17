"""
Polynomial multiplication using karatsuba's algorithm for large inputs,
and (regular) long multiplications for inputs of length <= 100.
Karatsuba's algorithm is slower for smaller inputs,
so this method achieves much higher speed in all cases.
"""


def multiply(matrix_a: list, matrix_b: list) -> list:
    """
    Inputs: lists of polynomial coefficients.
    Such that the polyomial = x^n * matrix_a[n] + ... + x^1 * matrix_a[1] + matrix_a[0]
    matrix_a: matrix_a[i] is the i'th coefficient of the first polynomial.
    matrix_b: matrix_b[i] is the i'th coefficient of the second polynomial.

    Examples:
    >>> multiply([3.0, 2.0], [-7.0, 1.0])
    [-21.0, -11.0, 2.0]
    >>> multiply([10.0, -1.0, 3.0], [2.0, 1.0])
    [20.0, 8.0, 5.0, 3.0]
    """
    max_degree = (len(matrix_a) - 1) + (len(matrix_b) - 1)
    result = karatsuba(matrix_a, matrix_b)
    result = result[: max_degree + 1]
    return result


def long_multiply(matrix_a: list, matrix_b: list) -> list:
    """
    Polynomial multiplication by regular long multiplication
    """
    result = [0] * len(matrix_a)
    for i, element in enumerate(matrix_b):
        intermediate = [element * x for x in matrix_a]
        intermediate = [0] * i + intermediate
        result = [x + y for x, y in zip(result, intermediate)]
        result.append(0)
    return result


def karatsuba(matrix_a: list, matrix_b: list) -> list:
    """
    Karatsuba's algorithm runs recursively.
    When it reaches a step with length <= 100, it switches to long multiplication.
    https://en.wikipedia.org/wiki/Karatsuba_algorithm
    """
    N = len(matrix_a)
    if N % 2 != 0:
        matrix_a.append(0.0)
        matrix_b.append(0.0)
        N += 1

    if N <= 100:
        return long_multiply(matrix_a, matrix_b)
    else:
        slicer = N // 2
        A0, A1 = matrix_a[:slicer], matrix_a[slicer:]
        B0, B1 = matrix_b[:slicer], matrix_b[slicer:]
        C0 = karatsuba(A0[:], B0[:])
        C2 = karatsuba(A1[:], B1[:])
        matrix_a_sum = [x + y for x, y in zip(A0, A1)]
        matrix_b_sum = [x + y for x, y in zip(B0, B1)]
        intermediate = karatsuba(matrix_a_sum, matrix_b_sum)
        C1 = [x - y - z for x, y, z in zip(intermediate, C0, C2)]
    C0.extend([0] * (N))
    C1 = [0] * (N // 2) + C1
    C1.extend([0] * (N // 2))
    C2 = [0] * N + C2
    result = [x + y + z for x, y, z in zip(C0, C1, C2)]
    return result
