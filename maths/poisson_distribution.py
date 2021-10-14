"""For more information about the Poisson Distribution -
    https://en.wikipedia.org/wiki/Poisson_distribution"""
from math import e, factorial


def poisson_distribution(occurence: int, mean: float) -> float:
    """
    Returns the probability of a given number of events occurring in a fixed 
    interval of time or space, given that these events occur with a known 
    constant mean rate and independently of the time since the last event.

    The function uses the factorial function and the Euler's constant 
    from the math library.

    Parameters:
    - occurence = the number of times the event occurs in a fixed interval.
    - mean = the known constant mean rate of the event occuring in a fixed interval.

    >>> poisson_distribution(2, 2.5)
    0.25651562069968376
    >>> poisson_distribution(2, 5)
    0.08422433748856836
    """
    if occurence < 0 or mean < 0:
        raise ValueError("an event cannot occur negative amount of times.")
    if not isinstance(occurence, int):
        raise ValueError("an event can occur in an integer amount of times.")
    if not isinstance(mean, float) and not isinstance(mean, int):
        raise ValueError("an event's mean rate should be in the form of a float or integer.")
    probability  = (mean ** occurence) * (e ** -mean) / factorial(occurence)
    return probability


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Probability of an event with mean rate 10/min")
    print("to occur twice in a minute is:", end=" ")
    print(poisson_distribution(2, 10))
