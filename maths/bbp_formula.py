def bbp_pi_approximation(num_iterations: int = 1000) -> float:
    """
    Uses a popular pi-approximating algorithm known as the 
    Bailey-Borwein-Plouffe (BBP) formula to approximate pi.
    Wikipedia page:
    https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    @param num_iterations: nonnegative integer representing the number 
    of terms in the formula to sum (more iterations leads to more accuracy)
    @return: the approximation of pi given by the formula
    
    >>> bbp_pi_approximation(-10)
    Traceback (most recent call last):
      ...
    ValueError: Please input a nonnegative integer
    >>> bbp_pi_approximation(1.7)
    Traceback (most recent call last):
      ...
    ValueError: Please input a nonnegative integer
    >>> "%.8f" % bbp_pi_approximation()
    '3.14159265'
    >>> "%.8f" % bbp_pi_approximation(1000)
    '3.14159265'
    >>> "%.8f" % bbp_pi_approximation(0)
    '3.13333333'
    >>> "%.8f" % bbp_pi_approximation(1)
    '3.14142247'
    """
    if (not isinstance(num_iterations, int)) or num_iterations < 0:
        raise ValueError("Please input a nonnegative integer")
    pi_approx = 0.0
    exponential_part = 1.0
    # num_iterations + 1 because sum notation includes the last term
    for index in range(num_iterations + 1):
        pi_approx += exponential_part * (
            4 / (8 * index + 1)
            - 2 / (8 * index + 4)
            - 1 / (8 * index + 5)
            - 1 / (8 * index + 6)
        )
        exponential_part /= 16
    return pi_approx


if __name__ == "__main__":
    import doctest

    doctest.testmod()
