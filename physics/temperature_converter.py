"""
Title: Temperature Converter
Description:
    This program converts the temperature from Celsius to Fahrenheit and vice versa.
    The user is asked to enter the temperature in Celsius or Fahrenheit
    and the program converts it to the other unit.
    The formula for conversion is:
    F = (9/5)*C + 32
    C = (F-32)*5/9
"""


def temperature_convertor(choice: int, temperature_unit: float) -> float:
    """
    Args:
        choice: 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius
        temperature_unit: temperature in Celsius or Fahrenheit

    Returns:
        temperature in Celsius or Fahrenheit

    >>> temperature_convertor(choice=1,temperature_unit=0)
    32.0
    >>> temperature_convertor(choice=2,temperature_unit=32)
    0.0
    """
    if choice == 1:
        celsius = temperature_unit
        fahrenheit = (9 / 5) * celsius + 32
        return fahrenheit
    elif choice == 2:
        fahrenheit = temperature_unit
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    else:
        raise ValueError("Only choice 1 or 2 is allowed")


if __name__ == "__main__":
    import doctest

    # run tests
    doctest.testmod()
