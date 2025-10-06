"""
Hamiltonian functions for classical and quantum mechanics.

This module provides two educational, minimal implementations:

- classical_hamiltonian(m, p, v): Computes H = T + v for a particle/system, where
  T = p^2 / (2 m) is the kinetic energy expressed in terms of momentum p, and v is
  the potential energy (can be a scalar or an array broadcastable to p).

- quantum_hamiltonian_1d(m, hbar, v, dx): Builds the 1D Hamiltonian matrix for a
  particle in a potential v using second-order central finite differences for the
  kinetic energy operator: T = - (hbar^2 / 2m) d^2/dx^2 with Dirichlet boundaries.

These functions are intended for learners to quickly prototype and simulate basic
physical systems.

References
----------
- Classical Hamiltonian mechanics: https://en.wikipedia.org/wiki/Hamiltonian_mechanics
- Discrete 1D Schrödinger operator: https://en.wikipedia.org/wiki/Finite_difference_method
"""

from __future__ import annotations

from typing import Any

import numpy as np


def classical_hamiltonian(m: float, p: Any, v: Any) -> Any:
    """
    Classical Hamiltonian H = T + v with T = p^2 / (2 m).

    The function supports scalars or array-like inputs for momentum ``p`` and
    potential energy ``v``; NumPy broadcasting rules apply. If inputs are scalars,
    a float is returned; otherwise a NumPy array is returned.

    Parameters
    ----------
    m : float
        Mass (must be positive).
    p : array-like or scalar
        Canonical momentum.
    v : array-like or scalar
        Potential energy evaluated for the corresponding configuration.

    Returns
    -------
    float | np.ndarray
        The Hamiltonian value(s) H = p^2/(2m) + v.

    Examples
    --------
    Free particle with p = 3 kg·m/s and m = 2 kg (v = 0):
    >>> classical_hamiltonian(2.0, 3.0, 0.0)
    2.25

    Harmonic oscillator snapshot with vectorized p and v:
    >>> m = 1.0
    >>> p = np.array([0.0, 1.0, 2.0])
    >>> v = np.array([0.5, 0.5, 0.5])  # e.g., 1/2 k x^2 at three positions
    >>> classical_hamiltonian(m, p, v).tolist()
    [0.5, 1.0, 2.5]
    """
    if m <= 0:
        raise ValueError("Mass m must be positive.")

    p_arr = np.asarray(p)
    v_arr = np.asarray(v)

    T = (p_arr * p_arr) / (2.0 * m)
    H = T + v_arr

    # Preserve scalar type when both inputs are scalar
    if np.isscalar(p) and np.isscalar(v):
        return float(H)
    return H


def quantum_hamiltonian_1d(m: float, hbar: float, v: Any, dx: float) -> np.ndarray:
    """
    Construct the 1D quantum Hamiltonian matrix using finite differences.

    Discretizes the kinetic operator with second-order central differences and
    Dirichlet boundary conditions (wavefunction assumed zero beyond endpoints):

        H = - (hbar^2 / 2m) d^2/dx^2 + v

    On a uniform grid with spacing ``dx`` and N sites, the Laplacian is
    approximated by the tridiagonal matrix with main diagonal ``-2`` and
    off-diagonals ``+1``. The resulting kinetic term has main diagonal
    ``(hbar^2)/(m*dx^2)`` and off-diagonals ``-(hbar^2)/(2*m*dx^2)``.

    Parameters
    ----------
    m : float
        Particle mass (must be positive).
    hbar : float
        Reduced Planck constant (can be set to 1.0 in natural units).
    v : array-like shape (N,)
        Potential energy values on the grid. Defines the matrix size.
    dx : float
        Grid spacing (must be positive).

    Returns
    -------
    np.ndarray shape (N, N)
        The Hermitian Hamiltonian matrix.

    Examples
    --------
    Free particle (v=0) on a small grid: main diagonal = 1/dx^2, off = -1/(2*dx^2) in units m=hbar=1.
    >>> N, dx = 5, 0.1
    >>> H = quantum_hamiltonian_1d(m=1.0, hbar=1.0, v=np.zeros(N), dx=dx)
    >>> float(H[0, 0])
    99.99999999999999
    >>> float(H[0, 1])
    -49.99999999999999

    Add a harmonic-like site potential to the diagonal:
    >>> x = dx * (np.arange(N) - (N-1)/2)
    >>> v = 0.5 * x**2  # k=m=omega=1 for illustration
    >>> H2 = quantum_hamiltonian_1d(1.0, 1.0, v, dx)
    >>> np.allclose(np.diag(H2) - np.diag(H), v)
    True
    """
    if m <= 0:
        raise ValueError("Mass m must be positive.")
    if dx <= 0:
        raise ValueError("Grid spacing dx must be positive.")

    v_arr = np.asarray(v, dtype=float)
    if v_arr.ndim != 1:
        raise ValueError("v must be a 1D array-like of potential values.")

    N = v_arr.size
    if N == 0:
        raise ValueError("v must contain at least one grid point.")

    coeff_main = (hbar * hbar) / (m * dx * dx)
    coeff_off = -0.5 * (hbar * hbar) / (m * dx * dx)

    # Build tridiagonal kinetic matrix
    H = np.zeros((N, N), dtype=float)
    np.fill_diagonal(H, coeff_main)
    idx = np.arange(N - 1)
    H[idx, idx + 1] = coeff_off
    H[idx + 1, idx] = coeff_off

    # Add the potential on the diagonal
    H[np.arange(N), np.arange(N)] += v_arr
    return H


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
