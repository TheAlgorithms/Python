import numpy as np

def hypercube_points(num_points, hypercube_size, num_dimensions):
    return hypercube_size * np.random.rand(num_points, num_dimensions)
