'''
Author : Dhruv B Kakadiya

'''

# here I'm going to generate n bit prime number using some Miller-Rabin test

import random as rd

starting_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                    31, 37, 41, 43, 47, 53, 59, 61, 67,
                    71, 73, 79, 83, 89, 97, 101, 103,
                    107, 109, 113, 127, 131, 137, 139,
                    149, 151, 157, 163, 167, 173, 179,
                    181, 191, 193, 197, 199, 211, 223]

# first with the use of 'n' we select radome number between (2**(n - 1) + 1, 2**n - 1)
def n_bit_random_num (n):
    return (rd.randrange(2**(n - 1) + 1, 2**n - 1))

# with the help of upper number we apply low level primality testing
def simple_testing (n):
    while (True):
        n_bit_num = n_bit_random_num(n)
        for i in starting_primes:
            if ((n_bit_num % i) == 0 and (i**2 <= n_bit_num)):
                break
            else:
                return n_bit_num

# applying miller rabin primality testing on n bit prime to check whether it is prime or not
def miller_rabin_test (n_bit_num):
    # first we have to change n_bit_num into (2**k * m) format
    k = 0
    # even because n_bit_num is already odd
    even_n_bit_num = n_bit_num - 1
    while (even_n_bit_num % 2 == 0):
        even_n_bit_num //= 2
        k += 1

    # handling assertion exception
    assert(2**k * even_n_bit_num == n_bit_num - 1)

    # function inside function
    def tester (test):
        if (pow(test, even_n_bit_num, n_bit_num) == 1):
            return False
        for i in range(k):
            if (pow(test, 2**i * even_n_bit_num, n_bit_num) == n_bit_num - 1):
                return False
        return True

    # we apply this test al least 15 times
    for i in range(15):
        test = rd.randrange(2, n_bit_num)
        if (tester(test)):
            return False
    return True
