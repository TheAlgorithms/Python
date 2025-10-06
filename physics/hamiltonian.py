"""
Hamiltonian functions for classical and quantum mechanics.

This module provides two educational, minimal implementations:

- ham_c(mass, momentum, potential_energy):
    Computes H = T + V, where T = p^2/(2m), and V is the potential (scalar or array).

- ham_1d(mass, hbar, potential_energy, dx):
    Builds the 1D Hamiltonian using second-order central differences for the kinetic
    operator: T = - (hbar^2 / 2m) d^2/dx^2 with Dirichlet boundaries.

These functions help learners quickly prototype and simulate basic physical systems.

References
----------
- Classical Hamiltonian mechanics:
    https://en.wikipedia.org/wiki/Hamiltonian_mechanics
- Discrete 1D Schrödinger operator:
    https://en.wikipedia.org/wiki/Finite_difference_method
"""

from typing import Any

import numpy as np


def ham_c(
    mass: float,
    momentum: Any,
    potential_energy: Any,
) -> Any:
    """
    Classical Hamiltonian H = T + V with T = p^2 / (2 m).

    The function supports scalars or array-like inputs for momentum ``p`` and
    potential energy ``v``. NumPy broadcasting rules apply. If inputs are scalars,
    a float is returned; otherwise a NumPy array is returned.

    Parameters
    ----------
    mass : float
        Mass (must be positive).
    momentum : array-like or scalar
        Canonical momentum.
    potential_energy : array-like or scalar
        Potential energy evaluated for the corresponding configuration.

    Returns
    -------
    float | np.ndarray
        The Hamiltonian value(s) H = p^2/(2m) + V.

    Examples
    --------
    Free particle with p = 3 kg·m/s and m = 2 kg (v = 0):
    >>> ham_c(2.0, 3.0, 0.0)
    2.25

    Harmonic oscillator snapshot with vectorized p and v:
    >>> mass = 1.0
    >>> momentum = np.array([0.0, 1.0, 2.0])
    >>> potential_energy = np.array([0.5, 0.5, 0.5])  # e.g., 1/2 k x^2 at positions
    >>> ham_c(mass, momentum, potential_energy).tolist()
    [0.5, 1.0, 2.5]
    """
    if mass <= 0:
        raise ValueError("Mass m must be positive.")

    p = np.asarray(momentum)
    v = np.asarray(potential_energy)

    t = (p * p) / (2.0 * mass)
    h = t + v

    # Preserve scalar type when both inputs are scalar
    if np.isscalar(momentum) and np.isscalar(potential_energy):
        return float(h)
    return h


def ham_1d(
    mass: float,
    hbar: float,
    potential_energy: Any,
    dx: float,
) -> np.ndarray:
    """
    Construct the 1D quantum Hamiltonian matrix using finite differences.

    Discretizes the kinetic operator with second-order central differences and
    Dirichlet boundary conditions (wavefunction assumed zero beyond endpoints):

    H = - (hbar^2 / 2m) d^2/dx^2 + V

    On a uniform grid with spacing ``dx`` and N sites, the Laplacian is
    approximated by a tridiagonal matrix with main diagonal ``-2`` and
    off-diagonals ``+1``. The resulting kinetic term has main diagonal
    ``(hbar^2)/(m*dx^2)`` and off-diagonals ``-(hbar^2)/(2*m*dx^2)``.

    Parameters
    ----------
    mass : float
        Particle mass (must be positive).
    hbar : float
        Reduced Planck constant (can be set to 1.0 in natural units).
    potential_energy : array-like shape (N,)
        Potential energy values on the grid. Defines the matrix size.
    dx : float
        Grid spacing (must be positive).

    Returns
    -------
    np.ndarray shape (n, n)
        The Hermitian Hamiltonian matrix.

    Examples
    --------
    Free particle (v=0) on a small grid: main diagonal = 1/dx^2, off = -1/(2*dx^2)
    in units m=hbar=1.
    >>> n, dx = 5, 0.1
    >>> h = ham_1d(
    ...     mass=1.0, hbar=1.0, potential_energy=np.zeros(n), dx=dx
    ... )
    >>> float(h[0, 0])
    99.99999999999999
    >>> float(h[0, 1])
    -49.99999999999999

    Add a harmonic-like site potential to the diagonal:
    >>> x = dx * (np.arange(n) - (n-1)/2)
    >>> potential_energy = 0.5 * x**2  # k=m=omega=1 for illustration
    >>> h2 = ham_1d(1.0, 1.0, potential_energy, dx)
    >>> np.allclose(np.diag(h2) - np.diag(h), potential_energy)
    True
    """
    if mass <= 0:
        raise ValueError("Mass m must be positive.")
    if dx <= 0:
        raise ValueError("Grid spacing dx must be positive.")

    v = np.asarray(potential_energy, dtype=float)
    if v.ndim != 1:
        raise ValueError("v must be a 1D array-like of potential values.")

    n = v.size
    if n == 0:
        raise ValueError("v must contain at least one grid point.")

    coeff_main = (hbar * hbar) / (mass * dx * dx)
    coeff_off = -0.5 * (hbar * hbar) / (mass * dx * dx)

    # Build tridiagonal kinetic matrix
    h = np.zeros((n, n), dtype=float)
    np.fill_diagonal(h, coeff_main)
    idx = np.arange(n - 1)
    h[idx, idx + 1] = coeff_off
    h[idx + 1, idx] = coeff_off

    # Add the potential on the diagonal
    h[np.arange(n), np.arange(n)] += v
    return h


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

# Backward-compatible aliases
classical_hamiltonian = ham_c
quantum_hamiltonian_1d = ham_1d
