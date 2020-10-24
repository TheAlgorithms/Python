"""
Project Euler Problem 58: https://projecteuler.net/problem=58

-----------------------------------------------------------------------------

PROBLEM STATEMENT

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is
the side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?

-----------------------------------------------------------------------------

SOLUTION

Let l(n) = the nth layer's side length

1. l(1) = 1
2. A new layer is formed by cloning the previous layer and
   shifting it in the corresponding direction (up, down, right, left) and then
   adding in the four corners. Moreover, l(n) = l(n - 1) + 2
3. To form the nth layer we proceed the following way:
    * insert next l(n-1) numbers
    * insert first corner
    * insert next l(n-1) numbers
    * insert second corner
    * insert next l(n-1) numbers
    * insert third corner
    * insert next l(n-1) numbers
    * insert last corner
5. For each layer we can recalculate the ratio and find the answer.


TIME 10.5s

"""


def is_prime(number: int) -> bool:
    """
    Check if the number argument is prime or not

    >>> is_prime(3)
    True
    >>> is_prime(1)
    False
    >>> is_prime(8)
    False
    >>> is_prime(-8)
    False
    >>> is_prime(29)
    True
    """

    if number < 2:
        # any number smaller than 2 is not prime
        return False

    for divizor in range(2, number + 1):
        if divizor * divizor > number:
            # if we didn't find a divisor until the square root, the number is prime
            break

        if number % divizor == 0:
            # we found a divisor, the number is not prime
            return False

    # no divisor found, the number is prime
    return True


def solution() -> int:
    """
    Iterate through layers until the answer is found

    >>> solution()
    26241
    """

    target_ratio = 0.1  # we want to go under 10%

    current_corner_number = 1  # the centre point can be considered a corner
    previous_side_length = 1
    how_many_primes_on_diagonals = 0
    how_many_numbers_on_diagonals = 1

    while True:
        current_side_length = previous_side_length + 2

        for _ in range(4):
            # check if corners are primes and update count
            current_corner_number += previous_side_length + 1
            if is_prime(current_corner_number):
                how_many_primes_on_diagonals += 1

        how_many_numbers_on_diagonals += 4  # 4 new corners

        new_ratio = how_many_primes_on_diagonals / how_many_numbers_on_diagonals

        if new_ratio < target_ratio:
            # return the answer
            return current_side_length

        # did not find the answer, continue with the next layer
        previous_side_length = current_side_length
        # print(current_side_length, how_many_primes_on_diagonals)

    return None


if __name__ == "__main__":
    print(solution())
