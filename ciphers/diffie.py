from __future__ import annotations


def find_primitive(n: int) -> int | None:
    """
    Find a primitive root modulo n, if one exists.

    Args:
        n (int): The modulus for which to find a primitive root.

    Returns:
        int | None: The primitive root if one exists, or None if there is none.

    Examples:
        >>> find_primitive(7)  # Modulo 7 has primitive root 3
        3

        >>> find_primitive(11)  # Modulo 11 has primitive root 2
        2

        >>> find_primitive(8)  # Modulo 8 has no primitive root

    """
    for r in range(1, n):
        li = []
        for x in range(n - 1):
            val = pow(r, x, n)
            if val in li:
                break
            li.append(val)
        else:
            return r
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
