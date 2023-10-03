import cmath

def fast_fourier_transform(poly: list) -> list:
    """
    Compute the Fast Fourier Transform of a polynomial.
    
    Args:
    - poly: A list of complex coefficients representing the polynomial.
    
    Returns:
    - A list of complex numbers representing the point-value form of the polynomial.
    
    >>> abs(fast_fourier_transform([1, 2, 3, 4])[3] + 2 + 2j) < 1e-10
    True
    """
    n = len(poly)
    if n <= 1:
        return poly
    even_terms = fast_fourier_transform(poly[0::2])
    odd_terms = fast_fourier_transform(poly[1::2])
    combined = [0] * n
    for i in range(n // 2):
        t = cmath.exp(-2j * cmath.pi * i / n) * odd_terms[i]
        combined[i] = even_terms[i] + t
        combined[i + n//2] = even_terms[i] - t
    return combined

def inverse_fast_fourier_transform(poly: list) -> list:
    """
    Compute the Inverse Fast Fourier Transform of a polynomial.
    
    Args:
    - poly: A list of complex coefficients representing the polynomial in point-value form.
    
    Returns:
    - A list of complex numbers representing the coefficient form of the polynomial.
    
    >>> abs(inverse_fast_fourier_transform([(10+0j), (-2+2j), (-2+0j), (-2-2j)])[1] - 2) < 1e-10
    True
    """
    n = len(poly)
    poly = fast_fourier_transform([x.conjugate() for x in poly])
    return [x.conjugate()/n for x in poly]

def multiply_using_fft(poly1: list, poly2: list) -> list:
    """
    Multiply two polynomials using FFT.
    
    Args:
    - poly1: First polynomial represented as a list of complex coefficients.
    - poly2: Second polynomial represented as a list of complex coefficients.
    
    Returns:
    - A list of complex coefficients representing the product polynomial.
    """
    n = len(poly1) + len(poly2) - 1
    m = 1
    while m < n:
        m *= 2
    poly1 += [0] * (m - len(poly1))
    poly2 += [0] * (m - len(poly2))

    transformed_poly1 = fast_fourier_transform(poly1)
    transformed_poly2 = fast_fourier_transform(poly2)
    return [a*b for a, b in zip(transformed_poly1, transformed_poly2)]

def perform_carry_propagation(values: list) -> list:
    """
    Convert the complex values obtained after inverse FFT into integers by rounding and carry propagation.
    
    Args:
    - values: List of complex numbers.
    
    Returns:
    - List of integers after performing carry propagation.
    """
    result = []
    carry = 0
    for val in values:
        current_value = int(val.real + 0.5) + carry
        result.append(current_value % 10)
        carry = current_value // 10
    while carry:
        result.append(carry % 10)
        carry //= 10
    return result[::-1]

def fast_multiply_numbers(num1: int, num2: int) -> int:
    """
    Multiply two integers using FFT-based polynomial multiplication.
    
    Args:
    - num1: First integer.
    - num2: Second integer.
    
    Returns:
    - The product of the two integers.
    
    >>> fast_multiply_numbers(12345, 6789)
    83810205
    """
    poly1 = [int(digit) for digit in str(num1)][::-1]
    poly2 = [int(digit) for digit in str(num2)][::-1]
    product_poly = inverse_fast_fourier_transform(multiply_using_fft(poly1, poly2))
    return int(''.join(map(str, perform_carry_propagation(product_poly))))
