"""
Project Euler Problem 7: https://projecteuler.net/problem=7
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.
What is the 10001st prime number?
References:
- https://en.wikipedia.org/wiki/Prime_number
"""


def nth_prime(n: int) -> [int]:
    """
    Returns the nth prime number.
    Args:
    n (int): The position of the prime number to find.
    Returns:
    int: The nth prime number, or None if n is less than 1.
    """
    if n < 1:
        return None

    prime_counter = 2
    for num in range(3, n**2, 2):
        divisor = 1
        while divisor * divisor < num:
            divisor += 2
            if num % divisor == 0:
                break
        else:
            prime_counter += 1
        if prime_counter == n:
            return num


def solution() -> int:
    """
    Returns the 10001st prime number.
    """

    if (result := nth_prime(10001)) is not None:
        return result
    else:
        return -1


if __name__ == "__main__":
    print(f"{solution() = }")
