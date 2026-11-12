"""
Bailey-Borwein-Plouffe (BBP) Formula
======================================
The BBP formula is a spigot algorithm for computing the nth binary digit
of pi (pi) WITHOUT computing all preceding digits. It was discovered in 1995
by David Bailey, Peter Borwein, and Simon Plouffe.

The formula is:
    pi = Sum (1/16^k) * (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
         k=0 to infinity

This makes it possible to extract any single hexadecimal digit of pi directly.

References:
    - https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    - https://www.experimentalmath.info/bbp-codes/bbp-alg.pdf
    - Bailey, D. H., Borwein, P. B., & Plouffe, S. (1997). "On the Rapid
      Computation of Various Polylogarithmic Constants." Mathematics of
      Computation, 66(218), 903-913.
"""


def _modular_pow(base: int, exp: int, mod: int) -> float:
    """
    Compute (base^exp) % mod using fast modular exponentiation,
    then return the fractional part when divided by mod.

    This is a helper for the BBP digit-extraction algorithm.

    Args:
        base: The base of the exponentiation.
        exp:  The exponent (non-negative integer).
        mod:  The modulus (positive integer).

    Returns:
        The fractional part of (base^exp mod mod) / mod as a float.

    Examples:
        >>> abs(_modular_pow(16, 0, 1) - 0.0) < 1e-10
        True
        >>> 0.0 <= _modular_pow(16, 5, 7) < 1.0
        True
    """
    if mod == 1:
        return 0.0

    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod

    return result / mod


def _series(j: int, n: int) -> float:
    """
    Compute the partial series used in the BBP formula:
        S_j(n) = Sum_{k=0}^{n} 16^(n-k) / (8k + j)  (mod 1)
                 + Sum_{k=n+1}^{inf} 16^(n-k) / (8k + j)

    Args:
        j: The denominator offset (1, 4, 5, or 6 for the standard BBP formula).
        n: The 0-based index of the hexadecimal digit of pi to extract.

    Returns:
        The fractional part of the series sum.

    Examples:
        >>> 0.0 <= _series(1, 0) < 1.0
        True
        >>> 0.0 <= _series(4, 10) < 1.0
        True
    """
    # Left sum: k = 0 to n (uses modular exponentiation)
    partial_sum = 0.0
    for k in range(n + 1):
        denom = 8 * k + j
        partial_sum += _modular_pow(16, n - k, denom)
        partial_sum %= 1.0

    # Right sum: k = n+1 to inf (geometrically decreasing, truncate when tiny)
    k = n + 1
    while True:
        term = (16.0 ** (n - k)) / (8 * k + j)
        if term < 1e-15:
            break
        partial_sum += term
        partial_sum %= 1.0
        k += 1

    return partial_sum


def bbp_pi_hex_digit(n: int) -> str:
    """
    Compute the nth fractional hexadecimal digit of pi (0-indexed) using the
    Bailey-Borwein-Plouffe (BBP) formula.

    The BBP formula allows extracting ANY hexadecimal digit of pi directly,
    without calculating all prior digits. This is a spigot algorithm.

    Pi in hexadecimal is 3.243F6A8885A308D3..., so this function returns
    the fractional digits: index 0 -> '2', index 1 -> '4', index 2 -> '3', etc.

    Args:
        n: The 0-based position of the fractional hexadecimal digit to extract.
           n=0 gives '2' (first fractional digit of 3.243F6A8885A308D3...)
           n=1 gives '4'
           n=2 gives '3'

    Returns:
        A single uppercase hexadecimal character (0-9, A-F).

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> bbp_pi_hex_digit(0)
        '2'
        >>> bbp_pi_hex_digit(1)
        '4'
        >>> bbp_pi_hex_digit(2)
        '3'
        >>> bbp_pi_hex_digit(3)
        'F'
        >>> bbp_pi_hex_digit(4)
        '6'
        >>> bbp_pi_hex_digit(5)
        'A'
        >>> bbp_pi_hex_digit(10)
        'A'
        >>> bbp_pi_hex_digit(-1)
        Traceback (most recent call last):
            ...
        ValueError: n must be a non-negative integer, got -1
    """
    if n < 0:
        msg = f"n must be a non-negative integer, got {n}"
        raise ValueError(msg)

    # pi in hex: 3.243F6A8885A308D3...
    # The BBP formula computes the fractional hex digit at position n
    x = 4.0 * _series(1, n) - 2.0 * _series(4, n) - _series(5, n) - _series(6, n)

    # Normalize to [0, 1) and extract first hex digit
    x = x % 1.0
    digit_value = int(x * 16)
    return format(digit_value, "X")


def pi_hex_string(num_digits: int) -> str:
    """
    Generate the first `num_digits` hexadecimal digits of pi using the BBP formula.

    Note: Each call to bbp_pi_hex_digit is O(n log n), so this function
    is O(n^2 log n) overall. It is intended for educational use, not
    high-performance computation.

    Args:
        num_digits: The number of hexadecimal digits to compute (must be > 0).

    Returns:
        A string of `num_digits` uppercase hexadecimal characters.

    Raises:
        ValueError: If num_digits is not a positive integer.

    Examples:
        >>> pi_hex_string(1)
        '2'
        >>> pi_hex_string(5)
        '243F6'
        >>> pi_hex_string(10)
        '243F6A8885'
        >>> pi_hex_string(0)
        Traceback (most recent call last):
            ...
        ValueError: num_digits must be a positive integer, got 0
    """
    if num_digits <= 0:
        msg = f"num_digits must be a positive integer, got {num_digits}"
        raise ValueError(msg)

    return "".join(bbp_pi_hex_digit(i) for i in range(num_digits))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Bailey-Borwein-Plouffe (BBP) Formula Demo")
    print("=" * 45)
    print("pi in hexadecimal: 3.243F6A8885A308D3...")
    print("BBP extracts the fractional hex digits: 2, 4, 3, F, 6, A, ...")
    print()
    for pos in range(15):
        digit = bbp_pi_hex_digit(pos)
        print(f"  Fractional hex digit at position {pos:2d}: {digit}")

    print()
    print(f"First 15 fractional hex digits of pi: {pi_hex_string(15)}")
    print("Expected:                               243F6A8885A308D")
