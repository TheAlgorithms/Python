import random

# Wave Formula Calculations / Formulas Related to waves

"""
Physics Classroom :-
https://www.physicsclassroom.com/class/waves/Lesson-2/The-Wave-Equation
Background:
The Wave Formulas are for calculating the characteristics
of a wave.

Used for stuff like the:-

1. Speed of a wave in water
2. Frequency of wave a in air
3. Frequency of an electromagnetic - basically like light - wave

Note:- Above are just some of the many cases this formula can be applied to.

This calculator is not really meant for light.
It can be used for it, just know that you will need to input the speed of light
again and again because no constant has been assigned to it.

Not sure if this can work for really big numbers.
"""


# ----- Demo -----#

# Initializing variables to 0
v = 0.0  # in m/s
wavelength = 0.0  # in meters
frequency = 0.0  # in Hz
ans = 0.0
calc_to_do = random.randint(1, 3)


def wave_formula(calc_to_do: int) -> float:
    global wavelength, v, frequency, ans

    """
    Inputs/Vars to be used
    ----------------------
    v : Velocity in m/s

    wavelength : distance between
        2 crests, or troughs of a wave, 1 complete cycle
        of a wave in meters

    frequency : cycles/second in Hz


    Returns
    -------
    v, or wavelength, or frequency depending on the situation in
    var ans

    >>> wavelength=5 * frequency=5
    v = 25
    """

    if calc_to_do == 1:

        wavelength = random.randint(1, 100)
        frequency = random.randint(1, 100)
        v = wavelength * frequency
        # v_str = str(v)
        # wavelength_str = str(wavelength)
        # frequency_str = str(frequency)
        ans = v

    if calc_to_do == 2:
        v = random.randint(1, 100)
        frequency = random.randint(1, 100)
        wavelength = v / frequency
        # v_str = str(v)
        # wavelength_str = str(wavelength)
        # frequency_str = str(frequency)
        ans = wavelength

    if calc_to_do == 3:

        v = random.randint(1, 100)
        wavelength = random.randint(1, 100)
        frequency = v / wavelength
        # v_str = str(v)
        # wavelength_str = str(wavelength)
        # frequency_str = str(frequency)
        ans = frequency

    return {"Ans": ans}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
