"""
Matrix trace calculation.

The trace of a square matrix is the sum of the elements on the main diagonal.
It's an important linear algebra operation with many applications.

Reference: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
"""

import numpy as np
from numpy import float64
from numpy.typing import NDArray


def trace(matrix: NDArray[float64]) -> float:
    """
    Calculate the trace of a square matrix.
    The trace is the sum of the diagonal elements of a square matrix.
    Parameters:
        matrix (NDArray[float64]): A square matrix
    Returns:
        float: The trace of the matrix
    Raises:
        ValueError: If the matrix is not square
    Examples:
    >>> import numpy as np
    >>> matrix = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    >>> trace(matrix)
    5.0
    >>> matrix = np.array([[2.0, -1.0, 3.0], [4.0, 5.0, -2.0], [1.0, 0.0, 7.0]], dtype=float)
    >>> trace(matrix)
    14.0
    >>> matrix = np.array([[5.0]], dtype=float)
    >>> trace(matrix)
    5.0
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")

    return float(np.sum(np.diag(matrix)))


def trace_properties_demo(matrix: NDArray[float64]) -> dict:
    """
    Demonstrate various properties of the trace operation.
    Parameters:
        matrix (NDArray[float64]): A square matrix
    Returns:
        dict: Dictionary containing trace properties and calculations
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")

    n = matrix.shape[0]

    # Calculate trace
    tr = trace(matrix)

    # Calculate transpose trace (should be equal to original)
    tr_transpose = trace(matrix.T)

    # Calculate trace of scalar multiple
    scalar = 2.0
    tr_scalar = trace(scalar * matrix)

    # Create identity matrix for comparison
    identity = np.eye(n, dtype=float64)
    tr_identity = trace(identity)

    return {
        "original_trace": tr,
        "transpose_trace": tr_transpose,
        "scalar_multiple_trace": tr_scalar,
        "scalar_factor": scalar,
        "identity_trace": tr_identity,
        "trace_equals_transpose": abs(tr - tr_transpose) < 1e-10,
        "scalar_property_check": abs(tr_scalar - scalar * tr) < 1e-10,
    }


def test_trace() -> None:
    """
    Test function for matrix trace calculation.

    >>> test_trace()  # self running tests
    """
    # Test 1: 2x2 matrix
    matrix_2x2 = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=float)
    tr_2x2 = trace(matrix_2x2)
    assert abs(tr_2x2 - 5.0) < 1e-10, "2x2 trace calculation failed"

    # Test 2: 3x3 matrix
    matrix_3x3 = np.array(
        [[2.0, -1.0, 3.0], [4.0, 5.0, -2.0], [1.0, 0.0, 7.0]], dtype=float
    )
    tr_3x3 = trace(matrix_3x3)
    assert abs(tr_3x3 - 14.0) < 1e-10, "3x3 trace calculation failed"

    # Test 3: Identity matrix
    identity_4x4 = np.eye(4, dtype=float)
    tr_identity = trace(identity_4x4)
    assert abs(tr_identity - 4.0) < 1e-10, (
        "Identity matrix trace should equal dimension"
    )

    # Test 4: Zero matrix
    zero_matrix = np.zeros((3, 3), dtype=float)
    tr_zero = trace(zero_matrix)
    assert abs(tr_zero) < 1e-10, "Zero matrix should have zero trace"

    # Test 5: Trace properties
    test_matrix = np.array(
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=float
    )
    properties = trace_properties_demo(test_matrix)
    assert properties["trace_equals_transpose"], "Trace should equal transpose trace"
    assert properties["scalar_property_check"], "Scalar multiplication property failed"

    # Test 6: Diagonal matrix
    diagonal_matrix = np.diag([1.0, 2.0, 3.0, 4.0])
    tr_diagonal = trace(diagonal_matrix)
    expected = 1.0 + 2.0 + 3.0 + 4.0
    assert abs(tr_diagonal - expected) < 1e-10, (
        "Diagonal matrix trace should equal sum of diagonal elements"
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_trace()
