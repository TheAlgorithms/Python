from __future__ import annotations

import numpy as np
import pytest

from adv_math_engine.vector_algebra import (
    angle_between,
    check_linear_independence,
    cross_product,
    dot_product,
    gram_schmidt,
    vector_projection,
)


def test_dot_product_vectorized() -> None:
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [1, 2, 3]])
    result = dot_product(a, b)
    assert np.allclose(result, np.array([50, 32]))


def test_cross_product_3d() -> None:
    result = cross_product([1, 0, 0], [0, 1, 0])
    assert np.allclose(result, np.array([0, 0, 1]))


def test_projection_rejects_zero_vector() -> None:
    with pytest.raises(ValueError):
        vector_projection([1, 2, 3], [0, 0, 0])


def test_angle_between_orthogonal_vectors() -> None:
    assert np.isclose(angle_between([1, 0], [0, 1]), np.pi / 2)


def test_gram_schmidt_orthonormality() -> None:
    basis = gram_schmidt([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
    assert np.allclose(basis @ basis.T, np.eye(3), atol=1e-10)


def test_linear_independence_rank_check() -> None:
    independent = check_linear_independence([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    dependent = check_linear_independence([[1, 2, 3], [2, 4, 6]])
    assert independent
    assert not dependent
