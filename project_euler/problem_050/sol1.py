"""
Project Euler Problem 50:  https://projecteuler.net/problem=50


Problem 50:
    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a
    prime below one-hundred.

    The longest sum of consecutive primes below one-thousand
    that adds to a prime,contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as
    the sum of the most consecutive primes?
"""


def prma(u: int, primes: dict, start_no: int = 2) -> None:
    """
    fills the primes dict with prime numbers <=u
       primes: Global Dictionary To fill
       start_no: (optional) Starting value

    >>> primes = {}
    >>> prma(10,primes)
    >>> primes
    {2: 1, 3: 3, 5: 3, 7: 4}
    """

    if len(primes) <= 1:
        primes[2] = 1
        primes[3] = 2

    psrt = 2
    while start_no <= u:

        if start_no > psrt ** 2:

            psrt = start_no ** 0.5

        for i in primes:

            if i > psrt:
                primes[start_no] = len(primes) + 1
                break

            if start_no % i == 0:
                break
        start_no += 1


def solution(MX: int = 1000000) -> int:
    """
    returns the  prime, below MX,
    that can be written as the sum of the most consecutive primes
    >>> solution()
    997651
    >>> solution(1000)  #lessthan 1000
    953
    """
    primes = {}  # using a dict To maintain order and o(1) searching..
    prma(MX, primes)  # fill dict with primes < MX
    primes_tuple = tuple(primes)
    running_sum = 0
    count = 0
    while running_sum < MX:
        running_sum += primes_tuple[count]
        count += 1
    count -= 1  # deleting off the last prime..
    running_sum -= primes_tuple[count]

    # counting from left
    si = 0
    ei = count - 1
    running_sum1 = running_sum
    while running_sum1 not in primes and ei >= 0:
        running_sum1 -= primes_tuple[ei]
        ei -= 1
    count_l = ei - si + 1
    # print(count_l,running_sum1,primes_tuple[0:ei])    #debug

    # counting from right
    ei = count - 1
    running_sum2 = running_sum
    while running_sum2 not in primes and si <= ei:
        running_sum2 -= primes_tuple[si]
        si += 1
    count_r = ei - si + 1
    # print(count_r,running_sum2,primes_tuple[0:count]) #debug

    return running_sum1 if count_l > count_r else running_sum2


if __name__ == "__main__":
    print(solution())
