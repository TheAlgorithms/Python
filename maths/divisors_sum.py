from random import randrange
from typing import List

"""Divisors Sum using the "math formula" """



"""
randomize the number to calculate the sum of all its divisors
"""
initial_number = randrange(1000000000)

print("The base number is: ", initial_number)


"""
factorization into primes
"""
factors = []
potential_prime = 2
while initial_number > 1:
    if initial_number % potential_prime == 0:
        initial_number = round(initial_number / potential_prime)
        factors.append(potential_prime)
    else:
        potential_prime += 1


"""
splits the prime factor and its frequency into two different lists
"""
freq_index = -1
frequency: List[int]  = []
primefactors: List[int]  = []
for i in factors:
    if i in primefactors:
        frequency[freq_index] += 1
    else:
        frequency.append(0)
        freq_index += 1
        frequency[freq_index] += 1
        primefactors.append(i)

"""
just make the sum of all its divisors following the formula
"""
final_sum = 1
for k in range(len(primefactors)):
    a = primefactors[k]
    b = frequency[k]
    final_sum *= ((a ** (b + 1)) - 1) / (a - 1)

print("The sum of all divisors is: ",int(final_sum))
