"""
Lorentz transformation describes the transition from a reference frame P
to another reference frame P', each of which is moving in a direction with
respect to the other. The Lorentz transformation implemented in this code
is the relativistic version using a four vector described by Minkowsky Space:
x0 = ct, x1 = x, x2 = y, and x3 = z

NOTE: Please note that x0 is c (speed of light) times t (time).

So, the Lorentz transformation using a four vector is defined as:

|ct'|   | γ  -γβ  0  0|  |ct|
|x' | = |-γβ  γ   0  0| *|x |
|y' |   | 0   0   1  0|  |y |
|z' |   | 0   0   0  1|  |z |

Where:
           1
γ = ---------------
      -----------
     /     v^2  |
    /(1 -  ---
  -/       c^2

      v
β = -----
      c

Reference: https://en.wikipedia.org/wiki/Lorentz_transformation
"""
from __future__ import annotations

from math import sqrt

import numpy as np  # type: ignore
from sympy import symbols  # type: ignore

# Coefficient
# Speed of light (m/s)
c = 299792458

# Symbols
ct, x, y, z = symbols("ct x y z")
ct_p, x_p, y_p, z_p = symbols("ct' x' y' z'")


# Vehicle's speed divided by speed of light (no units)
def beta(velocity: float) -> float:
    """
    >>> beta(c)
    1.0

    >>> beta(199792458)
    0.666435904801848

    >>> beta(1e5)
    0.00033356409519815205

    >>> beta(0.2)
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than 1!
    """
    if velocity > c:
        raise ValueError("Speed must not exceed Light Speed 299,792,458 [m/s]!")

    # Usually the speed u should be much higher than 1 (c order of magnitude)
    elif velocity < 1:
        raise ValueError("Speed must be greater than 1!")
    return velocity / c


def gamma(velocity: float) -> float:
    """
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
    ValueError: Speed must be greater than 1!

    >>> gamma(2*c)
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed Light Speed 299,792,458 [m/s]!
    """
    return 1 / (sqrt(1 - beta(velocity) ** 2))


def transformation_matrix(velocity: float) -> np.array:
    """
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
    ValueError: Speed must be greater than 1!

    >>> transformation_matrix(c * 1.5)
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed Light Speed 299,792,458 [m/s]!
    """
    return np.array(
        [
            [gamma(velocity), -gamma(velocity) * beta(velocity), 0, 0],
            [-gamma(velocity) * beta(velocity), gamma(velocity), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def transform(
    velocity: float, event: np.array = np.zeros(4), symbolic: bool = True  # noqa: B008
) -> np.array:
    """
    >>> transform(29979245,np.array([1,2,3,4]), False)
    array([ 3.01302757e+08, -3.01302729e+07,  3.00000000e+00,  4.00000000e+00])

    >>> transform(29979245)
    array([1.00503781498831*ct - 0.100503778816875*x,
           -0.100503778816875*ct + 1.00503781498831*x, 1.0*y, 1.0*z],
          dtype=object)

    >>> transform(19879210.2)
    array([1.0022057787097*ct - 0.066456172618675*x,
           -0.066456172618675*ct + 1.0022057787097*x, 1.0*y, 1.0*z],
          dtype=object)

    >>> transform(299792459, np.array([1,1,1,1]))
    Traceback (most recent call last):
      ...
    ValueError: Speed must not exceed Light Speed 299,792,458 [m/s]!

    >>> transform(-1, np.array([1,1,1,1]))
    Traceback (most recent call last):
      ...
    ValueError: Speed must be greater than 1!
    """
    # Ensure event is not a vector of zeros
    if not symbolic:

        # x0 is ct (speed of ligt * time)
        event[0] = event[0] * c
    else:

        # Symbolic four vector
        event = np.array([ct, x, y, z])

    return transformation_matrix(velocity).dot(event)


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

    # Substitute symbols with numerical values:
    values = np.array([1, 1, 1, 1])
    sub_dict = {ct: c * values[0], x: values[1], y: values[2], z: values[3]}
    numerical_vector = [four_vector[i].subs(sub_dict) for i in range(0, 4)]

    print(f"\n{numerical_vector}")
