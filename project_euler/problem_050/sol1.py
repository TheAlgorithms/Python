"""
Problem 50: https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def get_primes(limit: int) -> (set, list):
    """ 
    Returns the set & list(ordered) of primes up to the below limit
    using Sieve of Eratosthenes 

    >> get_primes(10)
    ({2, 3, 5, 7}, [2, 3, 5, 7])
    """
    SV_MAX = limit
    sv = [True for i in range(SV_MAX)]
    prime_set = set()
    primes = []

    # 1 is not prime
    sv[0] = False

    for i in range(2, SV_MAX+1):
        # if current number is prime
        if sv[i-1]:
            primes.append(i)
            prime_set.add(i)
            for j in range(2*i, SV_MAX+1, i):
                sv[j-1] = False
    return prime_set, primes


def solution(limit: int =1000000) -> int:
    """
    First, generate a list of all primes upto limit
    Then, try all sets of consecutive primes to see if they add up to 
    some other prime, successively trying smaller size sets if bigger 
    ones don't have any valid consecutive primes

    >>> solution(1000)
    953
    >>> solution(1000000)
    997651
    """
    prime_set, primes = get_primes(limit)
    prefix = []

    curr = 0
    for p in primes:
        curr += p
        prefix.append(curr)

    l = len(prefix)

    max_prime, max_l = -1, -1

    for i in range(l-1):
        # check if we can generate a solution with i terms
        # decrease i successively if we don't find a solution
        for j in range(i+1, l):
            # iterate over each sequence of i primes starting at
            # jth index
            p = prefix[j]
            if i >= 1:
                p -= prefix[i-1]
            if p >= limit:
                break
            if p in prime_set:
                curr_l = j-i+1
                if curr_l > max_l:
                    max_prime = p
                    max_l = curr_l
    return max_prime


# if __name__ == "__main__":
#     print(solution())


if __name__ == "__main__":
    print(f"solution = {solution()}")
