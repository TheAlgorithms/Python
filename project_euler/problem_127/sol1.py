from numpy import sqrt

N = 120000


def generate_primes(n: int):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n + 1)) + 1):
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
    return primes


def rad(n: int, primes_list: list[int]):
    f = 1
    for p in primes_list:
        if p > n:
            break
        if n % p == 0:
            f *= p
    return f


def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def solution(c_less: int = 120000) -> int:
    primes_bool = generate_primes(c_less)
    primes_list = []
    print("primes generated")
    for i in range(2, len(primes_bool)):
        if primes_bool[i]:
            primes_list += [i]

    rads = [1] * (c_less + 1)
    for i in range(c_less + 1):
        if i % 100 == 0:
            print("rads", i)
        rads[i] = rad(i, primes_list)

    sum_c = 0
    print("start main")
    for a in range(1, c_less):
        rad_a = rads[a]
        if a % 2 == 1:
            r = range(1, min(a, c_less - a))
        else:
            r = range(1, min(a, c_less - a), 2)
        for b in r:
            c = a + b
            if rad_a * rads[b] * rads[c] < c and gcd(rad_a, rads[b]) == 1:
                sum_c += c

    return sum_c


if __name__ == "__main__":
    print(f"{solution() = }")
