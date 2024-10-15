"""
# Sieve of Eratosthenes

# Input: n = 10
# Output: 2 3 5 7

# Input: n = 20
# Output: 2 3 5 7 11 13 17 19

# you can read in detail about this at
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# """


# def prime_sieve_eratosthenes(num: int) -> list[int]:
#     """
#     Print the prime numbers up to n

#     >>> prime_sieve_eratosthenes(10)
#     [2, 3, 5, 7]
#     >>> prime_sieve_eratosthenes(20)
#     [2, 3, 5, 7, 11, 13, 17, 19]
#     >>> prime_sieve_eratosthenes(2)
#     [2]
#     >>> prime_sieve_eratosthenes(1)
#     []
#     >>> prime_sieve_eratosthenes(-1)
#     Traceback (most recent call last):
#     ...
#     ValueError: Input must be a positive integer
#     """

#     if num <= 0:
#         raise ValueError("Input must be a positive integer")

#     primes = [True] * (num + 1)

#     p = 2
#     while p * p <= num:
#         if primes[p]:
#             for i in range(p * p, num + 1, p):
#                 primes[i] = False
#         p += 1

#     return [prime for prime in range(2, num + 1) if primes[prime]]

def sieve(n):
    isprime[0] = isprime[1] = False
    for i in range(2, math.sqrt(n) + 1):
        if isprime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                isprime[j] = False

n = int(input())
isprime = [True for i in range(n+1)]
primes = []

print('The prime numbers from 1 to', n, 'are:')
print(*primes)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_num = int(input("Enter a positive integer: ").strip())
    print(prime_sieve_eratosthenes(user_num))
