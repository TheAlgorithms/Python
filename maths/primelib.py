"""
Created on Thu Oct  5 16:44:23 2017

@author: Christian Bender

This Python library contains some useful functions to deal with
prime numbers and whole numbers.

Overview:

is_prime(number)
sieve_er(N)
get_prime_numbers(N)
prime_factorization(number)
greatest_prime_factor(number)
smallest_prime_factor(number)
get_prime(n)
get_primes_between(pNumber1, pNumber2)

----

is_even(number)
is_odd(number)
gcd(number1, number2)  // greatest common divisor
kg_v(number1, number2)  // least common multiple
get_divisors(number)    // all divisors of 'number' inclusive 1, number
is_perfect_number(number)

NEW-FUNCTIONS

simplify_fraction(numerator, denominator)
factorial (n) // n!
fib (n) // calculate the n-th fibonacci term.

-----

goldbach(number)  // Goldbach's assumption

"""

from math import sqrt


def is_prime(number: int) -> bool:
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


def sieve_er(n):
    """
    input: positive integer 'N' > 2
    returns a list of prime numbers from 2 up to N.

    This function implements the algorithm called
    sieve of erathostenes.

    """

    # precondition
    assert isinstance(n, int) and (n > 2), "'N' must been an int and > 2"

    # beginList: contains all natural numbers from 2 up to N
    begin_list = list(range(2, n + 1))

    ans = []  # this list will be returns.

    # actual sieve of erathostenes
    for i in range(len(begin_list)):
        for j in range(i + 1, len(begin_list)):
            if (begin_list[i] != 0) and (begin_list[j] % begin_list[i] == 0):
                begin_list[j] = 0

    # filters actual prime numbers.
    ans = [x for x in begin_list if x != 0]

    # precondition
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans


# --------------------------------


def get_prime_numbers(n):
    """
    input: positive integer 'N' > 2
    returns a list of prime numbers from 2 up to N (inclusive)
    This function is more efficient as function 'sieveEr(...)'
    """

    # precondition
    assert isinstance(n, int) and (n > 2), "'N' must been an int and > 2"

    ans = []

    # iterates over all numbers between 2 up to N+1
    # if a number is prime then appends to list 'ans'
    for number in range(2, n + 1):
        if is_prime(number):
            ans.append(number)

    # precondition
    assert isinstance(ans, list), "'ans' must been from type list"

    return ans


# -----------------------------------------


def prime_factorization(number):
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
    elif not is_prime(number):
        while quotient != 1:
            if is_prime(factor) and (quotient % factor == 0):
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


def greatest_prime_factor(number):
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
    prime_factors = prime_factorization(number)

    ans = max(prime_factors)

    # precondition
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans


# ----------------------------------------------


def smallest_prime_factor(number):
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
    prime_factors = prime_factorization(number)

    ans = min(prime_factors)

    # precondition
    assert isinstance(ans, int), "'ans' must been from type int"

    return ans


# ----------------------


def is_even(number):
    """
    input: integer 'number'
    returns true if 'number' is even, otherwise false.
    """

    # precondition
    assert isinstance(number, int), "'number' must been an int"
    assert isinstance(number % 2 == 0, bool), "compare bust been from type bool"

    return number % 2 == 0


# ------------------------


def is_odd(number):
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
        isinstance(number, int) and (number > 2) and is_even(number)
    ), "'number' must been an int, even and > 2"

    ans = []  # this list will returned

    # creates a list of prime numbers between 2 up to 'number'
    prime_numbers = get_prime_numbers(number)
    len_pn = len(prime_numbers)

    # run variable for while-loops.
    i = 0
    j = None

    # exit variable. for break up the loops
    loop = True

    while i < len_pn and loop:
        j = i + 1

        while j < len_pn and loop:
            if prime_numbers[i] + prime_numbers[j] == number:
                loop = False
                ans.append(prime_numbers[i])
                ans.append(prime_numbers[j])

            j += 1

        i += 1

    # precondition
    assert (
        isinstance(ans, list)
        and (len(ans) == 2)
        and (ans[0] + ans[1] == number)
        and is_prime(ans[0])
        and is_prime(ans[1])
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


def kg_v(number1, number2):
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
        prime_fac_1 = prime_factorization(number1)
        prime_fac_2 = prime_factorization(number2)

    elif number1 == 1 or number2 == 1:
        prime_fac_1 = []
        prime_fac_2 = []
        ans = max(number1, number2)

    count1 = 0
    count2 = 0

    done = []  # captured numbers int both 'primeFac1' and 'primeFac2'

    # iterates through primeFac1
    for n in prime_fac_1:
        if n not in done:
            if n in prime_fac_2:
                count1 = prime_fac_1.count(n)
                count2 = prime_fac_2.count(n)

                for _ in range(max(count1, count2)):
                    ans *= n

            else:
                count1 = prime_fac_1.count(n)

                for _ in range(count1):
                    ans *= n

            done.append(n)

    # iterates through primeFac2
    for n in prime_fac_2:
        if n not in done:
            count2 = prime_fac_2.count(n)

            for _ in range(count2):
                ans *= n

            done.append(n)

    # precondition
    assert isinstance(ans, int) and (
        ans >= 0
    ), "'ans' must been from type int and positive"

    return ans


# ----------------------------------


def get_prime(n):
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
        while not is_prime(ans):
            ans += 1

    # precondition
    assert isinstance(ans, int) and is_prime(
        ans
    ), "'ans' must been a prime number and from type int"

    return ans


# ---------------------------------------------------


def get_primes_between(p_number_1, p_number_2):
    """
    input: prime numbers 'pNumber1' and 'pNumber2'
            pNumber1 < pNumber2
    returns a list of all prime numbers between 'pNumber1' (exclusive)
            and 'pNumber2' (exclusive)
    """

    # precondition
    assert (
        is_prime(p_number_1) and is_prime(p_number_2) and (p_number_1 < p_number_2)
    ), "The arguments must been prime numbers and 'pNumber1' < 'pNumber2'"

    number = p_number_1 + 1  # jump to the next number

    ans = []  # this list will be returns.

    # if number is not prime then
    # fetch the next prime number.
    while not is_prime(number):
        number += 1

    while number < p_number_2:
        ans.append(number)

        number += 1

        # fetch the next prime number.
        while not is_prime(number):
            number += 1

    # precondition
    assert (
        isinstance(ans, list)
        and ans[0] != p_number_1
        and ans[len(ans) - 1] != p_number_2
    ), "'ans' must been a list without the arguments"

    # 'ans' contains not 'pNumber1' and 'pNumber2' !
    return ans


# ----------------------------------------------------


def get_divisors(n):
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


def is_perfect_number(number):
    """
    input: positive integer 'number' > 1
    returns true if 'number' is a perfect number otherwise false.
    """

    # precondition
    assert isinstance(number, int) and (
        number > 1
    ), "'number' must been an int and >= 1"

    divisors = get_divisors(number)

    # precondition
    assert (
        isinstance(divisors, list)
        and (divisors[0] == 1)
        and (divisors[len(divisors) - 1] == number)
    ), "Error in help-function getDivisiors(...)"

    # summed all divisors up to 'number' (exclusive), hence [:-1]
    return sum(divisors[:-1]) == number


# ------------------------------------------------------------


def simplify_fraction(numerator, denominator):
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
    gcd_of_fraction = gcd(abs(numerator), abs(denominator))

    # precondition
    assert (
        isinstance(gcd_of_fraction, int)
        and (numerator % gcd_of_fraction == 0)
        and (denominator % gcd_of_fraction == 0)
    ), "Error in function gcd(...,...)"

    return (numerator // gcd_of_fraction, denominator // gcd_of_fraction)


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

    for _ in range(n - 1):
        tmp = ans
        ans += fib1
        fib1 = tmp

    return ans
