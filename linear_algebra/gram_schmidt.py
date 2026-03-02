import math


def gram_schmidt(input_vectors: list[list[float]]) -> list[list[float]]:
    """
    Implements the Gram-Schmidt process to orthonormalize a set of vectors.
    Reference: https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process

    Case 1: Standard 2D Orthonormalization
    >>> v1 = [[3.0, 1.0], [2.0, 2.0]]
    >>> result1 = gram_schmidt(v1)
    >>> [[round(x, 3) for x in v] for v in result1]
    [[0.949, 0.316], [-0.316, 0.949]]

    Case 2: 3D Vectors (The example from your error log)
    >>> v2 = [[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]]
    >>> result2 = gram_schmidt(v2)
    >>> [[round(x, 3) for x in v] for v in result2]
    [[0.707, 0.707, 0.0], [0.408, -0.408, 0.816], [-0.577, 0.577, 0.577]]

    Case 3: Vectors that are already orthonormal (should remain unchanged)
    >>> v3 = [[1.0, 0.0], [0.0, 1.0]]
    >>> gram_schmidt(v3)
    [[1.0, 0.0], [0.0, 1.0]]
    """

    orthonormal_basis: list[list[float]] = []

    for v in input_vectors:
        # Create a copy of the current vector to work on (equivalent to v_dash)
        v_orthogonal = list(v)

        for u in orthonormal_basis:
            # Manual Dot Product: (v_dash * u)
            dot_product = sum(vi * ui for vi, ui in zip(v_orthogonal, u))

            # Manual Vector Subtraction & Scalar Mult: v_dash = v_dash - u * dot_product
            v_orthogonal = [vi - (dot_product * ui) for vi, ui in zip(v_orthogonal, u)]

        # Manual Norm Calculation: (v_dash * v_dash) ** 0.5
        norm = math.sqrt(sum(xi**2 for xi in v_orthogonal))

        if norm < 1e-15:
            raise ValueError("The vectors are not linearly independent.")

        # Manual Scalar Multiplication: u_new = v_dash * (1/norm)
        u_new = [xi / norm for xi in v_orthogonal]
        orthonormal_basis.append(u_new)

    return orthonormal_basis


if __name__ == "__main__":
    import doctest

    doctest.testmod()
