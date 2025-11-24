"""
Functions to calculate the Hamiltonian in both classical and quantum mechanics.

Overview:
    The Hamiltonian represents the total energy of a system.

    - In classical mechanics, it is the sum of kinetic and potential energies.

    - In quantum mechanics, it becomes an operator acting on the wavefunction ψ(x),
     describing how the system evolves in time.

This module includes:
    - classical_hamiltonian(): return total energy for given mass, momentum,
     and potential.
    - quantum_hamiltonian_1d(): Builds a 1D Hamiltonian matrix for numerical
     quantum systems.
"""

import numpy as np


def classical_hamiltonian(
    mass: float, momentum: float, potential_energy: float
) -> float:
    """
    Calculate the classical Hamiltonian (total energy) of a particle.

    The Hamiltonian(H) represents the total energy of the system:
        H = (momentum² / (2 * mass)) + potential_energy

    Parameters:
        mass (float): Mass of the particle (must be positive).
        momentum (float): Linear momentum of the particle.
        potential_energy (float): Potential energy of the particle.

    Returns:
        float: Total energy (Hamiltonian) of the particle.

    Examples:
    >>> classical_hamiltonian(1.0, 2.0, 5.0)
    7.0
    >>> classical_hamiltonian(2.0, 3.0, 1.0)
    3.25
    >>> classical_hamiltonian(1.0, 0.0, 10.0)
    10.0
    >>> classical_hamiltonian(1.0, 2.0, 0.0)
    2.0
    """
    if mass <= 0:
        raise ValueError("Mass must be a positive value.")
    return (momentum**2) / (2 * mass) + potential_energy


def quantum_hamiltonian_1d(
    mass: float,
    hbar: float,
    potential_energy_array: np.ndarray,
    grid_spacing: float,
    round_to: int | None = None,
) -> np.ndarray:
    """
    Construct the 1-D quantum Hamiltonian matrix for a particle in given potential.

    Description:
        In quantum mechanics, the Hamiltonian (H) represents the total energy
        of a particle, combining both kinetic and potential energy components.
        For a particle of mass m in one spatial dimension, it is defined as:

            H = - (ħ² / 2m) * (d²/dx²) + V(x)

            - The first term is the kinetic energy operator.
            - The second term is the potential energy V(x).

        Using the *finite difference method*, the second derivative is approximated by:
            d²ψ/dx² ≈ (ψ[i+1] - 2ψ[i] + ψ[i-1]) / (Δx²)

        This turns the continuous operator into a discrete matrix.

    Formula:
        H[i, i]   = (ħ² / (m * Δx²)) + V[i]
        H[i, i±1] = - (ħ² / (2m * Δx²))

    Parameters:
        mass (float): Mass of the particle. (must be positive)
        hbar (float): Reduced Planck constant. (must be positive)
        potential_energy_array (np.ndarray): Potential energy values V(x)
         at each grid point.
        grid_spacing (float): Distance between consecutive grid points Δx.
         (must be positive)
        round_to (int | None): Number of decimal places to round the matrix to.
                               If None (default), no rounding is applied.

    Returns:
        np.ndarray: The discrete Hamiltonian matrix representing
         the total energy operator.

    Examples:
        >>> import numpy as np
        >>> potential = np.array([0.0, 0.0, 0.0])
        >>> quantum_hamiltonian_1d(1.0, 1.0, potential, 1.0)
        array([[ 1. , -0.5,  0. ],
               [-0.5,  1. , -0.5],
               [ 0. , -0.5,  1. ]])
        >>> potential = np.array([1.0, 2.0, 3.0])
        >>> quantum_hamiltonian_1d(2.0, 1.0, potential, 0.5)
        array([[ 3., -1.,  0.],
               [-1.,  4., -1.],
               [ 0., -1.,  5.]])
    """
    if any(val <= 0 for val in (mass, hbar, grid_spacing)):
        raise ValueError("mass, hbar, and grid_spacing must be positive values.")

    num_points = len(potential_energy_array)
    kinetic_prefactor = hbar**2 / (2 * mass * grid_spacing**2)

    diagonal = np.full(num_points, 2)
    off_diagonal = np.ones(num_points - 1)

    kinetic_matrix = kinetic_prefactor * (
        np.diag(diagonal) - np.diag(off_diagonal, 1) - np.diag(off_diagonal, -1)
    )

    potential_matrix = np.diag(potential_energy_array)
    total_hamiltonian = kinetic_matrix + potential_matrix

    if round_to is not None:
        total_hamiltonian = np.round(total_hamiltonian, round_to)

    return total_hamiltonian


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
