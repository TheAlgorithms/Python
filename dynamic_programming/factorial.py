#Factorial is the product of all positive integers less than or equal to a given positive integer 
#and denoted by that integer and an exclamation point. 
#For example, factorial seven is written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7. 
#Factorial zero is defined as equal to 1.

# Factorial of a number using memoization
#If n = 0, return 1
#Otherwise if n is in the memo, return the memo's value for n
#Otherwise,
#Calculate (n - 1)! x n
#Store result in the memo
#Return result


from functools import lru_cache


@lru_cache
def factorial(num: int) -> int:
    """
    >>> factorial(7)
    5040
    >>> factorial(-1)
    Traceback (most recent call last):
      ...
    ValueError: Number should not be negative.
    >>> [factorial(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
