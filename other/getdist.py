'''
This is the "getdist" module.

The module supplies one function, getdist().  For example,

>>> getdist(52.47608904123904,-1.8896484375000002,51.48822432632349,-0.13183593750000003)
163.0105904573263

The great-circle distance, orthodromic distance, or spherical distance is the distance along a great circle. It is the shortest distance between two points on the surface of a sphere, measured along the surface of the sphere (as opposed to a straight line through the sphere's interior).
WIKI : https://en.wikipedia.org/wiki/Great-circle_distance#:~:text=The%20great%2Dcircle%20distance%2C%20orthodromic,line%20through%20the%20sphere's%20interior).
'''

def getdist(lat1:float,lon1:float,lat2:float,lon2:float) -> float:
    """Return the great circle distance between 2 co-ordinates on earth.

    >>> getdist(52.47608904123904,-1.8896484375000002,51.48822432632349,-0.13183593750000003)
    163.0105904573263
    >>> factorial(30)
    265252859812191058636308480000000
    >>> getdist(1,2,-3e50,2asd)
      File "<stdin>", line 1
        getdist(1,2,-3e50,2asd)
                           ^
    SyntaxError: invalid syntax

    Integers are also accepted, but floats are suggested for accuracy:
    >>> getdist(1,2,3,2)
    222.45966645919728

    Can also handle ridiculously large data:
    >>> getdist(1,2,3e50,2)
    4225.991157779084
    """

    from math import radians, sin, cos, atan2, sqrt
    R = 6373.0
    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
