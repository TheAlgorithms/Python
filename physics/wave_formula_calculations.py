# Wave Formula Calculations / Formulas Rlated to waves

"""
Physics Classroom - https://www.physicsclassroom.com/class/waves/Lesson-2/The-Wave-Equation
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
v = 0  # in m/s
wavelength = 25  # in meters
frequency = 5  # in Hz

v = wavelength * frequency
# To make output look like actual code
print(
    f"""
Demo:-
v = 0
wavelength = 25
frequency = 5

Now,
Wave Speed (v) = wavelength * frequency
or, v = {wavelength}m * {frequency}Hz
Therefore, v = {v}
"""
)


# ----- Actual Code when used when stuff is inputted ------#

# Formula components are strings so that its easier to print them out
# v = ''  # Wave Speed/Velocity
# wavelength = ''
# frequency = ''

# calc_to_do_in = input("""
# Would you like to :-
# 1. Calculate Speed of a Wave
# 2. Calculate Wavelength of a Wave
# 3. Calculate Frequency of a Wave
#
# Input 1, 2, 3 for the respective wave calculation.
# > """)
#
# while type(calc_to_do_in) != int:
#     if calc_to_do_in == "1" or calc_to_do_in == "2" or calc_to_do_in == "3":
#         calc_to_do = int(calc_to_do_in)
#         break
#     else:
#         print("\nChoice out of scope")
#         calc_to_do_in = input("""
# Would you like to :-
# 1. Calculate Speed of a Wave
# 2. Calculate Wavelength of a Wave
# 3. Calculate Frequency of a Wave

# Input 1, 2, 3 for the respective wave calculation.
# > """)


# if calc_to_do == 1:

#     wavelength_in = float(input("Enter the wavelength of the wave (meters): "))
#     while wavelength_in <= 0:
#         print("Wavelength must be greater than zero.")
#         wavelength_in = float(input("Enter the wavelength of the wave (meters): "))

#     frequency_in = float(input("Enter the frequency of the wave (Hz): "))
#     while frequency_in <= 0:
#         print("Frequency must be greater than zero.")
#         frequency_in = float(input("Enter the Frequency of the wave (Hz): "))
#
#     # Wave Speed Formula
#     calced_v = wavelength_in * frequency_in
#     v = str(calced_v)
#     print("Wave Speed =", v + 'm/s')

# if calc_to_do == 2:

#     v_in = float(input("Enter the speed of the wave (meters/second): "))
#     while v_in <= 0:
#         print("Speed must be greater than zero.")
#         v_in = float(input("Enter the Speed of the wave (meters/second): "))

#     frequency_in = float(input("Enter the frequency of the wave (Hz): "))
#     while frequency_in <= 0:
#         print("Frequency must be greater than zero.")
#         frequency_in = float(input("Enter the Frequency of the wave (Hz): "))

#     # Wavelength Formula
#     calced_wavelength = v_in / frequency_in
#     wavelength = str(calced_wavelength)
#     print("Wavelength =", wavelength + "m")

# if calc_to_do == 3:

#     v_in = float(input("Enter the speed of the wave (meters/second): "))
#     while v_in <= 0:
#         print("Speed must be greater than zero.")
#         v_in = float(input("Enter the Speed of the wave (meters/second): "))

#     wavelength_in = float(input("Enter the wavelength of the wave (meters): "))
#     while wavelength_in <= 0:
#         print("Wavelength must be greater than zero.")
#         wavelength_in = float(input("Enter the wavelength of the wave (meters): "))

#     # Frequency Formula
#     calced_frequency = v_in / wavelength_in
#     frequency = str(calced_frequency)
#     print("Frequency =", frequency + "Hz")
