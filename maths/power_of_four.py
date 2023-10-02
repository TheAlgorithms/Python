# Created by Pronay Debnath
# Date:- 2/10/2023
# Power of four using logarithm

import math
import doctest


def is_power_of_four(number_to_check: int) -> bool:
    """
    Determine if an integer is a power of four.

    Args:
    number_to_check (int): The integer to check.

    Returns:
    bool: True if number_to_check is a power of four, False otherwise.

    Examples:
    >>> is_power_of_four(16)
    True
    >>> is_power_of_four(8)
    False
    >>> is_power_of_four(1)
    True
    >>> is_power_of_four(0)
    False
    """
    return number_to_check > 0 and math.log(number_to_check, 4).is_integer()


if __name__ == "__main__":
    doctest.testmod()
    number_to_check = int(input("Enter an integer: "))
    result = is_power_of_four(number_to_check)
    if result:
        print("The given integer is a power of four.")
    else:
        print("The given integer is not a power of four.")
