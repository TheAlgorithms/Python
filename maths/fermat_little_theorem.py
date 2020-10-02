"""
Python program to show the usage of Fermat's little theorem in a division

If p is a prime number, then given any integer a,
(a**p) is congruent to (a) modulo the prime p.

Wikipedia reference: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
"""


def binary_exponentiation(a: int, n: int, mod: int) -> int:
    """
    Find a to the power of n, modulo mod.

    >>> binary_exponentiation(4, 3, 7)
    1

    >>> binary_exponentiation(2, 9, 9)
    8

    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return (binary_exponentiation(a, n - 1, mod) * a) % mod

    else:
        b = binary_exponentiation(a, n / 2, mod)
        return (b * b) % mod


def check_fermat_little_thm(a: int, p: int) -> bool:
    """
    Verifies the fermat little theorem

    Example prime: 13
    >>> check_fermat_little_thm(400, 13)
    True

    >>> check_fermat_little_thm(22, 13)
    True

    Example prime: 701
    >>> check_fermat_little_thm(13, 701)
    True

    >>> check_fermat_little_thm(22, 701)
    True
    """
    a_power_p = binary_exponentiation(a, p, p)
    a_mod_p = binary_exponentiation(a, 1, p)  # or just a % p

    return a_power_p == a_mod_p


def check_fermat_little_thm_indivisible(a: int, p: int) -> bool:
    """
    If a is indivisible by p, then the special case holds:

    a**(p-1) = 1 (mod p)

    >>> check_fermat_little_thm_indivisible(400, 13)
    True

    >>> check_fermat_little_thm_indivisible(13, 2)
    True

    """
    assert a % p != 0

    a_power_p_minus_one = binary_exponentiation(a, p - 1, p)
    return a_power_p_minus_one == 1


if __name__ == "__main__":
    # Test 1: Generic Case
    fermat_result = check_fermat_little_thm(183, 17)
    print(
        f"Checking fermat little thm with a = 183 and p = 17, result:\
    {fermat_result}"
    )

    # Test 2: Special Case
    fermat_special_result = check_fermat_little_thm_indivisible(19, 4)
    print(
        f"Checking fermat little thm special case with a = 19 and p = 4,\
    result: {fermat_special_result}"
    )
