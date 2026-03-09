c = 299792458

"""
The relativistic velocity summation formula calculates the combined velocity v2
of an object moving at speed v1 relative to a frame that is itself moving at velocity v
relative to an observer. I take the last one to be strictly lower than the speed of
light.
The formula is v2 = (v1 + v)/(1 + v1 * v / c**2)
v1 - speed of the object relative to a moving frame
v - speed of the moving frame
c - speed of light in the vacuum
v2 - speed of the object relative to an observer
"""


def relativistic_velocity_summation(
    object_velocity: float, frame_velocity: float
) -> float:
    """
    >>> relativistic_velocity_summation(200000000, 200000000)
    276805111.0636436
    >>> relativistic_velocity_summation(299792458, 100000000)
    299792458.0
    >>> relativistic_velocity_summation(100000000, 299792458)
    Traceback (most recent call last):
        ...
    ValueError: Speeds must not exceed light speed...
    """
    if (object_velocity > c or frame_velocity >= c or 
        object_velocity < -c or frame_velocity <= -c):
        raise ValueError(
            "Speeds must not exceed light speed, and "
            "the frame speed must be lower than the light speed!"
        )
    numerator = object_velocity + frame_velocity
    denominator = 1 + object_velocity * frame_velocity / c**2
    return numerator / denominator


if __name__ == "__main__":
    from doctest import testmod

    testmod()
