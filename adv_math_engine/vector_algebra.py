"""Vector algebra primitives.

Formulas:
- Dot product: a·b = Σ a_i b_i
- Projection of a onto b: proj_b(a) = ((a·b)/||b||^2) b
- Angle: θ = arccos((a·b)/(||a|| ||b||))
"""

from __future__ import annotations

import numpy as np

from adv_math_engine.utils import as_float_array


def dot_product(a: np.ndarray | list[float], b: np.ndarray | list[float]) -> np.ndarray:
    """Compute dot product, supporting vectorized leading dimensions."""
    a_arr = as_float_array(a)
    b_arr = as_float_array(b)
    if a_arr.shape[-1] != b_arr.shape[-1]:
        msg = "Dot product requires matching trailing dimensions."
        raise ValueError(msg)
    return np.sum(a_arr * b_arr, axis=-1)


def cross_product(a: np.ndarray | list[float], b: np.ndarray | list[float]) -> np.ndarray:
    """Compute 3D cross product for (..., 3) vectors."""
    a_arr = as_float_array(a)
    b_arr = as_float_array(b)
    if a_arr.shape[-1] != 3 or b_arr.shape[-1] != 3:
        msg = "Cross product is defined only for 3D vectors."
        raise ValueError(msg)
    return np.cross(a_arr, b_arr)


def vector_projection(a: np.ndarray | list[float], b: np.ndarray | list[float]) -> np.ndarray:
    """Project vector a onto vector b."""
    a_arr = as_float_array(a)
    b_arr = as_float_array(b)
    denom = np.sum(b_arr * b_arr, axis=-1, keepdims=True)
    if np.any(np.isclose(denom, 0.0)):
        msg = "Projection onto zero vector is undefined."
        raise ValueError(msg)
    scale = np.sum(a_arr * b_arr, axis=-1, keepdims=True) / denom
    return scale * b_arr


def angle_between(a: np.ndarray | list[float], b: np.ndarray | list[float]) -> np.ndarray:
    """Return the angle(s) between vectors in radians."""
    a_arr = as_float_array(a)
    b_arr = as_float_array(b)
    a_norm = np.linalg.norm(a_arr, axis=-1)
    b_norm = np.linalg.norm(b_arr, axis=-1)
    if np.any(np.isclose(a_norm, 0.0)) or np.any(np.isclose(b_norm, 0.0)):
        msg = "Angle with zero vector is undefined."
        raise ValueError(msg)
    cosine = dot_product(a_arr, b_arr) / (a_norm * b_norm)
    return np.arccos(np.clip(cosine, -1.0, 1.0))


def gram_schmidt(vectors: np.ndarray | list[list[float]], tol: float = 1e-12) -> np.ndarray:
    """Return an orthonormal basis via Gram-Schmidt."""
    matrix = as_float_array(vectors)
    if matrix.ndim != 2:
        msg = "Gram-Schmidt expects a 2D array (n_vectors, dimension)."
        raise ValueError(msg)
    orthonormal: list[np.ndarray] = []
    for vec in matrix:
        work = vec.copy()
        for basis in orthonormal:
            work = work - np.dot(work, basis) * basis
        norm = np.linalg.norm(work)
        if norm > tol:
            orthonormal.append(work / norm)
    if not orthonormal:
        msg = "No non-zero independent vectors were provided."
        raise ValueError(msg)
    return np.vstack(orthonormal)


def check_linear_independence(vectors: np.ndarray | list[list[float]], tol: float = 1e-10) -> bool:
    """Check linear independence using numerical rank."""
    matrix = as_float_array(vectors)
    if matrix.ndim != 2:
        msg = "Input must be 2D with shape (n_vectors, dimension)."
        raise ValueError(msg)
    rank = np.linalg.matrix_rank(matrix, tol=tol)
    return bool(rank == matrix.shape[0])
