"""
Find the minimum number of multiplications needed to multiply chain of matrices.
Reference: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

The algorithm has interesting real-world applications. Example:
1. Image transformations in Computer Graphics as images are composed of matrix.
2. Solve complex polynomial equations in the field of algebra using least processing
   power.
3. Calculate overall impact of macroeconomic decisions as economic equations involve a
   number of variables.
4. Self-driving car navigation can be made more accurate as matrix multiplication can
   accurately determine position and orientation of obstacles in short time.

Python doctests can be run with the following command:
python -m doctest -v matrix_chain_multiply.py

Given a sequence arr[] that represents chain of 2D matrices such that the dimension of
the ith matrix is arr[i-1]*arr[i].
So suppose arr = [40, 20, 30, 10, 30] means we have 4 matrices of dimensions
40*20, 20*30, 30*10 and 10*30.

matrix_chain_multiply() returns an integer denoting minimum number of multiplications to
multiply the chain.

We do not need to perform actual multiplication here.
We only need to decide the order in which to perform the multiplication.

Hints:
1. Number of multiplications (ie cost) to multiply 2 matrices
of size m*p and p*n is m*p*n.
2. Cost of matrix multiplication is associative ie (M1*M2)*M3 != M1*(M2*M3)
3. Matrix multiplication is not commutative. So, M1*M2 does not mean M2*M1 can be done.
4. To determine the required order, we can try different combinations.
So, this problem has overlapping sub-problems and can be solved using recursion.
We use Dynamic Programming for optimal time complexity.

Example input:
arr = [40, 20, 30, 10, 30]
output: 26000
"""
from collections.abc import Iterator
from contextlib import contextmanager
from functools import cache
from sys import maxsize


def matrix_chain_multiply(arr: list[int]) -> int:
    """
    Find the minimum number of multiplcations required to multiply the chain of matrices

    Args:
        arr: The input array of integers.

    Returns:
        Minimum number of multiplications needed to multiply the chain

    Examples:
        >>> matrix_chain_multiply([1, 2, 3, 4, 3])
        30
        >>> matrix_chain_multiply([10])
        0
        >>> matrix_chain_multiply([10, 20])
        0
        >>> matrix_chain_multiply([19, 2, 19])
        722
        >>> matrix_chain_multiply(list(range(1, 100)))
        323398

        # >>> matrix_chain_multiply(list(range(1, 251)))
        # 2626798
    """
    if len(arr) < 2:
        return 0
    # initialising 2D dp matrix
    n = len(arr)
    dp = [[maxsize for j in range(n)] for i in range(n)]
    # we want minimum cost of multiplication of matrices
    # of dimension (i*k) and (k*j). This cost is arr[i-1]*arr[k]*arr[j].
    for i in range(n - 1, 0, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 0
                continue
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                )

    return dp[1][n - 1]


def matrix_chain_order(dims: list[int]) -> int:
    """
    Source: https://en.wikipedia.org/wiki/Matrix_chain_multiplication
    The dynamic programming solution is faster than cached the recursive solution and
    can handle larger inputs.
    >>> matrix_chain_order([1, 2, 3, 4, 3])
    30
    >>> matrix_chain_order([10])
    0
    >>> matrix_chain_order([10, 20])
    0
    >>> matrix_chain_order([19, 2, 19])
    722
    >>> matrix_chain_order(list(range(1, 100)))
    323398

    # >>> matrix_chain_order(list(range(1, 251)))  # Max before RecursionError is raised
    # 2626798
    """

    @cache
    def a(i: int, j: int) -> int:
        return min(
            (a(i, k) + dims[i] * dims[k] * dims[j] + a(k, j) for k in range(i + 1, j)),
            default=0,
        )

    return a(0, len(dims) - 1)


@contextmanager
def elapsed_time(msg: str) -> Iterator:
    # print(f"Starting: {msg}")
    from time import perf_counter_ns

    start = perf_counter_ns()
    yield
    print(f"Finished: {msg} in {(perf_counter_ns() - start) / 10 ** 9} seconds.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    with elapsed_time("matrix_chain_order"):
        print(f"{matrix_chain_order(list(range(1, 251))) = }")
    with elapsed_time("matrix_chain_multiply"):
        print(f"{matrix_chain_multiply(list(range(1, 251))) = }")
    with elapsed_time("matrix_chain_order"):
        print(f"{matrix_chain_order(list(range(1, 251))) = }")
    with elapsed_time("matrix_chain_multiply"):
        print(f"{matrix_chain_multiply(list(range(1, 251))) = }")
