import math
import random

"""
Shor Algorithm is one of the basic quantum computing algorithm
that is used in breaking the RSA cryptography protocol, by finding the
prime numbers that are used to create the public key value, n

In this implementation, I have used a very simple construct without
the use of qiskit or cirq to help understand how Shor algorithm's
idea actually works.

Website referred for shor algorithm:
https://www.geeksforgeeks.org/shors-factorization-algorithm/

"""


class Shor:
    def period_find(self, num: int, number: int) -> int:
        """
        Find the period of a^x mod N.

        >>> shor = Shor()
        >>> shor.period_find(2, 15)
        4
        >>> shor.period_find(3, 7)
        6
        """
        start: int = 1
        while pow(num, start, number) != 1:
            start += 1
        return start

    def shor_algorithm(self, number: int) -> tuple[int, int]:
        """
        Run Shor's algorithm to factor a number.
        >>> shor = Shor()
        >>> random.seed(0)
        >>> factors = shor.shor_algorithm(15)
        >>> isinstance(factors, tuple) and len(factors) == 2
        True
        >>> factors
        (3, 5)
        """
        if number % 2 == 0:
            return 2, number // 2
        while True:
            random.seed(0)
            num: int = random.randint(2, number - 1)
            gcd_number_num: int = math.gcd(number, num)
            if gcd_number_num > 1:
                return gcd_number_num, number // gcd_number_num

            result: int = self.period_find(num, number)
            if not result % 2:
                start: int = pow(num, result // 2, number)
                if start != number - 1:
                    p_value: int = math.gcd(start - 1, number)
                    q_value: int = math.gcd(start + 1, number)
                    if p_value > 1 and q_value > 1:
                        return p_value, q_value


shor = Shor()
print(shor.shor_algorithm(15))
