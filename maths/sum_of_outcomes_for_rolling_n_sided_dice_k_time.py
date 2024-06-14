import numpy as np

def outcome_of_rolling_n_sided_dice_k_time(n_side: int, k_time: int) -> list | list:
    """
   Sum of outcomes for rolling an N-sided dice K times.
   
   This function returns a list. The first element is an array.
   That array contains indexes.
   The second element is another array.
   That array contains probabilities for getting each index values
   as the sum of obtained side values.

    Algorithm Explanation:
    
    1. Explanation of range:
    When we are rolling a six-sided dice the range becomes
    1 to 6.
    While rolling 5 times range becomes 2 to 12.
    The sum outcomes becomes 5 when all rolling finds 1.
    30 happens when all rolling finds 6.
    1 is the minimum and 6 is the maximum of side values
    for a 6 sided dice. Therefore, the range is 5 to 30.
    Therefore, the range is k to n*k.
    
    2. Explanation of probability distribution:
    Say we are rolling a six-sided dice 2 times.
    for 0 roll, the outcome is 0 with probability 1.
    For the first roll, the outcome is 1 to 6 equally distributed.
    
    For the second roll, each previous outcome (1-6) will face
    an addition from the second rolling (1-6).
    If the first outcome is (known) 3, then the probability of
    getting each of 4 to 9 will be 1/6.
    
    The sum becomes 2 for two 1 outcomes. But the sum becomes
    3 for two outcomes (1,2) and (2,1).
    
    Link:
    https://www.thoughtco.com/
    probabilities-of-rolling-two-dice-3126559
    
    That phenomenon is the same as the convolution. However, the
    index position is different. Therefore, we adjust the index.
    
    
    NB: a) We are assuming a fair dice
    b) Bernoulli's theory works with getting the probability of
    exactly 3 sixes while rolling 5 times. It does not work directly
    with the sum. The same sum can come in many combinations.
    Finding all of those combinations and applying Bernoulli
    is more computationally extensive.
    c) The algorithm can be used in playing games where the sum of
    multiple dice throwing is needed.
    
    I used that method in my paper to draw the distribution
    Titled: Uncertainty-aware Decisions in Cloud Computing:
    Foundations and Future Directions
    Journal: ACM Computing Surveys (CSUR)
    link: https://dl.acm.org/doi/abs/10.1145/3447583
    The PDF version of the paper is available on Google Scholar.


    >>> import numpy as np
    >>> outcome_of_rolling_n_sided_dice_k_time(.2,.5)
    Traceback (most recent call last):
        ...
    ValueError: The function only accepts integer values
    >>> outcome_of_rolling_n_sided_dice_k_time(-1,5)
    Traceback (most recent call last):
        ...
    ValueError: Side count should be more than 1
    >>> outcome_of_rolling_n_sided_dice_k_time(3,-2)
    Traceback (most recent call last):
        ...
    ValueError: Roll count should be more than 0

    >>> outcome_of_rolling_n_sided_dice_k_time(2,2)
    ([2, 3, 4], array([0.25, 0.5 , 0.25]))
    
    >>> outcome_of_rolling_n_sided_dice_k_time(4,2)    
    ([2, 3, 4, 5, 6, 7, 8], array([0.0625, 0.125 , 0.1875, 0.25  , 0.1875, 0.125 , 0.0625]))
    """
    
    if n_side != int(n_side) or k_time != int(k_time):
        raise ValueError("The function only accepts integer values")
    if n_side < 2:
        raise ValueError("Side count should be more than 1")
    if  k_time < 1:
        raise ValueError("Roll count should be more than 0")
    if k_time > 100 or n_side > 100:
        raise ValueError("Limited to 100 sides or rolling to avoid memory issues")
        
    probability_distribution = 1
    distribution_step = np.ones(n_side)/n_side
    
    iter1 = 0
    while iter1 < k_time:
        probability_distribution =np.convolve(probability_distribution, distribution_step)
        iter1 = iter1+1
    
    index = list(range(k_time,k_time*n_side+1))
    return index, probability_distribution


'''
# Extra code for the verification

index_dist = outcome_of_rolling_n_sided_dice_k_time(6, 5)

print("Indexes:",index_dist[0])
print("Distribution:",index_dist[1], "Their summation:",np.sum(index_dist[1]))

import matplotlib.pyplot as plt
plt.bar(index_dist[0], index_dist[1])

'''
