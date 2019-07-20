'''
Refrences: https://en.wikipedia.org/wiki/M%C3%B6bius_function
'''

from prime_factors import prime_factors'''
Refrences: https://en.wikipedia.org/wiki/M%C3%B6bius_function
References: wikipedia:square free number
'''

from typing import List



def prime_factors(n: int) -> List[int]:
    """
    Returns prime factors of n as a list.
    
    >>> prime_factors(0)
    []
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(2560)
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 5]
    >>> prime_factors(10**-2)
    []
    >>> prime_factors(0.02)
    []
    >>> x = prime_factors(10**241) # doctest: +NORMALIZE_WHITESPACE
    >>> x == [2]*241 + [5]*241
    True
    >>> prime_factors(10**-354)
    []
    >>> prime_factors('hello')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> prime_factors([1,2,'hello'])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'

    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_square_free(factors:List[int]) -> bool:
    '''
    This functions takes a list of prime factors as input.
    returns True if the factors are square free.

    >>> is_square_free([1,1,2,3,4])
    False

    These are wrong but should return some value
    it simply checks for repition in the numb
    >>> is_square_free([1,3,4,'sd', 0.0])
    True
    
    >>> is_square_free([1,0.5, 2, 0.0])
    True
    
    >>> is_square_free([1,2, 2, 5])
    False
    
    >>> is_square_free('asd')
    True
    
    >>> is_square_free(24)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    '''
    i: int
    if len(set(factors)) != len(factors):
            return False
    return True

def mobius(n:int) -> int:
    '''
    Mobius function
    >>> mobius(24)
    0
    >>> mobius(-1)
    1
    >>> mobius('asd')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> mobius(10**400)
    0
    >>> mobius(10**-400)
    1
    >>> mobius(-1424)
    1
    >>> mobius([1, '2', 2.0])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    '''
    factors = prime_factors(n)
    if is_square_free(factors):
        if len(factors)%2 == 0:
            return 1
        elif len(factors)%2 != 0:
            return -1
    else:
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

from is_square_free import is_square_free


def mobius(n:int) -> int:
    '''
    Mobius function
    >>> mobius(24)
    0
    >>> mobius(-1)
    1
    >>> mobius('asd')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> mobius(10**400)
    0
    >>> mobius(10**-400)
    1
    >>> mobius(-1424)
    1
    >>> mobius([1, '2', 2.0])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    '''
    factors = prime_factors(n)
    if is_square_free(factors):
        if len(factors)%2 == 0:
            return 1
        elif len(factors)%2 != 0:
            return -1
    else:
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
