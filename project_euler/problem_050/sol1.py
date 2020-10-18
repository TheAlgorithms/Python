"""
Problem:
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand 
    that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below 1 million, can be written as the sum of the most consecutive primes?
"""

prime_numbers = [2, 3]


def is_prime(number: int) -> bool:
    """
    Checks whether the number is a prime or not
    >>> is_prime(0)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(11)
    True
    >>> is_prime(15)
    False
    >>> is_prime(997651)
    True
    """
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False

    for n in range(3, int(number ** 0.5) + 1, 2):
        if number % n == 0:
            return False

    return True


def generate_prime_numbers(n: int):
    """Generates prime numbers needed for the solution"""
    start = prime_numbers[-1] + 2
    # 2 * n ** 0.56 is a random approximation I made
    # to compute the minimal amount of prime numbers
    for number in range(start, int(2 * n ** 0.56) + 1, 2):
        if is_prime(number):
            prime_numbers.append(number)


def solution(n: int) -> int:
    """
    Returns the longest sum of consecutives primes below n
    >>> solution(100)
    41
    >>> solution(1000)
    953
    >>> solution(1000000)
    997651
    """
    if n <= 2:
        raise ValueError("n is too small, there isn't any prime number in that range")
    elif n <= 5:
        return 2
    elif n <= 17:
        return 5

    generate_prime_numbers(n)

    consecutive_length = 1
    longest_sum = 2
    for start in range(len(prime_numbers)):
        total = prime_numbers[start]
        if total >= n:
            break
        for end in range(start + 1, len(prime_numbers)):
            total += prime_numbers[end]
            if total >= n:
                break
            if not is_prime(total):
                continue

            if end - start > consecutive_length:
                consecutive_length = end - start
                longest_sum = total

    return longest_sum


if __name__ == "__main__":
    print(
        solution(
            int(input("Find the longest sum of consecutives primes below: ").strip())
        )
    )
