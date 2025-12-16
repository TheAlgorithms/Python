import numpy as np


def outcome_of_rolling_n_sided_dice_k_time(n_side: int, k_time: int) -> float:
    """
    The sum of outcomes for rolling an N-sided dice K times.

    This function returns a list. The last two elements are the
    range of probability distribution.
    The range is: 'k_time' to 'k_time*n_side'

    Other elements contain probabilities for getting a summation
    from 'k_time' to 'k_time*n_side'.

    Algorithm Explanation:

    1. Explanation of range:
    When we are rolling a six-sided dice the range becomes
    1 to 6.
    While rolling 5 times range becomes 5 to 30.
    The sum outcomes become 5 when all rolling finds 1.
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

    While rolling 2 dice simultaneously,
    the sum becomes 2 for two 1 outcomes. But the sum becomes
    3 for two different outcome combinations (1,2) and (2,1).
    The probability of getting 2 is 1/6.
    The probability of getting 3 is 2/6

    Link to rolling two 6-sided dice combinations:
    https://www.thoughtco.com/
    probabilities-of-rolling-two-dice-3126559
    That phenomenon is the same as the convolution.

    The algorithm can be used in playing games or solving
    problems where the sum of multiple dice throwing is needed.


    NB: a) We are assuming a fair dice
    b) Bernoulli's theory works with getting the probability of
    exactly 3 sixes while rolling 5 times. It does not work directly
    with the sum. The same sum can come in many combinations.
    Finding all of those combinations and applying Bernoulli
    is more computationally extensive.

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
    array([0.25, 0.5 , 0.25, 2.  , 4.  ])
    >>> outcome_of_rolling_n_sided_dice_k_time(2,4)
    array([0.0625, 0.25  , 0.375 , 0.25  , 0.0625, 4.    , 8.    ])

    """

    if n_side != int(n_side) or k_time != int(k_time):
        raise ValueError("The function only accepts integer values")
    if n_side < 2:
        raise ValueError("Side count should be more than 1")
    if k_time < 1:
        raise ValueError("Roll count should be more than 0")
    if k_time > 100 or n_side > 100:
        raise ValueError("Limited to 100 sides or rolling to avoid memory issues")

    prob_dist = 1
    dist_step = np.ones(n_side, dtype=float) / n_side

    iter1 = 0
    while iter1 < k_time:
        prob_dist = np.convolve(prob_dist, dist_step)
        iter1 = iter1 + 1

    prob_index = np.concatenate((prob_dist, np.array([k_time, k_time * n_side])))

    return prob_index


"""
# Extra code for the verification

dist_index = outcome_of_rolling_n_sided_dice_k_time(6, 3)

the_range = range(int(dist_index[-2]), int(dist_index[-1]+1))
probabilities =  dist_index[:-2]
print("Indexes:",the_range)

print("Distribution:",probabilities, "Their summation:",np.sum(probabilities))

import matplotlib.pyplot as plt
plt.bar(the_range, probabilities)
plt.xlabel("Summation of Outcomes")
plt.ylabel("Probabilities")

"""
