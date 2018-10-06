# coding=utf-8
from math import sqrt, factorial
from random import randrange
from itertools import product

fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)


def euclidean_dist_sq(x1, x2, y1, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


def euclidean_dist(x1, x2, y1, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def partitions_up_to(lim):

    if lim < 0:
        return []
    if lim == 0:
        return [1]

    partitions = [1]
    n = 0
    while True:
        i = 0
        curr_pent = 1
        partitions.append(0)

        while curr_pent <= n:
            sign = -1 if i % 4 > 1 else 1
            partitions[n] += sign * partitions[n - curr_pent]
            i += 1

            j = int((i / 2 + 1)) if i % 2 == 0 else int(-(i / 2 + 1))
            curr_pent = int(j * (3 * j - 1) / 2)

        if n == lim:
            return partitions[:-1]
        n += 1


def factors(n):
    return [(i, n // i) for i in range(1, int(sqrt(n)) + 1) if n % i == 0]


def heron_area(side_a, side_b, side_c):
    p = (side_a + side_b + side_c) / 2
    return sqrt(p * (p-side_a) * (p-side_b) * (p-side_c))


def strings_to_ints(str_arr):
    return list(map(int, str_arr))


def is_perm(a, b): return sorted(str(a)) == sorted(str(b))


def is_palindromic(n): n = str(n); return n == n[::-1]


def is_pandigital(n, s=9): n = str(n); return len(n) == s and not '1234567890'[:s].strip(n)


# --- Get a count of integers less than n and relatively prime to n (Euler's Totient Function)----
def totient(n):

    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1

    return result


# --- Calculate the sum of proper divisors for n--------------------------------------------------
def d(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t) + 1):
        if n % i == 0: s += i + n / i
    if t == int(t): s -= t  # correct s if t is a perfect square
    return s


# --- Create a list of all palindromic numbers with k digits--------------------------------------
def pal_list(k):
    if k == 1:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [sum([n * (10 ** i) for i, n in enumerate(([x] + list(ys) + [z] + list(ys)[::-1] + [x]) if k % 2
                                                     else ([x] + list(ys) + list(ys)[::-1] + [x]))])
            for x in range(1, 10)
            for ys in product(range(10), repeat=k / 2 - 1)
            for z in (range(10) if k % 2 else (None,))]


# --- sum of factorial's digits-------------------------------------------------------------------
def sof_digits(n):
    if n == 0: return 1
    s = 0
    while n > 0:
        s, n = s + fact[n % 10], n // 10
    return s


# --- find the nth Fibonacci number---------------------------------------------------------------
def fibonacci(n):
    """
    Find the nth number in the Fibonacci series.  Example:

    >>>fibonacci(100)
    354224848179261915075

    Algorithm & Python source: Copyright (c) 2013 Nayuki Minase
    Fast doubling Fibonacci algorithm
    http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms
    """
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# Returns a tuple (F(n), F(n+1))
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (2 * b - a)
        d = b * b + a * a
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


# --- sum of squares of digits-------------------------------------------------------------------
def sos_digits(n):
    s = 0
    while n > 0:
        s, n = s + (n % 10) ** 2, n // 10
    return s


# --- sum of the digits to a power e-------------------------------------------------------------
def pow_digits(n, e):
    s = 0
    while n > 0:
        s, n = s + (n % 10) ** e, n // 10
    return s


# --- check n for prime--------------------------------------------------------------------------
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: return False
        f += 6
    return True


# --- Miller-Rabin primality test----------------------------------------------------------------
def miller_rabin(n):
    """
    Check n for primalty:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:
    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


# --- factor a number into primes and frequency----------------------------------------------------
"""
    find the prime factors of n along with their frequencies. Example:

    >>> factor(786456)
    [(2,3), (3,3), (11,1), (331,1)]

    Source: Project Euler forums for problem #3
"""


def prime_factor(n):
    f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
    if n < 1:
        return []
    while True:
        for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
            f += gap
            if f * f > n:  # If f > sqrt(n)
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if not n % f:
                e = 1
                n //= f
                while not n % f:
                    n //= f
                    e += 1
                factors.append((f, e))


# --- greatest common divisor----------------------------------------------------------------------
def gcd(a, b):
    """
    Compute the greatest common divisor of a and b. Examples:

    >>> gcd(14, 15)    #co-prime
    1
    >>> gcd(5*5, 3*5)
    5
    """
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while (b): a, b = b, a % b
    return a


# --- generate permutations-----------------------------------------------------------------------
def perm(n, s):
    """
    requires function factorial()
    Find the nth permutation of the string s. Example:

    >>>perm(30, 'abcde')
    bcade
    """


    if len(s) == 1: return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + perm(r, s[:q] + s[q + 1:])


# --- binomial coefficients-----------------------------------------------------------------------
def binomial(n, k):
    """
    Calculate C(n,k), the number of ways can k be chosen from n. Example:

    >>>binomial(30,12)
    86493225
    """
    nt = 1
    for t in range(min(k, n - k)):
        nt = nt * (n - t) // (t + 1)
    return nt


# --- catalan number------------------------------------------------------------------------------
def catalan_number(n):
    """
    Calculate the nth Catalan number. Example:

    >>>catalan_number(10)
    16796
    """
    nm = dm = 1
    for k in range(2, n + 1):
        nm, dm = (nm * (n + k), dm * k)
    return nm / dm


# --- generate prime numbers----------------------------------------------------------------------
def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.

    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


# --- bezout coefficients--------------------------------------------------------------------------
def bezout(a, b):
    """
    Bézout coefficients (u,v) of (a,b) as:

        a*u + b*v = gcd(a,b)

    Result is the tuple: (u, v, gcd(a,b)). Examples:

    >>> bezout(7*3, 15*3)
    (-2, 1, 3)
    >>> bezout(24157817, 39088169)    #sequential Fibonacci numbers
    (-14930352, 9227465, 1)

    Algorithm source: Pierre L. Douillet
    http://www.douillet.info/~douillet/working_papers/bezout/node2.html
    """
    u, v, s, t = 1, 0, 0, 1
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        u, s = s, u - q * s
        v, t = t, v - q * t

    return (u, v, a)


# --- number base conversion -------------------------------------------------------------------
# source: http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html
def dec2base(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return dec2base(n // base, base) + convertString[n % base]


# --- number to words ----------------------------------------------------------------------------
# this function copied from stackoverflow user: Developer, Oct 5 '13 at 3:45
def n2words(num, join=True):
    '''words = {} convert an integer number into words'''
    units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
             'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
            'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion',
                 'Quintillion', 'Sextillion', 'Septillion', 'Octillion',
                 'Nonillion', 'Decillion', 'Undecillion', 'Duodecillion',
                 'Tredecillion', 'Quattuordecillion', 'Sexdecillion',
                 'Septendecillion', 'Octodecillion', 'Novemdecillion',
                 'Vigintillion']
    words = []
    if num == 0:
        words.append('zero')
    else:
        numStr = '%d' % num
        numStrLen = len(numStr)
        groups = (numStrLen + 2) / 3
        numStr = numStr.zfill(groups * 3)
        for i in range(0, groups * 3, 3):
            h, t, u = int(numStr[i]), int(numStr[i + 1]), int(numStr[i + 2])
            g = groups - (i / 3 + 1)
            if h >= 1:
                words.append(units[h])
                words.append('Hundred')
            if t > 1:
                words.append(tens[t])
                if u >= 1: words.append(units[u])
            elif t == 1:
                if u >= 1:
                    words.append(teens[u])
                else:
                    words.append(tens[t])
            else:
                if u >= 1: words.append(units[u])
            if (g >= 1) and ((h + t + u) > 0): words.append(thousands[g] + '')
    if join:
        return ' '.join(words)
    return words
