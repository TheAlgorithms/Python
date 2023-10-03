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


# Re-running the doctests
doctest.testmod()
