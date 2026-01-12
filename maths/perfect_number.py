def is_perfect_number(n: int) -> bool:
    """
    Check whether a number is a Perfect Number.

    A perfect number is a positive integer that is equal to the sum
    of its proper positive divisors (excluding itself).

    >>> is_perfect_number(6)
    True
    >>> is_perfect_number(28)
    True
    >>> is_perfect_number(10)
    False
    """
    if n <= 1:
        return False

    divisors_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
        i += 1

    return divisors_sum == n
