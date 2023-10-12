# Atomical Length Unit Conversion

# REFRENCE  = https://en.wikipedia.org/wiki/Orders_of_magnitude_(length)


def convert_to_meters(value, unit):
    """
    Converts a length value from a given unit to meters.

    Available units:
    - cm (centimeter)
    - mm (millimeter)
    - μm (micrometer)
    - nm (nanometer)
    - A  (angstrom
    - pm (picometer)
    - fm (femtometer)
    - am (attometer)
    - zm (zeptometer)
    - ym (yoctometer)

    >>> convert_to_meters(5, "mm")
    0.005
    >>> convert_to_meters(100, "cm")
    1.0
    >>> convert_to_meters(3, "fm")
    3e-15
    >>> convert_to_meters(42, "invalid_unit")
    'Invalid unit'
    """

    conversions = {
        "cm": 0.01,
        "mm": 0.001,
        "μm": 1e-6,
        "nm": 1e-9,
        "A": 1e-10,
        "pm": 1e-12,
        "fm": 1e-15,
        "am": 1e-18,
        "zm": 1e-21,
        "ym": 1e-24,
    }

    if unit in conversions:
        return value * conversions[unit]
    else:
        return "Invalid unit"


# Function call example
value = 10  # Replace with  value
unit = "nm"  # Replace with  unit
result = convert_to_meters(value, unit)
if isinstance(result, str):
    print(result)
else:
    print(f"{value} {unit} is equal to {result} meters.")

if __name__ == "__main__":
    from doctest import testmod

    testmod()
