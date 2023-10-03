import math


def recursive_number_theoretic_transform(a: list, w: int, p: int) -> list:
    """
    Recursive function for number-theoretic transform.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - a: List of integers representing polynomial coefficients.
    - w: Primitive nth root of unity modulo p.
    - p: Prime modulus.

    Returns:
    - List of integers representing polynomial in point-value form.
    """
    n = len(a)
    if n == 1:
        return a
    a0 = a[::2]
    a1 = a[1::2]
    f0 = recursive_number_theoretic_transform(a0, w**2 % p, p)
    f1 = recursive_number_theoretic_transform(a1, w**2 % p, p)
    x = 1
    f = [0] * n
    for i in range(n // 2):
        f[i] = (f0[i] + x * f1[i]) % p
        f[i + n // 2] = (f0[i] - x * f1[i]) % p
        x = x * w % p
    return f


def number_theoretic_transform(a: list, p: int, g: int) -> list:
    """
    Compute the number-theoretic transform of a polynomial.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - a: List of integers representing polynomial coefficients.
    - p: Prime modulus.
    - g: Primitive root of p.

    Returns:
    - List of integers representing polynomial in point-value form.
    """
    n = len(a)
    assert (p - 1) % n == 0
    w = pow(g, (p - 1) // n, p)
    return recursive_number_theoretic_transform(a, w, p)


def recursive_inverse_ntt(f: list, w: int, p: int) -> list:
    """
    Recursive function for inverse number-theoretic transform.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - f: List of integers representing polynomial in point-value form.
    - w: Primitive nth root of unity modulo p.
    - p: Prime modulus.

    Returns:
    - List of integers representing polynomial coefficients.
    """
    n = len(f)
    if n == 1:
        return f
    f0 = f[::2]
    f1 = f[1::2]
    a0 = recursive_inverse_ntt(f0, w**2 % p, p)
    a1 = recursive_inverse_ntt(f1, w**2 % p, p)
    x = 1
    a = [0] * n
    for i in range(n // 2):
        a[i] = (a0[i] + x * a1[i]) % p
        a[i + n // 2] = (a0[i] - x * a1[i]) % p
        x = x * w % p
    return a


def inverse_number_theoretic_transform(f: list, p: int, g: int) -> list:
    """
    Compute the inverse number-theoretic transform of a polynomial.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - f: List of integers representing polynomial in point-value form.
    - p: Prime modulus.
    - g: Primitive root of p.

    Returns:
    - List of integers representing polynomial coefficients.
    """
    n = len(f)
    assert (p - 1) % n == 0
    w = pow(g, (p - 1) // n, p)
    w_inv = pow(w, p - 2, p)
    return [x * pow(n, p - 2, p) % p for x in recursive_inverse_ntt(f, w_inv, p)]


def multiply_polynomials(a: list, b: list, p: int, g: int) -> list:
    """
    Multiply two polynomials using the number-theoretic transform.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - a: List of integers representing the first polynomial's coefficients.
    - b: List of integers representing the second polynomial's coefficients.
    - p: Prime modulus.
    - g: Primitive root of p.

    Returns:
    - List of integers representing the coefficients of the product polynomial.
    """
    n = 1
    while n < len(a) + len(b) - 1:
        n *= 2
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))

    fa = number_theoretic_transform(a, p, g)
    fb = number_theoretic_transform(b, p, g)

    fc = [x * y % p for x, y in zip(fa, fb)]

    c = inverse_number_theoretic_transform(fc, p, g)

    # Remove trailing zeros
    while len(c) > 0 and c[-1] == 0:
        c.pop()
    return c


def multiply_numbers(x: int, y: int, p: int, g: int) -> int:
    """
    Multiply two numbers using polynomial multiplication based on the number-theoretic transform.
    Reference: https://en.wikipedia.org/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm

    Args:
    - x: First integer number.
    - y: Second integer number.
    - p: Prime modulus.
    - g: Primitive root of p.

    Returns:
    - The product of the two numbers.
    """
    a = [int(digit) for digit in str(x)][
        ::-1
    ]  # Reverse the digits to match polynomial representation
    b = [int(digit) for digit in str(y)][
        ::-1
    ]  # Reverse the digits to match polynomial representation
    c = multiply_polynomials(a, b, p, g)
    carry = 0
    for i in range(len(c)):
        c[i] += carry
        carry = c[i] // 10
        c[i] %= 10
    while carry:
        c.append(carry % 10)
        carry //= 10
    return int("".join(map(str, c[::-1])))


# Test the multiplication of two numbers
multiply_numbers(12345, 6789, p, g)
