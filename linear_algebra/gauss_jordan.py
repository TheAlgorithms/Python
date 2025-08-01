import numpy as np


def gauss_jordan(
    coefficients: np.ndarray, vertices: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Performs Gauss-Jordan elimination on the system Ax = b to reduce A to its
    Reduced Row Echelon Form (RREF) and transform b accordingly.

    Args:
        coefficients: A 2D NumPy array representing the coefficient matrix A.
        vertices: A column vector (2D NumPy array) representing the RHS b.

    Returns:
        A tuple containing:
            - RREF of matrix A
            - Transformed RHS vector b

    Raises:
        ValueError: If shapes of A and b are incompatible.

    See Also:
        https://en.wikibooks.org/wiki/Linear_Algebra/Gauss-Jordan_Reduction

    Examples:
        >>> import numpy as np
        >>> A = np.array([[1, 2, -1], [2, 4, -2], [3, 6, -3]])
        >>> b = np.array([[1], [2], [3]])
        >>> rref_A, rref_b = gauss_jordan(A, b)
        >>> np.allclose(rref_A, np.array([[1., 2., -1.], [0., 0., 0.], [0., 0., 0.]]))
        True
        >>> np.allclose(rref_b, np.array([[1.], [0.], [0.]]))
        True

    """
    if coefficients.ndim != 2 or vertices.ndim != 2:
        raise ValueError("Both inputs must be 2D arrays.")
    if coefficients.shape[0] != vertices.shape[0]:
        raise ValueError("Number of rows in coefficients and vertices must match.")

    coefficients = coefficients.astype(float).copy()
    vertices = vertices.astype(float).copy()
    rows, cols = coefficients.shape

    for col in range(cols):
        pivot_row = None
        for row in range(col, rows):
            if not np.isclose(coefficients[row, col], 0):
                pivot_row = row
                break

        if pivot_row is None:
            continue

        if pivot_row != col:
            coefficients[[col, pivot_row]] = coefficients[[pivot_row, col]]
            vertices[[col, pivot_row]] = vertices[[pivot_row, col]]

        pivot_val = coefficients[col, col]
        coefficients[col] /= pivot_val
        vertices[col] /= pivot_val

        for row in range(rows):
            if row == col:
                continue
            factor = coefficients[row, col]
            coefficients[row] -= factor * coefficients[col]
            vertices[row] -= factor * vertices[col]

    return coefficients, vertices


if __name__ == "__main__":
    import doctest

    doctest.testmod()
