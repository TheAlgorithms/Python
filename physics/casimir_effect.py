"""
Title : Finding the value of magnitude of either the Casimir force, the surface area
of one of the plates or distance between the plates provided that the other
two parameters are given.

Description : In quantum field theory, the Casimir effect is a physical force
acting on the macroscopic boundaries of a confined space which arises from the
quantum fluctuations of the field. It is a physical force exerted between separate
objects, which is due to neither charge, gravity, nor the exchange of particles,
but instead is due to resonance of all-pervasive energy fields in the intervening
space between the objects. Since the strength of the force falls off rapidly with
distance it is only measurable when the distance between the objects is extremely
small. On a submicron scale, this force becomes so strong that it becomes the
dominant force between uncharged conductors.

Dutch physicist Hendrik B. G. Casimir first proposed the existence of the force,
and he formulated an experiment to detect it in 1948 while participating in research
at Philips Research Labs. The classic form of his experiment used a pair of uncharged
parallel metal plates in a vacuum, and successfully demonstrated the force to within
15% of the value he had predicted according to his theory.

The Casimir force F for idealized, perfectly conducting plates of surface area
A square meter and placed at a distance of a meter apart with vacuum between
them is expressed as -

F = - ((Reduced Planck Constant ℏ) * c * Pi^2 * A) / (240 * a^4)

Here, the negative sign indicates the force is attractive in nature. For the ease
of calculation, only the magnitude of the force is considered.

Source :
- https://en.wikipedia.org/wiki/Casimir_effect
- https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/c/Casimir_effect.htm
- Casimir, H. B. ; Polder, D. (1948) "The Influence of Retardation on the
  London-van der Waals Forces", Physical Review, vol. 73, Issue 4, pp. 360-372
"""

from __future__ import annotations

from math import pi

# Define the Reduced Planck Constant ℏ (H bar), speed of light C, value of
# Pi and the function
REDUCED_PLANCK_CONSTANT = 1.054571817e-34  # unit of ℏ : J * s

SPEED_OF_LIGHT = 3e8  # unit of c : m * s^-1


def casimir_force(force: float, area: float, distance: float) -> dict[str, float]:
    """
    Input Parameters
    ----------------
    force -> Casimir Force : magnitude in Newtons

    area -> Surface area of each plate : magnitude in square meters

    distance -> Distance between two plates : distance in Meters

    Returns
    -------
    result : dict name, value pair of the parameter having Zero as it's value

    Returns the value of one of the parameters specified as 0, provided the values of
    other parameters are given.
    >>> casimir_force(force = 0, area = 4, distance = 0.03)
    {'force': 6.4248189174864216e-21}

    >>> casimir_force(force = 2635e-13, area = 0.0023, distance = 0)
    {'distance': 1.0323056015031114e-05}

    >>> casimir_force(force = 2737e-21, area = 0, distance = 0.0023746)
    {'area': 0.06688838837354052}

    >>> casimir_force(force = 3457e-12, area = 0, distance = 0)
    Traceback (most recent call last):
        ...
    ValueError: One and only one argument must be 0

    >>> casimir_force(force = 3457e-12, area = 0, distance = -0.00344)
    Traceback (most recent call last):
        ...
    ValueError: Distance can not be negative

    >>> casimir_force(force = -912e-12, area = 0, distance = 0.09374)
    Traceback (most recent call last):
        ...
    ValueError: Magnitude of force can not be negative
    """

    if (force, area, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if force < 0:
        raise ValueError("Magnitude of force can not be negative")
    if distance < 0:
        raise ValueError("Distance can not be negative")
    if area < 0:
        raise ValueError("Area can not be negative")
    if force == 0:
        force = (REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2 * area) / (
            240 * (distance) ** 4
        )
        return {"force": force}
    elif area == 0:
        area = (240 * force * (distance) ** 4) / (
            REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2
        )
        return {"area": area}
    elif distance == 0:
        distance = (
            (REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2 * area) / (240 * force)
        ) ** (1 / 4)
        return {"distance": distance}
    raise ValueError("One and only one argument must be 0")


# Run doctest
if __name__ == "__main__":
    import doctest

    doctest.testmod()
