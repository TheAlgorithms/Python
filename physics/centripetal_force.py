"""
Description : Centripetal force is the force acting on an object in
curvilinear motion directed towards the axis of rotation
or centre of curvature.

The unit of centripetal force is newton.

The centripetal force is always directed perpendicular to the
direction of the object’s displacement. Using Newton’s second
law of motion, it is found that the centripetal force of an object
moving in a circular path always acts towards the centre of the circle.
The Centripetal Force Formula is given as the product of mass (in kg)
and tangential velocity (in meters per second) squared, divided by the
radius (in meters) that implies that on doubling the tangential velocity,
the centripetal force will be quadrupled. Mathematically it is written as:
F = mv²/r
Where, F is the Centripetal force, m is the mass of the object, v is the
speed or velocity of the object and r is the radius.

Reference: https://byjus.com/physics/centripetal-and-centrifugal-force/
"""


def centripetal(mass: float, velocity: float, radius: float) -> float:
    """
    The Centripetal Force formula is given as: (m*v*v)/r

    >>> round(centripetal(15.5,-30,10),2)
    1395.0
    >>> round(centripetal(10,15,5),2)
    450.0
    >>> round(centripetal(20,-50,15),2)
    3333.33
    >>> round(centripetal(12.25,40,25),2)
    784.0
    >>> round(centripetal(50,100,50),2)
    10000.0
    """
    if mass < 0:
        raise ValueError("The mass of the body cannot be negative")
    if radius <= 0:
        raise ValueError("The radius is always a positive non zero integer")
    return (mass * (velocity) ** 2) / radius


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
