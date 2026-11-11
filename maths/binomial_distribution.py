"""For more information about the Binomial Distribution -
https://en.wikipedia.org/wiki/Binomial_distribution"""

from math import comb, exp, lgamma, log, log1p
from sys import float_info


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Return probability of k successes out of n tries, with p probability for one
    success

    The function uses math.comb for direct calculation and switches to
    a logarithmic approach for numerically challenging inputs.

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003
    >>> binomial_distribution (2, 4, 0.5)
    0.375
    >>> round(binomial_distribution(85, 171, 0.5), 12)
    0.060749764626
    >>> round(binomial_distribution(5000, 10000, 0.5), 10)
    0.0079786461
    """
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if not 0 < prob < 1:
        raise ValueError("prob has to be in range of 1 - 0")
    success_term = prob**successes
    failure_term = (1 - prob) ** (trials - successes)
    probability_terms = success_term * failure_term
    log_coefficient = (
        lgamma(trials + 1) - lgamma(successes + 1) - lgamma(trials - successes + 1)
    )

    if (
        success_term > 0
        and failure_term > 0
        and probability_terms > 0
        and log_coefficient < log(float_info.max) - 1
    ):
        coefficient = comb(trials, successes)

        try:
            return probability_terms * coefficient
        except OverflowError:
            pass

    log_probability = (
        log_coefficient + successes * log(prob) + (trials - successes) * log1p(-prob)
    )

    return exp(log_probability)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trials")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
