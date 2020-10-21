"""
Project Euler Problem 92:https://projecteuler.net/problem=92

A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen before.

For example,
44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will
become stuck in an endless loop.
What is most amazing is that EVERY starting number
will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

For a n digit number abc..p(n digits) if it arrive at 89
then any permutation of digits like bad..p will also arrive at 89
and same in the case if it does not.
So if I check for a single permutation whether it arrives or not.
If does arrive then I will increment the count by the no of
all its permutations ((A+B+C+...)!/(A!*B!*C!*...)
where A is the no. of a's and B is the no. of b's and so on.
For n=7 7-digit no. we can use beggars method to calculate the
no. of cases we have to check which is 1C(16,9) which equals to 11440
cases which is significantly less than checking 10 million numbers.
Also for a n digit no. maximum sum of squares its digits can be 81*n.
So if we will store the result of first n*100 no.'s we can use it
every time.

"""


def sod(d: int) -> int:
    """
    returns the sum of square of digits of d
    >>> sod(1)
    1
    >>> sod(77)
    98
    >>> sod(11067)
    87
    """
    sum = 0
    while d:
        sum += (d % 10) * (d % 10)
        d //= 10

    return sum


def arr_89(d: int) -> bool:
    """
    returns whether d will arrive at 89 or not
    >>> arr_89(10)
    False
    >>> arr_89(19872)
    True
    >>> arr_89(55555)
    True

    """
    if d == 0:
        return False

    while d != 89 and d != 1:
        d = sod(d)

    if d == 89:
        return True
    else:
        return False


def nums(dll: list, sll: list, curr: int, i: int) -> None:
    """
    Appends the list of all the possible ways in which an n digts can
    be distributed among 9 digits at the end of a 2-d list dll.
    """

    if i == 9:
        sll[i] = curr
        dll.append(sll.copy())
        return
    else:
        for j in range(0, curr + 1):
            sll[i] = j
            nums(dll, sll, curr - j, i + 1)
            sll[i] = 0


def solution(n: int = 7) -> int:
    """
    returns all the n digit numbers that arrive at 89
    >>> solution(6)
    856929
    >>> solution(1)
    7
    >>> solution(10)
    8507390852
    """

    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = i * fac[i - 1]
    dll = []
    sll = [0] * 10
    nums(dll, sll, n, 0)
    cnt = 0
    ca = [False] * n * 100
    for i in range(1, n * 100):
        ca[i] = arr_89(i)

    for sll in dll:
        d = 0
        for i in range(0, 10):
            d += (i * i) * sll[i]

        if ca[d]:
            tot = 1
            for j in sll:
                tot *= fac[j]
            cnt += fac[n] // tot

    return cnt
