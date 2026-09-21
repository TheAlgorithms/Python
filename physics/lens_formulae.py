"""
This module has functions which calculate focal length of lens, distance of
image from the lens and distance of object from the lens.
The above is calculated using the lens formula.

In optics, the relationship between the distance of the image (v),
the distance of the object (u), and
the focal length (f) of the lens is given by the formula known as the Lens formula.
The Lens formula is applicable for convex as well as concave lenses. The formula
is given as follows:

-------------------
| 1/f = 1/v + 1/u |
-------------------

Where
    f = focal length of the lens in meters.
    v = distance of the image from the lens in meters.
    u = distance of the object from the lens in meters.

To make our calculations easy few assumptions are made while deriving the formula
which are important to keep in mind before solving this equation.
The assumptions are as follows:
    1. The object O is a point object lying somewhere on the principle axis.
    2. The lens is thin.
    3. The aperture of the lens taken must be small.
    4. The angles of incidence and angle of refraction should be small.

Sign convention is a set of rules to set signs for image distance, object distance,
focal length, etc
for mathematical analysis of image formation. According to it:
    1. Object is always placed to the left of lens.
    2. All distances are measured from the optical centre of the mirror.
    3. Distances measured in the direction of the incident ray are positive and
    the distances measured in the direction opposite
    to that of the incident rays are negative.
    4. Distances measured along y-axis above the principal axis are positive and
    that measured along y-axis below the principal
    axis are negative.

Note: Sign convention can be reversed and will still give the correct results.

Reference for Sign convention:
https://www.toppr.com/ask/content/concept/sign-convention-for-lenses-210246/

Reference for assumptions:
https://testbook.com/physics/derivation-of-lens-maker-formula
"""


def focal_length_of_lens(
    object_distance_from_lens: float, image_distance_from_lens: float
) -> float:
    """
    Doctests:
    >>> from math import isclose
    >>> isclose(focal_length_of_lens(10,4), 6.666666666666667)
    True
    >>> from math import isclose
    >>> isclose(focal_length_of_lens(2.7,5.8), -5.0516129032258075)
    True
    >>> focal_length_of_lens(0, 20)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """

    if object_distance_from_lens == 0 or image_distance_from_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    focal_length = 1 / (
        (1 / image_distance_from_lens) - (1 / object_distance_from_lens)
    )
    return focal_length


def object_distance(
    focal_length_of_lens: float, image_distance_from_lens: float
) -> float:
    """
    Doctests:
    >>> from math import isclose
    >>> isclose(object_distance(10,40), -13.333333333333332)
    True

    >>> from math import isclose
    >>> isclose(object_distance(6.2,1.5), 1.9787234042553192)
    True

    >>> object_distance(0, 20)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """

    if image_distance_from_lens == 0 or focal_length_of_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )

    object_distance = 1 / ((1 / image_distance_from_lens) - (1 / focal_length_of_lens))
    return object_distance


def image_distance(
    focal_length_of_lens: float, object_distance_from_lens: float
) -> float:
    """
    Doctests:
    >>> from math import isclose
    >>> isclose(image_distance(50,40), 22.22222222222222)
    True
    >>> from math import isclose
    >>> isclose(image_distance(5.3,7.9), 3.1719696969696973)
    True

    >>> object_distance(0, 20)  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter non zero values with respect
    to the sign convention.
    """
    if object_distance_from_lens == 0 or focal_length_of_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    image_distance = 1 / ((1 / object_distance_from_lens) + (1 / focal_length_of_lens))
    return image_distance
