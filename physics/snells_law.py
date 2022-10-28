import math

"""
 Snell's Law: sin i/sin r = n2/n1
 Objective: To find the angle of refraction in degrees using the given information

Snell's law is a formula used to describe the relationship between the angles of incidence and refraction, when referring to light or other waves passing through a boundary between two different isotropic media, such as water, glass, or air. This law was named after the Dutch astronomer and mathematician Willebrord Snellius (also called Snell).

In optics, the law is used in ray tracing to compute the angles of incidence or refraction, and in experimental optics to find the refractive index of a material. The law is also satisfied in meta-materials, which allow light to be bent "backward" at a negative angle of refraction with a negative refractive index.

Snell's law states that, for a given pair of media, the ratio of the sines of angle of incidence ({\\displaystyle \theta _{1}}\theta_1 ) and angle of refraction ({\\displaystyle \theta _{2}}{\\displaystyle \theta _{2}}) is equal to the refractive index of the second medium w.r.t the first (n21) which is equal to the ratio of the refractive indices (n2/n1) of the two media, or equivalently, to the ratio of the phase velocities (v1/v2) in the two media.[1]

{\\displaystyle {\frac {\\sin \theta _{1}}{\\sin \theta _{2}}}=n_{21}={\frac {n_{2}}{n_{1}}}={\frac {v_{1}}{v_{2}}}}{\\displaystyle {\frac {\\sin \theta _{1}}{\\sin \theta _{2}}}=n_{21}={\frac {n_{2}}{n_{1}}}={\frac {v_{1}}{v_{2}}}}

Reference: https://en.wikipedia.org/wiki/Snell%27s_law
"""


def snell(i: float, n1: float, n2: float) -> float:
    """
    >>> round(snell(25,2,1),2)
    57.70
    >>> round(snell(30,1,2),2)
    14.48
    >>> round(snell(56.52,2,3),2)
    0.01
    >>> round(snell(19.9,2.33,1.5),2)
    31.92
    >>> round(snell(45,1.88,2.99),2)
    26.40

    """
    if i == 90 or n1 == n2:
        raise ValueError("Snell's law is not valid in this case!")
    return round((math.asin(math.sin(math.radians(i)) * n1) / n2), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="snell")
