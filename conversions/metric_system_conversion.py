"""
Conversions from the International Metric System
"""
import sys


def m_to_cm(meters):
    """
    Print the conversion from meters to centimeters
    >>> m_to_cm(5)
    23.0 m = 2300.0 cm
    >>> m_to_cm(12)
    421.0 m = 42100.0 cm
    >>> m_to_cm(2.36)
    2.36 m = 236.0 cm
    """
    centimeters = meters * 100
    result = f"{meters} m = {centimeters} cm"
    return result


def cm_to_m(centimeters):
    """
    Print the conversion from centimeters to meters
    >>> cm_to_m(5)
    5.0 cm = 0.05 m
    >>> cm_to_m(135) 
    135.0 cm = 1.35 m
    >>> cm_to_m(11235.125)
    11235.125 cm = 112.35125 m
    """
    meters = centimeters / 100
    result = f"{centimeters} cm = {meters} m"
    return result


def default():
    return "unvalid option"


def menu():
    print("SELECT AN OPTION:")
    print("1) Meters to Centimeters")
    print("2) Centimeters to Meters")


""""Using a dictionary for switching"""
def switch(case):

    if case == 0:
        sys.exit()
        pass

    print("Numbre to convert:")
    number = float(input().strip())
    switch_opciones = {
        1: m_to_cm(number),
        2: cm_to_m(number)
    }

    return switch_opciones.get(case, default())


if __name__ == "__main__":

    while True:
        print("\nInternational Metric System Conversions")
        print("Press '0' to exit")
        menu()
        case = int(input().strip())
        print(switch(case))
