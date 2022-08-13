"""
Horizontal Projectile Motion problem in physics.
This algorithm solves a specific problem in which
the motion starts from the ground as can be seen below:
      (v = 0)
        **
       *  *
      *    *
     *      *
    *        *
   *          *
GROUND      GROUND
For more info: https://en.wikipedia.org/wiki/Projectile_motion
"""

# Importing packages
from math import radians as angle_to_radians
from math import sin

# Acceleration Constant on Earth (unit m/s^2)
g = 9.80665


def check_args(init_velocity: float, angle: float) -> None:
    """
    Check that the arguments are valid
    """

    # Ensure valid instance
    if not isinstance(init_velocity, (int, float)):
        raise TypeError("Invalid velocity. Should be a positive number.")

    if not isinstance(angle, (int, float)):
        raise TypeError("Invalid angle. Range is 1-90 degrees.")

    # Ensure valid angle
    if angle > 90 or angle < 1:
        raise ValueError("Invalid angle. Range is 1-90 degrees.")

    # Ensure valid velocity
    if init_velocity < 0:
        raise ValueError("Invalid velocity. Should be a positive number.")


def horizontal_distance(init_velocity: float, angle: float) -> float:
    """
    Returns the horizontal distance that the object cover
    Formula:
            v_0^2 * sin(2 * alpha)
            ---------------------
                   g
    v_0 - initial velocity
    alpha - angle
    >>> horizontal_distance(30, 45)
    91.77
    >>> horizontal_distance(100, 78)
    414.76
    >>> horizontal_distance(-1, 20)
    Traceback (most recent call last):
        ...
    ValueError: Invalid velocity. Should be a positive number.
    >>> horizontal_distance(30, -20)
    Traceback (most recent call last):
        ...
    ValueError: Invalid angle. Range is 1-90 degrees.
    """
    check_args(init_velocity, angle)
    radians = angle_to_radians(2 * angle)
    return round(init_velocity**2 * sin(radians) / g, 2)


def max_height(init_velocity: float, angle: float) -> float:
    """
    Returns the maximum height that the object reach
    Formula:
            v_0^2 * sin^2(alpha)
            --------------------
                   2g
    v_0 - initial velocity
    alpha - angle
    >>> max_height(30, 45)
    22.94
    >>> max_height(100, 78)
    487.82
    >>> max_height("a", 20)
    Traceback (most recent call last):
        ...
    TypeError: Invalid velocity. Should be a positive number.
    >>> horizontal_distance(30, "b")
    Traceback (most recent call last):
        ...
    TypeError: Invalid angle. Range is 1-90 degrees.
    """
    check_args(init_velocity, angle)
    radians = angle_to_radians(angle)
    return round(init_velocity**2 * sin(radians) ** 2 / (2 * g), 2)


def total_time(init_velocity: float, angle: float) -> float:
    """
    Returns total time of the motion
    Formula:
            2 * v_0 * sin(alpha)
            --------------------
                   g
    v_0 - initial velocity
    alpha - angle
    >>> total_time(30, 45)
    4.33
    >>> total_time(100, 78)
    19.95
    >>> total_time(-10, 40)
    Traceback (most recent call last):
        ...
    ValueError: Invalid velocity. Should be a positive number.
    >>> total_time(30, "b")
    Traceback (most recent call last):
        ...
    TypeError: Invalid angle. Range is 1-90 degrees.
    """
    check_args(init_velocity, angle)
    radians = angle_to_radians(angle)
    return round(2 * init_velocity * sin(radians) / g, 2)


def test_motion() -> None:
    """
    >>> test_motion()
    """
    v0, angle = 25, 20
    assert horizontal_distance(v0, angle) == 40.97
    assert max_height(v0, angle) == 3.73
    assert total_time(v0, angle) == 1.74


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Get input from user
    init_vel = float(input("Initial Velocity: ").strip())

    # Get input from user
    angle = float(input("angle: ").strip())

    # Print results
    print()
    print("Results: ")
    print(f"Horizontal Distance: {str(horizontal_distance(init_vel, angle))} [m]")
    print(f"Maximum Height: {str(max_height(init_vel, angle))} [m]")
    print(f"Total Time: {str(total_time(init_vel, angle))} [s]")
