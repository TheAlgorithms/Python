"""
LU Decomposition

Decomposes a square matrix into a lower triangular matrix (L) and an
upper triangular matrix (U) such that A = L * U.

This decomposition is useful for:
- Solving systems of linear equations efficiently
- Computing matrix determinants
- Finding matrix inverses
- Repeated solving with the same coefficient matrix

Reference: https://en.wikipedia.org/wiki/LU_decomposition
"""

Matrix = list[list[float]]


def lu_decomposition(
    matrix: Matrix,
) -> tuple[Matrix, Matrix]:
    """Perform LU decomposition on a square matrix.

    Decomposes the input matrix A into L (lower triangular) and U (upper
    triangular) matrices such that A = L * U. The diagonal of L contains
    all ones (Doolittle algorithm).

    The algorithm proceeds by iterating through each column and computing
    the elements of U and L using the following formulas:

    For U (upper triangular):
        U[k][j] = A[k][j] - sum(L[k][s] * U[s][j] for s in range(k))

    For L (lower triangular):
        L[i][k] = (A[i][k] - sum(L[i][s] * U[s][k] for s in range(k))) / U[k][k]

    Args:
        matrix: A square matrix represented as a list of lists of floats.

    Returns:
        A tuple (L, U) where L is a lower triangular matrix with ones on
        the diagonal, and U is an upper triangular matrix.

    Raises:
        ValueError: If the matrix is not square or if a zero pivot is
            encountered (matrix is singular or requires pivoting).

    Examples:
        >>> l, u = lu_decomposition(
        ...     [[2, 1, 1], [4, 3, 3], [8, 7, 9]]
        ... )  # doctest: +NORMALIZE_WHITESPACE
        >>> l
        [[1.0, 0.0, 0.0], [2.0, 1.0, 0.0], [4.0, 3.0, 1.0]]
        >>> u
        [[2.0, 1.0, 1.0], [0.0, 1.0, 1.0], [0.0, 0.0, 2.0]]

        >>> lu_decomposition([[1, 2], [3, 4]])
        ([[1.0, 0.0], [3.0, 1.0]], [[1.0, 2.0], [0.0, -2.0]])

        >>> lu_decomposition([[4, 3], [6, 3]])
        ([[1.0, 0.0], [1.5, 1.0]], [[4.0, 3.0], [0.0, -1.5]])

        >>> lu_decomposition([[1, 0], [0, 1]])
        ([[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]])

        >>> lu_decomposition([[0, 1], [1, 0]])  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        ValueError: Zero pivot encountered...

        >>> lu_decomposition([[1, 2, 3], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: Matrix must be square.
    """
    n = len(matrix)

    # Validate that the matrix is square
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square.")

    # Convert matrix to float values
    a: list[list[float]] = [[float(val) for val in row] for row in matrix]

    # Initialize L with zeros and set diagonal to 1 (Doolittle algorithm)
    lower: list[list[float]] = [[0.0] * n for _ in range(n)]
    for i in range(n):
        lower[i][i] = 1.0

    # Initialize U with zeros
    upper: list[list[float]] = [[0.0] * n for _ in range(n)]

    for k in range(n):
        # Compute the k-th row of U
        for j in range(k, n):
            sum_val = sum(lower[k][s] * upper[s][j] for s in range(k))
            upper[k][j] = a[k][j] - sum_val

        # Check for zero pivot
        if upper[k][k] == 0:
            raise ValueError(
                "Zero pivot encountered. Matrix may be singular or require pivoting."
            )

        # Compute the k-th column of L
        for i in range(k + 1, n):
            sum_val = sum(lower[i][s] * upper[s][k] for s in range(k))
            lower[i][k] = (a[i][k] - sum_val) / upper[k][k]

    return lower, upper


def solve_with_lu(
    lower: list[list[float]], upper: list[list[float]], b: list[float]
) -> list[float]:
    """Solve a system of linear equations Ax = b using LU decomposition.

    Given the LU decomposition of A (where A = L * U), this function
    solves the system in two steps:

    1. Forward substitution: Solve L * y = b for y
    2. Back substitution: Solve U * x = y for x

    Args:
        lower: The lower triangular matrix L from LU decomposition.
        upper: The upper triangular matrix U from LU decomposition.
        b: The right-hand side vector of the system.

    Returns:
        The solution vector x.

    Examples:
        >>> l, u = lu_decomposition([[2, 1], [1, 3]])
        >>> solve_with_lu(l, u, [5, 7])
        [1.6, 1.8]

        >>> l, u = lu_decomposition([[1, 1, 1], [2, 3, 1], [1, 1, 2]])
        >>> solve_with_lu(l, u, [6, 11, 7])
        [5.0, 0.0, 1.0]
    """
    n = len(b)

    # Forward substitution: solve L * y = b
    y: list[float] = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(lower[i][j] * y[j] for j in range(i))

    # Back substitution: solve U * x = y
    x: list[float] = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(upper[i][j] * x[j] for j in range(i + 1, n))) / upper[i][i]

    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Demonstration: solve a system of equations
    # 2x + y + z = 8
    # 4x + 3y + 3z = 20
    # 8x + 7y + 9z = 46
    A = [[2, 1, 1], [4, 3, 3], [8, 7, 9]]
    b = [8, 20, 46]

    L, U = lu_decomposition(A)
    print("L matrix:")
    for row in L:
        print([f"{val:.2f}" for val in row])

    print("\nU matrix:")
    for row in U:
        print([f"{val:.2f}" for val in row])

    solution = solve_with_lu(L, U, b)
    print(f"\nSolution: x = {[f'{val:.2f}' for val in solution]}")
