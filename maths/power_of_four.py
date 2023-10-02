# Created by Pronay Debnath
# Date:- 2/10/2023
# Power of four using logarithm


import math
import doctest

def is_power_of_four(n):
    """
    Determine if an integer is a power of four.

    Args:
    n (int): The integer to check.

    Returns:
    bool: True if n is a power of four, False otherwise.

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
    return n > 0 and math.log(n, 4).is_integer()

if __name__ == "__main__":
    doctest.testmod()
    
    n = int(input("Enter an integer: "))
    result = is_power_of_four(n)
    
    if result:
        print("True")
    else:
        print("False")
