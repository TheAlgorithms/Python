import numpy

def probability_of_n_heads_in_m_tossing(head_count: int, toss_count: int) -> int:
    """
    Calculate the factorial of specified number (n!).

    >>> import math
    >>> all(factorial(i) == math.factorial(i) for i in range(20))
    True
    >>> Probability_of_n_heads_in_m_tossing(.2,.5)
    Traceback (most recent call last):
        ...
    ValueError: The function only accepts integer values
    >>> Probability_of_n_heads_in_m_tossing(-1,5)
    Traceback (most recent call last):
        ...
    ValueError: The function is not defined for negative values
    >>> Probability_of_n_heads_in_m_tossing(3,2)
    Traceback (most recent call last):
        ...
    ValueError: Head count should be smaller than toss count
    
    >>> Probability_of_n_heads_in_m_tossing(1,1)
    0.5
    >>> Probability_of_n_heads_in_m_tossing(0,2)
    0.25
    >>> Probability_of_n_heads_in_m_tossing(2,3)
    0.375
    """
    if head_count != int(head_count) or toss_count != int(toss_count):
        raise ValueError("The function only accepts integer values")
    if head_count < 0 or toss_count < 0:
        raise ValueError("The function only accepts positive values")
    if head_count > toss_count:
        raise ValueError("Head count should be smaller than toss count")
    
    value = numpy.ones(1)
    
    for iter1 in range(toss_count):
        value = numpy.append(value, [0], axis=0) + numpy.append([0], value, axis=0)
        value = value/2
    
    return value[head_count]
