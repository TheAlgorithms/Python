import numpy as np
from scipy.optimize import minimize, LinearConstraint, Bounds

# Vector = np.typing.ArrayLike  # using numpy arrays to represent data
Vector = np.ndarray


def norm_squared(v: Vector) -> float:
    """
    Returns the square norm of a vector

    Args:
        v (Vector): vector

    Returns:
        float: sqaured norm of the vector
    """
    return np.dot(v, v)


def margin_hard(xs: list[Vector], y: Vector) -> tuple[Vector, float]:
    """
    Assuming the data is linearly separable
    Result will be falsy otherwise

    Args:
        xs (list[Vector]): list of observations (each observation is a vector)
        y (list[int]): classification of each observation (in {1, -1})

    Returns:
        (w: Vector, b: float): if x is a point on the margin, x verifies
            w . x + b = 0
    """

    # using Wolf's Dual to calculate w.
    # Primal problem: minimize 1/2*norm_squared(w)
    #   constraint: yn(w . xn + b) >= 1
    #
    # Dual problem: maximize sum_n(ln) -
    #       1/2 * sum_n(sum_m(ln*lm*yn*ym*xn . xm))
    #   constraint: ln >= 0
    #           and sum_n(ln*yn) = 0
    # Then we get w using w = sum_n(ln*yn*xn)
    # At the end we can get b ~= mean(yn - w . xn)

    n, = np.shape(y)

    def to_minimize(l: Vector) -> float:
        """Negative of the function to maximize"""
        s = 0
        n, = np.shape(l)
        for i in range(n):
            for j in range(n):
                s += l[i] * l[j] * y[i] * y[j] * np.dot(xs[i], xs[j])
        return 1/2 * s - np.sum(l)

    ly_contraint = LinearConstraint(y, 0, 0)
    l_bounds = Bounds(0, np.inf)
    
    l_star = minimize(to_minimize, np.ones(n), bounds=l_bounds, constraints=[ly_contraint]).x
    w_star = np.asarray(sum([l_star[i] * y[i] * xs[i] for i in range(n)]))

    b = sum([y[i] - np.dot(w_star, xs[i]) for i in range(n)])/n

    return w_star, b
