"""Determine whether two square matrices are similar.

Two square matrices :math:`A` and :math:`B` of the same size are similar if
there exists an invertible matrix :math:`P` such that :math:`P^{-1} A P = B`.
This implementation relies on SymPy to compute the Jordan canonical form of
both matrices.  Two matrices are similar precisely when their Jordan forms are
equal up to permutation of the Jordan blocks.

Examples
--------
>>> are_similar_matrices([[3, 1], [0, 3]], [[3, 0], [0, 3]])
False
>>> from sympy import Matrix
>>> matrix_a = [[3, 1], [0, 3]]
>>> transform = Matrix([[1, 1], [0, 1]])
>>> matrix_b = (transform.inv() * Matrix(matrix_a) * transform).tolist()
>>> are_similar_matrices(matrix_a, matrix_b)
True
>>> are_similar_matrices(
...     [[1, 2, 0], [0, 1, 0], [0, 0, 3]],
...     [[1, 0, 0], [0, 1, 0], [0, 0, 3]],
... )
False
>>> are_similar_matrices([[1, 2], [0, 1]], [[1, 2, 0], [0, 1, 0]])
Traceback (most recent call last):
    ...
ValueError: both matrices must be square with the same dimensions
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from sympy import Matrix, nsimplify
from sympy.matrices.common import MatrixError

__all__ = ["are_similar_matrices"]


type MatrixLike = Sequence[Sequence[Any]] | Matrix


def _as_square_matrix(matrix: MatrixLike, *, simplify_entries: bool) -> Matrix:
    """Return a SymPy matrix after validating that ``matrix`` is square.

    Parameters
    ----------
    matrix:
        Nested sequences (or a SymPy matrix) describing the matrix entries.
    simplify_entries:
        When ``True`` each entry is passed through :func:`sympy.nsimplify`
        which helps treat values such as ``0.5`` and ``1/2`` as the same.

    Raises
    ------
    TypeError
        If ``matrix`` cannot be converted into a SymPy matrix.
    ValueError
        If ``matrix`` is not square.
    """

    try:
        sympy_matrix = Matrix(matrix)
    except (TypeError, ValueError) as exc:  # pragma: no cover - defensive
        msg = "matrix input must be a rectangular sequence of numbers"
        raise TypeError(msg) from exc

    if sympy_matrix.rows != sympy_matrix.cols:
        raise ValueError("both matrices must be square with the same dimensions")

    if simplify_entries:
        sympy_matrix = sympy_matrix.applyfunc(nsimplify)

    return sympy_matrix


def _jordan_signature(matrix: Matrix) -> tuple[tuple[Any, tuple[int, ...]], ...]:
    """Return a hashable representation of the Jordan form of ``matrix``."""

    _, blocks = matrix.jordan_cells()
    summary: dict[Any, list[int]] = {}
    for block in blocks:
        block_matrix = Matrix(block)
        eigenvalue = block_matrix[0, 0]
        summary.setdefault(eigenvalue, []).append(block_matrix.rows)

    return tuple(
        (
            eigenvalue,
            tuple(sorted(block_sizes, reverse=True)),
        )
        for eigenvalue, block_sizes in sorted(
            summary.items(), key=lambda item: repr(item[0])
        )
    )


def are_similar_matrices(
    matrix_a: MatrixLike,
    matrix_b: MatrixLike,
    *,
    simplify_entries: bool = True,
) -> bool:
    """Return ``True`` if ``matrix_a`` and ``matrix_b`` are similar matrices.

    Parameters
    ----------
    matrix_a, matrix_b:
        Square matrices represented as nested sequences (or SymPy matrices).
    simplify_entries:
        If ``True`` (default) the function attempts to simplify each entry so
        that values that are algebraically equal are treated as such. Set this
        to ``False`` to skip simplification when working with symbolic inputs
        that should remain untouched.

    Raises
    ------
    ValueError
        If the matrices are not square or their dimensions do not match.
    TypeError
        If either matrix cannot be interpreted as a numeric matrix.
    """

    sympy_a = _as_square_matrix(matrix_a, simplify_entries=simplify_entries)
    sympy_b = _as_square_matrix(matrix_b, simplify_entries=simplify_entries)

    if sympy_a.shape != sympy_b.shape:
        raise ValueError("both matrices must be square with the same dimensions")

    try:
        signature_a = _jordan_signature(sympy_a)
        signature_b = _jordan_signature(sympy_b)
    except MatrixError as exc:  # pragma: no cover - rare SymPy failure
        msg = "unable to determine the Jordan canonical form"
        raise ValueError(msg) from exc

    return signature_a == signature_b


if __name__ == "__main__":  # pragma: no cover - convenience execution
    from doctest import testmod

    testmod()
