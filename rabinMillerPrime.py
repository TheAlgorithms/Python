"""
Implementation of the Miller-Rabin Primality Test
@Author : Udit Maherwal
Date : June 4, 2020
Example:
    print(isPrime(143)) >> False
    print(isPrime(11)) >> True
"""


import random
def isPrime(number, certainty = 12):
    """
    :type number: int
    :type certainty: int
    :return: boolean
    """
    assert isinstance(number, int) and (number >= 0), \
        "'number' must been an int and positive"

    if ( number < 2 ):
        return False
    if(number != 2 and (number & 1) == 0):
        return False

    s = number-1

    while((s & 1) == 0):
        s >>= 1
    for _ in range( certainty) :
        r = random.randrange(number-1) + 1
        tmp = s
        mod = pow(r, tmp, number)
        while( tmp != number-1 and mod != 1 and mod != number - 1) :
            mod = (mod*mod) % number
            tmp <<= 1
        if ( mod != number-1 and  ( tmp & 1) == 0):
            return False
    return True

print(isPrime(11))
