"""Convert a Decimal Number to an Octal Number."""

import math

# Modified from:
# https://github.com/TheAlgorithms/Javascript/blob/master/Conversions/DecimalToOctal.js


def decimal_to_octal(num):
    """Convert a Decimal Number to an Octal Number."""
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.pow(10, counter))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        # This formatting removes trailing '.0' from `octal`.
    return'{0:g}'.format(float(octal))


def main():
    """Print octal equivelents of decimal numbers."""
    print("\n2 in octal is:")
    print(decimal_to_octal(2))  # = 2
    print("\n8 in octal is:")
    print(decimal_to_octal(8))  # = 10
    print("\n65 in octal is:")
    print(decimal_to_octal(65))  # = 101
    print("\n216 in octal is:")
    print(decimal_to_octal(216))  # = 330
    print("\n512 in octal is:")
    print(decimal_to_octal(512))  # = 1000
    print("\n")


if __name__ == '__main__':
    main()
