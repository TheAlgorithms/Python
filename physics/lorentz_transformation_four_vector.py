"""
Lorentz transformations describe the transition between two inertial reference
frames F and F', each of which is moving in some direction with respect to the
other. This code only calculates Lorentz transformations for movement in the x
direction with no spatial rotation (i.e., a Lorentz boost in the x direction).
The Lorentz transformations are calculated here as linear transformations of
four-vectors [ct, x, y, z] described by Minkowski space. Note that t (time) is
multiplied by c (the speed of light) in the first entry of each four-vector.

Thus, if X = [ct; x; y; z] and X' = [ct'; x'; y'; z'] are the four-vectors for
two inertial reference frames and X' moves in the x direction with velocity v
with respect to X, then the Lorentz transformation from X to X' is X' = BX,
where

    | y  -γβ  0  0|
B = |-γβ  y   0  0|
    | 0   0   1  0|
    | 0   0   0  1|

is the matrix describing the Lorentz boost between X and X',
y = 1 / √(1 - v²/c²) is the Lorentz factor, and β = v/c is the velocity as
a fraction of c.

Reference: https://en.wikipedia.org/wiki/Lorentz_transformation
"""

from math import sqrt

import numpy as np
from sympy import symbols

# Coefficient
# Speed of light (m/s)
c = 299792458

# Symbols
ct, x, y, z = symbols("ct x y z")


# Vehicle's speed divided by speed of light (no units)
def beta(velocity: float) -> float:
    """
    Calculates β = v/c, the given velocity as a fraction of c
    >>> beta(c)
    1.0
    >>> beta(199792458)
    0.666435904801848
    >>> beta(1e5)
    0.00033356409519815205
    >>> beta(0.2)
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than or equal to 1!
    """
    if velocity > c:
        raise ValueError("Speed must not exceed light speed 299,792,458 [m/s]!")
    elif velocity < 1:
        # Usually the speed should be much higher than 1 (c order of magnitude)
        raise ValueError("Speed must be greater than or equal to 1!")

    return velocity / c


def gamma(velocity: float) -> float:
    """
    Calculate the Lorentz factor y = 1 / √(1 - v²/c²) for a given velocity
    >>> gamma(4)
    1.0000000000000002
    >>> gamma(1e5)
    1.0000000556325075
    >>> gamma(3e7)
    1.005044845777813
    >>> gamma(2.8e8)
    2.7985595722318277
    >>> gamma(299792451)
    4627.49902669495
    >>> gamma(0.3)
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than or equal to 1!
    >>> gamma(2 * c)
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed light speed 299,792,458 [m/s]!
    """
    return 1 / sqrt(1 - beta(velocity) ** 2)


def transformation_matrix(velocity: float) -> np.ndarray:
    """
    Calculate the Lorentz transformation matrix for movement in the x direction:

    | y  -γβ  0  0|
    |-γβ  y   0  0|
    | 0   0   1  0|
    | 0   0   0  1|

    where y is the Lorentz factor and β is the velocity as a fraction of c
    >>> transformation_matrix(29979245)
    array([[ 1.00503781, -0.10050378,  0.        ,  0.        ],
           [-0.10050378,  1.00503781,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  1.        ,  0.        ],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
    >>> transformation_matrix(19979245.2)
    array([[ 1.00222811, -0.06679208,  0.        ,  0.        ],
           [-0.06679208,  1.00222811,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  1.        ,  0.        ],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
    >>> transformation_matrix(1)
    array([[ 1.00000000e+00, -3.33564095e-09,  0.00000000e+00,
             0.00000000e+00],
           [-3.33564095e-09,  1.00000000e+00,  0.00000000e+00,
             0.00000000e+00],
           [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00,
             0.00000000e+00],
           [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
             1.00000000e+00]])
    >>> transformation_matrix(0)
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than or equal to 1!
    >>> transformation_matrix(c * 1.5)
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed light speed 299,792,458 [m/s]!
    """
    return np.array(
        [
            [gamma(velocity), -gamma(velocity) * beta(velocity), 0, 0],
            [-gamma(velocity) * beta(velocity), gamma(velocity), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def transform(velocity: float, event: np.ndarray | None = None) -> np.ndarray:
    """
    Calculate a Lorentz transformation for movement in the x direction given a
    velocity and a four-vector for an inertial reference frame

    If no four-vector is given, then calculate the transformation symbolically
    with variables
    >>> transform(29979245, np.array([1, 2, 3, 4]))
    array([ 3.01302757e+08, -3.01302729e+07,  3.00000000e+00,  4.00000000e+00])
    >>> transform(29979245)
    array([1.00503781498831*ct - 0.100503778816875*x,
           -0.100503778816875*ct + 1.00503781498831*x, 1.0*y, 1.0*z],
          dtype=object)
    >>> transform(19879210.2)
    array([1.0022057787097*ct - 0.066456172618675*x,
           -0.066456172618675*ct + 1.0022057787097*x, 1.0*y, 1.0*z],
          dtype=object)
    >>> transform(299792459, np.array([1, 1, 1, 1]))
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed light speed 299,792,458 [m/s]!
    >>> transform(-1, np.array([1, 1, 1, 1]))
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than or equal to 1!
    """
    # Ensure event is not empty
    if event is None:
        event = np.array([ct, x, y, z])  # Symbolic four vector
    else:
        event[0] *= c  # x0 is ct (speed of light * time)

    return transformation_matrix(velocity) @ event


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example of symbolic vector:
    four_vector = transform(29979245)
    print("Example of four vector: ")
    print(f"ct' = {four_vector[0]}")
    print(f"x' = {four_vector[1]}")
    print(f"y' = {four_vector[2]}")
    print(f"z' = {four_vector[3]}")

    # Substitute symbols with numerical values
    sub_dict = {ct: c, x: 1, y: 1, z: 1}
    numerical_vector = [four_vector[i].subs(sub_dict) for i in range(4)]

    print(f"\n{numerical_vector}")
