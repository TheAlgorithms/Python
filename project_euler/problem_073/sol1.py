"""
Problem 73 Counting fractions in a range: https://projecteuler.net/problem=73

Description:

Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions
for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of
reduced proper fractions for d ≤ 12,000?

Solution:


In the following, d and x will always be natural numbers.



- Consider first only even values for d.
    The function "f(d, x) = ((d/2) - x) / d" has two properties
    that are useful for this problem:
        1) f(d, x) < 1/2 for every d and x
        2) d(x, x) > 1/3 has a closed form solution, for a fixed d, that is x < d/6


    Therefore, the number of possible fractions
    that lie between 1/3 and 1/2 for an even d is: x = math.floor(d/6).


    For each of those candidate, if the gcd between the candidate
    itself and d is 1 then we found a valid fraction.
    Otherwise, the fraction is not a proper reduced fraction.


- Now consider the odd values for d.
    Following the same reasoning and defining "f(d, x) = (((d-1)/2) - x) / d",
    we can conclude that
        1) The function is always smaller than 1/2
        2) The number of valid candidates is x < (d-3)/6,
           which is given by math.floor((d-3)/6) + 1,
           keeping in mind that x must be an integer
           and that the solution x = 0 always generates a valid candidate.


    The final part follows exactly the case for even values.


Time: 4.2 sec
"""


from math import floor, gcd


def solution(maximum_d: int = 12000) -> int:
    """
    Find how many fractions lie between 1/3 and 1/2
    in the sorted set of reduced proper fractions for d ≤ maximum_d.

    >>> solution(8)
    3
    >>> solution(50)
    129
    >>> solution(100)
    505
    """

    list_d = [d for d in range(1, maximum_d + 1)]
    tot = 0

    for d in list_d:
        # even case
        if d % 2 == 0:
            if d % 6 == 0:
                x = d // 6 - 1
            else:
                x = floor(d / 6)
            min_n = d // 2 - x
            for num in range(min_n, d // 2):
                if gcd(num, d) == 1:
                    tot += 1

        # odd case
        else:
            if (d - 3) % 6 == 0:
                x = (d - 3) // 6 - 1
            else:
                x = floor((d - 3) / 6)
            min_n = (d - 1) // 2 - x
            for num in range(min_n, ((d - 1) // 2) + 1):
                if gcd(num, d) == 1:
                    tot += 1

    return tot


if __name__ == "__main__":
    print(f"{solution() = }")
