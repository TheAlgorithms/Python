def degree_to_radian(degree):
    '''
    will take an integer degree and convert it to radians
    >>> degree_to_radian(180)
    3.14
    >>> degree_to_radian(360)
    6.28
    TypeError:  string was passed to the function
    >>>degree_to_radian('a')
    TypeError: can't multiply sequence by non-int of type 'float'
    '''

    return (3.14/180)*degree

def radian_to_degree(radian):
    '''
    will take an integer radian angle and return the converted into degree form
    >>>radian_to_degree(3.14)
    180.0
    >>>radian_to_degree(6.28)
    360
    TypeError:  string was passed to the function
    >>>radian_to_degree('a')
    TypeError: can't multiply sequence by non-int of type 'float'
    '''
    return(180/3.14)*radian

