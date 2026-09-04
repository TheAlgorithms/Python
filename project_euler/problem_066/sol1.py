"""
Project Euler Problem 61: https://projecteuler.net/problem=66

Problem statement-
Consider quadratic Diophantine equations of the form:
x^2 - D * y^2 = 1

For example, when D = 13 , the minimal solution in x is 649^2 - 13* 180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7} , we obtain the following:
3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1 (highest value of x)
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D<= 7 ,
the largest x is obtained when D = 5.

Find the value of D<=1000  in minimal solutions of x for
which the largest value of  is obtained.


Solution explanation -
The above given equation is known as Pell's equation. The solution uses the standard
method for solving pell's equation. Which is available on the wikipedia page.
The solution uses the continued fraction method for finding close approximations
of sqrt(D) which are of the form h/k. Because for these solutions the h and k are
solutions for x and y respectively. But we dont want an exact approximation because
there is a 1 on the RHS. We consider upto 2 periodic cycles, which guarantee a
solution. We check in the continued fraction considering newer fractions and checking
if numerator(x) and denominator(y) satisfy the diophantine equation.


References-
Wikipedia - https://en.wikipedia.org/wiki/Pell%27s_equation


"""

import math


def is_perfect_square(num: int) -> bool:
    """
    Checks if the number inputted is a perfect square or not.
    Returns True if perfect square else False.

    >>> is_perfect_square(25)
    True
    >>> is_perfect_square(3)
    False

    Time complexity - O(log2(num))

    """

    if num < 0:
        return False
    root = math.isqrt(num)
    return root * root == num


def continued_fraction(num: int) -> list[int]:
    """
    Computes and returns the continued fraction of the square root of the given integer.
    Note for irrational numbers, the continued fraction stops when there is repetition.
    The returned list is of the form -> [a0;a1,a2,a3...an]
    where a1,a2,a3...an represents the minimumperiodic part of the continued fraction.

    Time complexity - O(sqrt(num))

    >>> continued_fraction(2)
    [1, 2]
    >>> continued_fraction(13)
    [3, 1, 1, 1, 1, 6]
    """

    ans = []

    # Initialize variables for continued fraction
    m = 0
    d = 1
    a0 = math.isqrt(num)

    # this is the end point from where the sequence starts to repeat
    terminate_point = 2 * a0

    ans.append(a0)
    an = a0

    # loop till termination point is reached, storing each an value
    while an != terminate_point:
        m = d * an - m
        d = (num - m**2) / d
        an = math.floor((a0 + m) / d)
        ans.append(an)

    return ans


def diophantine_equation(var_x: int, var_y: int, var_d: int) -> int:
    """
    Returns the LHS of the diophantine equation using x, y and D.

    >>> diophantine_equation(3, 2, 2)
    1
    >>> diophantine_equation(8, 3, 7)
    1
    >>> diophantine_equation(3, 4, 5)
    -71
    """

    return var_x**2 - var_d * var_y**2


def solution(max_d: int = 1000) -> int:
    """
    This function provides a solution to the problem 66 from project Euler.
    The original problem is for D<= 1000. But there is a optional parameter
    max_d, by changing it you can find solutions for any D theoretically.

    Time complexity - O(max_d * (log2(max_d) + sqrt(max_d)))
    But since sqrt(max_d) dominates log2(max_d)
    Final time complexity is - O(max_d^3/2)

    >>> solution()
    661
    >>> solution(10000)
    9949
    """

    # Initialise answer which stored max value of D.
    answer = -1
    # Initialise max_x which stores max value of x.
    max_x = -1

    # loop over all values of D
    for d in range(2, max_d + 1):
        # skip if d is prefect square
        if is_perfect_square(d):
            continue

        # Get continued fraction and then
        # Add the periodic part of the fraction to itself because we are
        # guaranteed to find the solution in 2 cycles of the periodic part.
        # example -
        # fraction = [3,1,1,2]
        # First element is the integer part, rest is periodic fractional part.
        # Add the fractional part on itself.
        # fraction becomes [3,1,1,2,1,1,2].
        # This contains our solution for sure.
        fraction = continued_fraction(d)
        fraction += fraction[1:]

        num_0 = 0
        num_1 = 1
        den_0 = 1
        den_1 = 0

        # This is a recursive relation to find the next numerator and denominator
        num_2 = fraction[0] * num_1 + num_0
        den_2 = fraction[0] * den_1 + den_0

        n = 1
        # Use the recursive relation to get new, more accurate numerator and
        # denominator, then check if they satisfy the given diophantine equation.
        while diophantine_equation(num_2, den_2, d) != 1:
            num_0 = num_1
            num_1 = num_2
            num_2 = fraction[n] * num_1 + num_0

            den_0 = den_1
            den_1 = den_2
            den_2 = fraction[n] * den_1 + den_0

            n += 1

        # If we see a new larger value of x, we store the corresponding D
        # value as our answer.
        if num_2 > max_x:
            answer = d
            max_x = num_2

    return answer


if __name__ == "__main__":
    print(f"{solution(10000) = }")
