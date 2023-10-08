import random

"""
The primes 3, 7, 109 and 673 are quite remarkable. By taking any
two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109 both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.
Find the lowest sum for a set of five primes
for which any two primes concatenate to produce another prime.
"""


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """
    Generates prime numbers up to the specified
    limit using the Sieve of Eratosthenes algorithm.

    Parameters:
    limit (int): The upper limit for prime number generation.

    Returns:
    list[int]: A list of prime numbers up to the given limit.

    >>> sieve_of_eratosthenes(2)
    [2]
    >>> sieve_of_eratosthenes(5)
    [2, 3]
    """
    is_prime = [True] * limit
    if limit > 2:
        is_prime[0] = False
        is_prime[1] = False
        is_prime[2] = True
    for number in range(3, int(limit**0.5) + 1, 2):
        if is_prime[number]:
            for multiple in range(number * 2, limit, number):
                is_prime[multiple] = False
    primes = [2]
    for number in range(3, limit, 2):
        if is_prime[number]:
            primes.append(number)
    return primes


def is_prime(number: int, test_size: int = 3) -> bool:
    """
    Tests if a given number is prime using the Miller-Rabin primality test.

    Parameters:
    number (int): The number to be tested for primality.
    test_size (int): The number of iterations for the Miller-Rabin test.

    Returns:
    bool: True if the number is probably prime, False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(6)
    False
    """
    if number < 6:
        return [False, False, True, True, False, True][number]
    elif number % 2 == 0:
        return False
    else:
        s, d = 0, number - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for a in random.sample(range(2, number - 2), test_size):
            x = pow(a, d, number)
            if x != 1 and x + 1 != number:
                for _ in range(1, s):
                    x = pow(x, 2, number)
                    if x == 1:
                        return False
                    elif x == number - 1:
                        a = 0
                        break
                if a:
                    return False
        return True


def forms_prime_pair(num1: int, num2: int) -> bool:
    """
    Checks if two numbers form a prime pair when concatenated in any order.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    bool: True if the numbers form a prime pair, False otherwise.

    >>> forms_prime_pair(1,3)
    True
    >>> forms_prime_pair(2,3)
    False
    """
    num1_str = str(num1)
    num2_str = str(num2)
    num1_num2_concat = int(num1_str + num2_str)
    num2_num1_concat = int(num2_str + num1_str)
    return is_prime(num1_num2_concat) and is_prime(num2_num1_concat)


# Finding prime numbers up to a given limit


def find_primes(limit: int) -> list[int]:
    """
    Finds prime numbers up to the specified limit
    using the Sieve of Eratosthenes algorithm.

    Parameters:
    limit (int): The upper limit for prime number generation.

    Returns:
    list[int]: A list of prime numbers up to the given limit.
    >>> find_primes(2)
    [2]
    >>> find_primes(5)
    [2, 3]
    """
    return sieve_of_eratosthenes(limit)


def find_lowest_sum_of_five_primes(primes: list[int]) -> int:
    """
    Finds the lowest sum of five prime numbers that
    form prime pairs when concatenated in any order.

    Parameters:
    primes (list[int]): A list of prime numbers.

    Returns:
    int: The lowest sum of five prime numbers that satisfy the condition.

    >>> find_lowest_sum_of_five_primes([2, 3])
    0
    >>> find_lowest_sum_of_five_primes([2, 3, 5])
    0
    """
    for prime1 in primes:
        for prime2 in primes:
            if prime2 < prime1:
                continue
            if forms_prime_pair(prime1, prime2):
                for prime3 in primes:
                    if prime3 < prime2:
                        continue
                    if forms_prime_pair(prime1, prime3) and forms_prime_pair(
                        prime2, prime3
                    ):
                        for prime4 in primes:
                            if prime4 < prime3:
                                continue
                            if (
                                forms_prime_pair(prime1, prime4)
                                and forms_prime_pair(prime2, prime4)
                                and forms_prime_pair(prime3, prime4)
                            ):
                                for prime5 in primes:
                                    if prime5 < prime4:
                                        continue
                                    if (
                                        forms_prime_pair(prime1, prime5)
                                        and forms_prime_pair(prime2, prime5)
                                        and forms_prime_pair(prime3, prime5)
                                        and forms_prime_pair(prime4, prime5)
                                    ):
                                        return (
                                            prime1 + prime2 + prime3 + prime4 + prime5
                                        )
    return 0


def solution(primes_limit: int = 10000) -> int:
    """
    the lowest sum for a set of five primes for which
    any two primes concatenate to produce another prime.

    Parameters:
    primes_limit (int): The upper limit for prime number generation.

    Returns:
    int: The lowest sum of five prime numbers.
    >>> solution(1)
    0
    >>> solution(10000)
    26033
    """
    primes_list: list[int] = find_primes(primes_limit)
    return find_lowest_sum_of_five_primes(primes_list)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
