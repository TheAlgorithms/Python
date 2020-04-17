# Factorial of a number using memoization


def factorial(num):
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    'Number should not be negative.'
    >>> [factorial(i) for i in range(5)]
    [1, 1, 2, 6, 24]
    """
    result = [-1] * (num + 1)

    if num < 0:
        return "Number should not be negative."

    return factorial_aux(num, result)


def factorial_aux(num, result):

    if num == 0 or num == 1:
        return 1

    if result[num] != -1:
        return result[num]
    else:
        result[num] = num * factorial_aux(num - 1, result)
        return result[num]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
