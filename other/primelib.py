# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:44:23 2017

@author: Christian Bender

This python library contains some useful functions to deal with
prime numbers and whole numbers.

Overview:

isPrime(number)
sieveEr(N)
getPrimeNumbers(N)
primeFactorization(number)
greatestPrimeFactor(number)
smallestPrimeFactor(number)
getPrime(n)
getPrimesBetween(pNumber1, pNumber2)

----

isEven(number)
isOdd(number)
gcd(number1, number2)  // greatest common divisor
kgV(number1, number2)  // least common multiple
getDivisors(number)    // all divisors of 'number' inclusive 1, number
isPerfectNumber(number)

NEW-FUNCTIONS

simplifyFraction(numerator, denominator)
factorial (n) // n!
fib (n) // calculate the n-th fibonacci term.

-----

goldbach(number)  // Goldbach's assumption

"""

from math import sqrt


def isPrime(number):
    """
        input: positive integer 'number'
        returns true if 'number' is prime otherwise false.
    """

    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

    status = True

    # 0 and 1 are none primes.
    if number <= 1:
        status = False

    for divisor in range(2, int(round(sqrt(number))) + 1):

        # if 'number' divisible by 'divisor' then sets 'status'
        # of false and break up the loop.
        if number % divisor == 0:
            status = False
            break

    # precondition
    assert isinstance(status, bool), "'status' must been from type bool"

    return status


# ------------------------------------------


def sieveEr(N):
    """
        input: positive integer 'N' > 2
        returns a list of prime numbers from 2 up to N.

        This function implements the algorithm called
        sieve of erathostenes.

    """

    # precondition
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"

    # beginList: conatins all natural numbers from 2 upt to N
    beginList = [x for x in range(2, N + 1)]

    ans = []  # this list will be returns.

    # actual sieve of erathostenes
    for i in range(len(beginList)):

        for j in range(i + 1, len(beginList)):

            if (beginList[i] != 0) and (beginList[j] % beginList[i] == 0):
                beginList[j] = 0

    # filters actual prime numbers.
    ans = [x for x in beginList if x != 0]

    # precondition
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans


# --------------------------------


def getPrimeNumbers(N):
    """
        input: positive integer 'N' > 2
        returns a list of prime numbers from 2 up to N (inclusive)
        This function is more efficient as function 'sieveEr(...)'
    """

    # precondition
    assert isinstance(N, int) and (N > 2), "'N' must been an int and > 2"

    ans = []

    # iterates over all numbers between 2 up to N+1
    # if a number is prime then appends to list 'ans'
    for number in range(2, N + 1):

        if isPrime(number):

            ans.append(number)

    # precondition
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans


# -----------------------------------------


def primeFactorization(number):
    """
        input: positive integer 'number'
        returns a list of the prime number factors of 'number'
    """

    # precondition
    assert isinstance(number, int) and number >= 0, "'number' must been an int and >= 0"

    ans = []  # this list will be returns of the function.

    # potential prime number factors.

    factor = 2

    quotient = number

    if number == 0 or number == 1:

        ans.append(number)

    # if 'number' not prime then builds the prime factorization of 'number'
    elif not isPrime(number):

        while quotient != 1:

            if isPrime(factor) and (quotient % factor == 0):
                ans.append(factor)
                quotient /= factor
            else:
                factor += 1

    else:
        ans.append(number)

    # precondition
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans


# -----------------------------------------


def greatestPrimeFactor(number):
    """
        input: positive integer 'number' >= 0
        returns the greatest prime number factor of 'number'
    """

    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' bust been an int and >= 0"

    ans = 0

    # prime factorization of 'number'
    primeFactors = primeFactorization(number)

    ans = max(primeFactors)

    # precondition
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans


# ----------------------------------------------


def smallestPrimeFactor(number):
    """
        input: integer 'number' >= 0
        returns the smallest prime number factor of 'number'
    """

    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' bust been an int and >= 0"

    ans = 0

    # prime factorization of 'number'
    primeFactors = primeFactorization(number)

    ans = min(primeFactors)

    # precondition
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans


# ----------------------


def isEven(number):
    """
        input: integer 'number'
        returns true if 'number' is even, otherwise false.
    """

    # precondition
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 == 0, bool), "compare bust been from type bool"

    return number % 2 == 0


# ------------------------


def isOdd(number):
    """
        input: integer 'number'
        returns true if 'number' is odd, otherwise false.
    """

    # precondition
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 != 0, bool), "compare bust been from type bool"

    return number % 2 != 0


# ------------------------


def goldbach(number):
    """
        Goldbach's assumption
        input: a even positive integer 'number' > 2
        returns a list of two prime numbers whose sum is equal to 'number'
    """

    # precondition
    assert (
        isinstance(number, int) and (number > 2) and isEven(number)
    ), "'number' must been an int, even and > 2"

    ans = []  # this list will returned

    # creates a list of prime numbers between 2 up to 'number'
    primeNumbers = getPrimeNumbers(number)
    lenPN = len(primeNumbers)

    # run variable for while-loops.
    i = 0
    j = None

    # exit variable. for break up the loops
    loop = True

    while i < lenPN and loop:

        j = i + 1

        while j < lenPN and loop:

            if primeNumbers[i] + primeNumbers[j] == number:
                loop = False
                ans.append(primeNumbers[i])
                ans.append(primeNumbers[j])

            j += 1

        i += 1

    # precondition
    assert (
        isinstance(ans, list)
        and (len(ans) == 2)
        and (ans[0] + ans[1] == number)
        and isPrime(ans[0])
        and isPrime(ans[1])
    ), "'ans' must contains two primes. And sum of elements must been eq 'number'"

    return ans


# ----------------------------------------------


def gcd(number1, number2):
    """
        Greatest common divisor
        input: two positive integer 'number1' and 'number2'
        returns the greatest common divisor of 'number1' and 'number2'
    """

    # precondition
    assert (
        isinstance(number1, int)
        and isinstance(number2, int)
        and (number1 >= 0)
        and (number2 >= 0)
    ), "'number1' and 'number2' must been positive integer."

    rest = 0

    while number2 != 0:

        rest = number1 % number2
        number1 = number2
        number2 = rest

    # precondition
    assert isinstance(number1, int) and (
        number1 >= 0
    ), "'number' must been from type int and positive"

    return number1


# ----------------------------------------------------


def kgV(number1, number2):
    """
        Least common multiple
        input: two positive integer 'number1' and 'number2'
        returns the least common multiple of 'number1' and 'number2'
    """

    # precondition
    assert (
        isinstance(number1, int)
        and isinstance(number2, int)
        and (number1 >= 1)
        and (number2 >= 1)
    ), "'number1' and 'number2' must been positive integer."

    ans = 1  # actual answer that will be return.

    # for kgV (x,1)
    if number1 > 1 and number2 > 1:

        # builds the prime factorization of 'number1' and 'number2'
        primeFac1 = primeFactorization(number1)
        primeFac2 = primeFactorization(number2)

    elif number1 == 1 or number2 == 1:

        primeFac1 = []
        primeFac2 = []
        ans = max(number1, number2)

    count1 = 0
    count2 = 0

    done = []  # captured numbers int both 'primeFac1' and 'primeFac2'

    # iterates through primeFac1
    for n in primeFac1:

        if n not in done:

            if n in primeFac2:

                count1 = primeFac1.count(n)
                count2 = primeFac2.count(n)

                for i in range(max(count1, count2)):
                    ans *= n

            else:

                count1 = primeFac1.count(n)

                for i in range(count1):
                    ans *= n

            done.append(n)

    # iterates through primeFac2
    for n in primeFac2:

        if n not in done:

            count2 = primeFac2.count(n)

            for i in range(count2):
                ans *= n

            done.append(n)

    # precondition
    assert isinstance(ans, int) and (
        ans >= 0
    ), "'ans' must been from type int and positive"

    return ans


# ----------------------------------


def getPrime(n):
    """
        Gets the n-th prime number.
        input: positive integer 'n' >= 0
        returns the n-th prime number, beginning at index 0
    """

    # precondition
    assert isinstance(n, int) and (n >= 0), "'number' must been a positive int"

    index = 0
    ans = 2  # this variable holds the answer

    while index < n:

        index += 1

        ans += 1  # counts to the next number

        # if ans not prime then
        # runs to the next prime number.
        while not isPrime(ans):
            ans += 1

    # precondition
    assert isinstance(ans, int) and isPrime(
        ans
    ), "'ans' must been a prime number and from type int"

    return ans


# ---------------------------------------------------


def getPrimesBetween(pNumber1, pNumber2):
    """
        input: prime numbers 'pNumber1' and 'pNumber2'
                pNumber1 < pNumber2
        returns a list of all prime numbers between 'pNumber1' (exclusiv)
                and 'pNumber2' (exclusiv)
    """

    # precondition
    assert (
        isPrime(pNumber1) and isPrime(pNumber2) and (pNumber1 < pNumber2)
    ), "The arguments must been prime numbers and 'pNumber1' < 'pNumber2'"

    number = pNumber1 + 1  # jump to the next number

    ans = []  # this list will be returns.

    # if number is not prime then
    # fetch the next prime number.
    while not isPrime(number):
        number += 1

    while number < pNumber2:

        ans.append(number)

        number += 1

        # fetch the next prime number.
        while not isPrime(number):
            number += 1

    # precondition
    assert (
        isinstance(ans, list) and ans[0] != pNumber1 and ans[len(ans) - 1] != pNumber2
    ), "'ans' must been a list without the arguments"

    # 'ans' contains not 'pNumber1' and 'pNumber2' !
    return ans


# ----------------------------------------------------


def getDivisors(n):
    """
        input: positive integer 'n' >= 1
        returns all divisors of n (inclusive 1 and 'n')
    """

    # precondition
    assert isinstance(n, int) and (n >= 1), "'n' must been int and >= 1"

    ans = []  # will be returned.

    for divisor in range(1, n + 1):

        if n % divisor == 0:
            ans.append(divisor)

    # precondition
    assert ans[0] == 1 and ans[len(ans) - 1] == n, "Error in function getDivisiors(...)"

    return ans


# ----------------------------------------------------


def isPerfectNumber(number):
    """
        input: positive integer 'number' > 1
        returns true if 'number' is a perfect number otherwise false.
    """

    # precondition
    assert isinstance(number, int) and (
        number > 1
    ), "'number' must been an int and >= 1"

    divisors = getDivisors(number)

    # precondition
    assert (
        isinstance(divisors, list)
        and (divisors[0] == 1)
        and (divisors[len(divisors) - 1] == number)
    ), "Error in help-function getDivisiors(...)"

    # summed all divisors up to 'number' (exclusive), hence [:-1]
    return sum(divisors[:-1]) == number


# ------------------------------------------------------------


def simplifyFraction(numerator, denominator):
    """
        input: two integer 'numerator' and 'denominator'
        assumes: 'denominator' != 0
        returns: a tuple with simplify numerator and denominator.
    """

    # precondition
    assert (
        isinstance(numerator, int)
        and isinstance(denominator, int)
        and (denominator != 0)
    ), "The arguments must been from type int and 'denominator' != 0"

    # build the greatest common divisor of numerator and denominator.
    gcdOfFraction = gcd(abs(numerator), abs(denominator))

    # precondition
    assert (
        isinstance(gcdOfFraction, int)
        and (numerator % gcdOfFraction == 0)
        and (denominator % gcdOfFraction == 0)
    ), "Error in function gcd(...,...)"

    return (numerator // gcdOfFraction, denominator // gcdOfFraction)


# -----------------------------------------------------------------


def factorial(n):
    """
        input: positive integer 'n'
        returns the factorial of 'n' (n!)
    """

    # precondition
    assert isinstance(n, int) and (n >= 0), "'n' must been a int and >= 0"

    ans = 1  # this will be return.

    for factor in range(1, n + 1):
        ans *= factor

    return ans


# -------------------------------------------------------------------


def fib(n):
    """
        input: positive integer 'n'
        returns the n-th fibonacci term , indexing by 0
    """

    # precondition
    assert isinstance(n, int) and (n >= 0), "'n' must been an int and >= 0"

    tmp = 0
    fib1 = 1
    ans = 1  # this will be return

    for i in range(n - 1):

        tmp = ans
        ans += fib1
        fib1 = tmp

    return ans
