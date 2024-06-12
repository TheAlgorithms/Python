
"""
Algorithm Explanation:
If you toss 0 time -> 0 head
Distribution [1] -> Meaning: 1 in the 0-index

If you toss 1 time -> 0 or 1 head
Distribution [0.5 0.5] -> Meaning: 0.5 in both indexes

If you toss 2 times -> 0 to 2 heads
Distribution [0.25 0.5 0.25] -> 
Meaning:  probability of n heads from the distribution 
{HH, HT, TH, TT}

If you toss 3 times -> 0 to 3 heads
Distribution [0.125 0.375 0.375 0.125] -> 
Meaning:  probability of n heads from the distribution 
{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}

Therefore,
Probability_distribution(N+1) = 
      [Probability_distribution(N) 0]/2 + [0 Probability_distribution(N)]/2

I used that method in my paper
Titled: Uncertainty-aware Decisions in Cloud Computing: 
Foundations and Future Directions
Journal: ACM Computing Surveys (CSUR)
"""


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
