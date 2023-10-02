import numpy as np

'''
Soft Exponential can adapt to various tasks by
adjusting the parameter alpha.
It is a customizable activation function that can
learn different activation
characteristics based on the problem requirements.

For more details: https://lightrun.com/answers/keras-team-keras-soft-exponential-activation-function
'''

def soft_exponential(vector: np.ndarray, alpha: float) -> np.ndarray:
    """
    Implements the Soft Exponential activation function.

    Parameters:
        vector (np.ndarray): The input array for Soft Exponential activation.
        alpha (float): The parameter controlling the slope.

    Returns:
        np.ndarray: The input array after applying the Soft Exponential activation.

    Formula: Soft Exponential(x, alpha) = (alpha * (exp(alpha * x) - 1), alpha > 0;
                                        -log(1 - alpha * (x + alpha)), alpha < 0;
                                        x, alpha = 0)

    Use Case & Importance:
    - Soft Exponential provides flexibility in controlling the activation's behavior with the parameter alpha.
    - It can adapt to various tasks and learn different activation characteristics.

    Examples:
    >>> soft_exponential(np.array([2.3, 0.6, -2, -3.8], dtype=float), 0.1)
    array([ 0.02586   ,  0.00618365, -0.01812692, -0.03161386])

    >>> soft_exponential(np.array([-9.2, -0.3, 0.45, -4.56], dtype=float), -0.05)
    array([ 0.62082652,  0.01765494, -0.01980263,  0.26201433])
    """
    if alpha > 0:
        return alpha * (np.exp(alpha * vector) - 1)
    elif alpha < 0:
        return -np.log(1 - alpha * (vector + alpha))
    else:
        return vector

if __name__ == "__main__":
    import doctest
    doctest.testmod()
