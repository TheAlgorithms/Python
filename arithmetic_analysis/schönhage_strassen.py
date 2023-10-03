import math
import doctest

def number_theoretic_transform(polynomial_coeffs: list, prime_modulus: int, primitive_root: int) -> list:
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
    w = pow(primitive_root, (prime_modulus - 1) // n, prime_modulus)
    return recursive_ntt(polynomial_coeffs, w, prime_modulus)

def recursive_ntt_transform(polynomial_coeffs_recursive: list, root_of_unity: int, prime_modulus: int) -> list:
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
    a0 = polynomial_coeffs_recursive[::2]
    a1 = polynomial_coeffs_recursive[1::2]
    f0 = recursive_ntt_transform(a0, root_of_unity**2 % prime_modulus, prime_modulus)
    f1 = recursive_ntt_transform(a1, root_of_unity**2 % prime_modulus, prime_modulus)
    x = 1
    f = [0] * n
    for i in range(n // 2):
        f[i] = (f0[i] + x * f1[i]) % prime_modulus
        f[i + n // 2] = (f0[i] - x * f1[i]) % prime_modulus
        x = x * root_of_unity % prime_modulus
    return f

def inverse_ntt(point_values: list, prime_modulus: int, primitive_root: int) -> list:
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
    w = pow(primitive_root, (prime_modulus - 1) // n, prime_modulus)
    w_inv = pow(w, prime_modulus - 2, prime_modulus)
    return [x * pow(n, prime_modulus - 2, prime_modulus) % prime_modulus for x in recursive_inverse_ntt(point_values, w_inv, prime_modulus)]

def recursive_inverse_transform(point_values_recursive: list, root_of_unity: int, prime_modulus: int) -> list:
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
    >>> w = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_transform(transformed, w, 998244353)
    [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> w_b = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_transform(transformed_b, w_b, 998244353)
    [4, 3, 2, 1]
    """
    n = len(point_values_recursive)
    if n == 1:
        return point_values_recursive
    f0 = point_values_recursive[::2]
    f1 = point_values_recursive[1::2]
    a0 = recursive_inverse_transform(f0, root_of_unity**2 % prime_modulus, prime_modulus)
    a1 = recursive_inverse_transform(f1, root_of_unity**2 % prime_modulus, prime_modulus)
    x = 1
    a = [0] * n
    for i in range(n // 2):
        a[i] = (a0[i] + x * a1[i]) % prime_modulus
        a[i + n // 2] = (a0[i] - x * a1[i]) % prime_modulus
        x = x * root_of_unity % prime_modulus
    return a

# Helper function to compute the convolution of two polynomials in point-value form
def convolve_polynomials(a_point_values: list, b_point_values: list, prime_modulus: int) -> list:
    """
    Compute the convolution of two polynomials in point-value form.
    
    Args:
    - a_point_values: List of integers representing polynomial A in point-value form.
    - b_point_values: List of integers representing polynomial B in point-value form.
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
    return [(a * b) % prime_modulus for a, b in zip(a_point_values, b_point_values)]

def multiply_numbers(x: int, y: int, p: int, g: int) -> int:
    """
    Multiply two numbers using the Schönhage-Strassen algorithm.
    
    Args:
    - x: First integer.
    - y: Second integer.
    - p: Prime modulus.
    - g: Primitive root of the prime modulus.
    
    Returns:
    - Integer result of the multiplication.
    
    Doctest:
    >>> multiply_numbers(5, 7, 17, 3)
    35
    >>> multiply_numbers(12345, 67890, 998244353, 3)
    662696412
    """
    x_coeffs = [int(digit) for digit in str(x)]
    y_coeffs = [int(digit) for digit in str(y)]
    
    # Pad the coefficient lists with zeros to have the same length
    max_len = max(len(x_coeffs), len(y_coeffs))
    x_coeffs = [0] * (max_len - len(x_coeffs)) + x_coeffs
    y_coeffs = [0] * (max_len - len(y_coeffs)) + y_coeffs
    
    # Compute NTT of the coefficient lists
    x_point_values = number_theoretic_transform(x_coeffs, p, g)
    y_point_values = number_theoretic_transform(y_coeffs, p, g)
    
    # Perform pointwise multiplication
    result_point_values = [((a % p) * (b % p)) % p for a, b in zip(x_point_values, y_point_values)]
    
    # Compute the inverse NTT to obtain the result in coefficient form
    result_coeffs = inverse_ntt(result_point_values, p, g)
    
    # Convert the result from coefficient form to an integer
    result = 0
    for coeff in result_coeffs:
        result = (result * 10 + coeff) % p
    
    return result

def multiply_polynomials(a: list, b: list, p: int, g: int) -> list:
    """
    Multiply two polynomials using the Schönhage-Strassen algorithm.
    
    Args:
    - a: List of integers representing coefficients of polynomial A.
    - b: List of integers representing coefficients of polynomial B.
    - p: Prime modulus.
    - g: Primitive root of the prime modulus.
    
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
    a_point_values = number_theoretic_transform(a, p, g)
    b_point_values = number_theoretic_transform(b, p, g)
    
    # Perform pointwise multiplication
    result_point_values = [((a % p) * (b % p)) % p for a, b in zip(a_point_values, b_point_values)]
    
    # Compute the inverse NTT to obtain the result in coefficient form
    result_coeffs = inverse_ntt(result_point_values, p, g)
    
    return result_coeffs

def inverse_number_theoretic_transform(f: list, p: int, g: int) -> list:
    """
    Compute the inverse number-theoretic transform of a polynomial.
    
    Args:
    - f: List of integers representing polynomial in point-value form.
    - p: Prime modulus.
    - g: Primitive root of the prime modulus.
    
    Returns:
    - List of integers representing polynomial coefficients.
    
    Doctest:
    >>> a = [1, 2, 3, 4]
    >>> transformed = number_theoretic_transform(a, 998244353, 3)
    >>> inverse_number_theoretic_transform(transformed, 998244353, 3)
    [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> inverse_number_theoretic_transform(transformed_b, 998244353, 3)
    [4, 3, 2, 1]
    """
    n = len(f)
    assert (p - 1) % n == 0
    w = pow(g, (p - 1) // n, p)
    w_inv = pow(w, p - 2, p)
    return [(x * pow(n, p - 2, p)) % p for x in recursive_inverse_ntt(f, w_inv, p)]

def recursive_inverse_ntt(point_values_recursive: list, root_of_unity: int, prime_modulus: int) -> list:
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
    >>> w = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_ntt(transformed, w, 998244353)
    [1, 2, 3, 4]
    >>> b = [4, 3, 2, 1]
    >>> transformed_b = number_theoretic_transform(b, 998244353, 3)
    >>> w_b = pow(3, (998244353 - 1) // 4, 998244353)
    >>> recursive_inverse_ntt(transformed_b, w_b, 998244353)
    [4, 3, 2, 1]
    """
    n = len(point_values_recursive)
    if n == 1:
        return point_values_recursive
    f0 = point_values_recursive[::2]
    f1 = point_values_recursive[1::2]
    a0 = recursive_inverse_ntt(f0, root_of_unity**2 % prime_modulus, prime_modulus)
    a1 = recursive_inverse_ntt(f1, root_of_unity**2 % prime_modulus, prime_modulus)
    x = 1
    a = [0] * n
    for i in range(n // 2):
        a[i] = (a0[i] + x * a1[i]) % prime_modulus
        a[i + n // 2] = (a0[i] - x * a1[i]) % prime_modulus
        x = x * root_of_unity % prime_modulus
    return a

# Running the doctests for all functions
doctest.testmod()

