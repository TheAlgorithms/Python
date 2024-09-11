# __init__.py
import sys

# Check for Python version
if sys.version_info < (3, 12):
    raise RuntimeError("This package requires Python 3.12 or later")

# Importing specific functions from modules
from linear_algebra import gaussian_elimination, jacobi_iteration_method, lu_decomposition

# Package version
__version__ = "1.0.0"

# Defining what is available for import with 
__all__ = ["gaussian_elimination", "jacobi_iteration_method", "lu_decomposition", "matrix_inversion", "determinant", "eigenvalues"]

import math
import logging
logging.basicConfig(level=logging.INFO)
