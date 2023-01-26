def binary_exponentiation_multiplication(a, b):
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

    * @author chinmoy159
    * @version 1.0 dated 10/08/2017
    """

    res = 0
    while b > 0:
        if b & 1:
            res += a

        a += a
        b >>= 1

    return res


def binary_exponentiation_powers(a, b):
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

    * @author chinmoy159
    * @version 1.0 dated 10/08/2017
    """

    res = 1
    while b > 0:
        if b & 1:
            res *= a

        a *= a
        b >>= 1

    return res


def binary_exponentiation_recursion(a, b):
    """Binary Exponentiation with recursion.

    * Time Complexity : O(logn)
    * @author : Junth Basnet
    """

    if b == 0:
        return 1

    elif b % 2 == 1:
        return binary_exponentiation_recursion(a, b - 1) * a

    else:
        return binary_exponentiation_recursion(a, b / 2) ** 2


if __name__ == "__main__":
    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    RESULT = binary_exponentiation_recursion(BASE, POWER)
    print(f"{BASE}^({POWER}) : {RESULT}")
