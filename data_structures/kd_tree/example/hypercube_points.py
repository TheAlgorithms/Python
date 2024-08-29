import numpy as np


def hypercube_points(
    num_points: int, hypercube_size: float, num_dimensions: int
) -> np.ndarray:
    """
    Generates random points uniformly distributed within an n-dimensional hypercube.

    Args:
        num_points (int): Number of points to generate.
        hypercube_size (float): Size of the hypercube.
        num_dimensions (int): Number of dimensions of the hypercube.

    Returns:
        np.ndarray: An array of shape (num_points, num_dimensions)
                    with generated points.
    """
    rng = np.random.default_rng()
    shape = (num_points, num_dimensions)
    return hypercube_size * rng.random(shape)
