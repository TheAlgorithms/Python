"""
Euler Problem : 60
author : sandeep gupta
time   : 4 October 2020, 18:30

Problem: The primes 3, 7, 109, and 673, are quite remarkable. By taking
         any two primes and concatenating them in any order the result
         will always be prime. For example, taking 7 and 109, both 7109
         and 1097 are prime. The sum of these four primes, 792, represents
         the lowest sum for a set of four primes with this property.
         Find the lowest sum for a set of five primes for which any two primes
         concatenate to produce another prime.

    
    @answer     : sum(13, 5197, 5701, 6733, 8389) = 26033
"""

max_number = 100000000
prime_array = []
prime = []


def is_compound_prime(a, b):
    global prime_array
    global prime
    prefix = int(str(a) + str(b))
    suffix = int(str(b) + str(a))
    if prefix < max_number and suffix < max_number and prime[prefix] and prime[suffix]:
        return True
    return False


def generate_prime():
    global prime_array
    global prime
    prime = [True for i in range(max_number + 1)]
    p = 2
    while p * p <= max_number:

        # If prime[p] is not changed, then it is a prime

        if prime[p]:

            # Update all multiples of p

            for i in range(p * p, max_number + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers

    i = 0
    for p in range(2, max_number + 1):
        if prime[p]:
            i += 1
            prime_array.append(p)


def solution() -> int:  # function without any parameters

    """
    Solution: BRUTE - calculated all the prime numbers using seive and stored them
              in global to avoid any re-calculation after that in each iteration tried
              to optimize at each step to avoid re-dundant work.

    >>> solution()
    26033

    """

    answer = 1000000000000000
    max_limit = 1100
    generate_prime()
    global prime_array
    global prime
    for i in range(0, max_limit):
        for j in range(i + 1, max_limit):
            if is_compound_prime(prime_array[i], prime_array[j]):
                for k in range(j + 1, max_limit):
                    if is_compound_prime(
                        prime_array[k], prime_array[i]
                    ) and is_compound_prime(prime_array[k], prime_array[j]):
                        for x in range(k + 1, max_limit):
                            if (
                                is_compound_prime(prime_array[x], prime_array[i])
                                and is_compound_prime(prime_array[x], prime_array[j])
                                and is_compound_prime(prime_array[x], prime_array[k])
                            ):
                                for m in range(x + 1, max_limit):
                                    if (
                                        is_compound_prime(
                                            prime_array[m], prime_array[i]
                                        )
                                        and is_compound_prime(
                                            prime_array[m], prime_array[j]
                                        )
                                        and is_compound_prime(
                                            prime_array[m], prime_array[k]
                                        )
                                        and is_compound_prime(
                                            prime_array[m], prime_array[x]
                                        )
                                    ):

                                        current_list = [
                                            prime_array[i],
                                            prime_array[j],
                                            prime_array[k],
                                            prime_array[x],
                                            prime_array[m],
                                        ]
                                        answer = min(answer, sum(current_list))

    return answer


# Tests

if __name__ == "__main__":
    import doctest

    doctest.testmod()
