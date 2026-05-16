"""
This module contains the functions to calculate the focal length, object distance
and image distance of a mirror.

The mirror formula is an equation that relates the object distance (u),
image distance (v), and focal length (f) of a spherical mirror.
It is commonly used in optics to determine the position and characteristics
of an image formed by a mirror. It is expressed using the formulae :

-------------------
| 1/f = 1/v + 1/u |
-------------------

Where,
f = Focal length of the spherical mirror (metre)
v = Image distance from the mirror (metre)
u = Object distance from the mirror (metre)


The signs of the distances are taken with respect to the sign convention.
The sign convention is as follows:
    1) Object is always placed to the left of mirror
    2) Distances measured in the direction of the incident ray are positive
    and the distances measured in the direction opposite to that of the incident
    rays are negative.
    3) All distances are measured from the pole of the mirror.


There are a few assumptions that are made while using the mirror formulae.
They are as follows:
    1) Thin Mirror: The mirror is assumed to be thin, meaning its thickness is
    negligible compared to its radius of curvature. This assumption allows
    us to treat the mirror as a two-dimensional surface.
    2) Spherical Mirror: The mirror is assumed to have a spherical shape. While this
    assumption may not hold exactly for all mirrors, it is a reasonable approximation
    for most practical purposes.
    3) Small Angles: The angles involved in the derivation are assumed to be small.
    This assumption allows us to use the small-angle approximation, where the tangent
    of a small angle is approximately equal to the angle itself. It simplifies the
    calculations and makes the derivation more manageable.
    4) Paraxial Rays: The mirror formula is derived using paraxial rays, which are
    rays that are close to the principal axis and make small angles with it. This
    assumption ensures that the rays are close enough to the principal axis, making the
    calculations more accurate.
    5) Reflection and Refraction Laws: The derivation assumes that the laws of
    reflection and refraction hold.
    These laws state that the angle of incidence is equal to the angle of reflection
    for reflection, and the incident and refracted rays lie in the same plane and
    obey Snell's law for refraction.

(Description and Assumptions adapted from
https://www.collegesearch.in/articles/mirror-formula-derivation)

(Sign Convention adapted from
https://www.toppr.com/ask/content/concept/sign-convention-for-mirrors-210189/)


"""


def focal_length(distance_of_object: float, distance_of_image: float) -> float:
    """
    >>> from math import isclose
    >>> isclose(focal_length(10, 20), 6.66666666666666)
    True
    >>> from math import isclose
    >>> isclose(focal_length(9.5, 6.7), 3.929012346)
    True
    >>> focal_length(0, 20)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """

    if distance_of_object == 0 or distance_of_image == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    focal_length = 1 / ((1 / distance_of_object) + (1 / distance_of_image))
    return focal_length


def object_distance(focal_length: float, distance_of_image: float) -> float:
    """
    >>> from math import isclose
    >>> isclose(object_distance(30, 20), -60.0)
    True
    >>> from math import isclose
    >>> isclose(object_distance(10.5, 11.7), 102.375)
    True
    >>> object_distance(90, 0)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """

    if distance_of_image == 0 or focal_length == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    object_distance = 1 / ((1 / focal_length) - (1 / distance_of_image))
    return object_distance


def image_distance(focal_length: float, distance_of_object: float) -> float:
    """
    >>> from math import isclose
    >>> isclose(image_distance(10, 40), 13.33333333)
    True
    >>> from math import isclose
    >>> isclose(image_distance(1.5, 6.7), 1.932692308)
    True
    >>> image_distance(0, 0)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """

    if distance_of_object == 0 or focal_length == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    image_distance = 1 / ((1 / focal_length) - (1 / distance_of_object))
    return image_distance
