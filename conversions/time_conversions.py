"""
USAGE :
This function can be used for the following purposes:
1. Unit conversion
2. Standardization
3. Problem solving
4. Educational purposes



REFERENCES :

https://en.wikipedia.org/wiki/Unit_of_time
https://en.wikipedia.org/wiki/Time

"""


def convert_time(time, from_unit, to_unit):
    units = {"s": 1, "min": 60, "h": 3600, "d": 86400}

    if from_unit in units and to_unit in units:
        conversion_factor = units[from_unit] / units[to_unit]
        converted_time = time * conversion_factor
        return converted_time
    else:
        return "Invalid units provided."


"""
convert_time(60, s, min)
->1.0

convert_time(60,min,h)
->1.0
"""
