from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS = 6371000


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate great circle distance between two points on a sphere,
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
        lat1: latitude of coordinate 1 in degrees
        lon1: longitude of coordinate 1 in degrees
        lat2: latitude of coordinate 2 in degrees
        lon2: longitude of coordinate 2 in degrees
    Returns:
        geographical distance between two points in metres

    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> f"{haversine_distance(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meters"
    '253,748 meters'
    >>> NEW_YORK = point_2d(40.712776, -74.005974)
    >>> LOS_ANGELES = point_2d(34.052235, -118.243683)
    >>> f"{haversine_distance(*NEW_YORK, *LOS_ANGELES):0,.0f} meters"
    '3,935,746 meters'
    >>> LONDON = point_2d(51.507351, -0.127758)
    >>> PARIS = point_2d(48.856614, 2.352222)
    >>> f"{haversine_distance(*LONDON, *PARIS):0,.0f} meters"
    '343,549 meters'
    >>> haversine_distance(0, 0, 0, 0)
    0.0
    >>> from math import isclose
    >>> quarter_equator = haversine_distance(0, 0, 0, 90)
    >>> isclose(quarter_equator, 10_007_543, rel_tol=1e-3)
    True
    """
    # Convert geodetic coordinates from degrees to radians.
    # The Haversine formula operates on a sphere, so we use the raw geodetic
    # latitudes directly rather than reduced latitudes (which apply to
    # ellipsoidal models like Lambert's formula).
    # Reference: https://en.wikipedia.org/wiki/Haversine_formula#Formulation
    phi_1 = radians(lat1)
    phi_2 = radians(lat2)
    lambda_1 = radians(lon1)
    lambda_2 = radians(lon2)

    # Haversine equation
    sin_sq_phi = sin((phi_2 - phi_1) / 2)
    sin_sq_lambda = sin((lambda_2 - lambda_1) / 2)
    sin_sq_phi *= sin_sq_phi
    sin_sq_lambda *= sin_sq_lambda
    h_value = sqrt(sin_sq_phi + (cos(phi_1) * cos(phi_2) * sin_sq_lambda))
    return 2 * EARTH_RADIUS * asin(h_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
