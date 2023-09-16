def calculate_acceleration(force=None, mass=None, vi=None, vf=None, t=None):
    """
    Calculate acceleration using either F = ma or change in velocity formula.

    :param force: Force in Newtons (N) (default is None).
    :param mass: Mass in kilograms (kg) (default is None).
    :param vi: Initial velocity in m/s (default is None).
    :param vf: Final velocity in m/s (default is None).
    :param t: Time in seconds (default is None).
    :return: Acceleration in meters per second squared (m/s^2).

    Examples:
    >>> calculate_acceleration(50, 10)
    5.0

    >>> calculate_acceleration(vi=18.5, vf=46.1, t=2.47)
    11.17408906882591
    """
    if force is not None and mass is not None:
        if mass == 0:
            raise ValueError("Mass cannot be zero.")
        acceleration = force / mass
    elif vi is not None and vf is not None and t is not None:
        acceleration = (vf - vi) / t
    else:
        raise ValueError("Insufficient information provided to calculate acceleration.")

    return acceleration
