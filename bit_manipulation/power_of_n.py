# Assign values to author and version.
__author__ = "Himanshu Gupta"
__version__ = "1.0.0"
__date__ = "2023-09-03"

def binary_exponentiation(number: float, power: int) -> float:
    """
    Function to calculate number raised to the power (i.e., number^power) where number is a float number and power is an integer and it will return float value

    >>> binary_exponentiation(2.00000, 10)
    1024.0

    >>> binary_exponentiation(2.10000, 3)
    9.261000000000001

    >>> binary_exponentiation(2.00000, -2)
    0.25
    """

    if power == 0:
        return 1

    # Handle case where, power < 0.
    if power < 0:
        power = -1 * power
        number = 1.0 / number

    # Perform Binary Exponentiation.
    result = 1
    while power != 0:
        # If 'power' is odd we multiply result with 'number' and reduce 'power' by '1'.
        if power % 2 == 1:
            result *= number
            power -= 1
        # We square 'number' and reduce 'power' by half, number^power => (number^2)^(power/2).
        number *= number
        power //= 2
    return result


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()