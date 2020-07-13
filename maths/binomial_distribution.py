from math import factorial
"""For more information about the Binomial Distribution -
    https://en.wikipedia.org/wiki/Binomial_distribution"""


def binomial_distribution(successes: int, trials: int, prob: float) -> float:
    """

    Returns probability of k successes out of n tries,
    with p probability for one success

    The function uses the factorial function
    in order to calculate the binomial coefficient

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003

    >>> binomial_distribution (2, 4, 0.5)
    0.375

    """
    if successes > trials:
        raise ValueError("""successes must be lower or equal to trials""")
    if trials < 0 or successes < 0:
        raise ValueError("the function is defined for non-negative integers")
    if not isinstance(successes, int) or not isinstance(trials, int):
        raise ValueError("the function is defined for non-negative integers")
    if prob > 1 or prob < 0:
        raise ValueError("prob has to be in range of 1 - 0")
    probability = (prob ** successes) * ((1 - prob) ** (trials - successes))
    # Calculate the binomial coefficient:
    # Calculate n! / k!(n-k)!
    coefficient = float(factorial(trials))
    coefficient /= (factorial(successes) * factorial(trials - successes))

    return probability * coefficient


if __name__ == "__main__":
    from doctest import testmod
    testmod()
