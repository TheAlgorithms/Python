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

# v is in m/s
# wavelength is in meters
# frequency is in Hz
calc_to_do = random.randint(1, 3)


def wave_formula(calc_to_do: int) -> float:
    # function only leaves a side effect, no return
    # just returning a string to not cause errors
    global wavelength, v, frequency

    """
    Random Wave Equation Selected

    Wavelength = Wave Speed / Frequency    |
    Wavelength = 97 / 30                   |
    Wavelength = 3.2333333333333334m       |
    """

    if calc_to_do == 1:

        wavelength = random.randint(1, 100)
        frequency = random.randint(1, 100)
        v = wavelength * frequency
        v_str = str(v)
        wavelength_str = str(wavelength)
        frequency_str = str(frequency)

        print(
            f"""
Wave Speed = Wavelength * Frequency
v = {wavelength_str} * {frequency_str}
v = {v_str}m/s
"""
        )

    if calc_to_do == 2:
        v = random.randint(1, 100)
        frequency = random.randint(1, 100)
        wavelength = v / frequency
        v_str = str(v)
        wavelength_str = str(wavelength)
        frequency_str = str(frequency)

        print(
            f"""
Wavelength = Wave Speed / Frequency
Wavelength = {v_str} / {frequency_str}
Wavelength = {wavelength_str}m
"""
        )

    if calc_to_do == 3:

        v = random.randint(1, 100)
        wavelength = random.randint(1, 100)
        frequency = v / wavelength
        v_str = str(v)
        wavelength_str = str(wavelength)
        frequency_str = str(frequency)

        print(
            f"""
Frequency = Wave Speed / Wavelength
Frequency = {v_str} / {wavelength_str}
Frequency = {frequency_str}Hz
"""
        )
    return v, wavelength, frequency


wave_formula(calc_to_do)
