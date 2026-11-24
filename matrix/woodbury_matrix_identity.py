"""
Woodbury Matrix Identity (Rank-k Matrix Inverse Update and Downdate).

Computes (A + U C V)^(-1) = A^(-1) - A^(-1) U (C^(-1) + V A^(-1) U)^(-1) V A^(-1)
given A^(-1), reducing complexity from O(n^3) to O(n^2 k + k^3) when k << n.

https://en.wikipedia.org/wiki/Woodbury_matrix_identity
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray


def _validate_2d(matrix: ArrayLike, name: str) -> NDArray[np.float64]:
    """
    Validate and convert an input to a non-empty 2D float64 NumPy array.

    >>> _validate_2d([[1.0, 2.0], [3.0, 4.0]], "u").shape
    (2, 2)
    >>> _validate_2d([1.0, 2.0], "u")
    Traceback (most recent call last):
        ...
    ValueError: u must be a non-empty 2D array
    """
    array = np.asarray(matrix, dtype=np.float64)
    if array.ndim != 2 or array.shape[0] == 0 or array.shape[1] == 0:
        msg = f"{name} must be a non-empty 2D array"
        raise ValueError(msg)
    return array


def woodbury_inverse(
    a_inv: ArrayLike,
    u_matrix: ArrayLike,
    c_matrix: ArrayLike,
    v_matrix: ArrayLike,
) -> NDArray[np.float64]:
    """
    Compute (A + U C V)^(-1) using the Woodbury matrix identity given A^(-1).

    >>> a = np.array([[2.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
    >>> u = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    >>> c = np.array([[2.0, 0.0], [0.0, 0.5]])
    >>> v = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
    >>> updated_inv = woodbury_inverse(np.linalg.inv(a), u, c, v)
    >>> np.allclose(updated_inv, np.linalg.inv(a + u @ c @ v))
    True
    >>> woodbury_inverse(np.eye(2), np.ones((2, 1)), [[0.0]], np.ones((1, 2)))
    Traceback (most recent call last):
        ...
    ValueError: c_matrix or capacitance matrix is singular
    >>> woodbury_inverse(np.eye(2), np.ones((3, 1)), [[1.0]], np.ones((1, 2)))
    Traceback (most recent call last):
        ...
    ValueError: incompatible matrix dimensions for Woodbury update
    """
    a_inv_arr = _validate_2d(a_inv, "a_inv")
    u_arr = _validate_2d(u_matrix, "u_matrix")
    c_arr = _validate_2d(c_matrix, "c_matrix")
    v_arr = _validate_2d(v_matrix, "v_matrix")

    n_rows, n_cols = a_inv_arr.shape
    k_rows, k_cols = c_arr.shape
    if (
        n_rows != n_cols
        or k_rows != k_cols
        or u_arr.shape != (n_rows, k_rows)
        or v_arr.shape != (k_rows, n_rows)
    ):
        raise ValueError("incompatible matrix dimensions for Woodbury update")

    a_inv_u = a_inv_arr @ u_arr
    v_a_inv = v_arr @ a_inv_arr

    # Solve with the k x k capacitance matrix rather than forming explicit inverses
    # to avoid unnecessary numerical loss when C or K is ill-conditioned.
    try:
        c_inv = np.linalg.inv(c_arr)
        capacitance = c_inv + v_arr @ a_inv_u
        correction_term = np.linalg.solve(capacitance, v_a_inv)
    except np.linalg.LinAlgError as err:
        raise ValueError("c_matrix or capacitance matrix is singular") from err

    return a_inv_arr - a_inv_u @ correction_term


def woodbury_solve(
    a_inv: ArrayLike,
    u_matrix: ArrayLike,
    c_matrix: ArrayLike,
    v_matrix: ArrayLike,
    rhs: ArrayLike,
) -> NDArray[np.float64]:
    """
    Solve (A + U C V) x = rhs in O(n^2 k + k^3) without forming (A + U C V)^(-1).

    >>> a = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
    >>> u = np.array([[1.0], [0.0], [1.0]])
    >>> c = np.array([[0.5]])
    >>> v = np.array([[1.0, 1.0, 0.0]])
    >>> b = np.array([1.0, 2.0, 3.0])
    >>> x = woodbury_solve(np.linalg.inv(a), u, c, v, b)
    >>> np.allclose((a + u @ c @ v) @ x, b)
    True
    >>> woodbury_solve(np.eye(2), np.ones((2, 1)), [[1.0]], np.ones((1, 2)), [1.0])
    Traceback (most recent call last):
        ...
    ValueError: rhs length must match a_inv dimension
    """
    a_inv_arr = _validate_2d(a_inv, "a_inv")
    u_arr = _validate_2d(u_matrix, "u_matrix")
    c_arr = _validate_2d(c_matrix, "c_matrix")
    v_arr = _validate_2d(v_matrix, "v_matrix")
    rhs_arr = np.asarray(rhs, dtype=np.float64)

    n_dim = a_inv_arr.shape[0]
    k_dim = c_arr.shape[0]
    if (
        a_inv_arr.shape != (n_dim, n_dim)
        or c_arr.shape != (k_dim, k_dim)
        or u_arr.shape != (n_dim, k_dim)
        or v_arr.shape != (k_dim, n_dim)
    ):
        raise ValueError("incompatible matrix dimensions for Woodbury solve")
    if rhs_arr.ndim not in (1, 2) or rhs_arr.shape[0] != n_dim:
        raise ValueError("rhs length must match a_inv dimension")

    a_inv_b = a_inv_arr @ rhs_arr
    a_inv_u = a_inv_arr @ u_arr

    try:
        c_inv = np.linalg.inv(c_arr)
        capacitance = c_inv + v_arr @ a_inv_u
        inner = np.linalg.solve(capacitance, v_arr @ a_inv_b)
    except np.linalg.LinAlgError as err:
        raise ValueError("c_matrix or capacitance matrix is singular") from err

    return a_inv_b - a_inv_u @ inner


def rank_one_downdate(
    a_inv: ArrayLike,
    u_vector: ArrayLike,
    v_vector: ArrayLike,
) -> NDArray[np.float64]:
    """
    Compute (A - u v^T)^(-1) given A^(-1) as a rank-1 downdate special case.

    >>> a = np.array([[5.0, 1.0, 0.0], [1.0, 4.0, 1.0], [0.0, 1.0, 3.0]])
    >>> u = np.array([1.0, 0.0, 1.0])
    >>> v = np.array([0.5, 1.0, 0.5])
    >>> downdated = rank_one_downdate(np.linalg.inv(a), u, v)
    >>> np.allclose(downdated, np.linalg.inv(a - np.outer(u, v)))
    True
    >>> rank_one_downdate(np.eye(2), [[1.0, 2.0]], [1.0, 2.0])
    Traceback (most recent call last):
        ...
    ValueError: u_vector and v_vector must be 1D vectors of matching length
    """
    u_arr = np.asarray(u_vector, dtype=np.float64)
    v_arr = np.asarray(v_vector, dtype=np.float64)
    if u_arr.ndim != 1 or v_arr.ndim != 1 or u_arr.shape[0] != v_arr.shape[0]:
        raise ValueError("u_vector and v_vector must be 1D vectors of matching length")

    return woodbury_inverse(
        a_inv,
        u_arr[:, np.newaxis],
        np.array([[-1.0]]),
        v_arr[np.newaxis, :],
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
