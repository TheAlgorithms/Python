import numpy as np
from numpy import ndarray
from scipy.optimize import Bounds, LinearConstraint, minimize


class SVC:
    """
    Support Vector Classifier

    Args:
        kern (str): kernel to use. Default: linear
            Possible choices:
                - linear
        C: constraint for soft margin (data not linearly separable)
            Default: unbound
    """

    kernels = {
        "linear": lambda x, y: np.dot(x, y),
    }

    def __init__(
        self, *, C: float = np.inf, kern: str = "linear", gamma: float = None
    ) -> None:
        self.C = C
        self.kern = SVC.kernels[kern]

    def fit(self, xs: list[ndarray], y: ndarray) -> None:
        """
        Fits the SVC with a set of observations.

        Args:
            xs (list[Vector]): list of observations (each observation is a vector)
            y (list[int]): classification of each observation (in {1, -1})
        """

        self.xs = xs
        self.y = y

        # using Wolfe's Dual to calculate w.
        # Primal problem: minimize 1/2*norm_squared(w)
        #   constraint: yn(w . xn + b) >= 1
        #
        # With l a vector
        # Dual problem: maximize sum_n(ln) -
        #       1/2 * sum_n(sum_m(ln*lm*yn*ym*xn . xm))
        #   constraint: self.C >= ln >= 0
        #           and sum_n(ln*yn) = 0
        # Then we get w using w = sum_n(ln*yn*xn)
        # At the end we can get b ~= mean(yn - w . xn)
        #
        # Since we use kernels, we only need l_star to calculate b
        # and to classify observations

        (n,) = np.shape(y)

        # l = v because flake8...
        def to_minimize(v: ndarray) -> float:
            """Opposite of the function to maximize"""
            s = 0
            (n,) = np.shape(v)
            for i in range(n):
                for j in range(n):
                    s += v[i] * v[j] * y[i] * y[j] * self.kern(xs[i], xs[j])
            return 1 / 2 * s - sum(v)

        ly_contraint = LinearConstraint(y, 0, 0)
        l_bounds = Bounds(0, self.C)

        l_star = minimize(
            to_minimize, np.ones(n), bounds=l_bounds, constraints=[ly_contraint]
        ).x
        self.l_star = l_star

        b = 0
        for i in range(n):
            for j in range(n):
                b += y[i] - y[i] * l_star[i] * self.kern(xs[i], xs[j])
        self.b = b / n

    def predict(self, x: ndarray) -> int:
        """
        Get the expected class of an observation

        Args:
            x (Vector): observation

        Returns:
            int {1, -1}: expected class
        """
        s = sum(self.l_star[n] * self.y[n] * self.kern(xs[n], x) for n in range(len(y)))
        return 1 if s + self.b >= 0 else -1
        # return 1 if self.kern(self.w, x) + self.b >= 0 else -1


xs = [np.asarray([0, 1]), np.asarray([0, 2]), np.asarray([1, 1]), np.asarray([1, 2])]
y = np.asarray([1, 1, -1, -1])

s = SVC()
s.fit(xs, y)
print(s.predict(np.asarray([0, 1])))
print(s.predict(np.asarray([0, 3])))
print(s.predict(np.asarray([2, 2])))
