"""
Project Euler Problem 60: https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes
for which any two primes concatenate to produce another prime.

Note:
This takes 1.5 minutes to calculate for 5 numbers so the tests are done with 4.

"""
import math


def is_prime(number: int) -> bool:
    """
    Checks if a number is prime
    >>> is_prime(6)
    False
    >>> is_prime(-2)
    False
    >>> is_prime(1)
    False
    >>> is_prime(3)
    True
    >>> is_prime(99)
    False
    >>> is_prime(361)
    False

    Args:
        number: The number to check if prime

    Returns:
        if it is a prime
    """
    if 1 < number < 4:  # 2 and 3 are prime
        return True
    elif (
        number < 2 or not number % 2
    ):  # Numbers less than 2 and all even numbers are not primes
        return False
    factor_list = range(
        3, math.ceil(math.sqrt(number) + 1), 2
    )  # Will list all odd numbers up to the square root of the number
    return not any(
        not number % i for i in factor_list
    )  # Will make sure none of those numbers are a factor of the number being checked


def closest_prime(number: int) -> int:
    """
    Will find the closest prime that is greater than the number to the number given.
    >>> closest_prime(-2)
    2
    >>> closest_prime(5)
    7
    >>> closest_prime(4)
    5
    >>> closest_prime(99)
    101

    Args:
        number: The input number

    Returns:
        The closest prime that is greater than the input
    """
    number += 1
    while not is_prime(number):
        number += 1
    return number


def valid_solution(solution: list[int], next_number: int) -> bool:
    """
    Checks if adding next_number to the list still makes the solution valid.
    >>> valid_solution([2, 3, 5], 7)
    False
    >>> valid_solution([], 5)
    True
    >>> valid_solution([3, 7, 109], 673)
    True

    Args:
        solutions: The number of solutions to show

    Returns:
        A list of solutions.
    """
    for x in solution:
        if not is_prime(int(str(next_number) + str(x))) or not is_prime(
            int(str(x) + str(next_number))
        ):
            return False
    return True


def find_solution(prime_list: list[int], length: int, previous: list[int]) -> int:
    """
    Finds solutions that start with the list previous
    and have the length of length and contain only the numbers in prime length.
    Checks if adding next_number to the list still makes the solution valid.
    >>> find_solution([2, 3, 5], 2, [7])
    10

    Args:
        prime_list: A list of primes that are being checked
        length: The number of prime numbers
        previous: The data from the previous layers

    Returns:
        Sum of the smallest solution
    """

    total = 0  # Stores the best total recorded
    for x in prime_list:  # Goes through every prime number in the list
        if (
            previous[-1] > x
        ):  # Makes sure that the next number is less than the previous number
            if valid_solution(previous, x):  # Checks if it is a valid solution
                test_solution = previous.copy()
                test_solution.append(x)
                if length <= len(
                    test_solution
                ):  # Checks if the required length has been reached
                    total = (  # Replaces total if this is the lowest value.
                        sum(test_solution)
                        if sum(test_solution) < total or total == 0
                        else total
                    )
                else:  # Starts the next layer to check there
                    solution = find_solution(prime_list, length, test_solution)
                    if solution:
                        total = solution if solution < total or total == 0 else total
        else:
            break
    return total


def solution(length: int = 5) -> int:
    """
    Finds sum of the solution
    >>> solution(-1)
    Traceback (most recent call last):
        ...
    ValueError: No negative numbers allowed
    >>> solution(0)
    0
    >>> solution(1)
    2
    >>> solution(2)
    10
    >>> solution(3)
    107
    >>> solution(4)
    792

    Args:
        solutions: The number of solutions to show
        max_prime: The highest prime to check for solutions

    Returns:
        The sum of the solution of the problem
    """
    if length == 1:
        return 2
    elif length == 0:
        return 0
    elif length < 0:
        raise ValueError("No negative numbers allowed")
    prime = 2  # First prime number
    primes = []  # List of all primes that have been checked
    while True:
        primes.append(prime)  # Adds the prime number to a list of primes
        prime = closest_prime(prime)  # Gets the next prime after the previous one
        solution = find_solution(
            primes, length, [prime]
        )  # Finds all solutions that start with prime
        if solution:
            return solution


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
