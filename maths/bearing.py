"""
Initial bearing (forward azimuth) between two geographic points.

Points are (latitude, longitude) in decimal degrees. Returns bearing in degrees
clockwise from true north in the range [0, 360).

Reference: https://en.wikipedia.org/wiki/Bearing_(navigation)
"""

from __future__ import annotations

import math


def initial_bearing(
    origin: tuple[float, float], destination: tuple[float, float]
) -> float:
    """
    Compute the initial bearing from `origin` to `destination`.

    Parameters
    ----------
    origin, destination : tuple[float, float]
        (latitude, longitude) in decimal degrees.

    Returns
    -------
    float
        Initial bearing in degrees, clockwise from north in [0, 360).

    Raises
    ------
    TypeError
        If inputs are not 2-tuples of numbers.
    ValueError
        If the two points are identical (bearing undefined).

    Examples
    >>> round(initial_bearing((50.066389, -5.714722), (58.643889, -3.07)), 3)
    9.12
    >>> round(initial_bearing((0.0, 0.0), (1.0, 1.0)), 3)
    44.996
    >>> initial_bearing((0.0, 0.0), (0.0, 0.0))
    Traceback (most recent call last):
    ...
    ValueError: origin and destination are the same point; bearing is undefined
    """
    try:
        lat1, lon1 = float(origin[0]), float(origin[1])
        lat2, lon2 = float(destination[0]), float(destination[1])
    except Exception as exc:
        raise TypeError(
            "origin and destination must be 2-tuples of numeric values"
        ) from exc

    if lat1 == lat2 and lon1 == lon2:
        raise ValueError(
            "origin and destination are the same point; bearing is undefined"
        )

    # convert degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_lambda = math.radians(lon2 - lon1)

    x = math.sin(delta_lambda) * math.cos(phi2)
    y = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(
        delta_lambda
    )

    theta = math.atan2(x, y)  # result in radians relative to north
    bearing = (math.degrees(theta) + 360.0) % 360.0
    return bearing


if __name__ == "__main__":
    # simple demonstration
    print(initial_bearing((50.066389, -5.714722), (58.643889, -3.07)))
