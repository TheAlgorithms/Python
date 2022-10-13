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

v = 0  # Wave Speed/Velocity
wavelength = 0
frequency = 0

# Constant
CALC_TO_DO_STATEMENT = """
Would you like to :-
1. Calculate Speed of a Wave
2. Calculate Wavelength of a Wave
3. Calculate Frequency of a Wave

Input 1, 2, 3 or three for the respective wave calculation.
> """

calc_to_do = input(CALC_TO_DO_STATEMENT)

while type(calc_to_do) != int:
    if calc_to_do == "1" or calc_to_do == "2" or calc_to_do == "3":
        calc_to_do = int(calc_to_do)
    else:
        print("Choice out of scope")
        calc_to_do = input(CALC_TO_DO_STATEMENT)

if calc_to_do == 1:

    wavelength = float(input("Enter the wavelength of the wave (meters): "))
    while wavelength <= 0:
        print("Wavelength must be greater than zero.")
        wavelength = float(input("Enter the wavelength of the wave (meters): "))

    frequency = float(input("Enter the frequency of the wave (Hz): "))
    while frequency <= 0:
        print("Frequency must be greater than zero.")
        frequency = float(input("Enter the Frequency of the wave (Hz): ")) 

    # Wave Speed Formula
    v = wavelength * frequency

    # To remove pesky decimal point from values like 25.0
    if "." in str(v):
        v = int(v)
    print("Wave Speed =", str(v) + 'm/s')

if calc_to_do == 2:

    v = float(input("Enter the speed of the wave (meters/second): "))
    while v <= 0:
        print("Speed must be greater than zero.")
        v = float(input("Enter the Speed of the wave (meters/second): "))

    frequency = float(input("Enter the frequency of the wave (Hz): "))
    while frequency <= 0:
        print("Frequency must be greater than zero.")
        frequency = float(input("Enter the Frequency of the wave (Hz): ")) 

    # Wavelength Formula
    wavelength = v / frequency
    if "." in str(wavelength):
        wavelength = int(wavelength)
    print("Wavelength =", str(wavelength) + "m")

if calc_to_do == 3:

    v = float(input("Enter the speed of the wave (meters/second): "))
    while v <= 0:
        print("Speed must be greater than zero.")
        v = float(input("Enter the Speed of the wave (meters/second): "))

    wavelength = float(input("Enter the wavelength of the wave (meters): "))
    while wavelength <= 0:
        print("Wavelength must be greater than zero.")
        wavelength = float(input("Enter the wavelength of the wave (meters): "))
    
    # Frequency Formula
    frequency = v / wavelength
    if "." in str(frequency):
        frequency = int(frequency)
    print("Frequency =", str(frequency) + "Hz")   