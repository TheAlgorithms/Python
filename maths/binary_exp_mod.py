def bin_exp_mod(a, n, b):
    """
    >>> bin_exp_mod(3, 4, 5)
    1
    >>> bin_exp_mod(7, 13, 10)
    7
    """
    # mod b
    assert not (b == 0), "This cannot accept modulo that is == 0"
    if n == 0:
        return 1

    if n % 2 == 1:
        return (bin_exp_mod(a, n - 1, b) * a) % b

    r = bin_exp_mod(a, n / 2, b)
    return (r * r) % b


def binary_exponentiation_mod_multiplication(a, b, c):
    """
    * Binary Exponentiation with Multiplication
    * This is a method to find a*b in a time complexity of O(log b)
    * This is one of the most commonly used methods of finding result of multiplication.
    * Also useful in cases where solution to (a*b)%c is required,
    * where a,b,c can be numbers over the computers calculation limits.
    * Done using iteration, can also be done using recursion

    * Let's say you need to calculate a ^ b
    * RULE 1 : a * b = (a+a) * (b/2) -- example : 4 * 4 = (4+4) * (4/2) = 8 * 2
    * RULE 2 : IF b is ODD, then -- a * b = a + (a * (b - 1)) :: where (b - 1) is even.
    * Once b is even, repeat the process to get a * b
    * Repeat the process till b = 1 OR b = 0, because a*1 = a AND a*0 = 0
    *
    * As far as the modulo is concerned,
    * the fact : (a+b) % c = ((a%c) + (b%c)) % c
    * Now apply RULE 1 OR 2, whichever is required.

    * @author chinmoy159
    * @version 1.0 dated 10/08/2017
    """

    res = 0
    while b > 0:
        if b & 1:
            res = ((res % c) + (a % c)) % c

        a += a
        b >>= 1

    return res


def binary_exponentiation_mod_powers(a, b, c):
    """
    * Binary Exponentiation for Powers
    * This is a method to find a^b in a time complexity of O(log b)
    * This is one of the most commonly used methods of finding powers.
    * Also useful in cases where solution to (a^b)%c is required,
    * where a,b,c can be numbers over the computers calculation limits.
    * Done using iteration, can also be done using recursion

    * Let's say you need to calculate a ^ b
    * RULE 1 : a ^ b = (a*a) ^ (b/2) -- example : 4 ^ 4 = (4*4) ^ (4/2) = 16 ^ 2
    * RULE 2 : IF b is ODD, then -- a ^ b = a * (a ^ (b - 1)) :: where (b - 1) is even.
    * Once b is even, repeat the process to get a ^ b
    * Repeat the process till b = 1 OR b = 0, because a^1 = a AND a^0 = 1
    *
    * As far as the modulo is concerned,
    * the fact : (a*b) % c = ((a%c) * (b%c)) % c
    * Now apply RULE 1 OR 2 whichever is required.

    * @author chinmoy159
    * @version 1.0 dated 10/08/2017
    """

    res = 1
    while b > 0:
        if b & 1:
            res = ((res % c) * (a % c)) % c

        a *= a
        b >>= 1

    return res


if __name__ == "__main__":
    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
        MODULO = int(input("Enter Modulo : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    print(bin_exp_mod(BASE, POWER, MODULO))
