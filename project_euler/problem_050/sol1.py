"""
Project Euler Problem [50]: https://projecteuler.net/problem=50
    
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a
 prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the 
most consecutive primes?
"""


def is_prime(number: int) -> [bool]:
    """
    Test to see if the number is prime
    """
    i = 2 # begin from the smallest prime

    # if the number is a composite then it will atleat have a
    # factor less than equal to its square root
    
    while i * i <= number:
        # if number is divisible by i then i is a factor of number
        if  number % i == 0:
            return False
        i += 1
    return True

def sieve_of_eratosthenes(limit: int) -> list:
    """
    Returns a list of boolean values that indicate
    whether number at a given index is prime
    """
    is_prime_number = [True] * (limit + 1)
    i = 2 # begin from the smallest prime
    while i * i <= limit:
        if is_prime_number[i]:
            for j in range(2*i, limit + 1, i):
                is_prime_number[j] = False
        i += 1
    return is_prime_number

def solution(limit: int = 1_000_000) -> [int]:
    """
    Get the prime number less than limit which is
    longest sum of consecutive primes.
    >>> solution(100)
    41
    >>> solution(1000)
    953
    """
    prime_number = 0 #result
    max_length = 0 #length 
    is_prime_number = sieve_of_eratosthenes(limit)
    primes = []
    for i in range(2, limit):
        if is_prime_number[i]:
            primes.append(i)
    for i in range(len(primes)):
        total = 0
        for j in range(i, len(primes)):
            total += primes[j]
            if total >= limit:
                break
            if is_prime(total):
                if max_length < j - i + 1:
                    prime_number = total
                    max_length = j - i + 1
        
    return prime_number

if __name__ == "__main__":
    print(f"{solution() = }")




