"""
Project Euler Problem 719: https://projecteuler.net/problem=719

We define an S-number to be a natural number, n, that is a perfect square and its
square root can be obtained by splitting the decimal representation of n into 2 or 
more numbers then adding the numbers.

For example, 81 is an S-number because sqrt{81} = 8+1.<br />
6724 is an S-number: sqrt{6724} = 6+72+4. <br />
8281 is an S-number: sqrt{8281} = 8+2+81 = 82+8+1.<br />
9801 is an S-number: sqrt{9801}=98+0+1.

Further we define T(N) to be the sum of all S numbers n < N.
You are given T(10^4) = 41333.

Find T(10^{12})
"""
import math
import random
has_tqdm = True
try:
    from tqdm import tqdm
except ImportError:
    has_tqdm = False


def digit_sum(n: int) -> int:
    """
    Calculates sum of digits.
    """
    def num2digits(n: int) -> int:
        return [int(c) for c in str(n)]

    if n < 10:
        return n
    return digit_sum(sum(num2digits(n)))

def get_all_subset(iset: str, imax: int):
    """
    Get all digit splittings of n that, such that any part
    of the split does not exceed imax digits.

    iset - string repsentention of n.
    imax - max digit count of every part.
    """
    def helper(cur_set, depth):      
        if len(cur_set)/(depth + 1) > imax:
            yield None
        elif depth == 0:
            yield (cur_set,)
        else:
            for i in range(1, min(len(cur_set)-depth+1, imax+1)):
                for s in helper(cur_set[i:], depth-1):
                    if s is not None:
                        yield (cur_set[:i], *s)

    for j in range(1, len(iset)):
        for subsets in helper(iset, j):
            if subsets is not None:            
                yield subsets
        

def is_S(r: int, n: int) -> bool:
    """
    Test whether a given n is a S-number.
    n - perfect square input.
    r - square root of n.

    There are two main optimizations:
    (1) Note that digit_sum(a+b) = digit_sum(digit_sum(a)+digit_sum(b)),
        therefore, n is an S-number only if digit_sum(r) equals digit_sum(n).
        This simple test already disqualifies approximately 90% of possible pairs.
    (2) Note that for n to be S-number, every part of the n splitting must
        not exceed r, and thus must not exceed the length of r in digits.
        This further decrease the number of n splitting we have to consider.
    """
    if digit_sum(r) != digit_sum(n):
        return False

    for comb in get_all_subset(str(n), math.ceil(len(str(r)))):
        comb = [int("".join(c)) for c in comb]
        if sum(comb) == r:
            return True

    return False

def all_perfect_squares(n: int):
    """
    Generator for all perfect squares up-to n.
    The squares generated in a random order, 
    so that the ETA. will be more precise.
    """
    tmp = list(range(1, math.floor(math.sqrt(n)+1)))
    random.shuffle(tmp)
    if has_tqdm:
        for i in tqdm(tmp):
            yield i, (i ** 2)
    else:
        for i in tmp:
            yield i, (i ** 2)


def solution(N: int = 10**12) -> int:
    """
    returns T(N) for every given N

    >>> solution(10**6)
    10804656

    >>> solution(10**8)
    2818842841

    >>> solution(10**12)
    128088830547982
    """
    s = 0
    for r, n in all_perfect_squares(N):
        if is_S(r, n):
            s += n
    return s


if __name__ == "__main__":
    print(solution())
