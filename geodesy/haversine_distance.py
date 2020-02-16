from math import asin, atan, cos, sin, sqrt, tan, pow, radians


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate great circle distance between two points in a sphere,
    given longitudes and latitudes. 
    (https://en.wikipedia.org/wiki/Haversine_formula)

    Args:
        lat1, lon1: latitude and longitude of coordinate 1
        lat2, lon2: latitude and longitude of coordinate 2
        
    Returns: 
        geographical distance between two points in metres

    >>> int(haversine_distance(37.774856, -122.424227, 37.864742, -119.537521)) # From SF to Yosemite
    254352

    """

    # CONSTANTS per WGS84 https://en.wikipedia.org/wiki/World_Geodetic_System
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
    sin_sq_phi = pow(sin((phi_2 - phi_1) / 2), 2)
    sin_sq_lambda = pow(sin((lambda_2 - lambda_1) / 2), 2)
    h_value = sqrt(sin_sq_phi + (cos(phi_1) * cos(phi_2) * sin_sq_lambda))

    distance = 2 * RADIUS * asin(h_value)

    return distance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
