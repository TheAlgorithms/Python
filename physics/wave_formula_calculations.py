# Wave Formula Calculations

"""
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

# Formula components are strings so that its easier to print them out
v = ""  # Wave Speed/Velocity
wavelength = ""
frequency = ""

# Constant
CALC_TO_DO_STATEMENT = """
Would you like to :-
1. Calculate Speed of a Wave
2. Calculate Wavelength of a Wave
3. Calculate Frequency of a Wave

Input 1, 2, 3 for the respective wave calculation.
> """

calc_to_do_input = input(CALC_TO_DO_STATEMENT)

while type(calc_to_do_input) != int:
    if calc_to_do_input == "1" or calc_to_do_input == "2" or calc_to_do_input == "3":
        calc_to_do = int(calc_to_do_input)
        break
    else:
        print("\nChoice out of scope")
        calc_to_do_input = input(CALC_TO_DO_STATEMENT)

if calc_to_do == 1:

    wavelength_input = float(input("Enter the wavelength of the wave (meters): "))
    while wavelength_input <= 0:
        print("Wavelength must be greater than zero.")
        wavelength_input = float(input("Enter the wavelength of the wave (meters): "))

    frequency_input = float(input("Enter the frequency of the wave (Hz): "))
    while frequency_input <= 0:
        print("Frequency must be greater than zero.")
        frequency_input = float(input("Enter the Frequency of the wave (Hz): "))

    # Wave Speed Formula
    calced_v = wavelength_input * frequency_input
    v = str(calced_v)
    print("Wave Speed =", v + "m/s")

if calc_to_do == 2:

    v_input = float(input("Enter the speed of the wave (meters/second): "))
    while v_input <= 0:
        print("Speed must be greater than zero.")
        v_input = float(input("Enter the Speed of the wave (meters/second): "))

    frequency_input = float(input("Enter the frequency of the wave (Hz): "))
    while frequency_input <= 0:
        print("Frequency must be greater than zero.")
        frequency_input = float(input("Enter the Frequency of the wave (Hz): "))

    # Wavelength Formula
    calced_wavelength = v_input / frequency_input
    wavelength = str(calced_wavelength)
    print("Wavelength =", wavelength + "m")

if calc_to_do == 3:

    v_input = float(input("Enter the speed of the wave (meters/second): "))
    while v_input <= 0:
        print("Speed must be greater than zero.")
        v_input = float(input("Enter the Speed of the wave (meters/second): "))

    wavelength_input = float(input("Enter the wavelength of the wave (meters): "))
    while wavelength_input <= 0:
        print("Wavelength must be greater than zero.")
        wavelength_input = float(input("Enter the wavelength of the wave (meters): "))

    # Frequency Formula
    calced_frequency = v_input / wavelength_input
    frequency = str(calced_frequency)
    print("Frequency =", frequency + "Hz")
