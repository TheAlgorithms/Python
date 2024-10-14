"""
Project Euler Problem 912: https://projecteuler.net/problem=912

Problem:
Sum of squares of odd indices where the n-th positive integer does not contain
three consecutive ones in its binary representation.

We define `s_n` as the n-th positive integer that does not contain three
consecutive ones in its binary representation. Define `F(N)` to be the sum of
`n^2` for all `n ≤ N` where `s_n` is odd.

You are given:
F(10) = 199

Find F(10^16) modulo 10^9 + 7.
"""

MOD = 10**9 + 7


def matrix_mult(a, b, mod=MOD):
    """Multiplies two matrices a and b under modulo"""
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod,
        ],
    ]


def matrix_pow(mat, exp, mod=MOD):
    """Efficiently computes matrix to the power exp under modulo"""
    res = [[1, 0], [0, 1]]
    base = mat

    while exp > 0:
        if exp % 2 == 1:
            res = matrix_mult(res, base, mod)
        base = matrix_mult(base, base, mod)
        exp //= 2

    return res


def fib_like_sequence(n, mod=MOD):
    """
    Computes the n-th term in the Fibonacci-like sequence of numbers whose binary
    representation does not contain three consecutive 1s.

    This sequence follows the recurrence relation:
    a_n = a_(n-1) + a_(n-2) + a_(n-3)

    Returns the sequence value modulo `mod`.
    """

    if n == 0:
        return 0
    if n in (1, 2):  # Merge comparisons
        return 1

    # The recurrence relation can be represented using matrix exponentiation:
    t = [[1, 1], [1, 0]]  # Fibonacci-like transformation matrix
    result = matrix_pow(t, n - 1, mod)

    return result[0][0]  # This gives the n-th Fibonacci-like term


def calculate_sum_of_squares(limit):
    """
    Computes F(limit) which is the sum of squares of indices where s_n is odd.

    Arguments:
    - limit: up to which value of n we compute F(N)

    Returns:
    - the sum F(limit) modulo 10^9 + 7
    """

    total_sum = 0

    for n in range(1, limit + 1):
        s_n = fib_like_sequence(n)  # Get the n-th sequence number

        if s_n % 2 == 1:  # Check if s_n is odd
            total_sum = (total_sum + n**2) % MOD  # Add square of n to total sum

    return total_sum


def solution(limit=10**16):
    """
    The solution to compute F(limit) efficiently.
    This function returns F(10^16) modulo 10^9 + 7.
    """

    return calculate_sum_of_squares(limit)


if __name__ == "__main__":
    # We are given F(10) = 199, so let's test for N = 10 first.
    assert solution(10) == 199

    # Now find F(10^16)
    print(f"The result is: {solution(10**16)}")
