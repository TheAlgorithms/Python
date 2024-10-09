import math


def gerçek_güç(görünür_güç: float, güç_çarpanı: float) -> float:
    """
    Görünür güç ve güç çarpanından gerçek gücü hesaplayın.

    Örnekler:
    >>> gerçek_güç(100, 0.9)
    90.0
    >>> gerçek_güç(0, 0.8)
    0.0
    >>> gerçek_güç(100, -0.9)
    -90.0
    """
    if (
        not isinstance(güç_çarpanı, (int, float))
        or güç_çarpanı < -1
        or güç_çarpanı > 1
    ):
        raise ValueError("güç_çarpanı -1 ile 1 arasında geçerli bir float değeri olmalıdır.")
    return görünür_güç * güç_çarpanı


def reaktif_güç(görünür_güç: float, güç_çarpanı: float) -> float:
    """
    Görünür güç ve güç çarpanından reaktif gücü hesaplayın.

    Örnekler:
    >>> reaktif_güç(100, 0.9)
    43.58898943540673
    >>> reaktif_güç(0, 0.8)
    0.0
    >>> reaktif_güç(100, -0.9)
    43.58898943540673
    """
    if (
        not isinstance(güç_çarpanı, (int, float))
        or güç_çarpanı < -1
        or güç_çarpanı > 1
    ):
        raise ValueError("güç_çarpanı -1 ile 1 arasında geçerli bir float değeri olmalıdır.")
    return görünür_güç * math.sqrt(1 - güç_çarpanı**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
