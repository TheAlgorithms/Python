import numpy as np
from scipy.optimize import Bounds, LinearConstraint, minimize


def norm_squared(vector: np.ndarray) -> float:
    """Return the squared second norm of a vector."""
    return np.sum(vector ** 2)


class SVC:
    """
    Support Vector Classifier

    Args:
        kernel (str): kernel to use. Default: 'linear'
            Possible choices:
                - 'linear'
                - 'rbf' (radial basis function)
        regularization (float): constraint for soft margin (data not linearly separable)
            Default: np.inf
        gamma (float): gamma parameter for the RBF kernel. Ignored for linear kernel.
            Default: 0.0

    Raises:
        ValueError: if an unknown kernel is specified or if gamma is invalid for RBF kernel
    """

    kernels = {
        'linear': lambda x, y, gamma: np.dot(x, y),
        'rbf': lambda x, y, gamma: np.exp(-gamma * norm_squared(x - y)),
    }

    def __init__(
        self,
        *,
        kernel: str = 'linear',
        regularization: float = np.inf,
        gamma: float = 0.0,
    ) -> None:
        if kernel not in SVC.kernels:
            raise ValueError(f"Unknown kernel: {kernel}")
        self.kernel_name = kernel
        self.kernel = SVC.kernels[kernel]
        self.regularization = regularization
        self.gamma = gamma

    def fit(self, observations: list[np.ndarray], classes: np.ndarray) -> None:
        """
        Fit the SVC with a set of observations.

        Args:
            observations (list[np.ndarray]): list of observations
            classes (np.ndarray): classification of each observation (in {1, -1})
        """

        self.observations = observations
        self.classes = classes

        # using Wolfe's Dual to calculate support vectors
        # Dual problem: maximize sum_n(ln) -
        #       1/2 * sum_n(sum_m(ln*lm*yn*ym*xn . xm))
        #   constraint: 0 <= ln <= self.regularization
        #           and sum_n(ln*yn) = 0
        #
        # Then we get w using w = sum_n(ln*yn*xn)
        # At the end we can get b ~= mean(yn - w . xn)
        #
        # Since we use kernels, we only need l_star to calculate b
        # and to classify observations

        n = len(classes)

        def to_minimize(l: np.ndarray)
