#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11532
#  https://github.com/TheAlgorithms/Python/pull/11532
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

import numpy as np


def hypercube_points(
    num_points: int, hypercube_size: float, num_dimensions: int
) -> np.ndarray:
    """
    Generates random points uniformly distributed within an n-dimensional hypercube.

    Args:
        num_points: Number of points to generate.
        hypercube_size: Size of the hypercube.
        num_dimensions: Number of dimensions of the hypercube.

    Returns:
        An array of shape (num_points, num_dimensions)
                    with generated points.
    """
    rng = np.random.default_rng()
    shape = (num_points, num_dimensions)
    return hypercube_size * rng.random(shape)
