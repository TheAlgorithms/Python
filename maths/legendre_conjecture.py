"""
Legendre's Conjecture states that there is always one prime number in the range n^2 to (n+1)^2, where n is a natural number.

https://en.wikipedia.org/wiki/Legendre%27s_conjecture
"""

import math

def prime(number: int) -> bool:
    """
    :param number: a number to check for primality
    :return: truth value of whether number is prime
    >>> prime(3)
    True
    >>> prime(6)
    False
    """
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0: 
            return False
    return True


def legendre_conjecture(number: int) -> list:
    """
    :param number: a number to test Legendre's Conjecture
    :return: a list of primes between number*number and (number+1)*(number+1)
    >>> legendre_conjecture(2)
    [5, 7]
    >>> legendre_conjecture(-1)
    []
    """
    if(number < 1):
        return []
    arr = []
    for i in range (number*number, (((number+1)*(number+1))+1)):
        if(prime(i)):
            arr.append(i)
    return arr


if __name__ == "__main__":
    number = int(input("Enter a value for n to test Legendre's Conjecture: ").strip())
    arr = legendre_conjecture(number)
    if arr == []:
        print("This conjecture holds only when n is an natural number.")
    else:
        print(f"The prime numbers in the range {number*number} and {(number+1)*(number+1)} are: ")
        for i in arr:
            print(i)
