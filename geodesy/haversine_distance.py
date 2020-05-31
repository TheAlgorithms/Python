from math import asin, atan, cos, radians, sin, sqrt, tan


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate great circle distance between two points in a sphere,
    given longitudes and latitudes https://en.wikipedia.org/wiki/Haversine_formula

    We know that the globe is "sort of" spherical, so a path between two points
    isn't exactly a straight line. We need to account for the Earth's curvature
    when calculating distance from point A to B. This effect is negligible for
    small distances but adds up as distance increases. The Haversine method treats
    the earth as a sphere which allows us to "project" the two points A and B
    onto the surface of that sphere and approximate the spherical distance between
    them. Since the Earth is not a perfect sphere, other methods which model the
    Earth's ellipsoidal nature are more accurate but a quick and modifiable
    computation like Haversine can be handy for shorter range distances.

    Args:
        lat1, lon1: latitude and longitude of coordinate 1
        lat2, lon2: latitude and longitude of coordinate 2
    Returns:
        geographical distance between two points in metres
    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> f"{haversine_distance(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meters"
    '254,352 meters'
    """
    # CONSTANTS per WGS84 https://en.wikipedia.org/wiki/World_Geodetic_System
    # Distance in metres(m)
    AXIS_A = 6378137.0
    AXIS_B = 6356752.314245
    RADIUS = 6378137
    # Equation parameters
    # Equation https://en.wikipedia.org/wiki/Haversine_formula#Formulation
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    phi_1 = atan((1 - flattening) * tan(radians(lat1)))
    phi_2 = atan((1 - flattening) * tan(radians(lat2)))
    lambda_1 = radians(lon1)
    lambda_2 = radians(lon2)
    # Equation
    sin_sq_phi = sin((phi_2 - phi_1) / 2)
    sin_sq_lambda = sin((lambda_2 - lambda_1) / 2)
    # Square both values
    sin_sq_phi *= sin_sq_phi
    sin_sq_lambda *= sin_sq_lambda
    h_value = sqrt(sin_sq_phi + (cos(phi_1) * cos(phi_2) * sin_sq_lambda))
    return 2 * RADIUS * asin(h_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
