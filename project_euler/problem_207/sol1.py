"""

Project Euler Problem 207: https://projecteuler.net/problem=207

Problem Statement:
For some positive integers k, there exists an integer partition of the form
4**t = 2**t + k, where 4**t, 2**t, and k are all positive integers and t is a real
number. The first two such partitions are 4**1 = 2**1 + 2 and
4**1.5849625... = 2**1.5849625... + 6.
Partitions where t is also an integer are called perfect.
For any m ≥ 1 let P(m) be the proportion of such partitions that are perfect with
k ≤ m.
Thus P(6) = 1/2.
In the following table are listed some values of P(m)

   P(5) = 1/1
   P(10) = 1/2
   P(15) = 2/3
   P(20) = 1/2
   P(25) = 1/2
   P(30) = 2/5
   ...
   P(180) = 1/4
   P(185) = 3/13

Find the smallest m for which P(m) < 1/12345

Solution:
Equation 4**t = 2**t + k solved for t gives:
    t = log2(sqrt(4*k+1)/2 + 1/2)
For t to be real valued, sqrt(4*k+1) must be an integer which is implemented in
function check_t_real(k). For a perfect partition t must be an integer.
To speed up significantly the search for partitions, instead of incrementing k by one
per iteration, the next valid k is found by k = (i**2 - 1) / 4 with an integer i and
k has to be a positive integer. If this is the case a partition is found. The partition
is perfect if t os an integer. The integer i is increased with increment 1 until the
proportion perfect partitions / total partitions drops under the given value.

"""

import math


def check_partition_perfect(k):
    """

    Check if t = f(k) = log2(sqrt(4*k+1)/2 + 1/2) is a real number.

    >>> check_partition_perfect(2)
    True

    >>> check_partition_perfect(6)
    False

    """

    t = math.log2(math.sqrt(4 * k + 1) / 2 + 1 / 2)

    return t == int(t)


def solution(max_proportion: float = 1 / 12456) -> int:
    """
    Find m for which the proportion of perfect partitions to total partitions is lower
    than max_proportion

    >>> solution(1) > 5
    True

    >>> solution(3 / 13) > 185
    True

    >>> solution(1 / 12345)
    44043947822

    """

    total = 0
    perfect = 0

    i = 3
    while True:
        k = (i ** 2 - 1) / 4
        if k == int(k):  # if k = f(i) is an integer, then there is a partition for k
            k = int(k)
            total += 1
            if check_partition_perfect(k):
                perfect += 1
        if perfect > 0:
            if perfect / total < max_proportion:
                return k
        i += 1


if __name__ == "__main__":
    print(f"{solution() = }")
