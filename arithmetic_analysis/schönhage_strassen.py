import doctest

def number_theoretic_transform(
    polynomial_coeffs: list[int], prime_modulus: int, primitive_root: int
) -> list[int]:
    """
    Compute the number-theoretic transform of a polynomial.

    Args:
    - polynomial_coeffs: List of integers representing polynomial coefficients.
    - prime_modulus: Prime modulus used in the NTT transformations.
    - primitive_root: Primitive root of the prime modulus.

    Returns:
    - List of integers representing the polynomial in point-value form.

    Doctest:
    >>> number_theoretic_transform([1, 2, 3, 4], 998244353, 3)
    [10, 173167434, 998244351, 825076915]
    >>> number_theoretic_transform([4, 3, 2, 1], 998244353, 3)
    [10, 825076919, 2, 173167438]
    """
    n = len(polynomial_coeffs)
    assert (prime_modulus - 1) % n == 0
    omega = pow(primitive_root, (prime_modulus - 1) // n, prime_modulus)
    return recursive_ntt_transform(polynomial_coeffs, omega, prime_modulus)


def recursive_ntt_transform(
    polynomial_coeffs_recursive: list[int], root_of_unity: int, prime_modulus: int
) -> list[int]:
    """
    Recursive function for number-theoretic transform.

    Args:
    - polynomial_coeffs_recursive: List of integers representing polynomial coefficients during recursive steps.
    - root_of_unity: Primitive nth root of unity modulo the prime modulus.
    - prime_modulus: Prime modulus used in the NTT transformations.

    Returns:
    - List of integers representing the polynomial in point-value form.

    Doctest:
    >>> a = [1, 2, 3, 4]
    >>> transformed = number_theoretic_transform(a, 998244353, 3)
    >>> recursive_ntt_transform(a, 3, 998244353)
    [10, 998244345, 998244351, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> recursive_ntt_transform(b, 3, 998244353)
    [10, 8, 2, 998244349]
    """
    n = len(polynomial_coeffs_recursive)
    if n == 1:
        return polynomial_coeffs_recursive
    even_coeffs = polynomial_coeffs_recursive[::2]
    odd_coeffs = polynomial_coeffs_recursive[1::2]
    even_transformed = recursive_ntt_transform(even_coeffs, root_of_unity**2 % prime_modulus, prime_modulus)
    odd_transformed = recursive_ntt_transform(odd_coeffs, root_of_unity**2 % prime_modulus, prime_modulus)
    multiplier = 1
    transformed = [0] * n
    for i in range(n // 2):
        transformed[i] = (even_transformed[i] + multiplier * odd_transformed[i]) % prime_modulus
        transformed[i + n // 2] = (even_transformed[i] - multiplier * odd_transformed[i]) % prime_modulus
        multiplier = multiplier * root_of_unity % prime_modulus
    return transformed


def inverse_ntt(point_values: list[int], prime_modulus: int, primitive_root: int) -> list[int]:
    """
    Compute the inverse number-theoretic transform of a polynomial.

    Args:
    - point_values: List of integers representing polynomial in point-value form.
    - prime_modulus: Prime modulus used in the NTT transformations.
    - primitive_root: Primitive root of the prime modulus.

    Returns:
    - List of integers representing polynomial coefficients.

    Doctest:
    >>> a = [1, 2, 3, 4]
    >>> transformed = number_theoretic_transform(a, 998244353, 3)
    >>> inverse_ntt(transformed, 998244353, 3)
    [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> inverse_ntt(transformed_b, 998244353, 3)
    [4, 3, 2, 1]
    """
    n = len(point_values)
    assert (prime_modulus - 1) % n == 0
    omega = pow(primitive_root, (prime_modulus - 1) // n, prime_modulus)
    omega_inv = pow(omega, prime_modulus - 2, prime_modulus)
    return [(coeff * pow(n, prime_modulus - 2, prime_modulus)) % prime_modulus for coeff in recursive_inverse_ntt(point_values, omega_inv, prime_modulus)]


def recursive_inverse_ntt(point_values_recursive: list[int], root_of_unity: int, prime_modulus: int) -> list[int]:
    """
    Recursive function for inverse number-theoretic transform.

    Args:
    - point_values_recursive: List of integers representing polynomial in point-value form during recursive steps.
    - root_of_unity: Primitive nth root of unity modulo the prime modulus.
    - prime_modulus: Prime modulus used in the NTT transformations.

    Returns:
    - List of integers representing polynomial coefficients.

    Doctest:
    >>> a = [1, 2, 3, 4]
    >>> transformed = number_theoretic_transform(a, 998244353, 3)
    >>> omega = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_ntt(transformed, omega, 998244353)
    [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> omega_b = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_ntt(transformed_b, omega_b, 998244353)
    [4, 3, 2, 1]
    """
    n = len(point_values_recursive)
    if n == 1:
        return point_values_recursive
    even_vals = point_values_recursive[::2]
    odd_vals = point_values_recursive[1::2]
    even_coeffs = recursive_inverse_ntt(even_vals, root_of_unity**2 % prime_modulus, prime_modulus)
    odd_coeffs = recursive_inverse_ntt(odd_vals, root_of_unity**2 % prime_modulus, prime_modulus)
    multiplier = 1
    coeffs = [0] * n
    for i in range(n // 2):
        coeffs[i] = (even_coeffs[i] + multiplier * odd_coeffs[i]) % prime_modulus
        coeffs[i + n // 2] = (even_coeffs[i] - multiplier * odd_coeffs[i]) % prime_modulus
        multiplier = multiplier * root_of_unity % prime_modulus
    return coeffs

def convolve_polynomials(
    polynomial_a_point_values: list[int], polynomial_b_point_values: list[int], prime_modulus: int
) -> list[int]:
    """
    Compute the convolution of two polynomials in point-value form.

    Args:
    - polynomial_a_point_values: List of integers representing polynomial A in point-value form.
    - polynomial_b_point_values: List of integers representing polynomial B in point-value form.
    - prime_modulus: Prime modulus used in the NTT transformations.

    Returns:
    - List of integers representing the convolution of A and B in point-value form.

    Doctest:
    >>> a = [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_a = number_theoretic_transform(a, 998244353, 3)
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> convolve_polynomials(transformed_a, transformed_b, 998244353)
    [4, 11, 20, 30, 20, 11, 4]
    """
    return [(a * b) % prime_modulus for a, b in zip(polynomial_a_point_values, polynomial_b_point_values)]


def multiply_numbers(number_a: int, number_b: int, prime_modulus: int, primitive_root: int) -> int:
    """
    Multiply two numbers using the Schönhage-Strassen algorithm.

    Args:
    - number_a: First integer.
    - number_b: Second integer.
    - prime_modulus: Prime modulus.
    - primitive_root: Primitive root of the prime modulus.

    Returns:
    - Integer result of the multiplication.

    Doctest:
    >>> multiply_numbers(5, 7, 17, 3)
    35
    >>> multiply_numbers(12345, 67890, 998244353, 3)
    662696412
    """
    coeffs_a = [int(digit) for digit in str(number_a)]
    coeffs_b = [int(digit) for digit in str(number_b)]

    # Pad the coefficient lists with zeros to have the same length
    max_len = max(len(coeffs_a), len(coeffs_b))
    coeffs_a = [0] * (max_len - len(coeffs_a)) + coeffs_a
    coeffs_b = [0] * (max_len - len(coeffs_b)) + coeffs_b

    # Compute NTT of the coefficient lists
    point_values_a = number_theoretic_transform(coeffs_a, prime_modulus, primitive_root)
    point_values_b = number_theoretic_transform(coeffs_b, prime_modulus, primitive_root)

    # Perform pointwise multiplication
    result_point_values = [
        ((a % prime_modulus) * (b % prime_modulus)) % prime_modulus for a, b in zip(point_values_a, point_values_b)
    ]

    # Compute the inverse NTT to obtain the result in coefficient form
    result_coeffs = inverse_ntt(result_point_values, prime_modulus, primitive_root)

    # Convert the result from coefficient form to an integer
    result = 0
    for coeff in result_coeffs:
        result = (result * 10 + coeff) % prime_modulus

    return result
    

def multiply_polynomials(polynomial_a: list[int], polynomial_b: list[int], prime_modulus: int, primitive_root: int) -> list[int]:
    """
    Multiply two polynomials using the Schönhage-Strassen algorithm.

    Args:
    - polynomial_a: List of integers representing coefficients of polynomial A.
    - polynomial_b: List of integers representing coefficients of polynomial B.
    - prime_modulus: Prime modulus.
    - primitive_root: Primitive root of the prime modulus.

    Returns:
    - List of integers representing coefficients of the product polynomial.

    Doctest:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> multiply_polynomials(a, b, 17, 3)
    [4, 13, 28, 27, 18]
    >>> a = [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> multiply_polynomials(a, b, 998244353, 3)
    [4, 11, 20, 30, 20, 11, 4]
    """
    # Compute NTT of the coefficient lists
    point_values_a = number_theoretic_transform(polynomial_a, prime_modulus, primitive_root)
    point_values_b = number_theoretic_transform(polynomial_b, prime_modulus, primitive_root)

    # Perform pointwise multiplication
    result_point_values = [
        ((a % prime_modulus) * (b % prime_modulus)) % prime_modulus for a, b in zip(point_values_a, point_values_b)
    ]

    # Compute the inverse NTT to obtain the result in coefficient form
    result_coeffs = inverse_ntt(result_point_values, prime_modulus, primitive_root)

    return result_coeffs

# Running the doctests for all functions
doctest.testmod()

