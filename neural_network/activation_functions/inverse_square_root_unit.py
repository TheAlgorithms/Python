import numpy as np

'''
ISRU (Inverse Square Root Unit) is an activation function defined as f(x) = x / sqrt(1 + alpha * x^2). 
It introduces non-linearity while controlling the slope for negative values using the alpha parameter.

For more details: http://www.gabormelli.com/RKB/Inverse_Square_Root_Unit_(ISRU)_Activation_Function#:~:text=An%20Inverse%20Square%20Root%20Unit,activation%20of%20ISRUs%20in%20RNNs.
'''

def isru(vector: np.ndarray, alpha: float) -> np.ndarray:
    """
    Implements the ISRU (Inverse Square Root Unit) activation function.

    Parameters:
        vector (np.ndarray): The input array for ISRU activation.
        alpha (float): The parameter controlling the slope.

    Returns:
        np.ndarray: The input array after applying the ISRU activation.

    Formula: ISRU(x, alpha) = x / sqrt(1 + alpha * x^2)

    Use Case & Importance:
    - ISRU introduces non-linearity while controlling the slope for negative values.
    - It can be used in neural networks to customize the activation function's behavior.

    Examples:
    >>> isru(np.array([2.3, 0.6, -2, -3.8], dtype=float), 0.1)
    array([ 1.86004775,  0.58948312, -1.69030851, -2.43070915])

    >>> isru(np.array([-9.2, -0.3, 0.45, -4.56], dtype=float), 0.05)
    array([-4.02211015, -0.29932727,  0.44773903, -3.19288902])
    """
    return vector / np.sqrt(1 + alpha * vector**2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
