def find_prime(n):
    num_prime = []
    primes = [True for i in range(n)]
    for j in range(2, int(n ** (1/2)) + 1):
        if primes[j]:
            for i in range(2 * j, n, j):
                primes[i] = False

    for i in range(2, n):
        if primes[i]:
            num_prime.append(i)
    return num_prime
