import numpy as np
from typing import Union

def hypercube_points(num_points: int, hypercube_size: Union[int, float], num_dimensions: int) -> np.ndarray:
    """
    Generates random points uniformly distributed within an n-dimensional hypercube.

    Args:
        num_points (int): The number of random points to generate.
        hypercube_size (Union[int, float]): The size of the hypercube (side length).
        num_dimensions (int): The number of dimensions of the hypercube.

    Returns:
        np.ndarray: An array of shape (num_points, num_dimensions) with the generated points.
    """
    rng = np.random.default_rng()
    return hypercube_size * rng.random((num_points, num_dimensions))
