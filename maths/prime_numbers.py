import math
from collections.abc import Generator
def fast_primes(max_n: int) -> Generator[int, None, None]:
    """
    Return a list of all primes numbers up to max.
    >>> list(fast_primes(0))
    []
    >>> list(fast_primes(-1))
    []
    >>> list(fast_primes(-10))
    []
    >>> list(fast_primes(25))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> list(fast_primes(11))
    [2, 3, 5, 7, 11]
    >>> list(fast_primes(33))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> list(fast_primes(1000))[-1]
    997
    """
    #it is useless to calculate who is already 2 multiple 
   def countPrimes(self, max_n: int) -> int:
        seen, ans = [0] * max_n, 0
        for num in range(2, max_n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((max_n - 1) // num - num + 1)
        return ans

def benchmark():
    """
    Let's benchmark our functions side-by-side...
    """
    from timeit import timeit

    setup = "from __main__ import slow_primes, primes, fast_primes"
    print(timeit("slow_primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("fast_primes(1_000_000_000_000)", setup=setup, number=1_000_000))


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)
    benchmark()
