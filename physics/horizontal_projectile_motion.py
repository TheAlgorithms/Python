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

# Acceleration Constant on hearth (unit m/s^2)
g = 9.80665


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
    """
    radians = angle_to_radians(2 * angle)
    return round((init_velocity ** 2) * sin(radians) / g, 2)


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
    """

    radians = angle_to_radians(angle)
    return round(((init_velocity ** 2) * (sin(radians)) ** 2) / (2 * g), 2)


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
    """

    radians = angle_to_radians(angle)
    return round((2 * init_velocity) * (sin(radians)) / g, 2)


def test_motion() -> None:
    """
    >>> test_motion()
    """
    v0, angle = 25, 20
    assert horizontal_distance(v0, angle) == 40.97
    assert max_height(v0, angle) == 3.73
    assert total_time(v0, angle) == 1.74


if __name__ == "__main__":

    # Get input from user
    init_vel = float(input("Initial Velocity: "))

    # Get input from user
    angle = float(input("angle: "))

    # Ensure valid angle
    if angle > 90 or angle < 1:
        print("Error: Invalid angle. Range is 1-90 degrees.")

    # Ensure valid velocity
    elif init_vel < 0:
        print("Error: Invalid velocity. Should be a positive number.")

    # Print results
    else:
        print()
        h_dis = str(horizontal_distance(init_vel, angle))
        v_dis = str(max_height(init_vel, angle))
        t_time = str(total_time(init_vel, angle))
        print("Results: ")
        print(f"Horizontal Distance: {h_dis} [m]")
        print(f"Maximum Height: {v_dis} [m]")
        print(f"Total Time: {t_time} [s]")
