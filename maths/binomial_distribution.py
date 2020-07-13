"""For more information about the Binomial Distribution -
    https://en.wikipedia.org/wiki/Binomial_distribution"""


def binomial_distribution(k, n, p) -> float:
    """

    Returns probability of k successes out of n tries,
    with p probability for one success

    use: binomial_distribution(k, n, p):
    k - successes
    n - independent Bernoulli trials
    p - probability for one succes

    The function uses the factorial function
    in order to calculate the binomial coefficient

    >>> binomial_distribution(3, 5, 0.7)
    0.30870000000000003

    >>> binomial_distribution (2, 4, 0.5)
    0.375

    >>> binomial_distribution (2, 4, -0.5)
    Traceback (most recent call last):
    ...
    raise ValueError("p - Probability has to be in range of 1 - 0")
    ValueError: p - Probability has to be in range of 1 - 0
    """
    if k > n:
        raise ValueError("""k must be lower or equal to n""")
    if n < 0 or k < 0 or type(k) != int or type(n) != int:
        raise ValueError("the function is defined for non-negative integers k and n")
    if p > 1 or p < 0:
        raise ValueError("p - Probability has to be in range of 1 - 0")
    probability = (p**k)*(1-p)**(n-k)
    # Calculate the binomial coefficient:
    # Calculate n! / k!(n-k)!
    coefficient = factorial(n)/(factorial(k)*factorial(n-k))

    return probability * coefficient


# Implementation of the factorial function,
# used to calculate the binomial coefficient:
def factorial(n) -> int:
    """
    Factorial - The product of all positive integers less than or equal to n
    """

    if type(n) != int:
        raise ValueError("factorial(n) accepts only integer values")
    if n < 0:
        raise ValueError("factorial(n) works only for non-negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    print ("Probability of 2 successes out of 4 trails")
    print ("with probability of 0.75 is : ")
    print (str(binomial_distribution(2, 4, 0.75)))
