# __init__.py
import sys

# Check for Python version
if sys.version_info < (3, 12):
    raise RuntimeError("This package requires Python 3.12 or later")

# Importing specific functions from modules
from src import conjugate_gradient, gaussian_elimination_pivoting, polynom_for_points, power_iteration, rank_of_matrix, rayleigh_quotient, schur_complement, test_linear_algebra, transformations_2d
# Package version
__version__ = "1.0.0"

# Defining what is available for import with 
__all__ = ["gaussian_elimination", "jacobi_iteration_method", "lu_decomposition", "matrix_inversion", "determinant", "eigenvalues"]

import math
import logging
logging.basicConfig(level=logging.INFO)
