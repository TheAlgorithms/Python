import numpy as np


def hypercube_points(num_points, hypercube_size, num_dimensions):
    rng = np.random.default_rng()
    return hypercube_size * rng.random((num_points, num_dimensions))
