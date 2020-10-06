"""
"https://projecteuler.net/problem=120"

Name: Square remainders

Let r be the remainder when (a−1)n + (a+1)n is divided by a2.
For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49.
And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.
For 3 ≤ a ≤ 1000, find ∑ rmax.

Solution:

n=1: (a-1) + (a+1) = 2a
n=2: (a-1)^2 + (a+1)^2
     = a^2 + 1 - 2a + a^2 + 1 + 2a  (Using (a+b)^2 = (a^2 + b^2 + 2ab),
                                           (a-b)^2 = (a^2 + b^2 - 2ab) and b = 1)
     = 2a^2 + 2
n=3: (a-1)^3 + (a+1)^3  (Similary using (a+b)^3 & (a-b)^3 formula and so on)
     = 2a^3 + 6a
n=4: 2a^4 + 12a^2 + 2
n=5: 2a^5 + 20a^3 + 10a

As you could see, when the expression is divided by a^2.
Except for the last term, the rest will result in the remainder 0.

n=1: 2a
n=2: 2
n=3: 6a
n=4: 2
n=5: 10a

So it could be simplified as, r = 2an for odd & 2 for even n.
And the maximum value or r could be obtained for n = (a - 1) / 2

"""


def solution() -> int:
    """
    Returns the summation of rmax for 3 ≤ a ≤ 1000
    """
    r = 0
    for a in range(3, 1001):
        r += 2 * a * ((a - 1) // 2)
    return r


if __name__ == "__main__":
    print(solution())
