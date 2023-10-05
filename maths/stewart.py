"""
In geometry, Stewart's theorem yields a relation between the
lengths of the sides and the length of a cevian in a triangle.
Its name is in honour of the Scottish mathematician Matthew
Stewart, who published the theorem in 1746.[1]

Source: https://en.wikipedia.org/wiki/Stewart%27s_theorem
"""


def stewart(a: float, b: float, c: float, n: float, m: float) -> float:
    """
    Given the side lengths of the triangle (a,b,c), where the cevian intersects
    the side with side length a and splits it into segments with lengthes n and m,
    this formula finds the length of the cevian.

    >>> stewart(1,1,1,0.5,0.5)
    0.8660254037844386
    >>> stewart(1,2,3,4,5)
    Traceback (most recent call last):
        ...
    ValueError: This triangle violates the triangle inequality
    >>> stewart(1,1,1,1,1)
    Traceback (most recent call last):
        ...
    ValueError: n+m must equal a
    >>> stewart(3,2,4,1.7,1.3)
    2.9308701779505686
    """
    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("This triangle violates the triangle inequality")
    if n + m != a:
        raise ValueError("n+m must equal a")
    if a <= 0 or b <= 0 or c <= 0 or n < 0 or m < 0:
        raise ValueError("The side lengths of a triangle have to be positive")
    return ((b**2 * m + c**2 * n - m * a * n) / a) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
