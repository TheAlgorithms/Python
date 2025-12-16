"""
Monte Carlo Simulation of the 2D Ising Model using Metropolis Algorithm.

Reference:
https://en.wikipedia.org/wiki/Ising_model

This algorithm simulates spin interactions on a 2D lattice.
It demonstrates how spins evolve toward equilibrium at a given temperature.

>>> result = ising_model_simulation(lattice_size=10, temperature=2.0, sweeps=100)
>>> isinstance(result, np.ndarray)
True
"""

import numpy as np
import matplotlib.pyplot as plt


def delta_energy(matrix: np.ndarray, i: int, j: int, J: float = 1.0) -> float:
    """Compute change in energy (ΔE) if the spin at (i, j) is flipped."""
    n = matrix.shape[0]
    neighbors = (
        matrix[(i + 1) % n, j]
        + matrix[(i - 1) % n, j]
        + matrix[i, (j + 1) % n]
        + matrix[i, (j - 1) % n]
    )
    return 2 * J * matrix[i, j] * neighbors


def ising_model_simulation(
    lattice_size: int = 50,
    temperature: float = 1.5,
    sweeps: int = 5000,
    J: float = 1.0,
    kB: float = 1.0,
    visualize: bool = False,
) -> np.ndarray:
    """Run the 2D Ising Model Monte Carlo Simulation.

    Args:
        lattice_size: Number of spins per row/column.
        temperature: Simulation temperature (T).
        sweeps: Number of Monte Carlo sweeps.
        J: Spin coupling constant.
        kB: Boltzmann constant.
        visualize: If True, display intermediate lattice states.

    Returns:
        Final spin lattice (numpy array) after equilibration.
    """
    # Initialize lattice randomly with spins {-1, +1}
    matrix = 2 * np.random.randint(0, 2, size=(lattice_size, lattice_size)) - 1

    for sweep in range(sweeps):
        for _ in range(lattice_size * lattice_size):
            i, j = np.random.randint(0, lattice_size, size=2)
            dE = delta_energy(matrix, i, j, J)

            # Metropolis criterion
            if dE <= 0 or np.random.rand() < np.exp(-dE / (kB * temperature)):
                matrix[i, j] *= -1

        if visualize and sweep % 500 == 0:
            plt.imshow(matrix, cmap="bwr", vmin=-1, vmax=1)
            plt.title(f"Sweep {sweep}")
            plt.pause(0.01)

    if visualize:
        plt.imshow(matrix, cmap="bwr", vmin=-1, vmax=1)
        plt.title(f"Equilibrated Ising Model at T={temperature}")
        plt.show()

    return matrix


if __name__ == "__main__":
    ising_model_simulation(visualize=True)
