def calculate_acceleration(*args):
    """
    Calculate acceleration using either F = ma or a = (vf - vi) / t.

    Arguments:
    - If two arguments are provided: (force, mass)
    - If three arguments are provided: (vi, vf, t)

    :return: Acceleration in meters per second squared (m/s^2).
    """

    if len(args) == 2:
        force, mass = args
        if mass == 0:
            raise ValueError("Mass cannot be zero.")
        acceleration = force / mass
    elif len(args) == 3:
        vi, vf, t = args
        acceleration = (vf - vi) / t
    else:
        raise ValueError("Invalid number of arguments. Use either (force, mass) or (vi, vf, t) combinations.")

    return acceleration

print(calculate_acceleration(18.5, 46.1, 2.47))
