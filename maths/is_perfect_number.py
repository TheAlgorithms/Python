def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a Perfect Number.

    A perfect number is a positive integer that is equal to the sum 
    of its positive divisors, excluding the number itself.

    Example:
    6 = 1 + 2 + 3
    28 = 1 + 2 + 4 + 7 + 14
    """

    if n < 2:
        return False

    total = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total == n


if __name__ == "__main__":
    print(is_perfect_number(6))   # True
    print(is_perfect_number(28))  # True
    print(is_perfect_number(10))  # False
