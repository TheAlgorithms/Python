import math

"""
Finding the intensity of light transmitted through a polariser using Malus Law
and by taking initial intensity and angle between polariser and axis as input

Description : Malus's law, which is named after Étienne-Louis Malus,
says that when a perfect polarizer is placed in a polarized
beam of light, the irradiance, I, of the light that passes
through is given by
 I=I'cos²θ
where I' is the initial intensity and θ is the angle between the light's
initial polarization direction and the axis of the polarizer.
A beam of unpolarized light can be thought of as containing a
uniform mixture of linear polarizations at all possible angles.
Since the average value of cos²θ is 1/2, the transmission coefficient becomes
I/I' = 1/2
In practice, some light is lost in the polarizer and the actual transmission
will be somewhat lower than this, around 38% for Polaroid-type polarizers but
considerably higher (>49.9%) for some birefringent prism types.
If two polarizers are placed one after another (the second polarizer is
generally called an analyzer), the mutual angle between their polarizing axes
gives the value of θ in Malus's law. If the two axes are orthogonal, the
polarizers are crossed and in theory no light is transmitted, though again
practically speaking no polarizer is perfect and the transmission is not exactly
zero (for example, crossed Polaroid sheets appear slightly blue in colour because
their extinction ratio is better in the red). If a transparent object is placed
between the crossed polarizers, any polarization effects present in the sample
(such as birefringence) will be shown as an increase in transmission.
This effect is used in polarimetry to measure the optical activity of a sample.
Real polarizers are also not perfect blockers of the polarization orthogonal to
their polarization axis; the ratio of the transmission of the unwanted component
to the wanted component is called the extinction ratio, and varies from around
1:500 for Polaroid to about 1:106 for Glan–Taylor prism polarizers.

Reference : "https://en.wikipedia.org/wiki/Polarizer#Malus's_law_and_other_properties"
"""


def malus_law(initial_intensity: float, angle: float) -> float:
    """
    >>> round(malus_law(10,45),2)
    5.0
    >>> round(malus_law(100,60),2)
    25.0
    >>> round(malus_law(50,150),2)
    37.5
    >>> round(malus_law(75,270),2)
    0.0
    >>> round(malus_law(10,-900),2)
    Traceback (most recent call last):
        ...
    ValueError: In Malus Law, the angle is in the range 0-360 degrees
    >>> round(malus_law(10,900),2)
    Traceback (most recent call last):
        ...
    ValueError: In Malus Law, the angle is in the range 0-360 degrees
    >>> round(malus_law(-100,900),2)
    Traceback (most recent call last):
        ...
    ValueError: The value of intensity cannot be negative
    >>> round(malus_law(100,180),2)
    100.0
    >>> round(malus_law(100,360),2)
    100.0
    """

    if initial_intensity < 0:
        raise ValueError("The value of intensity cannot be negative")
        # handling of negative values of initial intensity
    if angle < 0 or angle > 360:
        raise ValueError("In Malus Law, the angle is in the range 0-360 degrees")
        # handling of values out of allowed range
    return initial_intensity * (math.cos(math.radians(angle)) ** 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="malus_law")
