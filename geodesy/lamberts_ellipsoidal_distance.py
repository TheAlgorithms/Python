from math import atan, cos, radians, sin, tan
from haversine_distance import haversine_distance


def lamberts_ellipsoidal_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:

    """
    Calculate the shortest distance along the surface of an ellipsoid between
    two points on the surface of earth given longitudes and latitudes
    https://en.wikipedia.org/wiki/Geographical_distance#Lambert's_formula_for_long_lines

    NOTE: This algorithm uses geodesy/haversine_distance.py to compute central angle,
        sigma

    Representing the earth as an ellipsoid allows us to approximate distances between
    points on the surface much better than a sphere. Ellipsoidal formulas treat the
    Earth as an oblate ellipsoid which means accounting for the flattening that happens
    at the North and South poles. Lambert's formulae provide accuracy on the order of
    10 meteres over thousands of kilometeres. Other methods can provide
    millimeter-level accuracy but this is a simpler method to calculate long range
    distances without increasing computational intensity.

    Args:
        lat1, lon1: latitude and longitude of coordinate 1
        lat2, lon2: latitude and longitude of coordinate 2
    Returns:
        geographical distance between two points in metres

    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> NEW_YORK = point_2d(40.713019, -74.012647)
    >>> VENICE = point_2d(45.443012, 12.313071)
    >>> f"{lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meters"
    '254,351 meters'
    >>> f"{lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *NEW_YORK):0,.0f} meters"
    '4,138,992 meters'
    >>> f"{lamberts_ellipsoidal_distance(*SAN_FRANCISCO, *VENICE):0,.0f} meters"
    '9,737,326 meters'
    """

    # CONSTANTS per WGS84 https://en.wikipedia.org/wiki/World_Geodetic_System
    # Distance in metres(m)
    AXIS_A = 6378137.0
    AXIS_B = 6356752.314245
    EQUATORIAL_RADIUS = 6378137

    # Equation Parameters
    # https://en.wikipedia.org/wiki/Geographical_distance#Lambert's_formula_for_long_lines
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    # Parametric latitudes
    # https://en.wikipedia.org/wiki/Latitude#Parametric_(or_reduced)_latitude
    b_lat1 = atan((1 - flattening) * tan(radians(lat1)))
    b_lat2 = atan((1 - flattening) * tan(radians(lat2)))

    # Compute central angle between two points
    # using haversine theta. sigma =  haversine_distance / equatorial radius
    sigma = haversine_distance(lat1, lon1, lat2, lon2) / EQUATORIAL_RADIUS

    # Intermediate P and Q values
    P_value = (b_lat1 + b_lat2) / 2
    Q_value = (b_lat2 - b_lat1) / 2

    # Intermediate X value
    # X = (sigma - sin(sigma)) * sin^2Pcos^2Q / cos^2(sigma/2)
    X_numerator = (sin(P_value) ** 2) * (cos(Q_value) ** 2)
    X_demonimator = cos(sigma / 2) ** 2
    X_value = (sigma - sin(sigma)) * (X_numerator / X_demonimator)

    # Intermediate Y value
    # Y = (sigma + sin(sigma)) * cos^2Psin^2Q / sin^2(sigma/2)
    Y_numerator = (cos(P_value) ** 2) * (sin(Q_value) ** 2)
    Y_denominator = sin(sigma / 2) ** 2
    Y_value = (sigma + sin(sigma)) * (Y_numerator / Y_denominator)

    return EQUATORIAL_RADIUS * (sigma - ((flattening / 2) * (X_value + Y_value)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
