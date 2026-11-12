"""For more information about the Binomial Distribution -
https://en.wikipedia.org/wiki/Binomial_distribution"""

from math import comb


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """
    Return probability of k successes out of n tries, with p probability for one
    success

    The function uses math.comb to calculate the binomial coefficient, avoiding
    OverflowError for large trial counts (e.g. trials >= 171).

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003
    >>> binomial_distribution (2, 4, 0.5)
    0.375
    >>> binomial_distribution(85, 171, 0.5)
    0.060749764626165485
    """
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if not 0 < prob < 1:
        raise ValueError("prob has to be in range of 1 - 0")
    probability = (prob**successes) * ((1 - prob) ** (trials - successes))
    # Calculate the binomial coefficient: n! / k!(n-k)!
    coefficient = comb(trials, successes)
    return probability * coefficient


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of 2 successes out of 4 trials")
    print("with probability of 0.75 is:", end=" ")
    print(binomial_distribution(2, 4, 0.75))
