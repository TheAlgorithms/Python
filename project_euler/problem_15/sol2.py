def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

def binomial_coefficient(n,k):
    """compute the number of ways, disregarding order, that k objects can be chosen
            from among n objects
            """
    return factorial(n)//(factorial(k)*factorial(n-k))

assert binomial_coefficient(40,20) == 137846528820