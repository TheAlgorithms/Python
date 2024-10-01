from math import asin, cos, radians, sin, sqrt


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points
    on the Earth specified by latitude and longitude using
    the Haversine formula.

    Args:
        lat1, lon1: Latitude and longitude of point 1 in decimal degrees.
        lat2, lon2: Latitude and longitude of point 2 in decimal degrees.


    Returns:
        Distance between the two points in meters.

    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> f"{haversine_distance(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meters"
    '254,033 meters'
    """

    radius = 6378137  # earth radius (meters)

    lat1_rad = radians(lat1)
    lat2_rad = radians(lat2)
    delta_lat = radians(lat2 - lat1)
    delta_lon = radians(lon2 - lon1)

    # Haversine formula
    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2) ** 2
    )
    c = 2 * asin(sqrt(a))

    # Great-Circle Distance
    return radius * c


if __name__ == "__main__":
    import doctest

    doctest.testmod()
