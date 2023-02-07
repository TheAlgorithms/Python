"""
Smallest multiple
Problem
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to n?
"""


def find_prime_numbers(num: int) -> list:
    """
    Find all prime numbers for one particular number.
    >>> find_prime_numbers(10)
    [2, 3, 5, 7]
    """
    ln = []
    x = 2
    while x < num:
        y = 2
        while y < x + 1:
            v = x // y
            r = x % y
            if v == 1 and r == 0:
                ln.append(x)
                break
            if r == 0:
                break
            y += 1
        x += 1
    return ln


def find_max_power(num: int, ln: list) -> int:
    """
    Find the max power for all prime numbers.
    >>> find_max_power(10, [2, 3, 5, 7])
    2520
    """
    lp = []
    result = 1
    for e in ln:
        max_power = 0
        value = 2
        while value < num + 1:
            power = 0
            v_actual = value
            while True:
                v_result = v_actual // e
                rest = v_actual % e
                if rest == 0:
                    power += 1
                v_actual = v_result

                # exit condition
                if (v_result <= e and rest == 1) or (v_result <= 1):
                    if power > max_power:
                        max_power = power
                    break

            value += 1
        result *= pow(e, max_power)
        lp.append([e, max_power])
    return result


if __name__ == "__main__":
    num = 10
    result = 0
    l_prime = []
    l_prime = find_prime_numbers(num)
    print("Prime numbers:")
    print(l_prime)
    result = find_max_power(num, l_prime)
    print("Smallest multiple:")
    print(result)
