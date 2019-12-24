from math import factorial

def gamma(num):
    '''
    >>> gamma(1)
    1

    >>> gamma(0)
    Traceback (most recent call last):
        ...
    ValueError:  math domain error
    
    >>> gamma(10)
    362880
    
    >>> gamma(-199)
    Traceback (most recent call last):
        ...
    ValueError:  math domain error
    '''


    if num < 1:
        raise ValueError(" math domain error")
    else:
        return factorial(num-1)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    