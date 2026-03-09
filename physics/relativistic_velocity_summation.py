c = 299792458

"""
The relativistic velocity summation formula calculates the combined velocity v2
of an object moving at speed v1 relative to a frame that is itself moving at velocity v
relative to an observer. I take the last one to be strictly lower than the speed of
light.
The formula is v2 = (v1 + v)/(1 + v1 * v / c^2)
"""


def relativistic_velocity_summation(v1: float, v: float) -> float:
    """
    >>> relativistic_velocity_summation(200000000, 200000000)
    276805111.0636436
    >>> relativistic_velocity_summation(299792458, 100000000)
    299792458.0
    >>> relativistic_velocity_summation(100000000, 299792458)
    Traceback (most recent call last):
        ...
    ValueError: Speeds must not exceed light speed, and the frame speed must be lower than the light speed!
    """
    if v1 > c or v >= c or v1 < -c or v <= -c:
        raise ValueError(
            "Speeds must not exceed light speed, and the frame speed must be lower than the light speed!"
        )
    return (v1 + v) / (1 + v1 * v / (c * c))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
