"""
Gaussian Error Linear Unit (GELU)

Use Case: GELU permits negative inputs for enhanced backprop gradients.
For more detailed information, you can refer to the following link:
https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#Gaussian-error_linear_unit_(GELU)
"""

import numpy as np
from scipy.special import erf


def gaussian_error_linear_unit(vector: np.ndarray) -> np.ndarray:
    """
         Implements the GELU activation function.
         Parameters:
             vector: the array containing input of gelu activation
         return:
         gelu (np.array): The input numpy array after applying gelu.

    Examples:
    >>> gaussian_error_linear_unit(vector=np.array([-1.1, 2.3, -3.4, 4.5]))
    array([-1.49232667e-01,  2.30000000e+00, -1.14555950e-03,  4.50000000e+00])

    >>> gaussian_error_linear_unit(vector=np.array([-9.2,-0.3,0.45,-4.56]))
    array([-0.00000000e+00, -1.14626573e-01,  4.50000000e-01, -1.16630255e-05])


    """
    return np.where(
        vector > 0, vector, (vector * 0.5 * (1.0 + erf(vector / np.sqrt(2.0))))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
